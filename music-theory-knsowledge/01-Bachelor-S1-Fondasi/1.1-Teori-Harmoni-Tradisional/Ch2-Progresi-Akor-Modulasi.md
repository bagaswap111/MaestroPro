---
title: "Progresi Akor & Modulasi"
tier: "Bachelor S1"
subject: "Teori Harmoni Tradisional"
xml_tags: ["<attributes>", "<key>", "<fifths>", "<mode>", "<transpose>", "<harmony>", "<root>", "<kind>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Progresi Akor & Modulasi

> **Buku panduan bab ini:** Kostka & Payne, *Tonal Harmony* (Bab 3–5, 18–21);
> Aldwell & Schachter, *Harmony and Voice Leading* (Bab 2–3, 26–30); Schachter,
> "Modulation" dalam *The Music Forum*. Fokus: bagaimana progresi menggerakkan
> frase, dan bagaimana modulasi memindahkan pusat tonal.

## 2.1 Progresi Akor Standar

Progresi adalah urutan fungsi bersiklus yang mengikat frase. Kekuatan diukur
dari **jarak root** dan **arah**:

### 2.1.1 Circle of Fifths (Descending Fifth)

Urutan **root turun kwinlima** adalah gerakan harmonik terkuat dan paling
mengikat:

```
C → F → B° → Em → Am → Dm → G → C
I → IV → vii° → iii → vi → ii → V → I
```

Bila dibalik, **I→IV** (naik kwinlima) menimbulkan stasis — dipakai pada
kadens plagal dan chorus pop.

```xml
<measure number="1">
  <harmony print-frame="no"><root><root-step>C</root-step></root><kind text="maj">major</kind></harmony>
  <harmony print-frame="no"><root><root-step>F</root-step></root><kind text="maj">major</kind></harmony>
  <harmony print-frame="no"><root><root-step>G</root-step></root><kind text="7">dominant</kind></harmony>
  <harmony print-frame="no"><root><root-step>C</root-step></root><kind text="maj">major</kind></harmony>
</measure>
```

### 2.1.2 Progresi yang Perlu Dicermati

| Progresi | Karakter | Catatan |
|----------|----------|---------|
| I → IV | Plagal/sim | Naik kwinlima; stasis bila berlebih |
| V → IV | *Backwards* | Kadang efektif (blues), bukan standar |
| V → VI/iii → … | Gerak b'lfur | Rantai "retrogresi" |
| ii → V | Prepared dominan | Paling umum menuju kaden |
| I → vi → IV → V | Doo-wop | Dasar pop (lihat genre tier) |
| vi → IV → I → V | Pop canon | Triangle (modern) |

**Prinsip Kostka-Payne:** progresi terbaik berjalan "lingkaran" — mendekati
V melalui ii/IV, lalu kembali ke I. Hindari rangkaian *descending fifth*
yang melebihi 3–4 langkah tanpa arah.

## 2.2 Pola Progresi Lintas Genre

| Gaya | Pola khas | Sifat |
|------|-----------|-------|
| Klasik | I–IV–V–I; I–vi–ii–V | fungsi tegas |
| Pop/ballad | I–V–vi–IV | loop melankolis |
| Doo-wop | I–vi–IV–V | nostalgia 50s |
| Jazz turnaround | I–vi–ii–V | siklus menuju V |
| Blues | I7–IV7–I7–V7 | dominant pile-up |
| Modal | I–IV (diatonic) vamp | statis, warna |

### 2.2.1 MusicXML: 8 Bar Progresi Pop (I–V–vi–IV)

```xml
<measure number="1">
  <harmony print-frame="no"><root><root-step>C</root-step></root><kind>major</kind></harmony>
</measure>
<measure number="2">
  <harmony print-frame="no"><root><root-step>G</root-step></root><kind text="maj">major</kind></harmony>
</measure>
<measure number="3">
  <harmony print-frame="no"><root><root-step>A</root-step></root><kind text="m">minor</kind></harmony>
</measure>
<measure number="4">
  <harmony print-frame="no"><root><root-step>F</root-step></root><kind>major</kind></harmony>
</measure>
```

## 2.3 Modulasi: Memindahkan Pusat Tonal

Modulasi bukan sekadar "ganti kunci"; ia adalah **proses** yang harus
didukung secara logis. Tiga tipe utama (Kostka Bab 21; Aldwell Bab 26):

### 2.3.1 Modulasi Pivot Chord (Common-Chord / Diatonic)

Ambil akor yang bisa dianalisis **di dua kunci** sekaligus:

- C mayor → G mayor: pivot **Dm** (ii di C, vi di G).
- C mayor → A minor: pivot **Am** (vi di C, i di Am) atau **F** (IV di C,
  VI di Am).

```
Menulis: [C] → Dm → [G] → C ... → G7 → C  (pivot Dm)
Analisis:  I    ii      V    I      V7   I
         (     vi di G      )
```

### 2.3.2 Modulasi Phrase (Phrase Modulation / Direct)

Pindah pusat **tanpa pivot** — biasa di awal *section baru* (Classical era,
pop bridges). MusicXML: cukup perbarui `<key>` di awal birama.

### 2.3.3 Modulasi Kromatik & Enhanced (Common-Tone / Chromatic)

- **Common-tone:** satu not dipertahankan sebagai jembatan ke kunci baru
  (C bass C → C#7? → F#m? konteks).
- **Chromatic:** pakai V7 sekunder (modulasi ke V: **D7** → G; ke IV:
  **C7** → F). Detail: Aldwell-Schachter "altered chords" eligibilitas.

### 2.3.4 MusicXML: `<key>` di `<attributes>` pada Birama Baru

```xml
<attributes>
  <divisions>2</divisions>
  <key>
    <fifths>1</fifths>
    <mode>major</mode>
  </key>
  <time><beats>4</beats><beat-type>4</beat-type></time>
  <clef><sign>G</sign><line>2</line></clef>
</attributes>
```

> `<fifths>` = jumlah krus/mol. G mayor = +1; F mayor = -1; A minor = 0
> (rela ke C); E minor = +1 (rela ke G). `cancel` berguna jika ada birama
> peralihan.

**Contoh dengan `<cancel>` (pergantian tanda menuju netral):**

```xml
<key>
  <cancel>2</cancel>
  <fifths>0</fifths>
</key>
```

## 2.4 Modulasi vs Transposisi — Perbedaan Krusial

| | Modulasi | Transposisi |
|--|----------|-------------|
| Definisi | Pindah *pusat* dalam karya | Salin *seluruh* karya ke kunci lain |
| Score | Tanda kunci berubah di tengah | Tanda kunci awal berubah total |
| MusicXML | `<key>` muncul di baris birama baru | `<transpose>` per part (instrumen transpos) |
| Tujuan | Ekspresif | Kebutuhan register/instrumen |

### 2.4.1 MusicXML `<transpose>` untuk Instrumen Transpos

Klarinet in B♭: bunyi konser = **1 nada lebih rendah** dari written. Maka:

```xml
<attributes>
  <transpose>
    <diatonic>-1</diatonic>
    <chromatic>-2</chromatic>
    <octave-change>0</octave-change>
  </transpose>
</attributes>
```

- `<diatonic>` — pergeseran nama derajat (B♭ klarinet: -1).
- `<chromatic>` — pergeseran semitone total (klarinet: -2).
- `<octave-change>` — bila ada perpindahan oktaf (piccolo, contrabass).

Saat mengimpor ke Dorico/MuseScore, transposisi dipakai per bagian; *display*
tetap *written* untuk pemain. (Detail: `Ch2-Transposisi-Instrumen.md`.)

## 2.5 Modulasi Bertahap & Sequences

- **Sequence (basa diatonik):** urutan progress naik/turun pada skala — salah
  satu mesin modulasi sampai 3–4 kunci berturut-turut.
- **Rosalia:** sequence kromatik naik (era Baroque mewah) — capai tonik
  jauh dengan *tendency tones*.

```
C:  I    V6/vi   ...   F#m ... → (modulasi kuat)
```

## 2.6 Latihan

1. **Dasar:** Labeli fungsi (T/S/D) pada progresi C–Am–F–G–C.
2. **Menengah:** Tulis modulasi pivot C→G (4 bar) di MusicXML: `<harmony>` +
  `<key>` di birama 4.
3. **Lanjut:** Buat *sequence* 6 chord naik (C–Am–Dm–G–C–F#°7/V?) dan uji
  mana pivot ke tonik baru; tulis analisis di komentar `<direction>`.

## 2.7 Repertoar Dengar

- Mozart, Piano Sonata K.283 I — modulasi ke V di eksposisi.
- Schubert, *Impromptu* D.935/2 — modulasi enharmonik (G#→♭).
- Chopin, Prelude Op.28 No.4 — harmonisasi kromatik/blues-ish.
- John Williams, *Imperial March* — progressive (modal–modulating).

## 2.8 Referensi Buku & Sumber Web

**Buku:**
- Kostka & Payne, *Tonal Harmony* (Bab 18–21).
- Aldwell & Schachter, *Harmony and Voice Leading* (Bab 26–30).
- Edward Aldwell, *The Music of ...* — essays modulasi.

**Web:**
- MusicXML `<key>` spec: https://www.w3.org/2021/06/musicxml40/
- Hooktheory: https://www.hooktheory.com/
- Open Notation (modulasi visual): https://www.musictheory.net/

---

**Rangkuman:** Progresi adalah siklus fungsi yang menentukan arah; modulasi
adalah perjalanan pusat tonal yang memerlukan pivot/chromatic/direct.
MusicXML mewakili melalui `<harmony>` untuk simbol, `<key>` (+`cancel`) untuk
perubahan tanda, dan `<transpose>` per bagian untuk instrumentasi. Lanjut ke
[Bab 3 — Voice Leading (`Ch3-Voice-Leading.md`)].