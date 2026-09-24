---
title: "The Note Element"
tier: "MusicXML Masterclass"
subject: "Anatomy of MusicXML"
xml_tags: ["<note>", "<pitch>", "<rest>", "<unpitched>", "<duration>", "<type>", "<chord>", "<tie>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — The Note Element

> **Reference books:** MusicXML W3C 4.0 spec, *The Note Element* and *The Global
> Note Element*; Gould *Behind Bars* (Chapter 8 rhythm). Focus: pitch, duration,
> chord, tie/grace — the atomic building blocks that compose all scores.

## 4.1 The `<pitch>` Element (Step, Octave, Alter)

Every pitched note has a `<pitch>`:

| Sub-element | Type | Example |
|------------|-------|--------|
| `<step>` | A–G (uppercase) | `C` |
| `<alter>` | int (0 natural; 1 sharp; −1 flat; ...) | `1`, `-1` |
| `<octave>` | 0–9 (commonly 1–7) | `4` |

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
      <note>
      <pitch>
      <step>F</step>
      <alter>1</alter>
      <octave>4</octave>
      </pitch>
      <duration>2</duration>
      <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<alter>` determines the *sounding pitch*; `<accidental>` is only a
> **display** (redundant hint / cautionary). Notation tools will often adjust
> `<accidental>` automatically from key+alter.

### 4.1.1 List of Types


| Element | Function |
|--------|--------|
| `<pitch>` | Pitched note (pitch class + octave) |
| `<rest>` | Silence (`measure="yes"` for a full-measure rest) |
| `<unpitched>` | Unpitched percussion (display-step/octave) |

## 4.2 Rest & Unpitched

### 4.2.1 `<rest>`

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
      <note>
      <rest/>
      <duration>4</duration>
      <voice>1</voice>
      <type>whole</type>
      </note>
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
      <note>
      <rest measure="yes">
      <display-step>C</display-step>
      <display-octave>4</display-octave>
      </rest>
      <duration>4</duration>
      <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `measure="yes"` = *full-measure rest*; the visual position may be set with
> display-step/octave.

### 4.2.2 `<unpitched>`

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
      <note>
      <unpitched>
      <display-step>C</display-step>
      <display-octave>5</display-octave>
      </unpitched>
      <duration>2</duration>
      <instrument id="P1-S"/>
      <type>eighth</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 4.3 Duration & Type

### 4.3.1 `<duration>` — units in `divisions`

`<divisions>` in `<attributes>` states that quarter = N units.

| Note | Duration (divisions=2) | `<type>` |
|-----|----------------------|----------|
| Whole | 8 | `whole` |
| Half | 4 | `half` |
| Quarter | 2 | `quarter` |
| Eighth | 1 | `eighth` |
| 16th | 0.5 (use larger divisions) | `16th` |

### 4.3.2 Dotted Values

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
      <note>
      <pitch><step>E</step><octave>4</octave></pitch>
      <duration>3</duration>
      <type>quarter</type>
      <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<dot/>` may repeat (double-dot). MusicXML computes duration, while
> `<type>`+`<dot>` give the *visual*; both must be consistent.

## 4.4 `<chord/>` — Vertical Chord Notation

- The first note has NO `<chord/>`.
- The 2nd note onward gets `<chord/>`.

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
      <note>
      <pitch><step>C</step><octave>4</octave></pitch>
      <duration>2</duration>
      <type>quarter</type>
      </note>
      <note>
      <pitch><step>E</step><octave>4</octave></pitch>
      <duration>2</duration>
      <type>quarter</type>
      <chord/>
      </note>
      <note>
      <pitch><step>G</step><octave>4</octave></pitch>
      <duration>2</duration>
      <type>quarter</type>
      <chord/>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Rule: all notes in a `<chord/>` series must have the **same duration**, and
> there must be no `<chord/>` on the first note of the series.

## 4.5 Tie, Grace, Fermata

### 4.5.1 Tie

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
      <note>
      <pitch><step>F</step><octave>4</octave></pitch>
      <duration>2</duration>
      <tie type="start"/>
      <notations>
      <tied type="start"/>
      </notations>
      </note>
      <note>
      <pitch><step>F</step><octave>4</octave></pitch>
      <duration>2</duration>
      <tie type="stop"/>
      <notations>
      <tied type="stop"/>
      </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<tie>` = playback; `<tied>` (inside `<notations>`) = the visual curve. Both
> must be synchronized.

### 4.5.2 Grace Notes

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
      <note>
      <grace slash="yes"/>
      <pitch><step>D</step><octave>5</octave></pitch>
      <type>eighth</type>
      <stem>up</stem>
      </note>
      <note>
      <pitch><step>C</step><octave>5</octave></pitch>
      <duration>2</duration>
      <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

- `grace` may have `slash="yes"`, `make-time="half"` (steals half), and
  `steal-time-previous/next` in MusicXML 3.1+.

## 4.6 Voice/Staff/Normal & Musis

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
      <note>
      <pitch><step>C</step><octave>4</octave></pitch>
      <duration>2</duration>
      <voice>1</voice>
      <type>quarter</type>
      <staff>1</staff>
      </note>
    </measure>
  </part>
</score-partwise>
```

- `<voice>` — voice index (polyphony).
- `<staff>` — staff number in a multi-staff part (1=top, 2=bottom).

### 4.6.1 `<normal-notes>` & dopp. in the accent

For simultaneous counts, `<time-modification>` is used:

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
      <norm k>
      <time-modification>
      <actual-notes>3</actual-notes>
      <normal-notes>2</normal-notes>
      </time-modification>
      </norm>
    </measure>
  </part>
</score-partwise>
```

(Triplet: 3 actual = 2 normal.)

## 4.7 Display: Accidental, Notehead, Colour

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
      <note>
      <pitch><step>B</step><alter>-0.5</alter><octave>4</octave></pitch>
      <duration>2</duration>
      <type>quarter</type>
      <accidental>quarter-flat</accidental>
      <notehead>diamond</notehead>
      </note>
    </measure>
  </part>
</score-partwise>
```

- `<accidental>`: `natural`, `sharp`, `flat`, `quarter-flat`, `double-sharp`,
  `cautionary`, `forced`.
- `<notehead>`: `normal`, `diamond`, `triangle`, `x`, `slash`, `circle`,
  `cluster`, `none`, and modifiers `filled`/`parentheses` (slashes).

## 4.8 Full Structure of a `<note>` Example

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
      <note>
      <chord/>
      <grace/>
      <pitch>
      <step>A</step>
      <alter>0</alter>
      <octave>5</octave>
      </pitch>
      <duration>2</duration>
      <tie type="start"/>
      <voice>2</voice>
      <type>quarter</type>
      <accidental>natural</accidental>
      <notations>
      <tied type="start"/>
      </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 4.9 Note Element Checklist

| Check | Yes/No |
|---------|----------|
| Pitched notes use `<pitch>`? | |
| Rest/unpitched matches the type? | |
| Duration consistent with `divisions`? | |
| `<type>`+`<dot/>` represent the duration? | |
| `<chord/>` only on the 2nd note onward? | |
| Voice/staff filled in for polyphony? | |
| Tie: `<tie>` & `<tied>` synchronized? | |

## 4.10 Misconceptions

- **"`<accidental>` affects sound"** — No; it must be redundant → the sound is
  `<alter>`; accidental is display-only.
- **"Duration may be inconsistent with type"** — Software will *resync*; always
  keep them consistent.
- **"Grace doesn't need duration"** — Grace notes are *left without `<duration>`*
  (`make-time` attribute) whenever possible.

## 4.11 Book & Source References

- W3C MusicXML 4.0 — Note chapter:
  https://www.w3.org/2021/06/musicxml40/
- music21 docs: https://web.mit.edu/music21/doc/
- Gould, *Behind Bars: The Definitive Guide to Music Notation*.

---

**Summary:** `<note>` is the atomic block: pitched (`<pitch>`), silence
(`<rest>`), percussion (`<unpitched>`), plus `<duration>`+`<type>` for rhythm,
`<chord/>` for verticality, `<tie>`/`<tied>` for ties, and `<grace>` for
ornaments. Continue to [Attributes & Directions
(`Ch3-Attributes-Directions.md`)].
