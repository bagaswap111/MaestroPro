---
title: "Instrument Transposition"
tier: "Bachelor S1"
subject: "Basic Orchestration"
xml_tags: ["<transpose>", "<score-instrument>", "<attributes>", "<midi-instrument>", "<midi-channel>", "<octave-change>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — Instrument Transposition

> **Textbook for this chapter:** Rimsky-Korsakov, *Principles of Orchestration*
> (chapter "Instrumentation Tables"); Adler, *Study of Orchestration* (Chapters 3–4,
> "Transposing Instruments"). Focus: the *written* vs *sounding* relationship, the
> `<transpose>` formula, and common mistakes when templating.

## 4.1 Concept: Concert vs Written

- **Concert (Sounding Pitch):** the sound actually heard — the universal
  language of conductors/analysts.
- **Written (Player's Notation):** the notes as written — adapted for the
  clef/fingering logic of the instrument.

### 4.1.1 Basic Formula

```
Written = Concert + Interval (up)
Sound   = Written − Interval (down)   [for transposing instruments]
```

| Instrument | Written vs concert distance |
|-----------|--------------------------|
| Clarinet/Trumpet in B♭ | written + Major 2nd, sound − Major 2nd |
| Horn in F | written + Perfect 5th, sound − P5 |
| Alto Sax in E♭ | written + Major 6th |
| Tenor Sax in B♭ | written + Major 9th (octave + Major 2nd) |
| Piccolo | sound + 1 octave above written |
| Double Bass | sound − 1 octave from written |

> When importing a score, turn off *concert pitch* for the part player; explain
> the difference when writing a *score*.

## 4.2 Woodwind: Flute, Clarinet Bb, Alto Sax

### 4.2.1 Clarinet in Bb — Practical Thinking

A B♭ clarinet is written **+1 major second**. Concert C4 → written D4, and the
key signature goes up one sharp/flat:

| Concert | Clarinet Bb |
|--------|-------------|
| C major (0) | D major (+2♯) |
| G major (+1♯) | A major (+3♯) |
| F major (−1♭) | G major (+1♯) |

### 4.2.2 MusicXML Structure for a B♭ Clarinet

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P3">
      <part-name>Clarinet in Bb</part-name>
      <part-abbreviation>Cl.</part-abbreviation>
      <score-instrument id="P3-I1">
        <instrument-name>Clarinet</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P3-I1">
        <midi-channel>4</midi-channel>
        <midi-program>71</midi-program>
        <volume>74.8031</volume>
        <pan>0</pan>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P3">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>2</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose>
          <diatonic>-1</diatonic>
          <chromatic>-2</chromatic>
          <octave-change>0</octave-change>
        </transpose>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.2.3 The `<transpose>` Element Inside `<attributes>`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Clarinet in Bb</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>2</divisions>
        <key>
          <fifths>2</fifths>
        </key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose>
          <diatonic>-1</diatonic>
          <chromatic>-2</chromatic>
          <octave-change>0</octave-change>
        </transpose>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>8</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

- `<diatonic>-1</diatonic>` — down 1 scale degree (written→sound).
- `<chromatic>-2</chromatic>` — down 2 semitones total (written D → sound C).
- `<octave-change>` — an additional octave (for octave-transposing instruments).

> **Remember the direction:** a **minus** value = written is higher than sound (sounds
> lower). B♭ Clarinet: written D sounds C → `-2` semitones.

### 4.2.4 Cloning for Clarinet A, E♭, Bass Clarinet

| Instrument | Interval (written → sound) | `<chromatic>` |
|------|----------------------------|---------------|
| Clarinet A | Minor 3rd (down 3 semitones) | -3 |
| Clarinet E♭ | Major 6th (up 9) | +9 (sound is higher) |
| Bass Clarinet B♭ | same as Bb | -2 |

## 4.3 Brass (Horn F, Trumpet Bb)

### 4.3.1 French Horn in F

Written a +Perfect 5th above concert:

- Concert C3 → written G3.
- Concert A4 → written E5.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>French Horn in F</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose>
          <diatonic>4</diatonic>
          <chromatic>7</chromatic>
          <octave-change>0</octave-change>
        </transpose>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `+7` semitones = written is higher than sound; horn in F: written G sounds C.
> In MusicXML a **positive** value indicates that the sound is lower than written
> (the instrument "transposes down"). Verify in your software.

**Excessive ledger lines:** move to a *notatable* register:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Double Bass</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef>
          <sign>G</sign>
          <line>2</line>
          <clef-octave-change>-1</clef-octave-change>
        </clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.3.2 Trumpet in Bb

Same as the B♭ clarinet:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Trumpet in Bb</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose>
          <diatonic>-1</diatonic>
          <chromatic>-2</chromatic>
        </transpose>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

- Sounding range: F#3 – C6; written range: Ab4 – D7.
- Mutes are represented per part with `<direction><words>con sord.</words>`.

## 4.4 Octave-Transposing Instruments

| Instrument | Written vs sounding | Clef |
|-----------|------------------|------|
| Double Bass | +1 octave (written higher) | F |
| Piccolo | −1 octave (sounds higher) | G |
| Guitar | +1 octave | G |
| Celesta | −1 octave | G |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Double Bass</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
        <transpose>
          <diatonic>-7</diatonic>
          <chromatic>-12</chromatic>
          <octave-change>-1</octave-change>
        </transpose>
      </attributes>
      <note>
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Example: bass guitar written C3 → reads middle C one octave lower (C2);
> in MusicXML `-12` semitones.

## 4.5 Transposition in Orchestration Practice (Rimsky)

- B♭ clarinet in ensembles: registerally flexible; transposition is *automatic*
  in software, but the skill of **writing it manually** matters for pencil drafts.
- Horn in F: traditional notation systems may use × (old notation);
  be careful when combining legacy scores.
- Trombone: **BC (bass clef non-transposing)** is standard; TC (treble clef in B♭/cornet
  technique) is used in brass bands — always mark it in the part-name.

## 4.6 Transposition Engraving Checklist

| Step | Details |
|---------|--------|
| 1 | Determine the mode (concert vs written) |
| 2 | Enter the transposition per instrument |
| 3 | Set clef + octave-change |
| 4 | Verify via the Concert Pitch toggle |
| 5 | Check extreme registers & ledger lines |

## 4.7 Misconceptions

- **"`<transpose>` changes the stored notes"** — No; notes are stored *written*;
  `<transpose>` is only consumed at playback/print time.
- **"Horn in F is written lower"** — The written pitch is always *higher* (P5), but
  the low range is hard to notate.
- **"All transposing instruments have `<octave-change>`"** — Only octave
  transpositions (bass, piccolo, guitar) need ±12.

## 4.8 Exercises

1. **Basic:** Convert a 4-bar C major melody to written clarinet (use
   `<transpose>`).
2. **Intermediate:** Create a Horn in F part from a concert melody, paying attention to register.
3. **Advanced:** Add an octave-change for double bass and compare
   *concert* vs *written* in playback.

## 4.9 Book & Web References

**Books:**
- Rimsky-Korsakov, *Principles of Orchestration*.
- Adler, *Study of Orchestration*.

**Web:**
- MusicXML transpose spec:
  https://www.w3.org/2021/06/musicxml40/
- MuseScore handbook (transposition):
  https://musescore.org/en/handbook

---

**Summary:** Transposition = the bridge between written↔sounding. MusicXML stores
the interval in `<transpose>` inside `<attributes>`, supported by
`<score-instrument>`/`<midi-instrument>`. Next: [Texture & Doubling
(`Ch3-Tekstur-Doubling.md`)].
