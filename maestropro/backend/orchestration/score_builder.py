"""
MaestroPro - Score Builder
Maya Instruments Technology
Version: 1.1.0

Step [3] of the Full Orchestration Workflow: split a SheetSage2 lead sheet
(melody + chord symbols) into per-instrument parts and export multi-part
MusicXML for human editing in MuseScore.
"""

import logging
from pathlib import Path
from typing import List, Optional, Tuple

from music21 import (
    chord as m21chord,
    clef,
    harmony,
    instrument,
    key as m21key,
    meter,
    note,
    stream,
    tempo,
)

from backend.orchestration.abc_bridge import ChordEvent, LeadNote, LeadSheet
from backend.orchestration.chords import chord_pitches, figure_to_native, parse_native_chord
from backend.orchestration.instruments import InstrumentSpec, resolve_roles
from backend.orchestration.models import ArrangementConfig

logger = logging.getLogger(__name__)


class ScoreBuildError(RuntimeError):
    """Raised when a lead sheet cannot be realized as a multi-part score."""


# ---------------------------------------------------------------------------
# Key helpers (native ABC key names ↔ music21)
# ---------------------------------------------------------------------------

def native_key_to_m21(native: str) -> m21key.Key:
    """Convert native ABC key ('C', 'Am', 'Eb', 'F#m') to a music21 Key."""
    text = native.strip()
    minor = text.endswith("m") and not text.endswith("em")  # 'Am', 'Bbm', ...
    if minor:
        tonic = text[:-1]
        mode = "minor"
    else:
        tonic = text
        mode = "major"
    tonic = tonic.replace("b", "-")
    try:
        return m21key.Key(tonic, mode)
    except Exception:
        logger.warning(f"Could not interpret native key {native!r}; defaulting to C major")
        return m21key.Key("C", "major")


def m21_key_to_native(key_obj: m21key.Key) -> str:
    """Convert a music21 Key to native ABC spelling ('Eb', 'F#m')."""
    tonic = key_obj.tonicPitchNameWithCase if hasattr(key_obj, "tonicPitchNameWithCase") else str(key_obj.tonic)
    # music21 uses 'e-' style; native uses 'eb'/'Eb'
    tonic = tonic.replace("-", "b")
    # Normalize octave marks away (e.g. 'c' → 'C')
    tonic = tonic[0].upper() + tonic[1:]
    if key_obj.mode == "minor":
        return f"{tonic}m"
    return tonic


def _parse_config_key(value: str) -> m21key.Key:
    """Parse user key strings: 'Eb major', 'F# minor', 'Am', 'C'."""
    text = value.strip()
    mode = "major"
    lowered = text.lower()
    if lowered.endswith(" minor"):
        mode, text = "minor", text[:-6]
    elif lowered.endswith(" major"):
        text = text[:-6]
    elif (
        len(text) >= 2 and text.endswith("m")
        and text[-2] in "ABCDEFG#" "b"
    ):
        mode, text = "minor", text[:-1]
    tonic = text.strip().replace("b", "-").replace(" ", "")
    if not tonic:
        raise ValueError(f"Empty tonic in key {value!r}")
    return m21key.Key(tonic, mode)


def meter_to_tuple(meter_str: str) -> Tuple[int, int]:
    n, d = meter_str.split("/")
    return int(n), int(d)


# ---------------------------------------------------------------------------
# Event timeline helpers
# ---------------------------------------------------------------------------

def _merge_events(notes: List[LeadNote]) -> List[LeadNote]:
    """Sort notes and truncate monophonic overlaps (later note wins)."""
    ordered = sorted(notes, key=lambda n: (n.onset, -n.duration))
    cleaned: List[LeadNote] = []
    for event in ordered:
        if cleaned:
            prev = cleaned[-1]
            prev_end = prev.onset + prev.duration
            if event.onset < prev_end:
                if event.onset <= prev.onset:
                    cleaned.pop()
                else:
                    prev.duration = event.onset - prev.onset
        if event.duration > 0:
            cleaned.append(event)
    return cleaned


def _total_length(lead: LeadSheet, measure_len: float) -> float:
    """Round the score length up to a whole measure."""
    total = lead.total_quarters
    if total <= 0:
        return measure_len
    import math
    measures = max(1, math.ceil(total / measure_len - 1e-9))
    return measures * measure_len


def _split_at_barlines(events: List[LeadNote], measure_len: float) -> List[LeadNote]:
    """Split notes that cross barlines so every event sits inside one measure."""
    if measure_len <= 0:
        return events
    result: List[LeadNote] = []
    for event in events:
        cursor = event.onset
        remaining = event.duration
        while remaining > 1e-9:
            measure_end = (int(cursor / measure_len) + 1) * measure_len
            # Snap cursor to bar grid when just inside due to float error
            if abs(cursor - round(cursor / measure_len) * measure_len) < 1e-7:
                cursor = round(cursor / measure_len) * measure_len
                measure_end = cursor + measure_len
            segment = min(remaining, measure_end - cursor)
            if segment <= 1e-9:
                break
            result.append(LeadNote(onset=cursor, pitch=event.pitch, duration=segment))
            cursor += segment
            remaining -= segment
    return result


