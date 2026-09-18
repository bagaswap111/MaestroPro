---
title: "MusicXML Scripting dengan Python"
tier: "Doctoral S3"
subject: "Komposisi Algoritmik"
xml_tags: ["score-partwise", "part-list", "measure", "note", "pitch", "duration"]
software: ["Python", "music21", "OpenMusic", "lxml"]
---

# Bab 2 — MusicXML Scripting dengan Python

> **Buku panduan bab ini:** Cuthbert & Ariza (*music21*), IRCAM/OpenMusic
> practices, *MusicXML Specification* (makemusic). Fokus: membangun dan
> memvalidasi file MusicXML secara programatik.

## 2.1 Mengapa Scripting MusicXML?

- Template orkestra 100+ instrument tanpa pengulangan manual.
- Transformasi batch (transposisi, reharmonisasi, re-notch).
- Integrasi dengan analisis/sistem algoritmik (lihat
  `Ch1-Dasar-Komposisi-Algoritmik.md`).

## 2.2 Struktur Dasar MusicXML (Refresher)

File `score-partwise`:

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

> Detail lengkap: `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch1-Struktur-Root-Partwise.md`.

## 2.3 music21 sebagai Generator

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

## 2.4 Menulis dari Data Mentah

```python
from music21 import stream, note

data = [("C4", 0.25), ("D4", 0.25), ("E4", 0.5),
        ("F4", 0.25), ("G4", 0.25), ("C5", 1.0)]

part = stream.Part()
for pitch_str, ql in data:
    part.append(note.Note(pitch_str, quarterLength=ql))

part.write('musicxml', fp='melodi.xml')
```

> Durasi dalam quarterLength; `divisions` dipilih music21 secara otomatis.

## 2.5 Membaca dan Transformasi

```python
from music21 import converter

score = converter.parse('partitur.musicxml')
key_obj = score.analyze('key')
for part in score.parts:
    print(part.partName, len(part.notes))
score.write('musicxml', fp='transpos.musicxml')
```

Transposisi part-level vs instrumen:
`../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`.

## 2.6 Pola Umum: Template Generator

```
skema (list part + instrumen)
        │
        ▼
score = build_template(parts)
        │
        ▼
masukkan data (harmoni/melodi)
        │
        ▼
tambahkan notations & expressions
        │
        ▼
write('musicxml')
```

### 2.6.1 Helper Part

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

## 2.7 Validasi & Debug (Round-trip)

### 2.7.1 Validasi XSD

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

# tulis → parse ulang → bandingkan element count
tmp = tempfile.NamedTemporaryFile(suffix='.musicxml', delete=False)
score.write('musicxml', fp=tmp.name)
back = converter.parse(tmp.name)
assert len(list(back.recurse().notes)) == len(list(score.recurse().notes))
```

> Round-trip deteksi kehilangan data pada engravings/expressions.

## 2.8 Praktik Repositori

1. Simpan skrip di `scripts/`.
2. Pisahkan input data (YAML/JSON) dari kode.
3. Commit MusicXML hasil sebagai *build artifact*.
4. Test buka di MuseScore/Dorico.

## 2.9 Checklist Scripting

| Periksa | Ya/Tidak |
|---------|----------|
| Part-list lengkap (id unik, nama, instrumen)? | |
| Transposisi instrumen (`transpose`) di-set? | |
| Durasi konsisten dengan `divisions`? | |
| Marker/expression via `direction`? | |
| Hasil divalidasi (XSD + round-trip)? | |

## 2.10 Miskonsepsi

- **"`score.write('musicxml')` selalu valid"** — Bisa menghasilkan XML tak
  memenuhi schema; selalu `validasi()`.
- **"Transposisi `score.transpose` cukup untuk part transposing"** — Tidak;
  per-instrumen perlu atribut transpose yang sesuai.
- **"MusicXML = MusicXML"** — Varian (geometry, print) bisa berbeda antar
  software; round-trip penting.

## 2.11 Latihan

1. Hide: buat template 12-part orkestra via helper (2.6).
2. Transform: transposisi + rename part + tambah dynamics.
3. Validasi: XSD + round-trip test pada output.
4. Integrasi: output Markov dari Ch1 langsung ke MusicXML.

## 2.12 Referensi

- MusicXML Specification: https://www.w3.org/2021/06/musicxml40/
- music21: https://web.mit.edu/music21/
- IRCAM OpenMusic docs.

---

**Rangkuman:** Scripting MusicXML dengan Python/music21 memungkinkan template
dan transformasi batch. Pahami struktur `score-partwise`, gunakan Stream API,
dan validasi hasil dengan XSD + round-trip. Lanjut ke [Etnomusikologi & Sistem
Non-Barat (`../3.3-Sistem-NonBarat-Etno/`)].