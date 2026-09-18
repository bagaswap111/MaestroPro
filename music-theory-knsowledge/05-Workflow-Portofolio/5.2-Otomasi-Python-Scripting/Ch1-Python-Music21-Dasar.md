---
title: "Python & Music21 — Dasar"
tier: "Workflow & Portfolio"
subject: "Otomasi Python Scripting"
xml_tags: ["score-partwise", "note", "pitch", "duration", "stream"]
software: ["Python", "music21", "Jupyter"]
---

# Bab 1 — Python & Music21: Dasar

> **Buku panduan bab ini:** Michael Cutbirth *et al.*, *music21 documentation*
> (musdomain); material Komposisi Algoritmik Tier 3
> (`../../03-Doctoral-S3-Riset/3.2-Komposisi-Algoritmik/`). Fokus: objek
> inti music21 untuk membaca & menulis MusicXML.

## 1.1 Persiapan

```bash
pip install music21
pip install jupyter          # opsional
```

Verifikasi:

```python
import music21
print(music21.__version__)
```

> music21 memerlukan lingkungan musical environment (MuseScore) untuk
> `show()`; untuk analisis tanpa GUI cukup `show('text')`.

## 1.2 Objek Inti music21

| Objek | Arti | Contoh |
|-------|------|--------|
| `Stream` | Kontainer wadah | Score, Part, Measure |
| `Measure` | Birama | `Measure(1)` |
| `Note` | Nada tunggal | `Note('C4')` |
| `Chord` | Kumpulan nada | `Chord(['C4','G4'])` |
| `Key` / `KeySignature` | Tonalitas | `Key('C')` |
| `Meter.TimeSignature` | Birama | `Meter.TimeSignature('4/4')` |

**Hirarki:** `Stream.Score` > `Stream.Part` > `Stream.Measure` > `Note/Chord`.

## 1.3 Membuat Partitur Mini

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

> `key.KeySignature(0)` vs `key.Key('C')` — Key menandai tonal (dengan
> konsekuensi analisis `analyze('key')`), KeySignature hanya aksidental.

## 1.4 Membaca Partitur (Parse)

```python
from music21 import converter

score = converter.parse('karya.musicxml')
for part in score.parts:
    print(part.partName, len(part.notes))
```

Opsi `format='musicxml'`, `format='midi'`, atau `corpus.parse('number')`
untuk korpus bawaan (fugue/chorale).

## 1.5 Menelusuri Stream (Recurse)

```python
for el in score.recurse():
    if el.isNote:
        print('Nota', el.pitch, el.quarterLength)
    elif el.isChord:
        print('Chord', el.pitches, el.quarterLength)
    elif el.isRest:
        print('Rest', el.quarterLength)
```

> **Penting:** `recurse()` menelusuri **semua** level (Part→Measure→Note);
> untuk satu part saja gunakan `part.recurse().notes`.

## 1.6 Analisis Dasar

```python
# Kunci
print(score.analyze('key'))

# Progresi roman numeral tiap chord
from music21 import roman
for c in score.chordify().flat.getElementsByClass('Chord'):
    rn = roman.romanNumeralFromChord(c, score.analyze('key'))
    print(rn.figure, c.pitches)
```

> `chordify()` mengubah seluruh konten menjadi deret chord — praktis untuk
> analisis harmonik cepat.

## 1.7 Transposisi & Transformasi

```python
score.transpose('M2', inPlace=True)   # naik major 2nd
score.write('musicxml', fp='trans.musicxml')
```

> Untuk part transpos (B♭/F/E♭-instrumen), gunakan `instrument` +
> atribut transpose, bukan hanya `score.transpose` (lihat
> `../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`).

## 1.8 Masking & Copy (Subset)

```python
import copy
subset = copy.deepcopy(score.measures(1, 8))
subset.write('musicxml', fp='intro.xml')
```

> `deepcopy` wajib bila Anda akan memodifikasi subset tanpa merusak sumber.

## 1.9 Miskonsepsi

- **"`score.transpose` otomatis mengurus transposisi instrumen"** — Tidak;
  transposisi part per-instrumen diatur oleh atribut `transpose` instrumen.
- **"`analyze('key')` selalu benar"** — Ini heuristik; untuk bagian ambigu
  bisa salah — koreksi manual.
- **"Semua elemen adalah Note"** — Ada `Expression`, `Spanner`, `Clef` dll;
  filter dengan `is*` method.

## 1.10 Latihan

1. Buat mini-score 4 bar Nada C mayor → tulis musicxml.
2. Parse file apa pun → hitung jumlah Note vs Chord per part.
3. Transposisi ke F → tulis.
4. Ekstrak bar 1–4 → tambah pickup → ukur durasi total.

## 1.11 Checklist Dasar

| Periksa | Ya/Tidak |
|---------|----------|
| music21 terinstal? | |
| Bisa buat `Stream`→`write('musicxml')`? | |
| Bisa parse file MusicXML/MIDI? | |
| Bisa iterate `recurse()` dan filter? | |
| Transpose/transform berhasil diuji? | |

## 1.12 Referensi

- Cutbirth et al., *music21 documentation*: https://web.mit.edu/music21/
- Cuthbert & Ariza, *music21: A Toolkit for Computer-Aided Musical Scoring*.
- Lanjut ke [Scripting Praktis (`Ch2-Scripting-Praktis.md`)].

---

**Rangkuman:** music21 menyediakan objek Stream/Part/Measure, parse/write
MusicXML, dan analisis dasar (key, chordify, roman numeral). Kuasai template
awal → transformasi → debugging.