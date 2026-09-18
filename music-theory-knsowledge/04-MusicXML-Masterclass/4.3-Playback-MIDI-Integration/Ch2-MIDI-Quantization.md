---
title: "MIDI Quantization & MIDI-to-MusicXML"
tier: "MusicXML Masterclass"
subject: "Playback & MIDI Integration"
xml_tags: ["<pitch>", "<duration>", "<type>", "<time-modification>", "<transpose>", "<articulations>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore", "music21"]
---

# Bab 2 — MIDI Quantization & MIDI-to-MusicXML

> **Buku panduan bab ini:** Curtis Roads, *The Computer Music Tutorial*
> (Bab MIDI & timing); Michael Good, dokumentasi export MusicXML; praktik
> DAW-to-notation. Fokus: membersihkan MIDI mentah menjadi MusicXML semantik.

## 2.1 Alur MIDI → Score

```
MIDI (performa / hasil improvisasi)
    │
    ▼
Analisis onset & durasi (raw)
    │
    ▼
Quantization → grid ritmis
    │
    ▼
Bersihkan ghost / legato / articulation
    │
    ▼
MusicXML (semantik, publishable)
```

## 2.2 Mengapa MIDI Perlu Dibersihkan?

- **Ghost notes** — not sangat pendek (hit tak sengaja).
- Onset tidak presisi grid (human feel).
- Durasi legato/staccato tidak sama dengan nilai not.
- Percussion/articulation tidak terekam otomatis.
- Pitch-bend, CC, dan *crosstalk* bisa menyisakan data aneh.

## 2.3 Konsep Quantization

*Quantization* — memindahkan onset (dan kadang durasi) ke grid terdekat.

| Grid | Pemakaian |
|------|-----------|
| 1/4 | Pop, rock dasar |
| 1/8 | Straight beat, rock |
| 1/8 swing | Jazz, shuffle |
| 1/16 | Funk, detail sinkopasi |
| 1/32 | Deteksi mikro, ornament |

Prinsip: grid terlalu kasar → menghilangkan *feel*; terlalu halus → noise.
Pilih sesuai gaya genre (lihat genre tier).

## 2.4 Pipeline Pembersihan

### 2.4.1 Manual (Dorico/Sibelius)

1. Import MIDI → pilih quantization value.
2. Cek ghost note (< 1/32), hapus.
3. Perbaiki *beaming* manual.
4. Tambahkan articulation sebelum export.

### 2.4.2 Dengan music21

```python
from music21 import converter, stream

midi = converter.parse('performance.mid')
midi.quantize(quantizationUnit=0.5)  # 1/8 grid (quarter = 1.0)

cleaned = stream.Stream()
for n in midi.flatten().notes:
    if n.quarterLength >= 0.125:      # buang ghost (< 1/32)
        cleaned.append(n)

cleaned.write('musicxml', fp='clean.musicxml')
```

> `quantize()` menggeser onset; saringan di atas membuang not pendek.
> `midi.quantize()` di music21 menerima `quantizationUnit` default 0.5 (8th).

## 2.5 Mapping Fulcrum: MIDI Note → Pitch MusicXML

MIDI note 60 = C4 (concert). Konversi pitch class:

| MIDI | Step | Alter | Octave |
|------|------|-------|--------|
| 60 | C | 0 | 4 |
| 61 | C | 1 | 4 |
| 62 | D | 0 | 4 |
| 63 | D | 1 | 4 |
| 64 | E | 0 | 4 |
| 65 | F | 0 | 4 |
| 66 | F | 1 | 4 |
| 67 | G | 0 | 4 |

Spelling enharmonic diserahkan ke heuristik (musik tradisional → favor
key signature). music21 default menentukan via key algorithm.

### 2.5.1 Contoh XML dari MIDI 60 (durasi quarter)

```xml
<note>
  <pitch><step>C</step><alternate>0</alternate><octave>4</octave></pitch>
  <duration>2</duration>
  <voice>1</voice>
  <type>quarter</type>
</note>
```

## 2.6 Percussion MIDI

- Channel 10 (GM perc).
- Mapping `midi-unpitched` dari nilai MIDI (kick 36, snare 38, hi-hat 42).
- Hindari *double hit* accidental saat konversi.

```xml
<midi-instrument id="P19-S">
  <midi-channel>10</midi-channel>
  <midi-program>0</midi-program>
  <midi-unpitched>38</midi-unpitched>
</midi-instrument>
```

## 2.7 Legato vs Staccato

| Suara MIDI | Notasi target |
|------------|---------------|
| Very short (staccato) | `<staccato/>` |
| Legato terhubung penuh | `<tie>`/`<tied>` |
| Accent | `<accent/>` |
| Human timing | snap grid (hitungan) |

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>quarter</type>
  <notations>
    <articulations>
      <staccato/>
    </articulations>
  </notations>
</note>
```

## 2.8 Swing & Tuplets

Swing feel dari MIDI ∼ triplets; tulis time-modification:

```xml
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>quarter</type>
  <time-modification>
    <actual-notes>3</actual-notes>
    <normal-notes>2</normal-notes>
  </time-modification>
</note>
```

Alternatif: simpan membagi grid straight lalu tambahkan *swing performance*
via DAW playback (bukan ubah XML).

## 2.9 Export Bersih

Sebelum export:

- Durasi valid & konsisten divisions.
- Gabungkan tie bila perlu (music21 `tie: sparkBeams`?).
- Bersihkan *spurious* data (redundant `<octave>` yang salah).

### 2.9.1 Verifikasi Round-Trip

```python
import music21
s = music21.converter.parse('clean.musicxml')
for onset in s.flat.getOffsets():
    assert onset.is_integer() or abs(onset % 0.5) < 1e-6
```

## 2.10 Checklist MIDI Cleanup

| Periksa | Ya/Tidak |
|---------|----------|
| Grid quantization sesuai gaya? | |
| Ghost notes dihapus (< 1/32)? | |
| Drum mapping benar (midi-unpitched)? | |
| Articulation ditambahkan? | |
| Human feel dipertahankan bila diinginkan? | |

## 2.11 Miskonsepsi

- **"Quantization menghilangkan feel selamanya"** — Tidak; simpan MIDI raw,
  quantize hanya untuk notasi.
- **"MIDI pitch = kunci benar otomatis"** — Spelling enharmonic harus
  diputuskan (musik21 key analysis / manual).
- **"Swing harus ditulis triplet di XML"** — Tergantung gaya; di playback bisa
  diset di engine (groove).

## 2.12 Referensi

- music21 quantize: https://web.mit.edu/music21/doc/
- music21 chordify/roman: https://web.mit.edu/music21/doc/
- Roads, *The Computer Music Tutorial* — MIDI chapter.

---

**Rangkuman:** MIDI-to-MusicXML = quantization grid + buang ghost + mapping
GM percussion + articulation; music21 `quantize()` + filter + `write()` sangat
efisien. Ini menutup Tier 4 MusicXML Masterclass.