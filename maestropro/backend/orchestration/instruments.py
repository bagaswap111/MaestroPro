"""
MaestroPro - Instrument Presets
Maya Instruments Technology
Version: 1.1.0

Registry used when splitting a SheetSage2 lead sheet into per-instrument parts.
Ranges are concert pitch MIDI note numbers.
"""

from dataclasses import dataclass
from typing import Dict, Optional


# Common MIDI pitch-name helpers (C4 = 60 = middle C)
_PITCH_BASE = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def pitch_from_name(name: str) -> int:
    """Convert scientific pitch names like 'C2', 'F#3', 'Bb4' to MIDI numbers."""
    letter = name[0].upper()
    idx = 1
    alteration = 0
    while idx < len(name) and name[idx] in "#b":
        alteration += 1 if name[idx] == "#" else -1
        idx += 1
    octave = int(name[idx:])
    return (octave + 1) * 12 + _PITCH_BASE[letter] + alteration


@dataclass(frozen=True)
class InstrumentSpec:
    name: str
    clef: str            # "treble" | "alto" | "bass"
    low: int             # MIDI range floor (concert)
    high: int            # MIDI range ceiling
    midi_program: int    # General MIDI program
    role: str = "harmony"  # "melody" | "bass" | "harmony"


def _spec(name, clef, low_name, high_name, program, role="harmony") -> InstrumentSpec:
    return InstrumentSpec(
        name=name, clef=clef,
        low=pitch_from_name(low_name), high=pitch_from_name(high_name),
        midi_program=program, role=role,
    )


INSTRUMENT_PRESETS: Dict[str, InstrumentSpec] = {
    # Strings
    "Violin I": _spec("Violin I", "treble", "G3", "E7", 40, "melody"),
    "Violin II": _spec("Violin II", "treble", "G3", "E7", 40),
    "Violin": _spec("Violin", "treble", "G3", "E7", 40, "melody"),
    "Viola": _spec("Viola", "alto", "C3", "A6", 41),
    "Cello": _spec("Cello", "bass", "C2", "A5", 42, "bass"),
    "Contrabass": _spec("Contrabass", "bass", "E1", "G4", 43, "bass"),
    "Double Bass": _spec("Double Bass", "bass", "E1", "G4", 43, "bass"),
    "String Quartet": _spec("String Quartet", "treble", "G3", "E7", 48),
    # Woodwinds
    "Flute": _spec("Flute", "treble", "C4", "C7", 73, "melody"),
    "Piccolo": _spec("Piccolo", "treble", "D5", "C8", 72),
    "Oboe": _spec("Oboe", "treble", "Bb3", "G6", 68, "melody"),
    "Clarinet": _spec("Clarinet", "treble", "D3", "C7", 71),
    "Bassoon": _spec("Bassoon", "bass", "Bb1", "E5", 70, "bass"),
    # Brass
    "Horn": _spec("Horn", "treble", "F2", "F6", 60),
    "Horn in F": _spec("Horn in F", "treble", "F2", "F6", 60),
    "Trumpet": _spec("Trumpet", "treble", "F#3", "D6", 56, "melody"),
    "Trombone": _spec("Trombone", "bass", "E2", "Bb4", 57, "bass"),
    "Tuba": _spec("Tuba", "bass", "D1", "F4", 58, "bass"),
    # Keys / fretted
    "Piano": _spec("Piano", "treble", "A0", "C8", 0),
    "Acoustic Grand Piano": _spec("Acoustic Grand Piano", "treble", "A0", "C8", 0),
    "Nylon Guitar": _spec("Nylon Guitar", "treble", "E3", "E6", 24),
    "Acoustic Guitar": _spec("Acoustic Guitar", "treble", "E3", "E6", 25),
    "Electric Guitar": _spec("Electric Guitar", "treble", "E3", "E6", 27),
    "Acoustic Bass": _spec("Acoustic Bass", "bass", "E1", "G4", 32, "bass"),
    "Electric Bass": _spec("Electric Bass", "bass", "E1", "G4", 33, "bass"),
    "Bass Guitar": _spec("Bass Guitar", "bass", "E1", "G4", 33, "bass"),
    # Fallback
    "Melody": _spec("Melody", "treble", "C3", "C6", 73, "melody"),
}

DEFAULT_SPEC = InstrumentSpec(
    name="Part", clef="treble",
    low=pitch_from_name("C3"), high=pitch_from_name("C6"),
    midi_program=0, role="harmony",
)

_BASS_NAME_HINTS = (
    "bass", "cello", "contrabass", "tuba", "bassoon", "trombone",
    "left hand", "acoustic bass",
)


def get_instrument_spec(name: str, *, default_role: str = "harmony") -> InstrumentSpec:
    """
    Look up an instrument preset. Unknown names fall back to DEFAULT_SPEC with a
    range inferred from common naming hints (e.g. anything containing 'bass').
    """
    preset = INSTRUMENT_PRESETS.get(name.strip())
    if preset is not None:
        if default_role == "melody" and preset.role != "bass":
            return InstrumentSpec(
                name=preset.name, clef=preset.clef, low=preset.low,
                high=preset.high, midi_program=preset.midi_program, role="melody",
            )
        return preset

    lowered = name.lower()
    if any(hint in lowered for hint in _BASS_NAME_HINTS):
        return InstrumentSpec(
            name=name, clef="bass",
            low=pitch_from_name("E1"), high=pitch_from_name("G4"),
            midi_program=32, role="bass",
        )
    if default_role == "melody":
        return InstrumentSpec(
            name=name, clef=DEFAULT_SPEC.clef, low=DEFAULT_SPEC.low,
            high=DEFAULT_SPEC.high, midi_program=DEFAULT_SPEC.midi_program,
            role="melody",
        )
    return InstrumentSpec(
        name=name, clef=DEFAULT_SPEC.clef, low=DEFAULT_SPEC.low,
        high=DEFAULT_SPEC.high, midi_program=DEFAULT_SPEC.midi_program,
        role="harmony",
    )


def resolve_roles(instruments: list) -> list:
    """
    Assign roles for the split: first instrument = melody, remaining bass-named
    instruments = bass, everything else = harmony. Returns InstrumentSpec list.
    """
    specs = []
    for index, name in enumerate(instruments):
        if index == 0:
            specs.append(get_instrument_spec(name, default_role="melody"))
        else:
            specs.append(get_instrument_spec(name))
    # Ensure at least one bass voice when possible
    if not any(s.role == "bass" for s in specs[1:]):
        for i, spec in enumerate(specs[1:], start=1):
            if spec.role != "melody":
                specs[i] = InstrumentSpec(
                    name=spec.name, clef=spec.clef, low=spec.low, high=spec.high,
                    midi_program=spec.midi_program, role="bass",
                )
                break
    return specs
