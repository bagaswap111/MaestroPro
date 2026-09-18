---
title: "Vokal & Choral — Adaptasi Lintas Instrumentasi"
tier: "Bachelor S1"
subject: "Genre Vokal & Choral"
xml_tags: ["<voice>", "<lyric>", "<degree>", "<harmony>", "<direction>", "<dynamics>"]
software: ["MuseScore", "Dorico", "Sibelius", "Finale"]
---

# Bab 2 — Vokal & Choral: Adaptasi Lintas Instrumentasi

## 2.1 Dari Suara ke Instrumen: Peta Peran

Suara adalah "instruksi" tersulit untuk dipindai — namun perannya jelas:

| Peran vokal | Padanan instrumental |
|-------------|----------------------|
| Soprano lead | Flute, oboe, violin 1, trumpet (soft) |
| Alto | Violin 2, clarinet, horn |
| Tenor | Cello tenore, sax tenor, english horn |
| Bass | Cello, bassoon, tuba (soft), piano LH |
| Choir pad (tutti) | String section / woodwind choir |
| Percussion vokal (beatbox) | Percussion kit/unpitched |

**Aturan paling penting:** *register* — jangan pindahkan soprano ke oktava
yang sama. Pilih oktav instrumen untuk menghasilkan warna instrumen yang
tidak menutupi melodi.

## 2.2 Adaptasi 1: SATB Choir → String Quartet

- Violin 1 → soprano (melodi + ornament).
- Violin 2 → alto (internal harmony, kontra).
- Viola → tenor (range register tengah).
- Cello → bass (walking / root, pizz.).

**Lirik hilang, ekspresi tetap:** bawa `<direction>` (dynamik, phrasing) dan
tambahkan *markings* musik (mf, subito p) dari tekstur vokal.

### 2.2.1 Contrapung imitatif → string divisi

```xml
<measure number="1">
  <note>
    <pitch><step>D</step><octave>5</octave></pitch>
    <duration>2</duration>
    <voice>1</voice>
    <type>8th</type>
    <notations>
      <slur type="start" number="1"/>
    </notations>
  </note>
  <!-- imitative entry at alto, d4 -->
  <note>
    <pitch><step>D</step><octave>4</octave></pitch>
    <duration>2</duration>
    <voice>2</voice>
    <type>8th</type>
  </note>
</measure>
```

## 2.3 Adaptasi 2: A Cappella Pop → Brass/Ensemble Kamar

Transformasi *a cappella* (Pentatonix style):

1. **Vocal bass (beatbox pattern)** → snare+lown drum pada staf percussion.
2. **Vocal pad (oo)** → sax quartet sustain.
3. **Vocal percussion/beat** → cajón atau rimshot.
4. **Melisma/ryzz (riff)** → sax/trumpet glissando/licks.

Buat `part-list` lengkap sedari awal (arranger akan "berkebalikan" pada
tempo/groove dari vokalnya).

## 2.4 Adaptasi 3: Choral Romantik → Orchestra (A Cappella Œuvre)

Seperti Brahms/Strauss yang mengorkestrasi chorus (essay):
- **Pad 4-suara** → string divisi (arco, homogeneous bowing).
- **Kontrapung** → woodwind+horn subsidiary.
- **Timpani** menonjolkan *cadence* and *Amen*.

Pengalaman standar: *transcription* choral untuk orchestra perlu **layout
bar-line lengkap** — semua part setiap birama; pastikan *time signature*
di semua staf konsisten.

## 2.5 Checklist Adaptasi Vokal/Choral

| Cek | Hasil |
|-----|-------|
| Melodi (soprano) masuk di register terbaik instrumen? | |
| Pad internal (alto/tenor) tersebar tanpa bentrok? | |
| Bass vokal → bass instrumen dengan tessitura benar? | |
| Lirik/melisma → frase & ornament diterjemahkan? | |
| Teknik vokal (belt, falsetto, melisma) → glissando/teknik alat? | |
| `lyric` dihapus bila tetap (atau petunjuk pronunciation di bar 1)? | |
| Jika ansambel campuran, vokal masih lead — pad instr di bawah? | |

## 2.6 Latihan

1. **Dasar:** Pindahkan 4-bar SATB himne ke string quartet (tulis ulang 4 voice).
2. **Menengah:** Buat *a cappella → brass ensemble*: 1 bar beatbox → percussion,
   pad → horn section.
3. **Lanjut:** Orkestrasi *Amen Fugue* pendek (Bach-esque): fugue bass → tuba,
   imitasi → woodwind, pad → strings.

## 2.7 Repertoar Adaptasi (Contoh)

- Voces8 / Swingle Singers (a cappella parallel).
- Pentatonix cover arsenal (funk→brass).
- Benjamin Britten, *Old Amer. Songs* → orchestral version.

## 2.8 Referensi Buku & Sumber Web

**Buku:**
- Robert Shaw; Tony Thornton (*Barbershop Music Theory*).
- Samuel Adler (bab vocal/choral entry).

**Web:**
- CPDL: https://www.cpdl.org/
- Barbershop Harmony Society: https://www.barbershop.org/
- MuseScore Choir templates:
  https://musescore.org/

---

**Rangkuman:** Adaptasi vokal/choral = transfer peran suara (lead/pad/bass/
perkusi vokal) ke instrumen dengan register sesuai, terjemahkan lirik/teknik ke
frase/glissando, dan jaga ekspresi dinamik. Kembali ke [Fondasi Genre
(`../1.4-Genre-Fondasi/Ch1-Parameter-Genre.md`)] — Genre Tier 1 selesai. Lanjut
ke Tier 2: [Jazz Style (`../../../02-Master-S2-Lanjutan/2.4-Genre-Jazz-Style/`)].