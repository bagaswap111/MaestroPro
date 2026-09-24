---
title: "Harmony & Chord Symbols"
tier: "MusicXML Masterclass"
subject: "Anatomy of MusicXML"
xml_tags: ["<harmony>", "<root>", "<kind>", "<degree>", "<bass>", "<frame>", "<degree-value>", "<degree-type>", "<function>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 3 — Harmony & Chord Symbols

> **Reference books:** W3C MusicXML 4.0 — *The Harmony Element*; Levine, *The
> Jazz Theory Book* (standard jazz chord symbols) for chord terminology;
> Gould *Behind Bars*. Focus: chord symbols, alterations, slash chords, and
> function analysis in a single `<harmony>` element.

## 4.1 Basic Chord Symbols

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

- `<root-step>` = root note; optional `<root-alter>` for chords like
  `C♯`/`E♭`.
- `<kind>` = quality; the `text` attribute = how it appears in the score.

### 4.1.1 Example: Dm7

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

### 4.1.2 Standard `<kind>` Values (W3C)

| Value | Meaning | Common text |
|-------|------|-----------|
| `major` | Major | C |
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
| `other` | custom | (custom symbol) |

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

- `degree-value`: 1–13 (degree).
- `degree-alter`: 0 (natural), 1 (sharp), −1 (flat), .5 (quarter).
- `degree-type`: `add`, `alter`, `subtract`.

### 4.2.2 Example: Fm11♭5

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

### 4.2.3 Sus Chord (Sus4)

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

## 4.3 Slash Chords, Polychords, Inversions

### 4.3.1 Slash/Inversion — `<bass>`

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

### 4.3.2 Polychord / Upper Structure — `<words>` Fallback

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

> Nonstandard extensions: some software render them, some do not; keep the
> strong symbol via `<harmony>`, analytical info in words/pedagogy.

## 4.4 `<frame>` — Fret Diagram for Guitar/Ukulele

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

- `frame-string`: number of strings.
- `frame-fret`: number of frets.
- `frame-note`: `fret`/`string` position, optional `fingering`.

## 4.5 `print-frame`, `print-object`, and Offset

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

- `print-frame="no"` → do not render the diagram.
- `print-object="no"` → do not render the symbol (for analysis only).

## 4.6 `<function>` — Analysis/Roman

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

> `<function>` is very useful for machine-learning pipelines & automated
> analysis (as used by labs) — but not all software export it.

## 4.7 Harmony Checklist

| Check | Yes/No |
|---------|----------|
| Root correct (`root-step`, `root-alter`)? | |
| `kind` matches the quality? | |
| Alteration via `<degree>` correct? | |
| Slash chord when the bass is not the root? | |
| Function/roman numeral optional? | |
| Frame only when a diagram is needed? | |

## 4.8 Misconceptions

- **"`<degree>` adds sound"** — It changes the *symbol*/understanding of the
  chord; playback comes from `kind`+degree on the other hand.
- **"Polychords are supported by all software"** — NO; provide a words
  fallback.
- **"`<function>` is required"** — Optional; some exporters drop it.

## 4.9 Exercises

1. **Basic:** Write Cmaj7, G7sus, Am7♭5 in `<harmony>`.
2. **Intermediate:** Slash chords C/E, D/F#; add degree b9 to G7.
3. **Advanced:** Create a polychord US bII; choose a words fallback; analyze
   guitar/ukulele frame diagrams.

## 4.10 Book & Source References

- W3C MusicXML 4.0 harmony: https://www.w3.org/2021/06/musicxml40/
- Levine, *The Jazz Theory Book* — chord symbol conventions.
- Gould, *Behind Bars* — harmonic notation chapter.

---

**Summary:** `<harmony>` = root + kind + optional degree/bass/frame/function;
renders chord symbols, slash chords, alterations, and analysis. This
concludes Subject [4.1 Anatomy of MusicXML]. Continue to [Music Engraving Rules
(`../4.2-Music-Engraving-Rules/`)].
