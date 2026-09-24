"""
MaestroPro - Chord Symbol Conversion
Maya Instruments Technology
Version: 1.1.0

Maps music21 chord figures to the quality vocabulary of the native ABC dialect
used by SheetSage2/YuE2 (see yue2-music/scripts/abc_tools.py QUALITIES).
"""

import re
from typing import Optional, Tuple

# Native dialect qualities (must stay aligned with abc_tools.QUALITIES)
NATIVE_QUALITIES = (
    "", "m", "dim", "aug", "7", "maj7", "m7", "dim7", "m7b5",
    "sus4", "sus2", "6", "m6", "7sus4", "m(maj7)",
)

# Normalizations applied to the figure suffix after the root
_SUFFIX_ALIASES = {
    "minor": "m",
    "min": "m",
    "-": "m",
    "major": "",
    "maj": "",
    "M7": "maj7",
    "Δ": "maj7",
    "Δ7": "maj7",
    "major7": "maj7",
    "min7": "m7",
    "minor7": "m7",
    "-7": "m7",
    "dim": "dim",
    "o": "dim",
    "°": "dim",
    "diminished": "dim",
    "aug": "aug",
    "+": "aug",
    "augmented": "aug",
    "min7b5": "m7b5",
    "ø": "m7b5",
    "/2": "sus2",
    "sus": "sus4",
    "sus4": "sus4",
    "sus2": "sus2",
    "sus24": "7sus4",
    "7sus": "7sus4",
    "7sus4": "7sus4",
    "minmaj7": "m(maj7)",
    "mM7": "m(maj7)",
    "m(maj7)": "m(maj7)",
}

_ROOT_RE = re.compile(
    r"^(?P<root>[A-G](?:#|b|bb|##)?)(?P<rest>.*?)(?:/(?P<bass>[A-G](?:#|b|bb|##)?))?$"
)


def normalize_root(name: str) -> Optional[str]:
    """Normalize a pitch spelling to native form ('F#', 'Bb', 'C')."""
    name = name.strip().replace("-", "b").replace("♯", "#").replace("♭", "b")
    match = re.fullmatch(r"([A-G])(#{1,2}|b{1,2})", name)
    if match:
        return f"{match.group(1)}{match.group(2)}"
    if re.fullmatch(r"[A-G]", name):
        return name
    return None


def figure_to_native(figure: str) -> Optional[str]:
    """
    Convert a music21-style chord figure ('Cmaj7', 'F#m7b5', 'Bb7sus4', 'C/G')
    to the native ABC chord symbol. Returns None when unsupported.
    """
    if not figure or not figure.strip():
        return None
    text = figure.strip()
    # Common text forms music21 may emit
    text = text.replace("minor", "m").replace("major", "") if text in (
        "Cminor", "Cmajor"
    ) else text

    match = _ROOT_RE.match(text)
    if not match:
        return None
    root = normalize_root(match.group("root"))
    if root is None:
        return None
    rest = (match.group("rest") or "").strip()
    bass_raw = match.group("bass")
    bass = normalize_root(bass_raw) if bass_raw else None

    suffix = _normalize_suffix(rest)
    if suffix is None:
        return None

    symbol = f"{root}{suffix}"
    if bass and bass != root:
        symbol = f"{symbol}/{bass}"
    return symbol


def _normalize_suffix(rest: str) -> Optional[str]:
    if rest == "":
        return ""
    if rest in NATIVE_QUALITIES:
        return rest
    lowered = rest.lower() if rest not in _SUFFIX_ALIASES else rest
    if rest in _SUFFIX_ALIASES:
        return _SUFFIX_ALIASES[rest]
    if lowered in _SUFFIX_ALIASES:
        return _SUFFIX_ALIASES[lowered]
    # Try progressive cleanup: strip 'maj'/'min' decorations
    candidates = {
        rest.replace("major", "").replace("maj", "maj7" if "7" in rest else "").strip(),
        rest.replace("min", "m").replace("or", ""),
    }
    for candidate in candidates:
        if candidate in NATIVE_QUALITIES:
            return candidate
        if candidate in _SUFFIX_ALIASES:
            return _SUFFIX_ALIASES[candidate]
    return None


# Chord quality → pitch-class intervals above the root (semitones)
_QUALITY_INTERVALS = {
    "": (0, 4, 7),
    "m": (0, 3, 7),
    "dim": (0, 3, 6),
    "aug": (0, 4, 8),
    "7": (0, 4, 7, 10),
    "maj7": (0, 4, 7, 11),
    "m7": (0, 3, 7, 10),
    "dim7": (0, 3, 6, 9),
    "m7b5": (0, 3, 6, 10),
    "sus4": (0, 5, 7),
    "sus2": (0, 2, 7),
    "6": (0, 4, 7, 9),
    "m6": (0, 3, 7, 9),
    "7sus4": (0, 5, 7, 10),
    "m(maj7)": (0, 3, 7, 11),
}

_ROOT_PC = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def parse_native_chord(symbol: str) -> Optional[Tuple[int, str, Optional[int]]]:
    """
    Parse a native chord symbol into (root_pc, quality, bass_pc|None).
    """
    match = _ROOT_RE.match(symbol.strip())
    if not match:
        return None
    root = normalize_root(match.group("root"))
    if root is None:
        return None
    rest = (match.group("rest") or "").strip()
    suffix = _normalize_suffix(rest)
    if suffix is None:
        return None
    bass_raw = match.group("bass")
    bass_pc = None
    if bass_raw:
        bass = normalize_root(bass_raw)
        if bass is None:
            return None
        bass_pc = _pc_of(bass)
    return _pc_of(root), suffix, bass_pc


def _pc_of(spelling: str) -> int:
    letter = spelling[0]
    pc = _ROOT_PC[letter]
    i = 1
    while i < len(spelling):
        pc += 1 if spelling[i] == "#" else -1
        i += 1
    return pc % 12


def chord_pitches(symbol: str) -> Optional[list]:
    """
    Return candidate MIDI pitches (ascending, spanning ~C2–C6) for a native
    chord symbol, or None when the symbol cannot be realized.
    """
    parsed = parse_native_chord(symbol)
    if parsed is None:
        return None
    root_pc, quality, bass_pc = parsed
    intervals = _QUALITY_INTERVALS.get(quality, _QUALITY_INTERVALS[""])

    pcs = []
    for iv in intervals:
        pc = (root_pc + iv) % 12
        if pc not in pcs:
            pcs.append(pc)
    if bass_pc is not None and bass_pc not in pcs:
        pcs = [bass_pc] + pcs

    pitches = []
    # Span roughly two and a half octaves from C2 (36) upward
    for base in (36, 48, 60, 72, 84):
        for pc in pcs:
            pitch = base + pc
            if 36 <= pitch <= 96:
                pitches.append(pitch)
    pitches = sorted(set(pitches))
    # Ensure bass note available at bottom when specified
    if bass_pc is not None:
        bass_candidates = [p for p in range(36, 60) if p % 12 == bass_pc]
        if bass_candidates:
            pitches = [bass_candidates[0]] + [p for p in pitches if p != bass_candidates[0]]
            pitches = sorted(set(pitches))
    return pitches or None
