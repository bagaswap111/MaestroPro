"""
MaestroPro - Native ABC Exporter
Maya Instruments Technology
Version: 1.1.0

Converts a (possibly human-edited) music21 Score back into the limited
two-voice ABC dialect understood by YuE2 / abc_tools, so the edited
MusicXML can condition a YuE2 audio mockup preview.

Dialect contract (see yue2-music/scripts/abc_tools.py):
- Header: X:1 / blank T: / M: / L:1/32 / Q:1/4=<int> / exact V: lines / K:
- Two voices: Vocal (melody + chord symbols) and Ins (second line or rests)
- Groups of 1-4 measures; both voices share identical bar grids
- Note durations must decompose into {1,2,3,4,6,8,12,16,24,32,48} units of 1/32
"""

import logging
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from music21 import harmony, key as m21key, meter as m21meter, note, tempo as m21tempo

from backend.orchestration.chords import figure_to_native

logger = logging.getLogger(__name__)

UNITS_PER_QUARTER = 8  # L:1/32 → one quarter = 8 units
ALLOWED_DURATIONS = (48, 32, 24, 16, 12, 8, 6, 4, 3, 2, 1)
NATURAL = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
# Canonical (sharp) letter for each pitch class
PC_LETTERS = ("C", "C", "D", "D", "E", "F", "F", "G", "G", "A", "A", "B")
ACC_MAP = {-2: "__", -1: "_", 0: "=", 1: "^", 2: "^^"}
MEASURES_PER_LINE = 4

VOICE_HEADERS = (
    'V: Vocal clef=treble name="Vocal Melody" snm="Vocal"',
    'V: Ins clef=treble name="Ins Melody" snm="Inst."',
)


class AbcExportError(RuntimeError):
    """Raised when a score cannot be represented in the native ABC dialect."""


@dataclass
class UnitEvent:
    start: int
    dur: int
    pitch: Optional[int]  # None → rest
    tie: bool = False     # tie to the following segment


@dataclass
class ChordAt:
    start: int
    symbol: str


@dataclass
class VoiceTimeline:
    events: List[UnitEvent] = field(default_factory=list)
    chords: List[ChordAt] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Score extraction
# ---------------------------------------------------------------------------

def _part_unit_events(part) -> Tuple[List[UnitEvent], int]:
    """Extract quantized monophonic note/rest events from a music21 Part."""
    raw: List[Tuple[int, int, Optional[int]]] = []  # start, dur, pitch|None
    for element in part.recurse().notesAndRests:
        if isinstance(element, harmony.ChordSymbol):
            continue
        offset = float(element.getOffsetInHierarchy(part))
        start = int(round(offset * UNITS_PER_QUARTER))
        duration = int(round(float(element.duration.quarterLength) * UNITS_PER_QUARTER))
        if duration <= 0:
            continue
        if isinstance(element, note.Rest):
            raw.append((start, duration, None))
        elif isinstance(element, note.Note):
            raw.append((start, duration, int(element.pitch.midi)))
        else:
            # Chord / polyphonic material → top note (native dialect is monophonic)
            try:
                pitches = [p.midi for p in element.pitches]
                raw.append((start, duration, max(pitches) if pitches else None))
            except Exception:
                raw.append((start, duration, None))

    if not raw:
        return [], 0

    raw.sort(key=lambda item: (item[0], -item[1]))
    events: List[UnitEvent] = []
    cursor = 0
    for start, dur, pitch in raw:
        if start < cursor:
            if start + dur <= cursor:
                continue
            dur = start + dur - cursor
            start = cursor
        events.append(UnitEvent(start=start, dur=dur, pitch=pitch))
        cursor = start + dur
    total = cursor
    return events, total


def _fill_rests(events: List[UnitEvent], total: int) -> List[UnitEvent]:
    filled: List[UnitEvent] = []
    cursor = 0
    for event in events:
        if event.start > cursor:
            filled.append(UnitEvent(start=cursor, dur=event.start - cursor, pitch=None))
        filled.append(event)
        cursor = event.start + event.dur
    if total > cursor:
        filled.append(UnitEvent(start=cursor, dur=total - cursor, pitch=None))
    return filled


def _ceil_to_measure(total: int, measure_units: int) -> int:
    if total <= 0:
        return measure_units
    return int(math.ceil(total / measure_units - 1e-9)) * measure_units


