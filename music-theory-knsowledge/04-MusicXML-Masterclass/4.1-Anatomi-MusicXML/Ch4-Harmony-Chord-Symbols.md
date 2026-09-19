---
title: "Harmony & Chord Symbols"
tier: "MusicXML Masterclass"
subject: "Anatomi MusicXML"
xml_tags: ["<harmony>", "<root>", "<kind>", "<degree>", "<bass>", "<frame>", "<degree-value>", "<degree-type>", "<function>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 3 — Harmony & Chord Symbols

> **Buku panduan:** W3C MusicXML 4.0 — *The Harmony Element*; Levine, *The
> Jazz Theory Book* (simbol akor standar jazz) untuk terminology chord;
> Gould *Behind Bars*. Fokus: chord symbol, alteration, slash, dan analisis
> fungsi dalam satu elemen `<harmony>`.

## 4.1 Chord Symbol Dasar

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
      <harmony>
      <root>
      <root-step>C</root-step>
      </root>
      <kind text="maj7">major-seventh</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

- `<root-step>` = nada dasar; optional `<root-alter>` untuk akor seperti
  `C♯`/`E♭`.
- `<kind>` = kualitas; `text` attribute = cara tampil di score.

### 4.1.1 Contoh: Dm7

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
      <harmony>
      <root>
      <root-step>D</root-step>
      </root>
      <kind text="m7">minor-seventh</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 4.1.2 Nilai `<kind>` Standar (W3C)

| Value | Arti | Teks umum |
|-------|------|-----------|
| `major` | Mayor | C |
| `minor` | Minor | Cm |
| `dominant` | Dominant | C7 |
| `major-seventh` | Maj7 | Cmaj7 |
| `minor-seventh` | Min7 | Cm7 |
| `diminished` | Dim | Cdim |
| `augmented` | Aug | C+ |
| `half-diminished` | m7♭5 | Cm7♭5 |
| `minor-major` | mMaj7 | Cm(maj7) |
| `suspended-second` | Sus2 | Csus2 |
| `suspended-fourth` | Sus4 | Csus4 |
| `other` | custom | (folder custom) |

## 4.2 Extended & Altered Chords

### 4.2.1 `<degree>` — Alter/Add/Subtract

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
      <harmony>
      <root><root-step>C</root-step></root>
      <kind text="7b9">dominant</kind>
      <degree>
      <degree-value>9</degree-value>
      <degree-alter>-1</degree-alter>
      <degree-type>alter</degree-type>
      </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

- `degree-value`: 1–13 (derajat).
- `degree-alter`: 0 (natural), 1 (kruis), −1 (mol), .5 (kuarto).
- `degree-type`: `add`, `alter`, `subtract`.

### 4.2.2 Contoh: Fm11♭5

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
      <harmony>
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

### 4.2.3 Sus-Chord (Sus4)

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
      <harmony>
      <root><root-step>G</root-step></root>
      <kind text="sus4">suspended-fourth</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 4.3 Slash Chords, Polychords, Inversi

### 4.3.1 Slash/Inversi — `<bass>`

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
      <harmony>
      <root><root-step>C</root-step></root>
      <kind text="C/E">major</kind>
      <bass>
      <bass-step>E</bass-step>
      </bass>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

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
      <harmony>
      <root><root-step>D</root-step></root>
      <kind text="D/F#">major</kind>
      <bass>
      <bass-step>F</bass-step>
      <bass-alter>1</bass-alter>
      </bass>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 4.3.2 Polychord / Upper Structure — Fallback `<words>`

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
      <harmony>
      <root><root-step>G</root-step></root>
      <kind text="G7alt">dominant</kind>
      </harmony>
      <direction placement="above">
      <direction-type>
      <words xml:space="preserve">G7alt (US bII: Db)</words>
      </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> Nonstandar lengan: sebagian software render penuh tidak; simpan simbol kuat
> via `<harmony>`, info analitik di words/pedagogy.

## 4.4 `<frame>` — Diagram Fret untuk Gitar/Ukulele

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
      <harmony>
      <root><root-step>C</root-step></root>
      <kind>major</kind>
      <frame>
      <frame-strings>6</frame-strings>
      <frame-frets>3</frame-frets>
      <frame-note fret="0" string="3"/>
      <frame-note fret="1" string="2"/>
      <frame-note fret="3" string="4"/>
      </frame>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

- `frame-string` : jumlah senar.
- `frame-fret` : jumlah fret.
- `frame-note` : posisi `fret`/`string`, optional `fingering`.

## 4.5 `print-frame`, `print-object`, dan Offset

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
      <root><root-step>Am</root-step></root>
      <kind text="m">minor</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

- `print-frame="no"` → jangan render diagram.
- `print-object="no"` → jangan render simbol (untuk analysis saja).

## 4.6 `<function>` — Analisis/Roman

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
      <harmony>
      <root><root-step>G</root-step></root>
      <kind>dominant</kind>
      <function>V</function>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

> `<function>` sangat berguna untuk pipeline machine-learning & analisis
> otomatis (dikelola lab) — tapi tidak semua software meng-export.

## 4.7 Checklist Harmony

| Periksa | Ya/Tidak |
|---------|----------|
| Root benar (`root-step`, `root-alter`)? | |
| `kind` sesuai kualitas? | |
| Alteration via `<degree>` benar? | |
| Slash chord saat bass bukan root? | |
| Function/romanic optional? | |
| Frame hanya bila perlu diagram? | |

## 4.8 Miskonsepsi

- **"`<degree>` menambah bunyi"** — Mengubah *simbol*/pemahaman akor; playback
  disatu pihak dari `kind`+degree.
- **"Polychord didukung semua software"** — TIDAK; sediakan fallback words.
- **"`<function>` wajib"** — Opsional; beberapa exporter menghapus.

## 4.9 Latihan

1. **Dasar:** Tulis Cmaj7, G7sus, Am7♭5 dalam `<harmony>`.
2. **Menengah:** Slash chords C/E, D/F#; tambah degree b9 di G7.
3. **Lanjut:** Buat polychord US bII; pilih fallback words; analisis frame
   guitar ukulele diagnostics.

## 4.10 Referensi Buku & Sumber

- W3C MusicXML 4.0 harmony: https://www.w3.org/2021/06/musicxml40/
- Levine, *The Jazz Theory Book* — chord symbol conventions.
- Gould, *Behind Bars* — ch. harmonic notation.

---

**Rangkuman:** `<harmony>` = root + kind + optional degree/bass/frame/function;
merender chord symbol, slash chords, alterations, dan analisis. Ini
menutup Subject [4.1 Anatomi MusicXML]. Lanjut ke [Music Engraving Rules
(`../4.2-Music-Engraving-Rules/`)].