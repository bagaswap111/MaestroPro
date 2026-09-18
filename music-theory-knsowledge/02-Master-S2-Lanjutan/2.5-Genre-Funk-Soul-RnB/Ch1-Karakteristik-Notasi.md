---
title: "Funk, Soul & R&B — Karakteristik & Notasi"
tier: "Master S2"
subject: "Genre Funk Soul R&B"
xml_tags: ["<harmony>", "<kind>", "<degree>", "<notehead>", "<stem>", "<ghost>", "<direction>", "<slur>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Funk, Soul & R&B: Karakteristik & Notasi

## 1.1 DNA Funk:Soul — One-Chord Groove dan Syncopation

Funk/Soul/R&B adalah raja **groove** dan *harmonic stasis*:

- **Harmoni 1 akor** (vamp) atau ii–V ringkas — balok e-he 8/16 bar.
- **Bayo adalah semuanya** — 16th grid, sinkopasi pada *"&a"* ketukan.
- **Backbeat** 2&4 di snare, *kick* di-dance pada empty pocket.
- **Timbral:** klavin ("clav"), wah-guitar, bass slap/pop, horns stabs,
  strings pad devine, vocal hooks.

### 1.1.1 Subgenre Matriks

| Subgenre | Tempo | Getasan |
|----------|-------|---------|
| **Funk** (60s–70s) | 90–115 | Clav + bass lines 16th, drum *power pocket* (Sly Stone, James Brown) |
| **Soul** (60s) | 110–130 | Backbeat tertipis, *string pads*, hormat tu |
| **R&B / Contemporary** | 60–100 | *trap-hihat 16th*, sub-bass, vocoder/auto, *swingy 16th* |
| **Disco** (70s) | 116–128 | 4-on-floor kick, *strings_, Horns, female vocal |
| **Boogie / early R&B** | 100 | Clavinet, octave bass |

## 1.2 Notasi Groove: 16th Grid + Ghost Notes

Tulis funk *grid* sebagai 16th — *ghost note* (dibunyikan sangat halus)
pakai `notehead` `ghost` di MusicXML (percussion) atau `<ghost>` text di bass.

```xml
<note>
  <pitch><step>G</step><octave>2</octave></pitch>
  <duration>2</duration>
  <type>16th</type>
  <voice>2</voice>
  <staff>2</staff>
</note>
<note>
  <pitch><step>G</step><octave>2</octave></pitch>
  <duration>2</duration>
  <type>16th</type>
  <voice>2</voice>
  <staff>2</staff>
  <notehead>ghost</notehead>
</note>
```

### 1.2.1 Pola Bass 16th Klasik

Funk bass (sqrt): ketatom sekaligus — rakit dari *octave + fifths*, *pickup
into* sebagai **key phrase**. Contoh (G, dalam 16th):

```
Ketuk:  1  &  2  &  3  &  4  &
Pitch:  G  G  D  G  G  Bb G  G
```

Bisa menggunakan `<articulations><staccato/></articulations>` pada
*syncopated* target.

## 1.3 Harmoni: Chord Menempel Ringsan

Funk jarang pindah akor; **stabs** memberikan *color change*:

| Fungsi | Jenis | Contoh |
|--------|-------|--------|
| Base vamp | One-chord | E9 (E7 + 9) |
| Stab | ii7–V7 cepat | C#m7–F#7 di bar 3 |
| *Slash* | 3rd bawah | D/F# |
| Tergantung | *Dominant + 9* + *♭7* | A7#9 (Jimi) |

### 1.3.1 Menulis Chord Stab di Rhythm Section

```xml
<harmony print-frame="no">
  <root><root-step>E</root-step></root>
  <kind text="9">dominant</kind>
  <degree>
    <degree-value>9</degree-value><degree-alter>0</degree-alter>
    <degree-type>add</degree-type>
  </degree>
</harmony>
```

## 1.4 Horns & String Pads (Aransemen R&B)

**Horn stabs** — di jaket groove:

- Tulis semua bagian serentak (unison rhythmic), `staccatissimo`+accent.
- Contoh 2 bar untuk trb (lead), puncak di register tengah.

**String pads** — R&B memakai *arrangement string* dengan 4th/6th spread,
tremolo *marcato*:
- Terlalu gemuk → mount. 3-note (root 5th 7th 9th), divisi.
- Menahan di chorus (*staccato notes* tanpa gemuk di chorus intra).

### 1.4.1 Contoh Horn Stab Bar

```xml
<measure number="1">
  <note>
    <pitch><step>C</step><octave>5</octave></pitch>
    <duration>2</duration>
    <voice>1</voice>
    <type>16th</type>
    <notations><articulations><accent/><staccatissimo/></articulations></notations>
  </note>
  <note>
    <rest/>
    <duration>2</duration>
    <voice>1</voice>
    <type>16th</type>
  </note>
</measure>
```

## 1.5 Vokal R&B: Runs, Melisma, Ad-libs

- **Run*/melisma:** garis 16th — tulis semua not (atau `<extend/>` pada 1
  slip). R&B typical: frase "You" → 8 not.
- **Ad-lib tails:** di akhir baris chorus — ditulis kecil (`8va`), *improvised
  ornament*, `[ad lib.]`.
- **Harmony stack:** 3rd/5th; higher harmony mengikuti lirik yang sama.

## 1.6 Miskonsepsi Umum

- **"Funk selalu cepat"** — Banyak funk standard di 90–110 (Sly), bisa slow-jam
  di 60.
- **"R&B = chord dicampur"** — Harmonic element minor; *groove+timbral* lebih
  krusial.
- **"Ghost notes tidak perlu ditulis"** — Untuk *notation playback* dan
  *unity of section*, vel. penting.
- **"Horns hanya staccato"** — Ada *swells*, *falls*, *fills*; color variety.

## 1.7 Latihan

1. **Dasar:** Tulis 8-bar funk vamp (E9): bass 16th + snare backbeat 2&4.
2. **Menengah:** Tambah horn stab 2-bar run dan string pad 3-note.
3. **Lanjut:** Rangkap chorus vocal hook *ad-lib* & harmony stack; tulis
  melisma `<extend/>`.

## 1.8 Repertoar Dengar

- James Brown, *Sex Machine* / *Cold Sweat* (bass, vamp).
- Sly & Family Stone, *Thank You (Falettinme Be Mice Elf Agin)*.
- Stevie Wonder, *Superstition* (clav riff).
- Chic, *Le Freak* (guitar muted funk).
- Drake/Orange, *Hotline Bling* (trap R&B 16th hi-hat).

## 1.9 Referensi Buku & Sumber Web

**Buku:**
- David Garibaldi, *Future Sounds* (drum funk chops).
- Stu Hunt, *Funk Bass Bible*.
- Jerry Coker, *Elements of the Jazz Language* (R&B).

**Web:**
- Funk bass transcriptions: https://www.oktav.com/
- DRUMMER funk notation: https://webdrummer.com/
- Hooktheory (R&B progressions): https://www.hooktheory.com/

---

**Rangkuman:** Funk/Soul/R&B = groove 16th + ghost notes + stab horns + pads
ringan. MusicXML: `<notehead>ghost`, `articulations`, `<harmony>` class kunci,
vokal melisma `<extend/>`. Lanjut ke [Adaptasi Funk/Soul/R&B
(`Ch2-Adaptasi-Instrumentasi.md`)].