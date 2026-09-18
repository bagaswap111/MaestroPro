---
title: "Tekstur & Doubling"
tier: "Bachelor S1"
subject: "Orkestrasi Dasar"
xml_tags: ["<part-list>", "<score-part>", "<part-abbreviation>", "<direction>", "<words>", "<note>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 3 — Tekstur & Doubling

> **Buku panduan bab ini:** Samuel Adler, *The Study of Orchestration*
> (Bab 10–12 — texture, doubling, balance); Rimsky-Korsakov, *Principles of
> Orchestration* (Bab "Doubling" & "Tutti"). Fokus: memilih tekstur sesuai
> dramaturgi, dan prinsip doubling agar warna & kekuatan tepat.

## 3.1 Tekstur Musikal

| Tekstur | Deskripsi | Contoh |
|---------|-----------|--------|
| *Monophony* | Satu melodi tanpa iringan | Gregorian chant |
| *Homophony* | Melodi utama + iringan akor | pop, chorale |
| *Polyphony* | Beberapa melodi independen | fugue, canon |
| *Heterophony* | Varian melodi sama serentak | musik gamelan |

### 3.1.1 Aplikasi MusicXML: Homophony (melodi + akor)

```xml
<note>
  <pitch><step>C</step><octave>5</octave></pitch>
  <duration>2</duration><voice>1</voice><type>half</type>
</note>
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>2</duration><voice>2</voice><type>half</type>
</note>
<note>
  <pitch><step>G</step><octave>4</octave></pitch>
  <duration>2</duration><voice>2</voice><type>half</type>
</note>
```

> Tiap lapisan tekstur = `<voice>` (atau `<part>` terpisah). Ini krusial saat
> *playback* dan *analysis midi*.

## 3.2 Konsep Doubling

*Doubling* = satu garis musikal dimainkan 2+ instrumen (oktaf sama atau
berbeda). Bukan kesalahan voicing SATB — doubling adalah **instrumentation
choice** untuk menambah ketebalan & warna.

### 3.2.1 Jenis Doubling

| Jenis | Deskripsi | Efek |
|-------|-----------|------|
| Unison doubling | dua alat oktaf sama | perpaduan timbre |
| Octave doubling | sejajar oktaf | perluasan register |
| *Structural doubling* | akor digandakan per lapis | massa |
| *Melodic doubling* | melodi + instrumen warna | proyeksi |

### 3.2.2 Aturan Umum (Rimsky & Adler)

- **Oboe + Violin 1** — melodi *penetrative* (proyeksi kuat).
- **Flute + Clarinet** (oktaf/oktaf) — warna netral, lembut.
- **Bassoon + Cello** — bass padu.
- **Horn + Viola/Tenor** — warna mesra di register tengah.
- **Hindari** doubling woodwind di register sangat tinggi tanpa dukungan
  (raiser register).
- **Equilibrium:** dynamics antar lapisan harus diset agar melodi *terdengar*;
  tidak semua doubling membuat lebih jelas — kadang justru *membaur*.

## 3.3 Tekstur Orkestra dalam Praktik

### 3.3.1 Piramida Orkestra

| Register | Peran | Instrumen khas |
|----------|-------|----------------|
| Soprano | Melodi utama | Vln I, Ob, Fl, Tpt |
| Alto | Pengisi harmoni | Vla, Hn, Cl |
| Tenor | Pengisi harmoni | Trb ten, Bsn |
| Bass | Fondasi | Vc, Cb, Tuba |

> Rimsky menyebut "orchestra is a pyramid of registers" — jaga tiap register
> *terisi* untuk tekstur penuh; untuk texture *thin* kosongkan register.

### 3.3.2 Faktor Keseimbangan

- Jumlah instrumen (2 oboe vs 4 violin).
- *Dynamic* kontra-instrumen (melodi **ff** vs akor **mf**).
- Register (atas lebih proyektif).
- *Tessitura* (register nyaman tiap alat — jangan paksakan register gelap
  pada atas).

## 3.4 MusicXML: Layout Doubling

### 3.4.1 Multi-Part (unison doubling)

```xml
<part-list>
  <score-part id="P1">
    <part-name>Violin I</part-name>
    <part-abbreviation>Vln I</part-abbreviation>
  </score-part>
  <score-part id="P4">
    <part-name>Oboe</part-name>
    <part-abbreviation>Ob.</part-abbreviation>
  </score-part>
</part-list>
```

```xml
<measure number="1">
  <note>
    <pitch><step>E</step><octave>5</octave></pitch>
    <duration>4</duration><type>whole</type>
  </note>
</measure>
<measure number="1" id="P4">
  <note>
    <pitch><step>E</step><octave>5</octave></pitch>
    <duration>4</duration><type>whole</type>
  </note>
</measure>
```

> Partwise XML: tiap `<part>` punya blok `<measure number="N">` masing-masing.
> Doubling tidak perlu di-deklarasi — cukup menulis melodi sama.

### 3.4.2 Doubling Oktaf dalam Satu Part (divisi)

```xml
<note>
  <pitch><step>E</step><octave>5</octave></pitch>
  <duration>4</duration><voice>1</voice><type>whole</type>
</note>
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>4</duration><voice>2</voice><type>whole</type>
</note>
```

## 3.5 Studru Kasus Doubling

1. **Beethoven, Sym. 5, I** — motif "da-da-da-dum" digandakan di seluruh
   *woodwind + tutti* → massa dramatis.
2. **Ravel, *Bolero*** — urutan doubling melodi pada tiap telathan; register
   naik → tekstur *layering*.
3. **Film scoring** — violin + high woodwind untuk *heat*; cello + bassoon
   untuk bass hangat.

## 3.6 Checklist Menulis Doubling

| Cek | Ya/Tidak |
|-----|----------|
| Melodi dapat didengar di atas harmoni? | |
| Register doubling ada di range kedua alat? | |
| Dynamics diset seimbang? | |
| Tidak ada tabrakan engraving antar part? | |

## 3.7 Miskonsepsi

- **"Doubling selalu membuat lebih keras"** — Tidak; dua alat *reeds* kadang
  *membaur* jika tessitura serupa & dinamik sama.
- **"Tutti = semua bermain sama"** — Tutti sering *doubling* per register;
  bukan semua alat oktaf sama.
- **"MusicXML mengetahui relasi doubling"** — Tidak ada elemen khusus; hanya
  via duplicated content dan `<instrument>` attribution.

## 3.8 Latihan

1. **Dasar:** Werktip 3 proyeksi melodi berbeda untuk satu tema.
2. **Menengah:** Tulis 8 bar tutti dengan unison doubling pada woodwind + string
   (gunakan partwise XML).
3. **Lanjut:** Buat dua perbandingan tekstur dari tema yang sama: homophonic
   (cushion chords) vs polyphonic (imitative), dan jelaskan pilihan register.

## 3.9 Repertoar Dengar

- Beethoven, Sym. 5 I.
- Ravel, *Bolero*.
- Mahler, Sym. 5 IV (Adagietto — strings divisi).
- John Williams, *Jurassic Park* theme.

## 3.10 Referensi Buku & Sumber Web

**Buku:**
- Adler, *The Study of Orchestration*.
- Rimsky-Korsakov, *Principles of Orchestration*.

**Web:**
- Orchestration videos & tables: https://www.orchestrationonline.com/
- VSL instrument pages: https://www.vsl.co.at/en/

---

**Rangkuman:** Tekstur = pilihan dramaturgi; doubling = alat untuk warna/
kekuatan. MusicXML memodelkan lewat struktur part & voice + atribusi
`<instrument>`. Lanjut: [Notasi Percussion (`Ch4-Notasi-Percussion.md`)] dan
[Genre Fondasi (`../1.4-Genre-Fondasi/Ch1-Parameter-Genre.md`)].