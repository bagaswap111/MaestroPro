---
title: "Upper Structures & Alterations"
tier: "Master S2"
subject: "Harmoni Jazz & Post-Tonal"
xml_tags: ["<harmony>", "<degree>", "<degree-value>", "<degree-alter>", "<degree-type>", "<kind>", "<bass>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Upper Structures & Alterations

> **Buku panduan bab ini:** Mark Levine, *The Jazz Theory Book* (Bab 7–9 —
> upper structures, tritone substitution, altered dominant); Frank Mantooth,
> *Voicings for Jazz Keyboard*; masterclass Berklee. Fokus: menulis warna
> "*altered*" pada dominan secara efisien pada symbol & part.

## 2.1 Definisi Upper Structure (US)

*Upper Structure* = triad (atau susunan teh) di atas **bagian dasar** dari
akor dominan. Idenya: alih-alih menulis G7(b9#9b13) penuh, tulis G7
ditumpuk dengan triad Db (b9–3–b13) di register atas.

> **Notasi umum:** `G7(US bII)` = G7 + triad Db → bunyi altered.

## 2.2 Pengelompokan Upper Structure pada Dominan

| US | Triad di atas | Nomor atas | Warna |
|----|---------------|------------|-------|
| US I | G–B–D | 9–11–13 | natural / Mixolydian |
| US bII | Db–F–Ab | b9–3–b13 | altered |
| US III | Eb–G–Bb | #9–5–b7 | altered (b7 di atas) |
| US IV | F–A–C | 11–b13–1 | sus/11 |
| US V | D–F#–A | 5–13–1 | Lydian dominant |
| US VI | A–C#–E | 13–b7–9 | warna puncak |

### 2.2.1 Regel Register

- Letakkan triad US di **register atas** (oktaf), bass tetap root.
- Jaga **bass + guide tones** (3rd & 7th) di lokasi jelas — jangan
  kerumunan di register tengah.

## 2.3 Altered Dominant — Tiga Notasi Setara

| Konsep | Simbol | Bunyi (atas G) |
|--------|--------|----------------|
| Altered chord symbol | G7alt | G B F + D♭ E♭ A♭ |
| Degree-based | G7(b9#9b13) | s/d degree |
| Upper Structure | G7(US bII) | triad Db |

Ketiganya *setara sonically*. Pilihan bergantung konteks/engraver.

### 2.3.1 MusicXML: C7#9♭13

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
        <kind text="7#9b13">dominant</kind>
        <degree>
          <degree-value>9</degree-value>
          <degree-alter>1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
        <degree>
          <degree-value>13</degree-value>
          <degree-alter>-1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 2.3.2 Fm11♭5 (half-diminished dengan 11)

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
        <root><root-step>F</root-step></root>
        <kind text="m11b5">other</kind>
        <degree>
          <degree-value>5</degree-value>
          <degree-alter>-1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
        <degree>
          <degree-value>11</degree-value>
          <degree-alter>0</degree-alter>
          <degree-type>add</degree-type>
        </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Tritone Substitution

*Tritone substitution* = mengganti V7 dengan **bII7** (jarak tritone), berbagi
guide tones:

| Akor | 3rd | 7th |
|------|-----|-----|
| G7 | B | F |
| D♭7 | F | C♭ (=B) |

Kekuatannya: resolusi turun setengah nada (C♭→B♮, F→E) menuju tonik.

### 2.4.1 Aplikasi: ii–V–I dengan Substitusi

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
        <root><root-step>D</root-step></root>
        <kind text="m7">minor-seventh</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>D♭</root-step></root>
        <kind text="7">dominant</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="maj7">major-seventh</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 2.4.2 Backup: bIII7 / bVI7

Substitusi sekunder: `bVI7 → I` (mixture), `bIII7` di atas relatif — 
penemuan umum di film scoring & modern jazz harmony.

## 2.5 Extensions & Polychord

Extensions (9, 11, 13) boleh ditulis sebagai polychord (dua root berbeda):
`C7` di atas `Db` (US bII). Kerepresentasian MusicXML:

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
        <kind text="C7/US bII">dominant</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

> Untuk diagram fret, gunakan `<frame>` dalam `<harmony>` (gitar) atau
> `words` (analytical fallback).

## 2.6 Harmoni Warna Tambahan

| Teknik | Simbol | MusicXML |
|--------|--------|----------|
| Sus4 | Csus | `<kind>suspended-fourth</kind>` |
| Sus2 | Csus2 | `<kind>suspended-second</kind>` |
| Add9 | Cadd9 | `<kind>major</kind>` + `<degree> add 9` |
| 6/9 | C6/9 | `major` + add 9 |
| Borrowed (modal mixture) | iv→I | `bVI`, `iv` via `<bass>`/degree |
| Diminished passing | °7 | `diminished` |

### 2.6.1 Separasi: Sus vs Add

- **SusX:** mengganti 3rd (tanpa major/minor).
- **Add9:** akor +9, 3rd tetap hadir (Cmaj → Cadd9).
- MusicXML: sus → `<kind>`; add → `kind` + `<degree> add`.

## 2.7 Voicing Compression (Piano)

- **Drop 2/4**, **quartal**, **cluster** — semua menambahkan ruang pada
  upper structure.
- Piano jazz: **root + guide tones di tangan kiri**; **US triad di kanan**
  atas oktaf dari bass.
- Satu *staf ganda*: staff 2 (bass/root), staff 1 (chord with `<chord/>`).

## 2.8 Latihan

1. Tulis G7alt dalam 3 versi: G7b9, G7#9b13, G7(US bII).
2. Terapkan tritone substitution pada ii–V–I di F mayor.
3. Analisis 10 bar lead sheet jazz — tandai setiap extension/altered.
4. Konversi ketiga akor ke MusicXML `<harmony>` + `<degree>`; verifikasi di
   MuseScore.

## 2.9 Checklist

| Periksa | Ya/Tidak |
|---------|----------|
| US triad di register atas? | |
| Guide tones (3rd/7th) jelas? | |
| Simbol + degree konsisten? | |
| Sus vs add dibedakan benar? | |
| Tritone sub disertai analisi? | |

## 2.10 Repertoar Dengar

- Herbie Hancock, *Maiden Voyage* — sus/upper structure.
- Thelonious Monk, *Round Midnight* — altered/bII.
- Bill Evans, *Blue in Green* — voicing.

## 2.11 Referensi

- Levine, *The Jazz Theory Book*.
- Mantooth, *Voicings for Jazz Keyboard*.
- MusicXML chord: https://www.w3.org/2021/06/musicxml40/

---

**Rangkuman:** US & alterations menambah warna dominan; MusicXML
`<degree>` (value/alter/type) menulis alterasi, `<bass>` untuk slash,
`<kind>` untuk sus/add, dan `words`/`frame` untuk polychord. Lanjut ke
[Harmoni Post-Tonal (`Ch3-Harmoni-PostTonal.md`)].