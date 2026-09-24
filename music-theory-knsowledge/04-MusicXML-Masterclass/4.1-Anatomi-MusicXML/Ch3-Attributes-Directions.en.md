---
title: "Attributes & Directions"
tier: "MusicXML Masterclass"
subject: "Anatomy of MusicXML"
xml_tags: ["<attributes>", "<divisions>", "<key>", "<time>", "<clef>", "<direction>", "<dynamics>", "<sound>", "<forward>", "<backup>", "<transpose>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — Attributes & Directions

> **Reference books:** W3C MusicXML 4.0 — *The Attributes Element* & *The
> Direction Element*; Gould, *Behind Bars* (Chapters 3–5: key, time, dynamics,
> tempo). Focus: setting scale/key/clef & encoding instructions above/below the
> staff.

## 4.1 The `<attributes>` Element (Divisions, Key, Time, Clef)

`<attributes>` establishes settings at the start of a measure — or whenever they
change.

### 4.1.1 `<divisions>`

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
      <divisions>2</divisions>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

> All `<duration>` values in the part are read against these divisions. It may
> change midway (when beat subunits require it), with a new `divisions`.

### 4.1.2 `<staves>` (Multi-Staff Part)

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
      <staves>2</staves>
      <clef number="1"><sign>G</sign><line>2</line></clef>
      <clef number="2"><sign>F</sign><line>4</line></clef>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

- When `<staves>` changes to 2, use `number` on `clef` & `staff`.

### 4.1.3 `<key>` — `fifths`/`mode`/`cancel`

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
      <key>
      <cancel>2</cancel>
      <fifths>1</fifths>
      <mode>minor</mode>
      </key>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

- `cancel` — number of accidentals canceled (for drastic key changes).
- `fifths` — sharps/flats; `mode` — `major`/`minor`.

### 4.1.4 `<time>` — Simple & Compound

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
      <time symbol="cut">
      <beats>2</beats>
      <beat-type>2</beat-type>
      </time>
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
      <time>
      <beats>6</beats>
      <beat-type>8</beat-type>
      </time>
    </measure>
  </part>
</score-partwise>
```

> Compound (`6/8`, `9/8`) only needs beats+beat-type; beat grouping usually
> comes from metronome/beam. `symbol="cut"` for alla breve.

### 4.1.5 `<clef>` — G, F, C, Percussion, TAB

| `sign` | Usage |
|--------|-----------|
| `G` | treble (default line 2) |
| `F` | bass (default line 4) |
| `C` | alto/tenor (line 3/4) |
| `percussion` | unpitched percussion |
| `TAB` | guitar tablature |
| `none` | no clef (percussion container) |

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
      <clef>
      <sign>G</sign>
      <line>2</line>
      <clef-octave-change>-1</clef-octave-change>
      </clef>
    </measure>
  </part>
</score-partwise>
```

- `clef-octave-change` — 8va/8vb transposition (±1 octave).

### 4.1.6 `<transpose>` — for transposing instruments (see `Ch2-Transposisi`)

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
      <transpose>
      <diatonic>-1</diatonic>
      <chromatic>-2</chromatic>
      <octave-change>0</octave-change>
      </transpose>
    </measure>
  </part>
</score-partwise>
```

## 4.2 `<direction>` — Instructions Above/Below the Staff

`<direction placement="above">` places text/graphics/dynamics at a specific
position.

### 4.2.1 `<direction-type>` → `<words>`/`<dynamics>`/`<wedge>`

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
      <direction placement="above">
      <direction-type>
      <words xml:space="preserve">pp</words>
      </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

Standard dynamics are notated with a dedicated element:

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
      <direction placement="above">
      <direction-type>
      <dynamics>
      <p/>
      </dynamics>
      </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> The `dynamics` element supports: `pppp`…`ppp`, `pp`, `p`, `mp`, `mf`, `f`,
> `ff`, `fff`, `ffff`, `fp`, `sf`, `sfz`, `rfz`, `rf`. Dynamics are separate
> from words (rendered below the staff baseline automatically).

### 4.2.2 Wedge (Hairpin)

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
      <direction placement="below">
      <direction-type>
      <wedge type="crescendo" number="1"/>
      </direction-type>
      </direction>
      ...
      <direction placement="below">
      <direction-type>
      <wedge type="stop" number="1"/>
      </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

- `wedge type`: `crescendo`, `diminuendo`, `stop`, `continue`.

### 4.2.3 Tempo — Metronome + Sound

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
      <direction placement="above">
      <direction-type>
      <metronome parentheses="no">
      <beat-unit>quarter</beat-unit>
      <per-minute>120</per-minute>
      </metronome>
      <words xml:space="preserve">Allegro</words>
      </direction-type>
      <sound tempo="120"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> `<sound tempo>` = BPM value for playback; the metronome mark is the display.

### 4.2.4 Other `<sound>` Attributes

| attribute | Meaning |
|---------|-------|
| `tempo` | BPM |
| `dynamics` | 0–100 |
| `dacapo` | da capo |
| `segno` | segno marker |
| `coda` | coda marker |
| `fine` | fine |
| `pizzicato` | string pizz |
| `pan` | stereo (0-90) |

## 4.3 `<forward>` & `<backup>` — Playback Position

When multi-voice polyphony has differing durations, `forward`/`backup` move the
playback cursor.

### 4.3.1 `<forward>` (forward)

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
      <duration>1</duration>
      <voice>2</voice>
      <type>eighth</type>
      </note>
      <forward>
      <duration>7</duration>
      </forward>
    </measure>
  </part>
</score-partwise>
```

> Fills a gap mid-voice so the total measure duration stays balanced.

### 4.3.2 `<backup>` (backward)

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
      <backup>
      <duration>4</duration>
      </backup>
    </measure>
  </part>
</score-partwise>
```

> Returns to the start of the measure to write the next voice. Common in
> piano parts (top staff, back up, bottom staff).

## 4.4 Complete Measure Example

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
      <measure number="1">
      <attributes>
      <divisions>2</divisions>
      <key><fifths>-1</fifths></key>
      <time><beats>3</beats><beat-type>4</beat-type></time>
      <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <direction placement="above">
      <direction-type>
      <dynamics><f/></dynamics>
      </direction-type>
      <sound dynamics="80"/>
      </direction>
      <note>
      <pitch><step>F</step><octave>4</octave></pitch>
      <duration>2</duration>
      <type>quarter</type>
      </note>
      </measure>
    </measure>
  </part>
</score-partwise>
```

## 4.5 Direction-Type Quick Reference

| Sub-element | Function |
|------------|--------|
| `<words>` | Free text |
| `<dynamics>` | Dynamic marks |
| `<wedge>` | Hairpin |
| `<metronome>` | Tempo mark |
| `<octave-shift>` | 8va/15ma display |
| `<dashes>` | dashed line |
| `<bracket>` | bracket (measures/technique) |
| `<pedal>` | piano pedal |
| `<sound>` | playback parameter |

## 4.6 Attributes & Directions Checklist

| Check | Yes/No |
|---------|----------|
| `<attributes>` at measure start / at each change? | |
| `divisions`/`key`/`time`/`clef` correct? | |
| Dynamics & tempo via `<direction>`? | |
| `<forward>`/`<backup>` tidy for multi-voice? | |
| `<sound>` set according to the target software? | |

## 4.7 Misconceptions

- **"Key signature may be ignored if there are no accidentals"** — Still
  required for parse & playback; do not remove it.
- **"`<dynamics>` = `<words>pp</words>`"** — Words work visually, but the
  `<dynamics><p/></dynamics>` element provides convention & automatic
  rendering.
- **"A direction is always a single voice"** — One `<direction>` per *span*;
  offset controls the relative position.

## 4.8 References

- W3C MusicXML 4.0: https://www.w3.org/2021/06/musicxml40/
- Gould, *Behind Bars* — dynamics/tempo chapter.
- music21: https://web.mit.edu/music21/doc/

---

**Summary:** `<attributes>` sets divisions/key/time/clef/transpose at the start
(or at a change); `<direction>` encodes dynamics, tempo, wedge, etc.;
`<forward>`/`<backup>` keep the cursor correct during polyphony. Continue to
[Harmony & Chord Symbols (`Ch4-Harmony-Chord-Symbols.md`)].
