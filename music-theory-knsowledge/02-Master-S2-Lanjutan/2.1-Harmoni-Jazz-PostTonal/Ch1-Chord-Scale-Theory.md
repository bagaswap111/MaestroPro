---
title: "Chord-Scale Theory"
tier: "Master S2"
subject: "Harmoni Jazz & Post-Tonal"
xml_tags: ["<harmony>", "<root>", "<kind>", "<degree>", "<root-alter>", "<degree-alter>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Chord-Scale Theory

> **Buku panduan bab ini:** Mark Levine, *The Jazz Theory Book* (Bab 1–7);
> George Russell, *The Lydian Chromatic Concept of Tonal Organization*
> (LCC); hal bantu *The Berklee Book of Jazz Harmony*. Fokus: menghubungkan
> setiap akor dengan skala/modenya sebagai bahan improvisasi dan harmoni.

## 1.1 Konsep Chord-Scale

*Chord-scale theory* menghubungkan setiap akor dengan skala/kolase di atasnya
— Untuk improvisasi kalimat dan komposisi vertikal. Sebuah akor bukan hanya
kumpulan nada, tetapi "menyalakan" sebuah scale yang berisi sonority aman
untuk memberikannya.

| Akor | Skala | Interval |
|------|-------|----------|
| Cmaj7 | Ionian (C mayor) | 1 2 3 4 5 6 7 |
| Dm7 | Dorian | 1 2 b3 4 5 6 b7 |
| G7 | Mixolydian | 1 2 3 4 5 6 b7 |
| Fmaj7 | Lydian | 1 2 3 #4 5 6 7 |
| Am7 | Aeolian | 1 2 b3 4 5 b6 b7 |
| Bø7 | Locrian | 1 b2 b3 4 b5 b6 b7 |
| C7alt | Super Locrian | 1 b2 #2 3 b5 b6 b7 |

### 1.1.1 Tujuh Mode sebagai Warna

| Mode | Karakter | Triad/7th ke atas |
|------|----------|--------------------|
| Ionian | netral, dasar | maj7 |
| Dorian | minor + 6 natural (fleksibel) | m7 |
| Phrygian | minor + b2 | m7 |
| Lydian | maj7 + #4 (dreamy) | maj7 |
| Mixolydian | dom7 + b7 (blues) | 7 |
| Aeolian | minor natural | m7 |
| Locrian | m7b5 / semidim | ø7 |

## 1.2 Menerapkan dalam Improvisasi

1. min7 → Dorian (atau Aeolian bila warna lebih gelap).
2. dom7 → Mixolydian; *alterations* (b9/#9/b13) tepat bila menyentuh
   akor altered.
3. maj7 → Ionian atau Lydian (Lydian inferior umum untuk avoid #4).
4. ø7 → Locrian (atau Locrian #2 bila pakai skala minor-melodik).
5. Ganti skala **saat akor berganti** (biasanya batas ketukan).

### 1.2.1 Guide Tones — 3rd & 7th

- 3rd menentukan mayor/minor.
- 7th menentukan fungsi (dom vs maj).
- Semua soli jazz membangun **voice leading lewat guide tones**.

## 1.3 Aplikasi: ii–V–I di F

| Akor | Skala | Nada |
|------|-------|------|
| Gm7 | G Dorian | G A Bb C D E F |
| C7 | C Mixolydian | C D E F G A Bb |
| Fmaj7 | F Lydian | F G A B C D E |

Contoh garis solo 2 bar:

```
Gm7:  G – A – Bb – C      (stepwise, dorian)
C7:   D – F – E            (guide 7-3 + passing)
Fmaj7: C – E – F           (approach ke F)
```

## 1.4 Avoid Notes & Chord-Scale

- **Avoid note** = nada yang *bertabrakan* dengan dasar (mis. 4th pada
  Ionian/maj7 bila tidak diberi pola).
- Pada *Maj7*: 4th sering "avoid" (miring), diganti 3rd atau #4 (Lydian).
- Pada *dom7*: batas avoid bergantung konteks (Mixolydian#11 ok bila
  digaris).
- Konsep LCC (Russell): **Lydian** di atas akord mayor adalah skala "paling
  terang"; "Chord = scale pancaran warna" — skala ditentukan oleh *akor*.

## 1.5 Upper Structures sebagai Konsekuensi Chord-Scale

| US | Triad di atas | Nomor atas | Efek |
|----|---------------|------------|------|
| US bII | Db–F–Ab | b9–3–b13 | altered |
| US III | Eb–G–Bb | #9–5–b7 | altered |
| US V | D–F#–A | 9–5–13 | Lydian dominant |
| US VI | A–C#–E | 13–b7–9 | warna puncak |

### 1.5.1 MusicXML: Altered Dominant dengan `<degree>`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Piano</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="7b9#9">dominant</kind>
        <degree>
          <degree-value>9</degree-value>
          <degree-alter>-1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
        <degree>
          <degree-value>9</degree-value>
          <degree-alter>1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

> `degree-value`=9, `degree-alter` -1 = mol, 1 = kruis, `degree-type` `alter`.

## 1.6 Lydian Chromatic Concept (Russell)

- Empat "generating scales" dari root C (paling terang hingga gelap):
  Lydian > Ionian > Mixolydian > ... > Locrian.
- Lydian sebagai "super-istana"; akord mayor asli = sub-Lydian chu.
- Praktis: untuk maj7 gunakan **Lydian** (a #4 menghindari b9 clash), pada
  dom7 gunakan **Lydian dominant** (maj3, #4, b7).

## 1.7 Menyatukan dalam Komposisi

1. Tulis progresi (ii–V–I, turnarounds, modal).
2. Tentukan skala & guide tones tiap akor.
3. Buat melodi dari langkah diatonik + guide approach.
4. Perkaya harmoni dengan upper structures agar warna altered tersirat
   tanpa menghitung tiap not di pengiring.

## 1.8 Studi Kasus

- **Levine** — bab 1–7 (chord-scale, ii–V–I, rhythm changes).
- **Russell LCC** — "recharges" pendekatan modal.
- **Herbie Hancock "Maiden Voyage"** — modal: D dorian, C dorian, F mix.
- **John Coltrane "Giant Steps"** — perubahan kunci jarak jauh (CDM
  application).

## 1.9 Checklist Penulisan Chord-Scale

| Periksa | Ya/Tidak |
|---------|----------|
| Setiap akor punya skala implisit? | |
| Guide tones jelas pada register utama? | |
| Upper structure/alteration via `<degree>`? | |
| Mode sesuai warna yang diminta? | |
| Avoid note dihindari / ditangani? | |

## 1.10 Latihan

1. **Dasar:** Tulis skala Dorian, Mixolydian, Lydian dari root G.
2. **Menengah:** Improvisasi 8 bar ii–V–I di Bb; endapkan guide-tone
   approach.
3. **Lanjut:** Analisis "Giant Steps" — chord-scale untuk tiap bar; buat
   lead-sheet MusicXML dengan `<harmony>`.

## 1.11 Repertoar Dengar

- Miles Davis, *So What* — modal dorian.
- John Coltrane, *Giant Steps / Naima* — progresi kolom.
- Herbie Hancock, *Maiden Voyage*.
- Bill Evans trio — voicings chord-scale.

## 1.12 Referensi Buku & Sumber Web

**Buku:**
- Levine, *The Jazz Theory Book*.
- Russell, *Lydian Chromatic Concept of Tonal Organization*.
- *The Berklee Book of Jazz Harmony*.

**Web:**
- iReal Pro chord list: https://irealpro.com/
- *Jazz Theory* resource: https://tobiasone.gr/ jazz library
- MusicXML chord docs: https://www.w3.org/2021/06/musicxml40/

---

**Rangkuman:** Chord-scale theory menghubungkan akor & skala-mode sebagai
dasar warna/improvisasi; Levine + Russell memberi dua kaca: fungsi dan
modal-warna. MusicXML menyimpan kelas akor di `<harmony>`, alterasi/upper
structure di `<degree>`. Lanjut ke [Upper Structures & Alterations
(`Ch2-Upper-Structures-Alterations.md`)].