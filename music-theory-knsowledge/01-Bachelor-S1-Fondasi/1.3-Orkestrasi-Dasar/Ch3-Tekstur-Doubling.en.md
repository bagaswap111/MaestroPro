---
title: "Texture & Doubling"
tier: "Bachelor S1"
subject: "Basic Orchestration"
xml_tags: ["<part-list>", "<score-part>", "<part-abbreviation>", "<direction>", "<words>", "<note>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 3 — Texture & Doubling

> **Textbook for this chapter:** Samuel Adler, *The Study of Orchestration*
> (Chapters 10–12 — texture, doubling, balance); Rimsky-Korsakov, *Principles of
> Orchestration* (chapters "Doubling" & "Tutti"). Focus: choosing texture to suit
> the dramaturgy, and the principles of doubling for correct color & strength.

## 3.1 Musical Texture

| Texture | Description | Example |
|---------|-----------|--------|
| *Monophony* | A single melody without accompaniment | Gregorian chant |
| *Homophony* | Main melody + chordal accompaniment | pop, chorale |
| *Polyphony* | Several independent melodies | fugue, canon |
| *Heterophony* | Simultaneous variants of the same melody | gamelan music |

### 3.1.1 MusicXML Application: Homophony (melody + chords)

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
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>2</duration><voice>1</voice><type>half</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>2</duration><voice>2</voice><type>half</type>
      </note>
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>2</duration><voice>2</voice><type>half</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Each texture layer = a `<voice>` (or a separate `<part>`). This is crucial for
> *playback* and *midi analysis*.

## 3.2 The Concept of Doubling

*Doubling* = one musical line played by 2+ instruments (same or
different octave). It is not a SATB voicing error — doubling is an **instrumentation
choice** to add thickness & color.

### 3.2.1 Types of Doubling

| Type | Description | Effect |
|-------|-----------|------|
| Unison doubling | two instruments at the same octave | timbre blend |
| Octave doubling | parallel octaves | register expansion |
| *Structural doubling* | chords doubled layer by layer | mass |
| *Melodic doubling* | melody + color instrument | projection |

### 3.2.2 General Rules (Rimsky & Adler)

- **Oboe + Violin 1** — a *penetrating* melody (strong projection).
- **Flute + Clarinet** (octave/unison) — neutral, soft color.
- **Bassoon + Cello** — solid bass.
- **Horn + Viola/Tenor** — warm color in the middle register.
- **Avoid** woodwind doubling in very high registers without support
  (it raises the register).
- **Equilibrium:** dynamics between layers must be set so the melody is *heard*;
  not all doubling makes things clearer — sometimes it actually *blends* them.

## 3.3 Orchestral Texture in Practice

### 3.3.1 The Orchestral Pyramid

| Register | Role | Typical instruments |
|----------|-------|----------------|
| Soprano | Main melody | Vln I, Ob, Fl, Tpt |
| Alto | Harmony filler | Vla, Hn, Cl |
| Tenor | Harmony filler | Trb ten, Bsn |
| Bass | Foundation | Vc, Cb, Tuba |

> Rimsky said "orchestra is a pyramid of registers" — keep every register *filled*
> for a full texture; for a *thin* texture, empty some registers.

### 3.3.2 Balance Factors

- Number of instruments (2 oboes vs 4 violins).
- Dynamics vs instruments (melody **ff** vs chords **mf**).
- Register (higher is more projecting).
- *Tessitura* (each instrument's comfortable register — do not force dark
  registers upward).

## 3.4 MusicXML: Doubling Layout

### 3.4.1 Multi-Part (unison doubling)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin I</part-name>
      <part-abbreviation>Vln I</part-abbreviation>
    </score-part>
    <score-part id="P4">
      <part-name>Oboe</part-name>
      <part-abbreviation>Ob.</part-abbreviation>
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
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
  <part id="P4">
    <measure number="1">
      <note>
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>16</duration>
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
      <part-name>Violin I</part-name>
    </score-part>
    <score-part id="P4">
      <part-name>Oboe</part-name>
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
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
    </measure>
  </part>
  <part id="P4">
    <measure number="1">
      <note>
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Partwise XML: each `<part>` has its own `<measure number="N">` blocks.
> Doubling does not need to be declared — simply write the same melody.

### 3.4.2 Octave Doubling Within One Part (divisi)

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
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>4</duration><voice>1</voice><type>whole</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>4</duration><voice>2</voice><type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 3.5 Doubling Case Studies

1. **Beethoven, Sym. 5, I** — the "da-da-da-dum" motif doubled across
   *woodwind + tutti* → dramatic mass.
2. **Ravel, *Bolero*** — a sequence of melody doublings at each return; the register
   rises → *layered* texture.
3. **Film scoring** — violin + high woodwind for *heat*; cello + bassoon
   for a warm bass.

## 3.6 Doubling Writing Checklist

| Check | Yes/No |
|-----|----------|
| Can the melody be heard above the harmony? | |
| Is the doubling register within both instruments' ranges? | |
| Are dynamics set in balance? | |
| Are there no engraving collisions between parts? | |

## 3.7 Misconceptions

- **"Doubling always makes it louder"** — No; two *reed* instruments sometimes
  *blend* if their tessituras are similar and the dynamics equal.
- **"Tutti = everyone plays the same"** — Tutti often *doubles* by register;
  not every instrument at the same octave.
- **"MusicXML knows about doubling relationships"** — There is no special element; only
  duplicated content and `<instrument>` attribution.

## 3.8 Exercises

1. **Basic:** Work out 3 different melodic projections for one theme.
2. **Intermediate:** Write 8 bars of tutti with unison doubling across woodwind + string
   (use partwise XML).
3. **Advanced:** Create two texture comparisons from the same theme: homophonic
   (cushion chords) vs polyphonic (imitative), and explain your register choices.

## 3.9 Listening Repertoire

- Beethoven, Sym. 5 I.
- Ravel, *Bolero*.
- Mahler, Sym. 5 IV (Adagietto — divisi strings).
- John Williams, *Jurassic Park* theme.

## 3.10 Book & Web References

**Books:**
- Adler, *The Study of Orchestration*.
- Rimsky-Korsakov, *Principles of Orchestration*.

**Web:**
- Orchestration videos & tables: https://www.orchestrationonline.com/
- VSL instrument pages: https://www.vsl.co.at/en/

---

**Summary:** Texture = a dramaturgical choice; doubling = a tool for color/
strength. MusicXML models this through part & voice structure + `<instrument>`
attribution. Next: [Percussion Notation (`Ch4-Notasi-Percussion.md`)] and
[Genre Foundations (`../1.4-Genre-Fondasi/Ch1-Parameter-Genre.md`)].