def _split_at_times(events: List[UnitEvent], times: List[int], total: int) -> List[UnitEvent]:
    """Split notes/rests at forced boundaries (chord onsets). Notes keep ties."""
    points = sorted({t for t in times if 0 < t < total})
    if not points:
        return events
    result: List[UnitEvent] = []
    for event in events:
        cuts = [p for p in points if event.start < p < event.start + event.dur]
        boundaries = [event.start] + cuts + [event.start + event.dur]
        is_note = event.pitch is not None
        for index in range(len(boundaries) - 1):
            seg_start, seg_end = boundaries[index], boundaries[index + 1]
            if seg_end <= seg_start:
                continue
            continues = seg_end < event.start + event.dur
            result.append(UnitEvent(
                start=seg_start,
                dur=seg_end - seg_start,
                pitch=event.pitch,
                tie=is_note and (continues or event.tie),
            ))
    result.sort(key=lambda e: e.start)
    return result


# ---------------------------------------------------------------------------
# Token emission
# ---------------------------------------------------------------------------

def decompose_duration(units: int) -> List[int]:
    """Decompose a positive duration into allowed native units."""
    if units <= 0:
        raise AbcExportError(f"Non-positive duration {units}")
    pieces: List[int] = []
    remaining = units
    for size in ALLOWED_DURATIONS:
        while remaining >= size:
            pieces.append(size)
            remaining -= size
        if remaining == 0:
            break
    if remaining != 0:
        raise AbcExportError(f"Cannot decompose duration {units}")
    return pieces


def _octave_marks(shift: int) -> Tuple[str, bool]:
    """Return (mark_string, use_lowercase) for an octave shift from C4 (60)."""
    if shift == 0:
        return "", False
    if shift > 0:
        return "'" * (shift - 1) if shift > 1 else "", True
    return "," * (-shift), False


def _pitch_token_parts(pitch: int, key_table: Dict[str, int], local: Dict[str, int]) -> str:
    """Format '<acc><letter><octave>' resolving accidentals against key/bar state."""
    pitch = max(0, min(127, int(pitch)))
    pc = pitch % 12
    letter = PC_LETTERS[pc]
    key_alt = key_table.get(letter, 0)
    base = 60 + NATURAL[letter]
    shift = int(round((pitch - base) / 12.0))
    written = base + 12 * shift
    alt = pitch - written
    # Keep alteration within the dialect's -2..2 range
    while alt > 2:
        shift += 1
        written += 12
        alt = pitch - written
    while alt < -2:
        shift -= 1
        written -= 12
        alt = pitch - written

    current = local.get(letter, key_alt)
    acc = ""
    if current != alt:
        acc = ACC_MAP.get(alt)
        if acc is None:
            raise AbcExportError(f"Unsupported alteration {alt} for pitch {pitch}")
        local[letter] = alt

    marks, lower = _octave_marks(shift)
    emitted_letter = letter.lower() if lower else letter
    return f"{acc}{emitted_letter}{marks}"


def _emit_event(event: UnitEvent, key_table: Dict[str, int], local: Dict[str, int],
                allow_tie: bool) -> List[str]:
    """Token(s) for one event, decomposed into allowed durations with ties."""
    pieces = decompose_duration(event.dur)
    tokens: List[str] = []
    for index, size in enumerate(pieces):
        is_last = index == len(pieces) - 1
        tie = (not is_last) or (event.tie and allow_tie)
        if event.pitch is None:
            tokens.append(f"z{size}")
        else:
            core = _pitch_token_parts(event.pitch, key_table, local)
            tokens.append(f"{core}{size}{'-' if tie else ''}")
    return tokens


# ---------------------------------------------------------------------------
# Key accidental table (native KEYS equivalent)
# ---------------------------------------------------------------------------

