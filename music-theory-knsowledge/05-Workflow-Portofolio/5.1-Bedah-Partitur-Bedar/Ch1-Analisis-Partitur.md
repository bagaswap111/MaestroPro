---
title: "Analisis Partitur"
tier: "Workflow & Portfolio"
subject: "Bedah Partitur"
xml_tags: ["<part-list>", "<key>", "<time>", "<measure>", "<direction>"]
software: ["Dorico", "Sibelius", "MuseScore", "IMSLP", "music21"]
---

# Bab 1 — Analisis Partitur

> **Buku panduan bab ini:** Samuel Adler, *The Study of Orchestration*
> (Bab "Analyzing Scores"); Nikolai Rimsky-Korsakov, *Principles of
> Orchestration* (Bab 1–5); praktik *score reading* ala Bach Society.
> Fokus: kerangka bedah partitur sistematis yang bisa diulang di karya apa pun.

## 1.1 Mengapa Membedah Partitur?

Menganalisis karya master adalah salah satu cara tercepat membangun
kosakata orkestrasi: setiap keputusan penulis — instrumentasi, register,
doubling, keseimbangan, dan fugue — menjadi pelajaran yang bisa
direplikasi. Ini inti ketrampilan arranger.

**Manfaat nyata:**
- Melihat *bagaimana* efektif itu dibuat (proses), bukan hanya hasil.
- Membangun referensi internal "rasa lebar" orkestra.
- Memberi landasan objektif untuk keputusan arrangement sendiri.

## 1.2 Kerangka Analisis 7-Tahap

| Tahap | Fokus | Pertanyaan Kunci | Alat |
|-------|-------|------------------|------|
| 1. Identitas | Karya, komposer, era, editor | Siapa & kapan? Edisi mana? | IMSLP/partitur |
| 2. Instrumentasi | `part-list` lengkap | Berapa bagian? Instrumen apa? | MusicXML part-list |
| 3. Kunci & Meter | `key`, `time`, tempo | Pengaturan tonal & ritmik | music21 analyze |
| 4. Struktur Form | section, rehearsal | Exposition? Development? | Rehearsal marks |
| 5. Tekstur | melodi, harmoni, bass | Homophonic/polyphonic? | Score inspection |
| 6. Palette orkestrasi | doubling, register | Siapa melodi? Siapa pengisi? | Instrument pairs |
| 7. Detail ekspresi | articulations, dynamics | Nuansa ekspresi | Part inspection |

> **Adler** menyarankan analisis bertahap: pertama *skim* (identitas +
> struktur) → kedua *zoom in* (palette + detail) → ketiga *rill* ke
> portofolio pribadi.

## 1.3 Sumber Partitur

| Sumber | Tipe | Catatan |
|--------|------|---------|
| **IMSLP.org** | Public domain (PDF & MusicXML) | Sumber utama |
| **MuseScore.com** | Komunitas (MusicXML sakti) | Cek kualitas |
| **Digital scores** | Edisi komersial (scanned) | Ada hak cipta |
| **Library of Congress** | Manuskrip/historis | Untuk riset |

> Unduh versi PDF **dan** MusicXML bila memungkinkan: PDF untuk visual
> (register, bowing), XML untuk analisis terisolasi di music21.

## 1.4 Workflow Analisis di music21

```python
from music21 import converter, corpus

score = converter.parse('beethoven.musicxml')

# 1) Kunci & progresi (key relatif/nisbi)
print(score.analyze('key'))

# 2) Ukuran tiap part
for part in score.parts:
    print(part.partName, 'len:', len(part.notes))

# 3) Tempo & metronome
for tm in score.metronomeMarkBoundaries():
    print('bar', tm[0].number, '→', tm[1])

# 4) Potong section (extract exposition: bar 1–8)
subset = score.measures(1, 8)
subset.show('text')
```

> `converter.parse` menerima `format='musicxml'`, `format='midi'`, atau
> `corpus.parse('fugue')` untuk korpus bawaan.

## 1.5 Teknik Analisis Register & Doubling

- **Celeigh register test:** periksa apakah melodi berada di register
  nyaman instrumen utama.
- **Doubling map:** buat tabel siapa memainkan nada yang sama di tiap
  momen kunci (identifikasi serentak oktaf/unison).

Contoh tabel doubling untuk momen klimaks:

| Bar | Instrumen | Register | Peran |
|-----|-----------|----------|-------|
| 45–52 | Violin I + Flute | A5–E6 | Melodi unison |
| 45–52 | Trombone 1 + Bassoon | G3–C4 | Pengisi harmoni |
| 45–52 | Cello + Bass | C2–C3 | Bass |

## 1.6 Checklist Analisis

| Check | Catatan |
|-------|---------|
| 1. Identitas lengkap (komposer, era)? | |
| 2. Instrumentasi teridentifikasi? | |
| 3. Kunci/meter/tempo dicatat? | |
| 4. Form dipetakan (section labels)? | |
| 5. Tekstur & palette dianalisis? | |
| 6. Detail (dyn/artic) dipelajari? | |
| 7. Kesimpulan terdokumentasi di portfolio? | |

## 1.7 Miskonsepsi

- **"Analisis partitur = menghafal not"** — Tujuan utamanya memahami
  keputusan orkestrasi (mengapa), bukan sekadar not.
- **"Satu part mencukupi"** — Partitur lengkap (full score) wajib untuk
  melihat keseimbangan.
- **"Semua karya bisa dibedah 7-tahap"** — Sketsa pendek/lagu pop cukup
  iga tahap: instrumentasi → struktur → tekstur.

## 1.8 Latihan

1. **Skim** — ambil partitur 1 simfoni Mozart, catat instrumentasi &
   form (15 menit).
2. **Zoom in** — pilih 16 bar klimaks, gambar doubling map.
3. **Rill** — tulis 3 pelajaran → miniaturorkestrasi 8 bar sendiri.
4. **Digital** — parsial MusicXML via music21, ekstrak tempo/key.

## 1.9 Repertoar Rekomendasi untuk Dibedah

- **Mozart — Symphony No. 40:** form & structure jernih.
- **Beethoven — Symphony No. 5, I:** motif + doubling.
- **Ravel — Boléro:** crescendo orkestrasi gradual.
- **Stravinsky — The Rite of Spring:** warna tekstur modern.

## 1.10 Referensi

- Adler, *The Study of Orchestration*.
- Rimsky-Korsakov, *Principles of Orchestration*.
- IMSLP: https://imslp.org/

---

**Rangkuman:** Bedah partitur memakai kerangka sistematis (identitas →
instrumentasi → struktur → detail). Gunakan IMSLP + music21 untuk
mempercepat; dokumentasikan tiap analisis di portofolio. Lanjut ke [Studi
Kasus (`Ch2-Studi-Kasus.md`)].