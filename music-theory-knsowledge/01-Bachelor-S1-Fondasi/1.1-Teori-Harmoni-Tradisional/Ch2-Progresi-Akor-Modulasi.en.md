---
title: "Chord Progressions & Modulation"
tier: "Bachelor S1"
subject: "Traditional Harmony Theory"
xml_tags: ["<attributes>", "<key>", "<fifths>", "<mode>", "<transpose>", "<harmony>", "<root>", "<kind>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — Chord Progressions & Modulation

> **Textbook for this chapter:** Kostka & Payne, *Tonal Harmony* (Chapters 3–5, 18–21);
> Aldwell & Schachter, *Harmony and Voice Leading* (Chapters 2–3, 26–30); Schachter,
> "Modulation" in *The Music Forum*. Focus: how progressions drive
> phrases, and how modulation moves the tonal center.

## 2.1 Standard Chord Progressions

A progression is a cyclical sequence of functions that binds a phrase. Its strength is measured
by **root distance** and **direction**:

### 2.1.1 Circle of Fifths (Descending Fifth)

A **descending-fifth root** sequence is the strongest and most
binding harmonic motion:

```
C → F → B° → Em → Am → Dm → G → C
I → IV → vii° → iii → vi → ii → V → I
```

Reversed, **I→IV** (ascending fifth) creates stasis — used in
plagal cadences and pop choruses.

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
      <harmony print-frame="no"><root><root-step>C</root-step></root><kind text="maj">major</kind></harmony>
      <harmony print-frame="no"><root><root-step>F</root-step></root><kind text="maj">major</kind></harmony>
      <harmony print-frame="no"><root><root-step>G</root-step></root><kind text="7">dominant</kind></harmony>
      <harmony print-frame="no"><root><root-step>C</root-step></root><kind text="maj">major</kind></harmony>
    </measure>
  </part>
</score-partwise>
```

### 2.1.2 Progressions to Watch Closely

| Progression | Character | Notes |
|----------|----------|---------|
| I → IV | Plagal/sim | Ascending fifth; stasis if overused |
| V → IV | *Backwards* | Sometimes effective (blues), not standard |
| V → VI/iii → … | Bifurcating motion | A "retrograde" chain |
| ii → V | Prepared dominant | Most common approach to a cadence |
| I → vi → IV → V | Doo-wop | Pop's foundation (see genre tier) |
| vi → IV → I → V | Pop canon | Triangle (modern) |

**Kostka–Payne principle:** the best progressions run in a "circle" — approaching
V through ii/IV, then returning to I. Avoid *descending fifth*
chains longer than 3–4 steps without direction.

## 2.2 Progression Patterns Across Genres

| Style | Typical pattern | Nature |
|------|-----------|-------|
| Classical | I–IV–V–I; I–vi–ii–V | clear functions |
| Pop/ballad | I–V–vi–IV | melancholic loop |
| Doo-wop | I–vi–IV–V | 50s nostalgia |
| Jazz turnaround | I–vi–ii–V | cycle toward V |
| Blues | I7–IV7–I7–V7 | dominant pile-up |
| Modal | I–IV (diatonic) vamp | static, color |

### 2.2.1 MusicXML: 8-Bar Pop Progression (I–V–vi–IV)

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
  </part>
</score-partwise>
```

## 2.3 Modulation: Moving the Tonal Center

Modulation is not merely "changing the key"; it is a **process** that must
be logically supported. Three main types (Kostka Chapter 21; Aldwell Chapter 26):

### 2.3.1 Pivot-Chord Modulation (Common-Chord / Diatonic)

Take a chord that can be analyzed **in two keys** at once:

- C major → G major: pivot **Dm** (ii in C, vi in G).
- C major → A minor: pivot **Am** (vi in C, i in Am) or **F** (IV in C,
  VI in Am).

```
Writing: [C] → Dm → [G] → C ... → G7 → C  (pivot Dm)
Analysis:  I    ii      V    I      V7   I
         (     vi in G      )
```

### 2.3.2 Phrase Modulation (Phrase / Direct)

Move the center **without a pivot** — usual at the start of a *new section*
(Classical era, pop bridges). In MusicXML: simply update `<key>` at the start of a measure.

### 2.3.3 Chromatic & Enharmonic Modulation (Common-Tone / Chromatic)

- **Common-tone:** one note is held as a bridge to the new key
  (bass C → C#7? → F#m? depending on context).
- **Chromatic:** use a secondary V7 (modulation to V: **D7** → G; to IV:
  **C7** → F). Details: Aldwell–Schachter on "altered chords" and their eligibility.

### 2.3.4 MusicXML: `<key>` in `<attributes>` on a New Measure

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
        <key>
          <fifths>1</fifths>
          <mode>major</mode>
        </key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

> `<fifths>` = number of sharps/flats. G major = +1; F major = −1; A minor = 0
> (relative to C); E minor = +1 (relative to G). `cancel` is useful if there is a
> transitional measure.

**Example with `<cancel>` (changing the signature toward neutral):**

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
        <key>
          <cancel>2</cancel>
          <fifths>0</fifths>
        </key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Modulation vs Transposition — A Crucial Difference

| | Modulation | Transposition |
|--|----------|-------------|
| Definition | Move the *center* within a work | Copy the *entire* work to another key |
| Score | The key signature changes mid-score | The initial key signature changes entirely |
| MusicXML | `<key>` appears at the new measure | `<transpose>` per part (transposing instruments) |
| Purpose | Expressive | Register/instrument needs |

### 2.4.1 MusicXML `<transpose>` for Transposing Instruments

B♭ Clarinet: concert sound = **1 whole step lower** than written. Hence:

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
        <transpose>
          <diatonic>-1</diatonic>
          <chromatic>-2</chromatic>
          <octave-change>0</octave-change>
        </transpose>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

- `<diatonic>` — shift of the scale degree name (B♭ clarinet: -1).
- `<chromatic>` — total semitone shift (clarinet: -2).
- `<octave-change>` — when there is an octave shift (piccolo, contrabass).

When importing into Dorico/MuseScore, transposition is applied per part; the *display*
stays *written* for the player. (Details: `Ch2-Transposisi-Instrumen.md`.)

## 2.5 Gradual Modulation & Sequences

- **Sequence (diatonic base):** an ascending/descending series on the scale — one
  of the engines of modulation through 3–4 keys in succession.
- **Rosalia:** an ascending chromatic sequence (lavish Baroque era) — reach a distant
  tonic with *tendency tones*.

```
C:  I    V6/vi   ...   F#m ... → (strong modulation)
```

## 2.6 Exercises

1. **Basic:** Label the functions (T/S/D) on the progression C–Am–F–G–C.
2. **Intermediate:** Write a pivot modulation C→G (4 bars) in MusicXML: `<harmony>` +
   `<key>` in measure 4.
3. **Advanced:** Create a 6-chord ascending sequence (C–Am–Dm–G–C–F#°7/V?) and test
   which one is the pivot to the new tonic; write the analysis in a `<direction>` comment.

## 2.7 Listening Repertoire

- Mozart, Piano Sonata K.283 I — modulation to V in the exposition.
- Schubert, *Impromptu* D.935/2 — enharmonic modulation (G#→♭).
- Chopin, Prelude Op.28 No.4 — chromatic/blues-ish harmonization.
- John Williams, *Imperial March* — progressive (modal–modulating).

## 2.8 Book & Web References

**Books:**
- Kostka & Payne, *Tonal Harmony* (Chapters 18–21).
- Aldwell & Schachter, *Harmony and Voice Leading* (Chapters 26–30).
- Edward Aldwell, *The Music of ...* — essays on modulation.

**Web:**
- MusicXML `<key>` spec: https://www.w3.org/2021/06/musicxml40/
- Hooktheory: https://www.hooktheory.com/
- Open Notation (visual modulation): https://www.musictheory.net/

---

**Summary:** Progressions are cyclical functions that determine direction; modulation
is a journey of the tonal center that requires pivot/chromatic/direct means.
MusicXML represents this through `<harmony>` for symbols, `<key>` (+`cancel`) for
signature changes, and `<transpose>` per part for instrumentation. Continue to
[Chapter 3 — Voice Leading (`Ch3-Voice-Leading.md`)].
