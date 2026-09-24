"""
MaestroPro - Native ABC Bridge
Maya Instruments Technology
Version: 1.1.0

Loads the limited two-voice ABC dialect used by SheetSage2 and YuE2 (the
portable abc_tools module from the yue2-music skill) and converts transcriptions
into a simple lead-sheet structure the orchestration pipeline can consume.
"""

import importlib.util
import logging
import sys
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import List, Optional

from backend.config import settings

logger = logging.getLogger(__name__)

_abc_tools_module = None


class AbcBridgeError(RuntimeError):
    """Raised when the native ABC bridge cannot be loaded or parsed."""


def load_abc_tools(skill_dir: Optional[Path] = None):
    """Import abc_tools.py from the yue2-music skill directory (cached)."""
    global _abc_tools_module
    skill_dir = Path(skill_dir or settings.SHEETSAGE2_SKILL_DIR)
    script = skill_dir / "scripts" / "abc_tools.py"
    if not script.is_file():
        raise AbcBridgeError(f"abc_tools.py not found at {script}")

    if _abc_tools_module is not None:
        return _abc_tools_module

    spec = importlib.util.spec_from_file_location("maestropro_abc_tools", script)
    if spec is None or spec.loader is None:
        raise AbcBridgeError(f"Cannot load module spec from {script}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["maestropro_abc_tools"] = module
    spec.loader.exec_module(module)
    _abc_tools_module = module
    return module


@dataclass
class LeadNote:
    onset: float      # quarter notes from start
    pitch: int        # MIDI
    duration: float   # quarter notes


@dataclass
class ChordEvent:
    onset: float      # quarter notes from start
    symbol: str       # native chord symbol, e.g. "Cmaj7"


@dataclass
class LeadSheet:
    """Parsed SheetSage2 transcription (melody + chords + metadata)."""

    bpm: int
    meter: str                 # e.g. "4/4"
    key: str                   # native key, e.g. "C", "Am", "Eb"
    melody: List[LeadNote] = field(default_factory=list)
    secondary: List[LeadNote] = field(default_factory=list)
    chords: List[ChordEvent] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    abc_text: str = ""
    melody_voice: str = "Vocal"
    duration_quarters: float = 0.0

    @property
    def total_quarters(self) -> float:
        ends = [self.duration_quarters]
        if self.melody:
            ends.append(max(n.onset + n.duration for n in self.melody))
        if self.secondary:
            ends.append(max(n.onset + n.duration for n in self.secondary))
        if self.chords:
            ends.append(max(c.onset for c in self.chords))
        return max(ends)


def _to_float(value) -> float:
    if isinstance(value, Fraction):
        return float(value)
    return float(value)


def parse_lead_sheet(
    abc_text: str,
    *,
    melody_voice: str = "Vocal",
    warnings: Optional[List[str]] = None,
) -> LeadSheet:
    """
    Parse native two-voice ABC (SheetSage2 output) into a LeadSheet.

    The requested melody voice is used when it has notes; otherwise the other
    voice is promoted so an empty Vocal part does not produce an empty score.
    """
    tools = load_abc_tools()
    try:
        score = tools.parse_abc(abc_text)
    except Exception as exc:
        raise AbcBridgeError(f"Native ABC parse failed: {exc}") from exc

    def notes_of(name: str) -> List[LeadNote]:
        voice = score.voices[name]
        return [
            LeadNote(onset=_to_float(t), pitch=int(p), duration=_to_float(d))
            for t, p, d in voice.notes
        ]

    primary_name = melody_voice if melody_voice in score.voices else "Vocal"
    other_name = "Ins" if primary_name == "Vocal" else "Vocal"

    melody = notes_of(primary_name)
    secondary = notes_of(other_name)
    used_voice = primary_name
    if not melody and secondary:
        melody, secondary = secondary, melody
        used_voice = other_name

    vocal = score.voices["Vocal"]
    chords = [ChordEvent(onset=_to_float(t), symbol=str(sym)) for t, sym in vocal.chords]

    n, d = vocal.meter
    key = vocal.key if vocal.key else "C"
    total = _to_float(vocal.time)

    return LeadSheet(
        bpm=int(score.bpm),
        meter=f"{n}/{d}",
        key=key,
        melody=melody,
        secondary=secondary,
        chords=chords,
        warnings=list(warnings or []),
        abc_text=abc_text,
        melody_voice=used_voice,
        duration_quarters=total,
    )


def strip_chords(abc_text: str) -> str:
    """Remove chord symbols from native ABC (required for YuE2 cot='melody')."""
    tools = load_abc_tools()
    return tools.strip_chords(abc_text)


def validate_abc(abc_text: str) -> dict:
    """Structural check of native ABC; returns the abc_tools report dict."""
    tools = load_abc_tools()
    score = tools.parse_abc(abc_text)
    return tools.report(score)