def _fill_with_rests(events: List[LeadNote], start: float, end: float) -> List[Tuple[float, str, float, Optional[int]]]:
    """
    Produce a gap-free timeline of ('note'|'rest', onset, duration, pitch) tuples.
    """
    timeline: List[Tuple[float, str, float, Optional[int]]] = []
    cursor = start
    for event in events:
        if event.onset > cursor + 1e-9:
            timeline.append((cursor, "rest", event.onset - cursor, None))
            cursor = event.onset
        elif event.onset < cursor - 1e-9:
            # Overlap: clip
            if event.onset + event.duration <= cursor + 1e-9:
                continue
            event = LeadNote(onset=cursor, pitch=event.pitch,
                             duration=event.onset + event.duration - cursor)
        timeline.append((event.onset, "note", event.duration, event.pitch))
        cursor = event.onset + event.duration
    if end > cursor + 1e-9:
        timeline.append((cursor, "rest", end - cursor, None))
    return timeline


# ---------------------------------------------------------------------------
# Harmony realization
# ---------------------------------------------------------------------------

def _center(spec: InstrumentSpec) -> int:
    return (spec.low + spec.high) // 2


def realize_harmony(
    chords: List[ChordEvent],
    specs: List[InstrumentSpec],
    total: float,
    measure_len: float,
) -> dict:
    """
    Realize chord symbols into per-instrument note events.

    Returns {instrument_name: List[LeadNote]}. The melody spec (index 0) is
    excluded; the bass role receives chord roots, harmony roles receive upper
    chord tones nearest their range center.
    """
    if not chords:
        return {}

    segments = []
    ordered = sorted(chords, key=lambda c: c.onset)
    for i, chord_event in enumerate(ordered):
        start = chord_event.onset
        end = ordered[i + 1].onset if i + 1 < len(ordered) else total
        if end > start:
            segments.append((start, end, chord_event.symbol))

    harmony_specs = [s for s in specs[1:]]
    if not harmony_specs:
        return {}

    parts: dict = {s.name: [] for s in harmony_specs}
    for start, end, symbol in segments:
        pitches = chord_pitches(symbol)
        if not pitches:
            for spec in harmony_specs:
                parts[spec.name].append(LeadNote(onset=start, pitch=0, duration=0))
            continue
        duration = end - start
        used = set()
        assignments: dict = {}

        # Bass first: root (or lowest chord tone) nearest range floor/center
        bass_specs = [s for s in harmony_specs if s.role == "bass"]
        for spec in bass_specs:
            in_range = [p for p in pitches if spec.low <= p <= spec.high]
            if not in_range:
                in_range = [min(pitches, key=lambda p: abs(p - _center(spec)))]
            # Prefer the lowest available pitch for the bass line
            choice = min(in_range, key=lambda p: (p, abs(p - _center(spec))))
            # Bass root preference: try any pitch class matching symbol root at low octave
            parsed = parse_native_chord(symbol)
            if parsed:
                root_pc = parsed[0]
                root_opts = [p for p in range(spec.low, spec.high + 1)
                             if p % 12 == root_pc and p not in used]
                if root_opts:
                    choice = root_opts[len(root_opts) // 2] if len(root_opts) > 2 else root_opts[0]
            assignments[spec.name] = choice
            used.add(choice)

        # Harmony voices: chord tone closest to range center, avoid duplicates
        for spec in harmony_specs:
            if spec.role == "bass" and spec.name in assignments:
                continue
            candidates = [p for p in pitches if spec.low <= p <= spec.high]
            if not candidates:
                candidates = [min(pitches, key=lambda p: abs(p - _center(spec)))]
            free = [p for p in candidates if p not in used] or candidates
            choice = min(free, key=lambda p: abs(p - _center(spec)))
            assignments[spec.name] = choice
            used.add(choice)

        for spec in harmony_specs:
            pitch = assignments.get(spec.name)
            if pitch is None:
                continue
            # Split at barlines for clean measures
            for segment in _split_at_barlines(
                [LeadNote(onset=start, pitch=pitch, duration=duration)], measure_len
            ):
                parts[spec.name].append(segment)

    return {name: _merge_events(events) for name, events in parts.items() if events}


# ---------------------------------------------------------------------------
# Score assembly
# ---------------------------------------------------------------------------

def _make_part(spec: InstrumentSpec, ts, key_obj, metro) -> stream.Part:
    part = stream.Part()
    part.id = spec.name.replace(" ", "_")
    part.partName = spec.name
    part.partAbbreviation = spec.name[:4]

    inst = instrument.Instrument()
    inst.partName = spec.name
    inst.instrumentName = spec.name
    inst.midiProgram = spec.midi_program
    part.insert(0, inst)

    clef_map = {
        "treble": clef.TrebleClef(),
        "alto": clef.AltoClef(),
        "bass": clef.BassClef(),
    }
    part.insert(0, clef_map.get(spec.clef, clef.TrebleClef()))
    part.insert(0, ts)
    part.insert(0, key_obj)
    part.insert(0, metro)
    return part


def _append_events(part: stream.Part, timeline) -> None:
    for onset, kind, duration, pitch in timeline:
        if duration <= 0:
            continue
        if kind == "rest":
            element = note.Rest()
        else:
            element = note.Note()
            element.pitch.midi = int(pitch)
            element.pitch.ps = float(pitch)
        element.duration.quarterLength = duration
        part.insert(onset, element)


def _attach_chords(part: stream.Part, chords: List[ChordEvent]) -> int:
    """Insert ChordSymbol objects; returns how many figures were accepted."""
    attached = 0
    for chord_event in chords:
        figure = chord_event.symbol
        # music21 understands most figures; normalize native-only forms first
        try:
            symbol = harmony.ChordSymbol(figure)
        except Exception:
            native = figure_to_native(figure)
            try:
                symbol = harmony.ChordSymbol(native if native else figure)
            except Exception:
                logger.debug(f"Skipping unrepresentable chord figure: {figure}")
                continue
        try:
            symbol.writeAsChord = False
            part.insert(chord_event.onset, symbol)
            attached += 1
        except Exception:
            logger.debug(f"Failed to insert chord symbol at {chord_event.onset}: {figure}")
    return attached


def build_orchestration_score(
    lead: LeadSheet,
    config: ArrangementConfig,
) -> stream.Score:
    """
    Split a lead sheet into configured instrument parts and build a music21 Score.

    - instruments[0] carries the melody
    - remaining instruments receive realized chord voicings (bass role → roots)
    - chord symbols are attached above the melody part
    """
    if not lead.melody:
        raise ScoreBuildError("Lead sheet has no melody notes to orchestrate")
    if not config.instruments:
        raise ScoreBuildError("ArrangementConfig.instruments must not be empty")

    specs = resolve_roles(config.instruments)
    n, d = meter_to_tuple(lead.meter or "4/4")
    measure_len = 4.0 * n / d
    total = _total_length(lead, measure_len)

    # Key & tempo (config overrides)
    key_obj = native_key_to_m21(lead.key)
    if config.key:
        try:
            requested = _parse_config_key(config.key)
            delta = (requested.tonic.midi - key_obj.tonic.midi) % 12
            if delta > 6:
                delta -= 12
            if delta != 0:
                lead = _transpose_lead(lead, delta)
            key_obj = requested
        except Exception as exc:
            logger.warning(f"Ignoring key override {config.key!r}: {exc}")

    bpm = config.tempo or lead.bpm or 120
    ts = meter.TimeSignature(f"{n}/{d}")
    metro = tempo.MetronomeMark(number=bpm)

    score = stream.Score()
    metadata_title = f"{config.genre} Orchestration"
    try:
        from music21 import metadata as m21meta
        md = m21meta.Metadata()
        md.title = metadata_title
        md.composer = "MaestroPro / Maya Instruments Technology"
        score.insert(0, md)
    except Exception:
        pass

    melody_events = _split_at_barlines(_merge_events(lead.melody), measure_len)
    melody_timeline = _fill_with_rests(melody_events, 0.0, total)

    secondary_events = _split_at_barlines(_merge_events(lead.secondary), measure_len) if lead.secondary else []
    secondary_timeline = _fill_with_rests(secondary_events, 0.0, total) if secondary_events else None

    harmony_parts = realize_harmony(lead.chords, specs, total, measure_len)

    for index, spec in enumerate(specs):
        part = _make_part(spec, ts, key_obj, metro)
        if index == 0:
            _append_events(part, melody_timeline)
            _attach_chords(part, lead.chords)
        elif index == 1 and secondary_timeline and spec.name not in harmony_parts:
            # Second native voice feeds the second instrument when no harmony part claims it
            _append_events(part, secondary_timeline)
        elif spec.name in harmony_parts:
            events = _split_at_barlines(harmony_parts[spec.name], measure_len)
            timeline = _fill_with_rests(events, 0.0, total)
            _append_events(part, timeline)
        else:
            _append_events(part, _fill_with_rests([], 0.0, total))
        score.insert(0, part)

    return score


def _transpose_lead(lead: LeadSheet, semitones: int) -> LeadSheet:
    if not semitones:
        return lead
    from copy import deepcopy
    transposed = deepcopy(lead)
    transposed.melody = [
        LeadNote(onset=n.onset, pitch=max(0, min(127, n.pitch + semitones)), duration=n.duration)
        for n in lead.melody
    ]
    transposed.secondary = [
        LeadNote(onset=n.onset, pitch=max(0, min(127, n.pitch + semitones)), duration=n.duration)
        for n in lead.secondary
    ]
    return transposed


def export_musicxml(score: stream.Score, output_path: Path) -> Path:
    """Write a multi-part score as MusicXML (partwise)."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        score.write("musicxml", fp=str(output_path))
    except Exception as exc:
        raise ScoreBuildError(f"MusicXML export failed: {exc}") from exc
    if not output_path.is_file():
        raise ScoreBuildError(f"MusicXML export produced no file at {output_path}")
    return output_path