def key_accidentals(native_key: str) -> Dict[str, int]:
    """Letter → alteration for a native key name (mirrors abc_tools.key_accidentals)."""
    sharps_order = "FCGDAEB"
    flats_order = "BEADGCF"
    sharp_count = {
        "Cb": -7, "Gb": -6, "Db": -5, "Ab": -4, "Eb": -3, "Bb": -2, "F": -1,
        "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7,
    }
    minor_equivalent = {
        "Abm": -7, "Ebm": -6, "Bbm": -5, "Fm": -4, "Cm": -3, "Gm": -2, "Dm": -1,
        "Am": 0, "Em": 1, "Bm": 2, "F#m": 3, "C#m": 4, "G#m": 5, "D#m": 6, "A#m": 7,
    }
    if native_key in sharp_count:
        count = sharp_count[native_key]
    elif native_key in minor_equivalent:
        count = minor_equivalent[native_key]
    else:
        # Unknown key → treat as C (caller should have validated)
        logger.warning(f"Unknown native key {native_key!r}; assuming C major")
        count = 0
    result = {letter: 0 for letter in NATURAL}
    order = sharps_order if count > 0 else flats_order
    for letter in order[:abs(count)]:
        result[letter] = 1 if count > 0 else -1
    return result


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def extract_chords(score) -> List[ChordAt]:
    """Collect ChordSymbol objects from a score as quantized native chords."""
    chords: List[ChordAt] = []
    for symbol in score.recurse().getElementsByClass(harmony.ChordSymbol):
        try:
            offset = float(symbol.getOffsetInHierarchy(score))
        except Exception:
            offset = float(symbol.offset)
        figure = getattr(symbol, "figure", None) or str(symbol)
        native = figure_to_native(str(figure))
        if native is None:
            logger.debug(f"Dropping chord figure not representable in native ABC: {figure}")
            continue
        chords.append(ChordAt(start=int(round(offset * UNITS_PER_QUARTER)), symbol=native))
    chords.sort(key=lambda c: c.start)
    return chords


def score_to_native_abc(
    score,
    *,
    melody_part_index: int = 0,
    ins_part_index: Optional[int] = 1,
    bpm: Optional[int] = None,
) -> str:
    """
    Export a music21 Score to native two-voice ABC.

    - Part[0] (or melody_part_index) → Vocal voice
    - Part[1] (or None) → Ins voice; missing Ins becomes full-measure rests
    - All ChordSymbol objects → Vocal chord symbols
    """
    parts = list(score.parts)
    if not parts:
        raise AbcExportError("Score has no parts to export")
    if not (0 <= melody_part_index < len(parts)):
        melody_part_index = 0
    melody_part = parts[melody_part_index]
    ins_part = parts[ins_part_index] if (
        ins_part_index is not None and 0 <= ins_part_index < len(parts)
        and ins_part_index != melody_part_index
    ) else None

    # Meter
    ts = score.getTimeSignatures()[0] if score.getTimeSignatures() else None
    if ts is None:
        from music21 import meter as _meter
        ts = _meter.TimeSignature("4/4")
    n, d = int(ts.numerator), int(ts.denominator)
    measure_units = int(round(float(ts.barDuration.quarterLength) * UNITS_PER_QUARTER))
    if measure_units <= 0:
        raise AbcExportError("Invalid measure length")

    # Tempo
    if bpm is None:
        bpm = 120
        marks = list(score.recurse().getElementsByClass(m21tempo.MetronomeMark))
        for mark in marks:
            if mark.number and float(mark.number) > 0:
                bpm = int(round(float(mark.number)))
                break
    bpm = max(20, min(300, int(bpm)))

    # Key
    native_key = "C"
    keys = list(score.recurse().getElementsByClass(m21key.Key))
    if keys:
        try:
            from backend.orchestration.score_builder import m21_key_to_native
            native_key = m21_key_to_native(keys[0])
        except Exception:
            native_key = "C"
    else:
        signatures = list(score.recurse().getElementsByClass(m21key.KeySignature))
        if signatures:
            try:
                as_key = signatures[0].asKey("major")
                from backend.orchestration.score_builder import m21_key_to_native
                native_key = m21_key_to_native(as_key)
            except Exception:
                native_key = "C"
    key_table = key_accidentals(native_key)

    # Melody timeline
    melody_events, melody_total = _part_unit_events(melody_part)
    ins_events, ins_total = _part_unit_events(ins_part) if ins_part is not None else ([], 0)
    chords = extract_chords(score)

    total = _ceil_to_measure(max(melody_total, ins_total, 0), measure_units)
    if total <= 0:
        total = measure_units

    melody_events = _fill_rests(melody_events, total)
    ins_events = _fill_rests(ins_events, total)

    # Force splits at chord onsets so chord tokens land on exact boundaries
    chord_times = [c.start for c in chords if 0 < c.start < total]
    melody_events = _split_at_times(melody_events, chord_times, total)
    # Re-fill in case splits introduced gaps (they should not)
    melody_events = _fill_rests(melody_events, total)

    bar_count = total // measure_units
    vocal_bars: List[str] = []
    ins_bars: List[str] = []

    chords_by_start: Dict[int, List[str]] = {}
    for chord in chords:
        if chord.start >= total:
            logger.debug(f"Chord at {chord.start} beyond score end; dropped")
            continue
        chords_by_start.setdefault(chord.start, []).append(chord.symbol)

    for bar_index in range(bar_count):
        bar_start = bar_index * measure_units
        bar_end = bar_start + measure_units
        vocal_bars.append(_render_bar(
            [e for e in melody_events if e.start < bar_end and e.start + e.dur > bar_start],
            bar_start, bar_end, measure_units, key_table,
            chords_by_start,
        ))
        ins_events_in_bar = [
            e for e in ins_events if e.start < bar_end and e.start + e.dur > bar_start
        ]
        ins_chords: Dict[int, List[str]] = {}  # Ins voice must carry no chords
        ins_bars.append(_render_bar(
            ins_events_in_bar, bar_start, bar_end, measure_units, key_table,
            ins_chords,
        ))

    lines = [
        "X:1",
        "T:",
        f"M:{n}/{d}",
        "L:1/32",
        f"Q:1/4={bpm}",
        VOICE_HEADERS[0],
        VOICE_HEADERS[1],
        f"K:{native_key}",
    ]
    for index in range(0, bar_count, MEASURES_PER_LINE):
        chunk_v = vocal_bars[index:index + MEASURES_PER_LINE]
        chunk_i = ins_bars[index:index + MEASURES_PER_LINE]
        lines.append("V: Vocal")
        lines.append("|".join(chunk_v) + "|")
        lines.append("V: Ins")
        lines.append("|".join(chunk_i) + "|")
    return "\n".join(lines) + "\n"


