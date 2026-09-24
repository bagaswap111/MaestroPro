---
title: "Extended Techniques — Woodwind & Brass"
tier: "Master S2"
subject: "Extended Techniques"
xml_tags: ["<note>", "<notations>", "<articulations>", "<technical>", "<words>", "<direction>", "<ornaments>", "<notehead>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Extended Techniques: Woodwind & Brass

> **Guidebook for this chapter:** Gardner Read, *Contemporary Instrumental
> Techniques*; contemporary libretti (Berio, Sequenza); practices adopted from
> IRCAM. Focus: multiphonics, flutter, key clicks, mutes, microtones —
> their representation in MusicXML.

## 1.1 The Concept of Extended Technique

*Extended technique* = playing methods outside the norm to produce new timbres;
a pillar of contemporary music & film design. Notation principle: **clear for the
player**, because many techniques have no standard symbols — text instructions
are required.

## 1.2 Woodwind

### 1.2.1 Multiphonics

Two or more pitches sounding simultaneously via special fingerings.

- Write both pitches (or a diagonal rhythm slash) + `<words>multiph.</words>`.
- Fingerings optional below the staff (numbers/table).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
          <words xml:space="preserve">multiph.</words>
        </direction-type>
      </direction>
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
      <part-name>Woodwind</part-name>
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
        <pitch><step>D</step><octave>5</octave></pitch>
        <duration>2</duration><type>half</type>
      </note>
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>2</duration><type>half</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Make sure two notes on one staff use different `<voice>` elements; if a
> shorter duration is needed for one of them, use chord semantics.

### 1.2.2 Flutter Tongue

Instruction `flutter` / `frullato`; some software recognize
`<technical><tonguing>`; words as fallback.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
      <notations>
        <articulations>
          <ornamental/>
        </articulations>
      </notations>
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
      <part-name>Woodwind</part-name>
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
      <notations>
        <technical>
          <tonguing>flutter-tongue</tonguing>
        </technical>
      </notations>
    </measure>
  </part>
</score-partwise>
```

### 1.2.3 Key Clicks

- Mechanical sound; `×` notehead at the pitch of the key.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>1</duration>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
    </measure>
  </part>
</score-partwise>
```

> If the sound is unpitched, should you add `<technical><mute on="yes"/>`? No —
> use the `keyclick` keyword and appropriate display position.

### 1.2.4 Overblown & Singing While Playing

- **Overblown:** high pitch + high dynamic (`ff`), false harmonic.
- **Sing while playing:** two lines — one for the whistle, one for the humming.

## 1.3 Brass

### 1.3.1 Half-Valve / False Tones

Half valve = *false tones* (low nonharmonic pitches). Write the sounding pitch
+ the `half-valve` instruction.

### 1.3.2 Mutes (Sordino)

| Mute | Effect | Instruction |
|------|------|-----------|
| Straight | bright, sharp | `con sord.` |
| Cup | mellow | `cup` |
| Harmon (wah) | nasal | `harmon` / `+ pedal` |
| Plunger | wah-wah | `plunger` |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
          <words xml:space="preserve">con sord.</words>
        </direction-type>
      </direction>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">senza sord.</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### 1.3.3 Lip/Valve Trill

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>2</duration>
        <type>half</type>
        <notations>
          <ornaments>
            <trill/>
          </ornaments>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 1.3.4 Trombone Glissandi (Slide)

Trombone glissando = chromatic slide-position change:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
        <pitch><step>F</step><octave>3</octave></pitch>
        <duration>2</duration><type>half</type>
        <notations><glissando type="start"/></notations>
      </note>
      <note>
        <pitch><step>B</step><octave>3</octave></pitch>
        <duration>2</duration><type>half</type>
        <notations><glissando type="stop"/></notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Microtonal

- `<alter>0.5</alter>` → quarter-tone.
- Custom accidentals `quarter-flat`/`quarter-sharp` when font support exists.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
          <step>E</step>
          <alter>0.5</alter>
          <octave>4</octave>
        </pitch>
        <duration>2</duration>
        <type>quarter</type>
        <accidental>quarter-flat</accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

> In MusicXML as `<accidental>`; rule: alter 0.5 = quarter sharp,
> -0.5 = quarter flat. Some fonts (SMuFL) support microtonal symbols.

## 1.5 Handling in Software

| Software | Ext. Features |
|----------|------------|
| Dorico | symbol browser; playback skips |
| Sibelius | ExtraTechniques plugin |
| MuseScore | × notehead, ornament symbols |

**Tip:** if a symbol doesn't exist, use `<words>` + a footnote for the technique;
consistency matters more than a unique symbol.

## 1.6 Repertoire

- **Berio — Sequenza I** (flute): multiphonics, flutter, gliss.
- **Ligeti — Horn Trio**: harmonics & mutes.
- **Penderecki — Threnody**: brass cluster techniques.
- **Hindemith / Takemitsu** — wind colors.

## 1.7 Checklist

| Check | Yes/No |
|---------|----------|
| Technique instructions clear (text)? | |
| × notehead key clicks correct? | |
| Multiphonics have pitch + `multiph.`? | |
| Mute/unmute indicated? | |
| Microtone alter & accidental consistent? | |

## 1.8 Common Misconceptions

- **"Mutes are supported in playback"** — NO; only notated; sound via a custom
  mapping.
- **"Key clicks must use the correct pitch"** — better to show the intended
  display pitch, not necessarily the sounding one.
- **"Flutter = ornament symbol is enough"** — players need the word `flutter` —
  a symbol without the word is ambiguous.

## 1.9 Exercises

1. Write a flute multiphonic (2 pitches) + `flutter` in one bar.
2. Create a mute-switching sequence on trumpet (straight→cup→open).
3. Write a microtonal E♭ quarter-flat in the clarinet part; verify.

## 1.10 References

- Read, *Contemporary Instrumental Techniques*.
- Berio, *Sequenzas* (scores).
- SMuFL details: https://www.smufl.org/

---

**Summary:** Ext. woodwind/brass = multiphonics, flutter, key clicks, mutes,
microtones. MusicXML via `<direction><words>`, `<notehead>`, `<technical>`,
`<ornaments>`, and microtonal accidentals (`alter=.5`). Continue to [Extended
Strings (`Ch2-Extended-Strings.md`)].
