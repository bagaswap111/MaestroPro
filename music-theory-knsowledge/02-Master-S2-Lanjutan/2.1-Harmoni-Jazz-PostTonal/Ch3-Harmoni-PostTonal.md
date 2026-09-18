---
title: "Harmoni Post-Tonal"
tier: "Master S2"
subject: "Harmoni Jazz & Post-Tonal"
xml_tags: ["<note>", "<pitch>", "<alter>", "<accidental>", "<rest>", "<direction>", "<words>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 3 — Harmoni Post-Tonal

> **Buku panduan bab ini:** Joseph N. Straus, *Introduction to Post-Tonal
> Theory* (set theory, serialisme); Miguel A. Roig-Francolí, *Understanding
> Post-Tonal Music*; Grisey/Murail jurnal (spektral). Fokus: impresionisme,
> atonalitas, 12-tone, dan spektral — semuanya dalam representasi MusicXML.

## 3.1 Dari Tonal ke Post-Tonal

Abad ke-20 melampaui fungsi tonal:

| Gerak | Perwakilan | Gaya |
|-------|-----------|------|
| Impressionisme | Debussy, Ravel | whole-tone, paralel |
| Atonalitas | Schoenberg | kebebasan pusat |
| Serialisme/12-tone | Schoenberg, Webern, Berg | tone rows |
| Spektral | Grisey, Murail | overtone & microstructure |
| Neoton?ality | Copland, Bartók | kembali terarah |

## 3.2 Impressionisme & Harmoni Paralel

### 3.2.1 Ciri

- Skala whole-tone, pentatonik, mode kuno.
- Akor paralel (*same voicing* berpindah).
- Tanpa kadens fungsional; **warna > fungsi**.
- Bass sering bergerak triton? no — bergerak kecil & ostinato.

### 3.2.2 MusicXML: Akor Paralel

```xml
<measure number="1">
  <note><pitch><step>C</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
  <note><pitch><step>E</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
  <note><pitch><step>G</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
</measure>
<measure number="2">
  <note><pitch><step>D</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
  <note><pitch><step>F</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
  <note><pitch><step>A</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
</measure>
```

## 3.3 Pitch-Class & Set Theory (Straus)

### 3.3.1 Konsep Dasar

- **Pitch class (PC):** C=0, C#=1, …, B=11.
- **Interval class (IC):** jarak terpendek antara dua PC (0–6).
- **Pitch-class set:** himpunan PC; transposisi/inversi berbagi struktur.
- **Tn / In / TnI:** transformasi klas.

### 3.3.2 MusicXML: Menulis Kromatisme Bebas

- Key signature boleh 0 fifths; tiap not diberi `<alter>` eksplisit +
  `<accidental>` lengkap (StudioPraktik set notation).

```xml
<note>
  <pitch>
    <step>B</step>
    <alter>-1</alter>
    <octave>4</octave>
  </pitch>
  <duration>2</duration>
  <type>eighth</type>
  <accidental>flat</accidental>
</note>
```

## 3.4 Serialisme (12-Tone)

### 3.4.1 Prinsip

- Gunakan **seluruh 12 PC** sebelum mengulang.
- Matrix dasar: Prime (P), Retrograde (R), Inversion (I), Retrograde-Inversion
  (RI).

| Transformasi | Definisi |
|--------------|----------|
| P | row asli |
| R | mundur |
| I | interval dibalik arah |
| RI | I lalu mundur |

### 3.4.2 MusicXML: Menulis Serial Score

1. Key 0 fifths; semua not dengan alter eksplisit.
2. `<midi-instrument>` per *row* bila mau warna beda.
3. `<direction><words>` untuk tanda P/R/I/RI.

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">Row P</words>
  </direction-type>
</direction>
```

## 3.5 Spektral Harmony (Grisey, Murail)

Prinsip: harmoni diambil dari **overtones** satu nada dasar.

- Chord = notasie overtone (harmonik 1–n).
- Mikrotonal sering muncul di luar 12-ET.
- Integrasi dengan seluruh *continuum* (limites praktis engraving:
  24-tone mikrotonal default; lihat
  `../../03-Doctoral-S3-Riset/3.1-Psikoakustik-Spektral/Ch1-Teori-Spektral.md`).

### 3.5.1 MusicXML: Harmoni Spektral (12-ET approximation)

Overtone stack dari C2 (16.35 Hz); harmonik urut ≈ mayor triad plus 7th/9th:

```xml
<note><pitch><step>C</step><octave>2</octave></pitch><duration>4</duration><type>whole</type></note>
<note><pitch><step>C</step><octave>3</octave></pitch><duration>4</duration><type>whole</type></note>
<note><pitch><step>G</step><octave>3</octave></pitch><duration>4</duration><type>whole</type></note>
<note><pitch><step>C</step><octave>4</octave></pitch><duration>4</duration><type>whole</type></note>
<note><pitch><step>E</step><octave>4</octave></pitch><duration>4</duration><type>whole</type></note>
```

## 3.6 Set Theory Lanjutan (Straus)

### 3.6.1 Normal Form & Prime Form

| Set | Normal Form | Prime Form |
|-----|-------------|------------|
| {C,Eb,G} (0,3,7) | [0,3,7] | (037) |
| {C,E,G,Bb} (0,4,7,10) | [0,4,7,10] | (0247) |

- Normal form = permutasi paling padat (least circular span).
- Prime form = normal yang dimulai 0 dan terkecil antara T & I.

### 3.6.2 Interval Vector (IV)

Untuk (027): pasangan → masing-masing IC; hitung 6 vektor `[v1..v6]`.

| Set | IV |
|-----|----|
| (012) | [210000] |
| (027) | [011010] |
| (037) | [001110] |

IV membantu membandingkan karakter dan *focal* center.

### 3.6.3 Investiture Z-relation

Dua set berbeda bisa berbagi IV — contoh (014) vs (013) dll.; Lihat Straus
untuk tabel lengkap.

## 3.7 Neotonal & Modal (Bartók, Copland)

- Menggunakan pusat **modal** (bukan fungsi chordal).
- Akor *mirror-symmetric* (axes), folk modes.
- Representasi MusicXML standar (key + alter) — hanya interpretasi berubah.

## 3.8 Latihan

1. Buat deret 12-nada sendiri; tulis P, I, R, RI dengan key 0 fifths.
2. Identifikasi pitch-class set motif Debussy (*Voiles*).
3. Susun harmoni spektral 5-nada dari C2 + ejaan MusicXML.
4. Analisis Webern op.21 — temukan row & fragmentasi.
5. Hitung IV dari set (0146) dan bandingkan dengan (0137/4).

## 3.9 Checklist Post-Tonal

| Periksa | Ya/Tidak |
|---------|----------|
| Alter eksplisit pada tiap not? | |
| Key signature sesuai (0 atau netral)? | |
| Row transformasi ditandai? | |
| Set/prime/IV dianalisis? | |
| Spektral dihitung via overtone? | |

## 3.10 Repertoar Dengar

- Debussy, *Voiles / Pelléas*.
- Schoenberg, *Pierrot Lunaire*, Op. 21 (Webern).
- Grisey, *Partiels / Vortex Temporum*.
- Strauss, examples di *Intro to Post-Tonal Theory*.

## 3.11 Referensi

**Buku:**
- Straus, *Introduction to Post-Tonal Theory*.
- Roig-Francolí, *Understanding Post-Tonal Music*.
- Grisey, *Structuration des timbres* (jurnal).

**Web:**
- emusician set theory tools: https://www.mta.ca/~rrosebrugh/set-theory/
- Laitz, *The Complete Musician* (post-tonal ch).

---

**Rangkuman:** Post-tonal membuka warna impresionis, atonal (set theory),
serialisme row, dan spektral overtone. MusicXML menulis semua dengan
kromatisme eksplisit (`<alter>`+`<accidental>`), key netral, dan tanda
struktural di `<direction>`; analisis tetap di tangan manusia.
Lanjut ke [Arranging Komersial & Film (`../2.2-Arranging-Komersial-Film/`)].