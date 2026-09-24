---
title: "Root Structure and Score-Partwise"
tier: "MusicXML Masterclass"
subject: "Anatomy of MusicXML"
xml_tags: ["score-partwise", "work", "identification", "part-list", "credit", "measure", "score-instrument"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Root Structure & Score-Partwise

> **Chapter reference books:** Michael Good, "MusicXML: An Internet-Friendly
> Format for Sheet Music" (foundational paper); *MusicXML W3C spec* 4.0
> (chapter *Quick Start*). Gould, *Behind Bars* (Chapter 6 — score layout) for
> the engraver's perspective. Focus: the `score-partwise` document hierarchy and
> metadata for cross-software exchange.

## 4.1 Score-Partwise vs Score-Timewise

| Format | Structure | Usage |
|--------|----------|------------|
| `score-partwise` | `<part>` → all `<measure>` per part | Dominant (all exporter apps) |
| `score-timewise` | `<measure>` → all `<part>` | Time flow / layout transformation |

> Partwise documents are more natural for engraving; most parser libraries
> (music21) support *partwise* first.

## 4.2 Root Elements and Header

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <work>
  <work-title>Simfoni No. 1</work-title>
  <work-number>Op. 1</work-number>
  </work>
  <identification>
  <creator type="composer">J. S. Bach</creator>
  <creator type="poet">—</creator>
  <rights>Public Domain</rights>
  <encoding>
  <software>Dorico 5.0</software>
  <encoding-date>2026-01-15</encoding-date>
  <supports element="accidental" type="yes"/>
  </encoding>
  </identification>
  <defaults>
  <scaling>...</scaling>
  <page-layout>...</page-layout>
  </defaults>
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
      <duration>4</duration>
      <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.2.1 The `<work>` & `<identification>` Routine

- `<work-title>` — major title.
- `<work-number>` / `<opus>` — opus number (optional).
- `<creator type="...">` — composer/arranger/lyricist, if applicable.
- `<rights>` — copyright/license (e.g., CC0/Public Domain).
- `<encoding>` — producing software + date + `<supports>` (features
  supported by the export).

> Best practice: always fill in `<encoding>` with the software version & date so
> *round-trips* can be debugged across applications.

## 4.3 `<part-list>` and `<score-part>`

Instrument list — order = order of score staves. Groups are called
`<part-group>`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<part-list>
  <part-group number="1" type="start">
    <group-name>Woodwinds</group-name>
    <group-symbol>bracket</group-symbol>
  </part-group>
  <score-part id="P1">
    <part-name>Flute</part-name>
    <part-abbreviation>Fl.</part-abbreviation>
    <score-instrument id="P1-I1">
      <instrument-name>Flute</instrument-name>
      <instrument-sound>pitched</instrument-sound>
      <virtual-instrument>
        <virtual-library>EastWest</virtual-library>
        <virtual-name>EW Flute</virtual-name>
      </virtual-instrument>
    </score-instrument>
    <midi-instrument id="P1-I1">
      <midi-channel>1</midi-channel>
      <midi-program>73</midi-program>
    </midi-instrument>
  </score-part>
  <score-part id="P2">
    <part-name>Oboe</part-name>
    <part-abbreviation>Ob.</part-abbreviation>
  </score-part>
  <part-group number="1" type="stop"/>
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
      <duration>4</duration>
      <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> The part `id` (P1, P2, ...) is the **reference key** to `<part id="P1">`.
> `score-instrument` may appear more than once for divisions/multi-sound
> percussion.

## 4.4 `<part>` and `<measure>` Structure

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
<measure number="1" implicit="no" non-controlling="no">
<attributes>
<divisions>2</divisions>
<key><fifths>0</fifths></key>
<time><beats>4</beats><beat-type>4</beat-type></time>
<clef><sign>G</sign><line>2</line></clef>
</attributes>
<note>
<pitch><step>C</step><octave>4</octave></pitch>
<duration>2</duration>
<type>quarter</type>
</note>
</measure>
<measure number="2">
...
</measure>
</part>
</score-partwise>
```

- `implicit="yes"` → an unnumbered measure (initial pickup bar).
- `non-controlling="yes"` → a measure that does not advance progress (for
  highlighting / rehearsal numbering).
- `<attributes>` at the start of each change: divisions, key/time, clef.

## 4.5 `<credit>` and Additional Metadata

Measured in *tenths of staff space* relative to the page. Format:

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
      <credit page="1">
      <credit-type>title</credit-type>
      <credit-words default-x="300" default-y="600" font-size="24" font-style="bold">Judul Karya</credit-words>
      </credit>
      <credit page="1">
      <credit-type>composer</credit-type>
      <credit-words default-x="70" default-y="120">Diteliti & diarans.</credit-words>
      </credit>
    </measure>
  </part>
</score-partwise>
```

- `<credit-type>`: `title`, `subtitle`, `composer`, `arranger`, `lyricist`,
  `rights`, `part-name`.
- Multiple `<credit-words>` can appear within one `<credit>`.

## 4.6 Element Order in the Root (Schema-valid)

1. `<?xml ... ?>` (optional prolog)
2. `<work>` (optional)
3. `<movement-number>` / `<movement-title>` (optional)
4. `<identification>` (optional)
5. `<defaults>` (optional)
6. `<music>` → `part-group`, `credit`, `part-list` ... (version 4.0)
7. `<part>`* 
8. `</score-partwise>`

> **Version 4.0 note:** layout/credit may now appear inside the `<music>`
> element; the schema order is still maintained. Practice: always
> `version="4.0"` so there is no ambiguity.

## 4.7 Mini Validation (Round-Trip)

1. `version="4.0"` on the root.
2. part-list `id` consistent with `<part id>`.
3. Number of `<part>` = number of `<score-part>`.
4. `measure number` unique per part, ascending in order.
5. `divisions` consistent per part.

### 4.7.1 Verification with music21

```python
import music21
s = music21.converter.parse("file.mxl")
for p in s.parts:
    print(p.id, p.measureNumber)
```

## 4.8 Root Structure Checklist

| Check | Yes/No |
|---------|----------|
| Root `<score-partwise version="4.0">`? | |
| `<work>`/`<identification>`/`<credit>`? | |
| `<part-list>` covers all parts + instruments? | |
| `id` consistent? | |
| Every `<part>` has a `<measure>` block? | |
| `divisions` consistent + durations valid? | |

## 4.9 Misconceptions

- **"Partwise & timewise can be mixed in one file"** — No; choose one of them
  for the root.
- **"`<credit>` is required for parsing"** — Optional; only `part-list`
  & parts are required.
- **"MIDI instrument is enough without score-instrument"** — For playback, yes;
  for engraving/part IDs you need `score-instrument`.

## 4.10 Book & Source References

- Good, *Majors in the Mix* / W3C MusicXML 4.0 spec:
  https://www.w3.org/2021/06/musicxml40/
- music21 docs: https://web.mit.edu/music21/doc/
- MuseScore export internals (MXML writer): https://musescore.org/

---

**Summary:** A `score-partwise` document = header (work, identification,
defaults, credit) → `part-list` → one `<part>` per instrument, each part contains
`<measure>`; `divisions`/`key`/`time`/`clef` go in `<attributes>`. Continue to
[The Note Element (`Ch2-The-Note-Element.md`)].
