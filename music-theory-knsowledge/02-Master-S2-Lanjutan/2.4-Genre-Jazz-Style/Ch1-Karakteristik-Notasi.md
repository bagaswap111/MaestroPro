---
title: "Jazz Style — Karakteristik & Notasi"
tier: "Master S2"
subject: "Genre Jazz Style"
xml_tags: ["<harmony>", "<kind>", "<degree>", "<slur>", "<glissando>", "<tie>", "<swing>", "<sound>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Jazz Style: Karakteristik & Notasi

## 1.1 Jazz sebagai Bahasa (Era & Subgenre)

Jazz adalah bahasa dengan aksen historis yang berbeda. Untuk arranger,
parameter (tempo/bayo/harmoni/form) berubah dari satu era ke era lain:

| Era/Gaya | Tempo/Feel | Harmoni | Instrumen khas |
|----------|-----------|---------|----------------|
| New Orleans (Dixie) | 2/2, *two-beat* | Tonik–dominant | Cornet, clarinet, trombone, banjo, tuba |
| Swing (Big Band) | 4/4, *four swing* | ii–V–I, blues | Full big band (5 sax, 4–5 trb, 4 trb, rhythm) |
| Bebop | 4/4 uptempo, *rubato intro* | Chord extensions + alterations | Small group (sax/trp + rhythm) |
| Cool | Lembut, *West Coast* | Same, lebih tenang | French horn, flute add |
| Hard Bop / Soul | Mid-tempo, groovy | Blues + gospel | Tenor, organ |
| Modal | *One-chord vamp* | Skala (Dorian, dll.) | Post-bop group |
| Free / Avant | Bebas tempo | Pan-tone | Woodwind teknik ekstend |
| Fusion | Elektrik, 16th | *Vamp*, riff | E-piano, synth, wah-guitar, bass fretless |

**Levine, *The Jazz Theory Book*, bab 1–4:** dasar ii–V–I, 7th chords, skala
jazz; bab 9–11 blues; bab 19 (alternate), bab 21–22 (modal & slash chords).

## 1.2 Swing: Notasi & Playback

Swing = **asimetri 8th** (long-short). Aturan praktis:

- *Swing 8ths* ditulis sebagai 8th **sama** (straight) tapi *dimainkan* 2:1 —
  jangan tulis triplet benar di score (memusingkan baca dunia nyata).
- Software: MuseScore `Swing playback` (54–66%), Dorico `Swing` directive,
  Sibelius `Playback → Swing`.

Di MusicXML 3.1+, swing ditulis `<sound swing>`:

```xml
<direction placement="above">
  <direction-type>
    <words>Swing</words>
    <sound tempo="144" swing="eighth" first="third" second="third"/>
  </direction-type>
</direction>
```

Jika perlu **exact notation** (untuk exam/engraving), tulis triplet 8th
(3+3 per beat).

## 1.3 Harmoni Jazz: Kosakata Wajib

Kosakata (Levine tab): **7th chords** pada setiap derajat; extensions
9/11/13; alterasi (b9, #9, #11, b13); *lead-sheet symbols*.

### 1.3.1 Kelas, Kind, dan Degree di MusicXML

| Simbol | `<kind>` | Degree |
|--------|----------|--------|
| Cmaj7 | major-seventh | — |
| C7 | dominant | — |
| Cm7 | minor-seventh | — |
| C7alt | dominant + degree b9/#9/b13 | `<degree>` |
| Cmaj7#11 | major-seventh + add #11 | `<degree><alter>1</alter>` |

```xml
<harmony>
  <root><root-step>C</root-step></root>
  <kind text="7b9#9">dominant</kind>
  <degree>
    <degree-value>9</degree-value><degree-alter>-1</degree-alter>
    <degree-type>alter</degree-type>
  </degree>
  <degree>
    <degree-value>9</degree-value><degree-alter>1</degree-alter>
    <degree-type>alter</degree-type>
  </degree>
</harmony>
```

Lihat detail: `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch4-Harmony-Chord-Symbols.md`.

### 1.3.2 ii–V–I dan *Turnaround*

Progresi jiwa jazz: **ii–V–I** (Dm7–G7–Cmaj7) dan *turnaround*
(I–vi–ii–V: Cmaj7–Am7–Dm7–G7). Substitusi yang wajib:

- **Tritone sub:** G7 → D♭7 (bass turun semitone, sama 3rd/7th).
- **Backdoor:** ♭VII7 (F#7 berkekuatan ke C — karakter jazz).
- **Diminished passing:** antara akor naik turun.

## 1.4 Voicing: Drop 2, Rootless (Three-Note), dan Upper Structures

- **Drop-2:** voicing 4-note — suara 2nd dari atas diturunkan 1 oktaf; sangat
  umum untuk comping kunci.
- **Rootless (Bud Powell voicing):** 3rd+7th (9th) tanpa root — untuk solo
  piano comping: C7 → E–B♭–D–G (3rd, 7th, 9th, 5th).
- **Upper structures:** 2 atau 3 not dari triad atas (lihat bab
  `Ch2-Upper-Structures-Alterations.md`).

### 1.4.1 Basin: Piano Voicing Rootless di MusicXML

```xml
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>4</duration>
  <voice>3</voice>
  <staff>2</staff>
  <type>quarter</type>
</note>
<note>
  <pitch><step>Bb</step><octave>4</octave></pitch>
  <duration>4</duration>
  <voice>3</voice>
  <staff>2</staff>
  <type>quarter</type>
  <chord/>
</note>
<note>
  <pitch><step>D</step><octave>5</octave></pitch>
  <duration>4</duration>
  <voice>3</voice>
  <staff>2</staff>
  <type>quarter</type>
  <chord/>
</note>
```

## 1.5 Melodi Jazz: Bebop Scale, Approach, dan Enclosure

- **Bebop scale:** menaruh *color* note (b7→7 bebop mayor, b3→3 bebop minor)
  sehingga skala 8-note cocok dengan ketukan.
- **Approach tones:** chromatic 1/2 step sebelum chord tone (walking).
- **Enclosure:** approach atas+bawah target (C → B–B♭/A–C).

```xml
<note>
  <pitch><step>B</step><octave>4</octave></pitch>
  <duration>1</duration>
  <type>16th</type>
  <slur type="stop"/>
</note>
<note>
  <pitch><step>C</step><octave>5</octave></pitch>
  <duration>3</duration>
  <type>8th</type>
  <dot/>
</note>
```

## 1.6 Big Band Scoring: Layout & Part

Layout standar 5-sax / 4-trumpet / 4-trombone / rhythm:

| Part | Range (written) | Transpos |
|------|-----------------|----------|
| Alto Sax 1/2 | G3–E6 | E♭ |
| Tenor Sax 1/2 | G2–E5 | B♭ |
| Bari Sax | A1–G4 | E♭ |
| Trumpet 1–3 | F3–C6 | B♭ |
| Lead Trumpet | (sekitar C6 lead) | B♭ |
| Trombone 1–3 | E2–B♭4 | C (BC) |
| Bass Trombone | G1–F4 | C (BC) |
| Rhythm | — | konser |

**Doubling sax:** 1st requires flute/clarinet — tulis di part yang sama dengan
clef switch (flute treble 8, clarinet B♭).

## 1.7 Miskonsepsi Umum

- **"Swing = triplet"** — Layak penulisan not triplet jika ingin *exact*;
  score umum tulis straight + "Swing" + `<sound swing>`.
- **"Semua akor pakai extensions"** — Tambah extension hanya jika berguna;
  rootless untuk comping, symbols untuk lead sheet.
- **"Hanya ii–V–I"** — Modal & free jazz punya bahasa berbeda; blues memakai
  harmoni dominan statis.
- **"Voicing ascending = power slide"** — Drop-2 besar, cluster, dsb. adalah
  *colors*, tidak selalu *chord-tone*.

## 1.8 Latihan

1. **Dasar:** Tulis ii–V–I (Dm7–G7–Cmaj7) sebagai lead sheet di MusicXML.
2. **Menengah:** Voicing rootless C7 untuk piano (3rd 7th 9th 5th) dalam 2 oktaf.
3. **Lanjut:** Susun 8 bar *head* B-flat blues untuk sax section, swing text,
   + turnaround ii–V–I dengan *tritone sub*.

## 1.9 Repertoar Dengar

- Swing: Duke Ellington, *It Don't Mean a Thing*; Count Basie, *April in Paris*.
- Bebop: Charlie Parker, *Ornithology*; Bud Powell.
- Cool: Miles Davis, *Birth of the Cool*.
- Modal: Miles, *So What*; John Coltrane, *Impressions*.
- Fusion: Weather Report, *Birdland*.

## 1.10 Referensi Buku & Sumber Web

**Buku:**
- Mark Levine, *The Jazz Theory Book* (Sher Music).
- Mark Levine, *The Jazz Piano Book*.
- Jerry Coker, *Elements of the Jazz Language*.
- Russ Garcia, *The Arranger's Guide* (Big Band).

**Web:**
- Jazzadvice: https://www.jazzadvice.com/
- ii-V7-I practice (Jazz Studies):
  https://www.learnjazzstandards.com/
- IMSLP — jazz transcriptions public domain:
  https://imslp.org/

---

**Rangkuman:** Jazz = swing feel + ii–V–I + extensions/alterations + langkah
melodi bebop. MusicXML: `<kind>`/`<degree>` untuk chord, `<sound swing>` untuk
feel, `<slur>`/`<glissando>` untuk frase. Lanjut ke [Adaptasi Jazz Lintas
Instrumentasi (`Ch2-Adaptasi-Instrumentasi.md`)].