---
title: "Perpustakaan Teori Musik MaestroPro"
tier: "0-Root"
subject: "Index"
xml_tags: ["score-partwise", "note", "pitch", "harmony", "transpose"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# MaestroPro — Perpustakaan Teori Musik & MusicXML

> **Tagline:** "Dari Teori ke Notasi Digital"
>
> Perpustakaan berbasis Markdown ini menggabungkan kurikulum teori musik akademik
> (S1–S3) dengan implementasi teknis **MusicXML** untuk para arranger, komposer,
> dan *digital engraver* menggunakan Dorico, Sibelius, Finale, dan MuseScore.

## Struktur 5 Level

Setiap konsep teori langsung diikat dengan tag/node MusicXML atau aturan
*engraving* spesifik:

| Level | Nama | Bentuk |
|-------|------|--------|
| 1 | Tier (Derajat Akademik) | Folder utama |
| 2 | Subject / Buku Inti | Sub-folder |
| 3 | Chapter (Bab) | File `.md` |
| 4 | Section (Sub-Bab) | Heading `##` |
| 5 | Sub-Section / XML Node | Heading `###` / `####` + `<tag>` MusicXML |

## Peta Kurikulum

### 🎓 Tier 1 — Bachelor S1 (Fondasi)

**Fokus:** Aturan tradisional, rentang instrumen, dan penerjemahan suara ke notasi standar.

| Subject | Buku Wajib | Chapter |
|---------|-----------|---------|
| `1.1-Teori-Harmoni-Tradisional` | Kostka & Payne; Aldwell & Schachter | Harmoni Diatonik; Progresi & Modulasi; Voice Leading |
| `1.2-Kontrapung-Bentuk-Musik` | Mann; Goetschius | Species Counterpoint; Fugue; Sonata & Rondo |
| `1.3-Orkestrasi-Dasar` | Adler; Rimsky-Korsakov | Ranges; Transposisi; Tekstur & Doubling; Notasi Percussion |
| `1.4-Genre-Fondasi` | Parameter Genre 7-dial | Parameter Genre |
| `1.5-Genre-Blues` | Blues form & skala | Karakteristik Notasi; Adaptasi Instrumentasi |
| `1.6-Genre-Rock-Pop` | Rock/pop grid | Karakteristik Notasi; Adaptasi Instrumentasi |
| `1.7-Genre-Brassband-March` | Brass band & march | Karakteristik Notasi; Adaptasi Instrumentasi |
| `1.8-Genre-Vokal-Choral` | Vokal & paduan suara | Karakteristik Notasi; Adaptasi Instrumentasi |

> **Catatan Genre:** Pelajaran genre **tertanam** (embedded) pada tiap tier
> sebagai subject L2, bukan tier terpisah — sesuai keputusan kurikulum.

### 🎓 Tier 2 — Master S2 (Lanjutan)

**Fokus:** Harmoni modern, teknik *extended*, arranging media (film/game).

| Subject | Buku Wajib | Chapter |
|---------|-----------|---------|
| `2.1-Harmoni-Jazz-PostTonal` | Levine; Straus; Russell | Chord-Scale; Upper Structures; Harmoni Post-Tonal |
| `2.2-Arranging-Komersial-Film` | Garcia; Snow & Meyer | Big Band; String Section; Film Scoring |
| `2.3-Extended-Techniques` | Perspektif New Music; Berio; Ligeti | Woodwind-Brass; Strings; Percussion |
| `2.4-Genre-Jazz-Style` | Jazz style | Karakteristik Notasi; Adaptasi Instrumentasi |
| `2.5-Genre-Funk-Soul-RnB` | Funk/soul/R&B | Karakteristik Notasi; Adaptasi Instrumentasi |
| `2.6-Genre-Latin` | Latin (salsa, bossa) | Karakteristik Notasi; Adaptasi Instrumentasi |
| `2.7-Genre-EDM-Electronic` | EDM & electronic | Karakteristik Notasi; Adaptasi Instrumentasi |

### 🎓 Tier 3 — Doctoral S3 (Riset)

**Fokus:** Akustik, komposisi algoritmik, mikrotonal, dan manipulasi skema XML.

| Subject | Chapter |
|---------|---------|
| `3.1-Psikoakustik-Spektral` | Teori Spektral; Mikrotonal & Tuning |
| `3.2-Komposisi-Algoritmik` | Dasar Komposisi Algoritmik; MusicXML Scripting Python |
| `3.3-Sistem-NonBarat-Etno` | Gamelan; Maqam & Raga |

### 🛠️ Tier 4 — MusicXML Masterclass (Teknis XML)

**Fokus:** Anatomi, *engraving rules*, dan integrasi playback.

| Subject | Chapter |
|---------|---------|
| `4.1-Anatomi-MusicXML` | Struktur Root; Element Note; Attributes & Directions; Harmony |
| `4.2-Music-Engraving-Rules` | Fundamentals; Advanced; Expressions |
| `4.3-Playback-MIDI-Integration` | Playback; MIDI Quantization |

### 🗂️ Tier 5 — Workflow & Portfolio (Studi Kasus & Otomasi)

| Subject | Chapter |
|---------|---------|
| `5.1-Bedah-Partitur-Bedar` | Analisis Partitur; Studi Kasus |
| `5.2-Otomasi-Python-Scripting` | Music21 Dasar; Scripting Praktis |
| `5.3-Version-Control-Git` | Git Dasar; Git Music Workflow |

## Cara Menggunakan

1. **Navigasi:** Buka folder sesuai Tier → Subject → pilih file chapter.
2. **Frontmatter:** Setiap chapter memiliki metadata YAML (`title`, `tier`,
   `subject`, `xml_tags`, `software`) untuk keperluan indeks dan pencarian.
3. **Contoh Kode:** Semua contoh MusicXML berada dalam *code block* `xml`
   yang siap disalin untuk diuji di Dorico/Sibelius/Finale/MuseScore.
4. **Referensi Silang:** Ikuti tautan antar chapter untuk menghubungkan konsep
   teori dengan implementasi MusicXML-nya.

## Konvensi Penulisan

```yaml
---
title: "Contoh Chapter"
tier: "Bachelor S1"
subject: "Orkestrasi Dasar"
xml_tags: ["<transpose>", "<score-instrument>", "<attributes>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---
```

- Bahasa utama: **Indonesia**, dengan istilah teknis berbahasa Inggris.
- Setiap konsep teori memiliki bagian **Aplikasi MusicXML**.
- Aturan *engraving* mengacu pada *Behind Bars* (Elaine Gould) dan standar
  MusicXML 4.0 W3C.