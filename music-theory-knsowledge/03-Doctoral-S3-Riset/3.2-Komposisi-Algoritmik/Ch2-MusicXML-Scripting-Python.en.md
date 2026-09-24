---
title: "MusicXML Scripting with Python"
tier: "Doctoral S3"
subject: "Algorithmic Composition"
xml_tags: ["score-partwise", "part-list", "measure", "note", "pitch", "duration"]
software: ["Python", "music21", "OpenMusic", "lxml"]
---

# Chapter 2 — MusicXML Scripting with Python

> **Guide books for this chapter:** Cuthbert & Ariza (*music21*), IRCAM/OpenMusic
> practices, *MusicXML Specification* (makemusic). Focus: building and
> validating MusicXML files programmatically.

## 2.1 Why Script MusicXML?

- 100+ instrument orchestral templates without manual repetition.
- Batch transformations (transposition, reharmonization, re-notching).
- Integration with analysis/algorithmic systems (see
  `Ch1-Dasar-Komposisi-Algoritmik.md`).

## 2.2 Basic MusicXML Structure (Refresher)

`score-partwise` file:

```xml
<?xml version="1.0"?>
<score-partwise version="4.0">
  <work><work-title>Contoh</work-title></work>
  <part-list>
    <score-part id="P1">
      <part-name>Piano</part-name>
      <score-instrument id="P1-I1"><instrument-name>Grand Piano</instrument-name></score-instrument>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Full details: `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch1-Struktur-Root-Partwise.md`.

## 2.3 music21 as a Generator

```python
from music21 import stream, note, pitch, chord, key, meter

s = stream.Score()
piano = stream.Part()
piano.partName = "Piano"
piano.append(meter.TimeSignature('4/4'))
piano.append(key.Key('C'))

for n in ['C4', 'E4', 'G4', 'B4']:
    piano.append(note.Note(n, quarterLength=1))

s.insert(0, piano)
s.write('musicxml', fp='keluaran.musicxml')
```

## 2.4 Writing from Raw Data

```python
from music21 import stream, note

data = [("C4", 0.25), ("D4", 0.25), ("E4", 0.5),
        ("F4", 0.25), ("G4", 0.25), ("C5", 1.0)]

part = stream.Part()
for pitch_str, ql in data:
    part.append(note.Note(pitch_str, quarterLength=ql))

part.write('musicxml', fp='melodi.xml')
```

> Durations in quarterLength; `divisions` chosen by music21 automatically.

## 2.5 Reading and Transforming

```python
from music21 import converter

score = converter.parse('partitur.musicxml')
key_obj = score.analyze('key')
for part in score.parts:
    print(part.partName, len(part.notes))
score.write('musicxml', fp='transpos.musicxml')
```

Part-level vs instrument transposition:
`../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`.

## 2.6 Common Pattern: Template Generator

```
schema (part list + instruments)
        │
        ▼
score = build_template(parts)
        │
        ▼
insert data (harmony/melody)
        │
        ▼
add notations & expressions
        │
        ▼
write('musicxml')
```

### 2.6.1 Part Helper

```python
from music21 import stream, instrument

def make_part(name, abbr, clef='G', program=0):
    p = stream.Part()
    p.partName = name
    p.partAbbreviation = abbr
    p.append(instrument.Instrument(
        midiProgram=program, midiChannel=1,
        soundingPitch=None, pitchRange=None))
    return p
```

## 2.7 Validation & Debugging (Round-trip)

### 2.7.1 XSD Validation

```python
from lxml import etree

def validasi(path, xsd_path='musicxml.xsd'):
    schema = etree.XMLSchema(etree.parse(xsd_path))
    return schema.validate(etree.parse(path))
```

### 2.7.2 Round-trip Test

```python
import tempfile
from music21 import converter

# write → re-parse → compare element count
tmp = tempfile.NamedTemporaryFile(suffix='.musicxml', delete=False)
score.write('musicxml', fp=tmp.name)
back = converter.parse(tmp.name)
assert len(list(back.recurse().notes)) == len(list(score.recurse().notes))
```

> Round-trip detects data loss in engravings/expressions.

## 2.8 Repository Practices

1. Store scripts in `scripts/`.
2. Separate input data (YAML/JSON) from code.
3. Commit the resulting MusicXML as a *build artifact*.
4. Test opening in MuseScore/Dorico.

## 2.9 Scripting Checklist

| Check | Yes/No |
|---------|----------|
| Complete part-list (unique id, name, instruments)? | |
| Instrument transposition (`transpose`) set? | |
| Durations consistent with `divisions`? | |
| Markers/expressions via `direction`? | |
| Output validated (XSD + round-trip)? | |

## 2.10 Misconceptions

- **"`score.write('musicxml')` is always valid"** — It can produce XML that does not
  meet the schema; always `validasi()`.
- **"`score.transpose` transposition is enough for transposing parts"** — No;
  each instrument needs the appropriate transpose attribute.
- **"MusicXML = MusicXML"** — Variants (geometry, print) can differ between
  software; round-trip is important.

## 2.11 Exercises

1. Hide: create a 12-part orchestral template via the helper (2.6).
2. Transform: transposition + part rename + add dynamics.
3. Validate: XSD + round-trip test on the output.
4. Integration: Markov output from Ch1 directly to MusicXML.

## 2.12 References

- MusicXML Specification: https://www.w3.org/2021/06/musicxml40/
- music21: https://web.mit.edu/music21/
- IRCAM OpenMusic docs.

---

**Summary:** Scripting MusicXML with Python/music21 enables templates
and batch transformations. Understand the `score-partwise` structure, use the Stream API,
and validate output with XSD + round-trip. Continue to [Ethnomusicology & Non-Western
Systems (`../3.3-Sistem-NonBarat-Etno/`)].
