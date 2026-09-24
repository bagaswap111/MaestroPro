---
title: "Practical Scripting for Arrangers"
tier: "Workflow & Portfolio"
subject: "Python Scripting Automation"
xml_tags: ["score-partwise", "note", "pitch", "transpose", "duration"]
software: ["Python", "music21", "MuseScore", "Dorico"]
---

# Chapter 2 — Practical Scripting for Arrangers

> **Guidebook for this chapter:** music21 documentation; automation practices from
> the MIDI workflow (quantization — link to
> `../../04-MusicXML-Masterclass/4.3-Playback-MIDI-Integration/Ch2-MIDI-Quantization.md`).
> Focus: 5 scripts that solve an arranger's daily work.

## 2.1 Common Case Scenarios

| # | Scenario | Benefit |
|---|----------|---------|
| 1 | Batch transposition | Move entire parts at once |
| 2 | Part splitting | 1 file per instrument for print parts |
| 3 | Template generator | 100+ part orchestra skeleton instantly |
| 4 | Range validation | Flag notes outside range |
| 5 | MIDI normalization | Clean up imported MIDI files |

## 2.2 Script A: Batch Transposition

```python
from pathlib import Path
from music21 import converter

for xml_path in Path('scores').glob('*.musicxml'):
    score = converter.parse(str(xml_path))
    score.transpose('M2', inPlace=True)
    out = xml_path.with_name(xml_path.stem + '_transposed.musicxml')
    score.write('musicxml', fp=str(out))
    print('Done:', out.name)
```

**Note:** for per-instrument transposing parts see
`../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`.

## 2.3 Script B: Part Splitting

```python
from music21 import converter, stream

score = converter.parse('full_score.musicxml')

for i, part in enumerate(score.parts):
    single = stream.Score()
    single.insert(0, part)
    safe_name = part.partName or f"part_{i}"
    safe_name = "".join(c for c in safe_name if c.isalnum() or c in " _-")
    single.write('musicxml', fp=f"parts/{safe_name}.musicxml")
```

## 2.4 Script C: Orchestra Template

```python
from music21 import stream, instrument, meter, key

TEMPLATE = [
    ("Flute 1", "Fl.1", 73, 1),       # (name, abbr, mgm, channel)
    ("Oboe 1", "Ob.1", 68, 2),
    ("Clarinet Bb 1", "Cl.1", 71, 3),
    ("Bassoon 1", "Bsn.1", 70, 4),
    ("Horn in F 1", "Hn.1", 60, 5),
    ("Trumpet Bb 1", "Tpt.1", 56, 6),
    ("Trombone 1", "Tbn.1", 57, 7),
    ("Percussion", "Perc.", 0, 10),
    ("Violin I", "Vl.I", 40, 9),
    ("Viola", "Vla.", 41, 10),
    ("Cello", "Vc.", 42, 11),
    ("Double Bass", "Db.", 43, 12),
]

def build_template():
    score = stream.Score()
    for name, abbr, prog, ch in TEMPLATE:
        part = stream.Part()
        part.partName = name
        part.partAbbreviation = abbr
        inst = instrument.Instrument(midiProgram=prog, midiChannel=ch)
        part.append(inst)
        part.append(key.Key('C'))
        part.append(meter.TimeSignature('4/4'))
        score.append(part)
    return score

tpl = build_template()
tpl.write('musicxml', fp='orchestra_template.musicxml')
```

> **Percussion channel 10** is GM-specific; use `midiProgram=0` (perc). For
> hi-hat/snare refer to `Ch4-Notasi-Percussion`.

## 2.5 Script D: Range Validation

```python
RANGES = {
    "Flute": ("C4", "D7"),
    "Oboe": ("Bb3", "A6"),
    "Clarinet Bb 1": ("D3", "A6"),
    "Horn in F 1": ("F2", "F5"),
}

for part in score.parts:
    lo, hi = RANGES.get(part.partName, (None, None))
    if lo is None:
        continue
    lo_p = note.Note(lo).pitch
    hi_p = note.Note(hi).pitch
    for n in part.recurse().notes:
        if not lo_p <= n.pitch <= hi_p:
            print(f"[{part.partName}] out:", n.pitch, 'bar', n.measureNumber)
```

> Ranges follow Adler/Rimsky from Tier 1 (`Ch1-Keluarga-Instrumen-Ranges`).

## 2.6 Script E: MIDI-Import Normalization

```python
midi = converter.parse('draft.mid')
midi.quantize(quantizationUnit=0.5)

from music21 import stream
cleaned = stream.Stream()
for n in midi.flatten().notes:
    if n.quarterLength >= 0.125:      # discard ghosts < 1/32
        cleaned.append(n)
cleaned.write('musicxml', fp='cleaned.musicxml')
```

> Quantization reference: `../../04-MusicXML-Masterclass/4.3-Playback-MIDI-Integration/Ch2-MIDI-Quantization.md`.

## 2.7 Workflow Recommendations

1. Keep scripts in `scripts/` + `requirements.txt`.
2. Use `argparse` for CLI-friendliness.
3. Run in bulk with `concurrent.futures` when there are many files.
4. Always validate output by re-parsing (MuseScore round-trip).

## 2.8 Misconceptions

- **"Scripting replaces the ear"** — Automation speeds up
  mechanical tasks; musical decisions remain human.
- **"`quantize` fixes everything"** — It cannot fix severely
  off timing; combine loops + manual edits.
- **"A template is made once forever"** — Update it whenever ranges or
  new instruments change.

## 2.9 Exercises

1. Run Script A on 3 files → check the results in an editor.
2. Build Script D with ranges for 10 instruments → run it on your work.
3. Integrate Script C + part splitting → a complete orchestra workflow.
4. Extract chordify + roman numeral for quick analysis (from Ch1).

## 2.10 Practical Checklist

| Check | Yes/No |
|-------|--------|
| Script tested on a small file first? | |
| Output path/folder clear? | |
| Output validated (re-parsed)? | |
| Error logging + exception handling? | |
| Dependencies documented? | |

## 2.11 References

- *music21 docs*: https://web.mit.edu/music21/userGuide/
- Cutbirth/Ariza.
- Tier 4 quantization reference.

---

**Summary:** 5 practical scripts — batch transposition, part splitting, templates,
range validation, MIDI normalization — automate the arranger's repetitive work.
Test small → scale up → validate output.
