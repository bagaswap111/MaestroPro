---
title: "Python & Music21 — Basics"
tier: "Workflow & Portfolio"
subject: "Python Scripting Automation"
xml_tags: ["score-partwise", "note", "pitch", "duration", "stream"]
software: ["Python", "music21", "Jupyter"]
---

# Chapter 1 — Python & Music21: Basics

> **Guidebook for this chapter:** Michael Cutbirth *et al.*, *music21 documentation*
> (musdomain); Algorithmic Composition Tier 3 materials
> (`../../03-Doctoral-S3-Riset/3.2-Komposisi-Algoritmik/`). Focus: core
> music21 objects for reading & writing MusicXML.

## 1.1 Setup

```bash
pip install music21
pip install jupyter          # optional
```

Verification:

```python
import music21
print(music21.__version__)
```

> music21 requires a musical environment (MuseScore) for
> `show()`; for GUI-free analysis `show('text')` suffices.

## 1.2 Core music21 Objects

| Object | Meaning | Example |
|--------|---------|---------|
| `Stream` | Container | Score, Part, Measure |
| `Measure` | Bar | `Measure(1)` |
| `Note` | Single pitch | `Note('C4')` |
| `Chord` | Collection of pitches | `Chord(['C4','G4'])` |
| `Key` / `KeySignature` | Tonality | `Key('C')` |
| `Meter.TimeSignature` | Meter | `Meter.TimeSignature('4/4')` |

**Hierarchy:** `Stream.Score` > `Stream.Part` > `Stream.Measure` > `Note/Chord`.

## 1.3 Creating a Mini Score

```python
from music21 import stream, note, chord, key, meter

s = stream.Score()
piano = stream.Part()
piano.partName = "Piano"

piano.append(key.KeySignature(0))      # 0 sharps → C major
piano.append(meter.TimeSignature('4/4'))

for p in ['C4', 'E4', 'G4', 'C5']:
    piano.append(note.Note(p, quarterLength=1))

s.insert(0, piano)
s.write('musicxml', fp='mini.musicxml')
```

> `key.KeySignature(0)` vs `key.Key('C')` — Key marks tonality (with
> consequences for `analyze('key')` analysis); KeySignature is only accidentals.

## 1.4 Reading a Score (Parse)

```python
from music21 import converter

score = converter.parse('karya.musicxml')
for part in score.parts:
    print(part.partName, len(part.notes))
```

Options `format='musicxml'`, `format='midi'`, or `corpus.parse('number')`
for the built-in corpus (fugue/chorale).

## 1.5 Traversing a Stream (Recurse)

```python
for el in score.recurse():
    if el.isNote:
        print('Note', el.pitch, el.quarterLength)
    elif el.isChord:
        print('Chord', el.pitches, el.quarterLength)
    elif el.isRest:
        print('Rest', el.quarterLength)
```

> **Important:** `recurse()` traverses **all** levels (Part→Measure→Note);
> for a single part use `part.recurse().notes`.

## 1.6 Basic Analysis

```python
# Key
print(score.analyze('key'))

# Roman numeral progression for each chord
from music21 import roman
for c in score.chordify().flat.getElementsByClass('Chord'):
    rn = roman.romanNumeralFromChord(c, score.analyze('key'))
    print(rn.figure, c.pitches)
```

> `chordify()` turns the entire content into a chord sequence — handy for
> quick harmonic analysis.

## 1.7 Transposition & Transformation

```python
score.transpose('M2', inPlace=True)   # up a major 2nd
score.write('musicxml', fp='trans.musicxml')
```

> For transposing parts (B♭/F/E♭ instruments), use `instrument` +
> the transpose attribute, not just `score.transpose` (see
> `../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`).

## 1.8 Masking & Copy (Subset)

```python
import copy
subset = copy.deepcopy(score.measures(1, 8))
subset.write('musicxml', fp='intro.xml')
```

> `deepcopy` is mandatory if you will modify the subset without corrupting the source.

## 1.9 Misconceptions

- **"`score.transpose` automatically handles instrument transposition"** — No;
  per-instrument part transposition is governed by the instrument's `transpose` attribute.
- **"`analyze('key')` is always correct"** — It's a heuristic; in ambiguous
  passages it can be wrong — correct manually.
- **"All elements are Notes"** — There are `Expression`, `Spanner`, `Clef` etc.;
  filter with `is*` methods.

## 1.10 Exercises

1. Create a 4-bar mini-score in C major → write musicxml.
2. Parse any file → count Notes vs Chords per part.
3. Transpose to F → write.
4. Extract bars 1–4 → add a pickup → measure the total duration.

## 1.11 Basic Checklist

| Check | Yes/No |
|-------|--------|
| music21 installed? | |
| Can create a `Stream`→`write('musicxml')`? | |
| Can parse a MusicXML/MIDI file? | |
| Can iterate `recurse()` and filter? | |
| Transpose/transform tested successfully? | |

## 1.12 References

- Cutbirth et al., *music21 documentation*: https://web.mit.edu/music21/
- Cuthbert & Ariza, *music21: A Toolkit for Computer-Aided Musical Scoring*.
- Continue to [Practical Scripting (`Ch2-Scripting-Praktis.md`)].

---

**Summary:** music21 provides Stream/Part/Measure objects, parse/write
MusicXML, and basic analysis (key, chordify, roman numeral). Master the initial
template → transformation → debugging.