def _render_bar(
    events: List[UnitEvent],
    bar_start: int,
    bar_end: int,
    measure_units: int,
    key_table: Dict[str, int],
    chords_by_start: Dict[int, List[str]],
) -> str:
    """Render one measure body (without trailing '|')."""
    bar_events = sorted(events, key=lambda e: e.start)
    # Clip events to bar and rebuild a gap-free sequence
    clipped: List[UnitEvent] = []
    cursor = bar_start
    for event in bar_events:
        original_end = event.start + event.dur
        start = max(event.start, bar_start)
        end = min(original_end, bar_end)
        if end <= start:
            continue
        if start > cursor:
            clipped.append(UnitEvent(start=cursor, dur=start - cursor, pitch=None))
            cursor = start
        # A note continuing past this bar must tie over the barline
        continues = original_end > end
        clipped.append(UnitEvent(
            start=cursor,
            dur=end - cursor,
            pitch=event.pitch,
            tie=event.pitch is not None and (event.tie or continues),
        ))
        cursor = end
    if cursor < bar_end:
        clipped.append(UnitEvent(start=cursor, dur=bar_end - cursor, pitch=None))

    total_dur = sum(e.dur for e in clipped)
    if total_dur != measure_units:
        raise AbcExportError(
            f"Bar at {bar_start} sums to {total_dur} units, expected {measure_units}"
        )

    bar_has_chords = any(bar_start <= t < bar_end for t in chords_by_start)
    only_rests = all(e.pitch is None for e in clipped)
    if only_rests and not bar_has_chords:
        return "Z"

    local: Dict[str, int] = {}
    tokens: List[str] = []
    for event in clipped:
        for symbol in chords_by_start.get(event.start, []):
            if bar_start <= event.start < bar_end:
                tokens.append(f'"{symbol}"')
        tokens.extend(_emit_event(event, key_table, local, allow_tie=True))

    rendered = "".join(tokens)
    # Validate duration by replaying token durations
    _validate_bar_tokens(tokens, measure_units)
    return rendered


def _validate_bar_tokens(tokens: List[str], measure_units: int) -> None:
    """Replay duration numbers of a rendered bar (chord quotes are zero-width)."""
    import re
    total = 0
    for token in tokens:
        if token.startswith('"'):
            continue
        match = re.fullmatch(r"(?:[=^_]{0,2}[A-Ga-g])(?:[',]*)(\d+)(-?)", token)
        if not match:
            # rests: z<dur>
            match = re.fullmatch(r"z(\d+)", token)
            if not match:
                raise AbcExportError(f"Unparseable emitted token: {token!r}")
        total += int(match.group(1))
    if total != measure_units:
        raise AbcExportError(f"Emitted bar sums to {total}, expected {measure_units}")


def validate_native_abc(abc_text: str) -> dict:
    """Structural validation through the shared abc_tools parser."""
    from backend.orchestration.abc_bridge import validate_abc
    return validate_abc(abc_text)
