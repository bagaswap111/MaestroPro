---
title: "Sonata, Rondo, Theme & Variation Forms"
tier: "Bachelor S1"
subject: "Counterpoint & Musical Form"
xml_tags: ["<direction>", "<words>", "<repeat>", "<rehearsal>", "<barline>", "<sound>", "<segno>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 3 — Sonata, Rondo, Theme & Variation Forms

> **Textbook for this chapter:** Percy Goetschius, *The Homophonic Forms of Musical
> Composition* (source of classical form theory) and *Lessons in Music Form*;
> Charles Rosen, *Sonata Forms* (modern perspective). Focus: large-scale harmonic
> drama — exposition, development, recapitulation, rondo, variations.

## 3.1 Sonata Form (Sonata-Allegro)

The form that has dominated the first movements of symphonies, sonatas, quartets, and solo
sonatas since Haydn→Beethoven. Its hallmark: **tonal conflict** between theme 1 (tonic) and
theme 2 (the second key), reconciled in the recapitulation.

### 3.1.1 General Structure (Rosen / Goetschius)

| Section | Content | Key |
|--------|--------|-------|
| **Exposition** | Theme 1 → *transition* → Theme 2 → *codetta* | I → V (or the relative major) |
| **Development** | Motivic fragmentation, distant modulation, retransition (dominant pedal) | free |
| **Recapitulation** | Theme 1→2 (now in the tonic) + coda | I |

### 3.1.2 Supporting Terminology

- **Bridge/Transition** — a connector that also modulates from key I to key II.
- **Codetta** — the *small* closing of the exposition before the *repeat*.
- **Retransition** — the bridge back, usually a *dominant pedal* (tremolo).
- **Coda** — an expanded coda (may develop the theme).

### 3.1.3 Key of Theme 2 in Minor Mode

In minor, theme 2 generally lies in the **relative major (III)** or the **minor
dominant (v)** — not the major dominant as in major mode.

### 3.1.4 MusicXML: Marking Structure + Repeat

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
          <words xml:space="preserve">Exposition</words>
        </direction-type>
        <sound tempo="120"/>
      </direction>
      <barline location="right">
        <bar-style>heavy-light</bar-style>
        <repeat direction="forward"/>
      </barline>
    </measure>
  </part>
</score-partwise>
```

> Repeating the exposition is standard (classical). Use `<repeat direction="forward"/>`
> at the start, `direction="backward"` at the end.

### 3.1.5 Classical & Modern Variations

- **Sonata-rondo** (Mozart, Beethoven): A–B–A–C–A–B'–A (rondo + sonata).
- **Slow-movement sonata** (without development, short A–B–A').
- **Ternary-like** recapitulations can tilt the balance; Rosen emphasizes the importance of
  the *arrival* of theme 2 in the tonic as the "resolution of the tonal drama".

## 3.2 Rondo

An A–B–A–C–A–…–A structure with a recurring *refrain* between the couplets.

### 3.2.1 Example Mapping

| Measures | Section | Key |
|--------|--------|-------|
| 1–16 | A (Refrain) | I |
| 17–32 | B (First couplet) | V or the relative major |
| 33–40 | A' | I |
| 41–64 | C (Second couplet) | vi / a distant key |
| 65–80 | A'' | I |
| 81–96 | Coda | I |

### 3.2.2 Principles of Couplet Variation

- *Contrast* in rhythm, register, and orchestration.
- Keep the *transition* to the couplet brief; the *refrain* returns assertively.
- In a *sonata-rondo*, the B/S couplet is usually written in the dominant (it may become
  *theme 2*).

### 3.2.3 MusicXML: Refrain + Coda Navigation

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
      <barline location="left">
        <repeat direction="forward"/>
      </barline>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">Coda</words>
        </direction-type>
      </direction>
      <direction placement="below">
        <direction-type>
          <words xml:space="preserve">Da Capo al Coda</words>
        </direction-type>
      </direction>
      <barline location="right">
        <bar-style>dotted</bar-style>
        <segno/>
      </barline>
    </measure>
  </part>
</score-partwise>
```

## 3.3 Theme & Variations

Preserve the harmonic/melodic framework of the theme while altering other parameters.

### 3.3.1 Genre-Based Approaches (Goetschius, "Variation" chapter)

| Variation type | What changes |
|---------------|--------------|
| **Melodic / ornamentation** | small melodic decoration |
| **Harmonic** | reharmonization (often preserving the *contour*) |
| **Rhythmic** | triplets, diminished values, isorhythm |
| **Textural** | voices swap roles (melody+bass → block chords) |
| **Register & mode** | octaves/mode (major→minor) |
| **Character** | tempo/forces (Bach *Goldberg*) |

### 3.3.2 General Variation Structure (Classical)

- Variations preserve the **total duration** and main **cadences** (directly mappable).
- Beethoven (*Eroica* finale) reduces and becomes contrast; modern practice is freer.

### 3.3.3 MusicXML: Marking Variation Numbers

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
          <words xml:space="preserve">Var. III</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 3.4 Related Forms

| Form | Structure | Example |
|--------|----------|--------|
| **Ternary** | A–B–A | widely known |
| **Binary** | A–B | dance suite |
| **Rounded binary** | A–B: A' | small sonata scale |
| **Minuet & Trio** | A (minuet) B (trio) A (da capo) | Haydn Minuets |
| **Theme & Variations** | A–A1–A2–… | Mozart K.265 "Ah vous dirai-je" |
| **Passepied/Gigue** | Binary with figuration character | Bach suites |

## 3.5 Form Markers & Engraving Workflow

Recommendations from the Dorico era (integrity joints):

1. **Name every section** — `<words>`, `<rehearsal>` at the start.
2. **Set the tempo** literally in `<sound tempo>` (not just a visual tempo mark).
3. **Use repeat/dc/segno** consistently — do not stack manual DCs.
4. **Check the "jump" solver** in the software — make sure `D.S. al Coda` is correct.

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
          <rehearsal letters="A">A</rehearsal>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 3.6 Case Studies

- **Mozart, Piano Sonata K.545 I** — clear exposition; theme 2 in G; short
  development — a teaching model.
- **Mozart, Rondo alla Turca (K.331 III)** — A–B–A–C–…–A with a virtuosic coda.
- **Beethoven, Symph. No.5 II** — *double variation* (two alternating themes,
  one of them lyrical).
- **Bach, Goldberg Variations** — systematic tessitura across variations.

## 3.7 Common Misconceptions

- **"Sonata form = 3 sections with double repeats"** — Repeats are *additional*, not
  mandatory; the core is the key of theme 2 + reconciling recapitulation.
- **"Rondo is always at the end"** — Common as a *finale*, but a sonata-rondo
  can be anywhere.
- **"Variations are only ornamented melodies"** — There are texture/harmony/mode
  variations; in Beethoven it is character/register that are pushed.
- **"MusicXML has a section element"** — There is no `<section>`; use
  `direction`+`words`/`rehearsal` and repeat/segno for navigation.

## 3.8 Exercises

1. **Basic:** Map Mozart's Rondo K.331 (III) with the table in 3.2.
2. **Intermediate:** Write a 16-bar mini sonata exposition: I–transition–V (+ repeat
   in `<barline>`).
3. **Advanced:** Compose 3 variations of an 8-bar theme (melodic, rhythmic, textural); mark
   `Var.` in MusicXML; ensure seamless *playback*.

## 3.9 Listening Repertoire

- Mozart: K.545 I, K.331 III, String Quartet K.387 (sonata).
- Beethoven: *Waldstein*, *Eroica* II (double variation), Op. 111 II.
- Schumann, *Carnaval* — short character pieces.
- Brahms, *Variations on a Theme of Haydn* (Op. 56a) — orchestra.

## 3.10 Book & Web References

**Books:**
- Goetschius, *Lessons in Music Form* & *Homophonic Forms*.
- Charles Rosen, *Sonata Forms*.
- Wallace-Branham? study for general tempo.

**Web:**
- Open Music Theory (form sections):
  https://openmusictheory.github.io/form/
- IMSLP: https://imslp.org/

---

**Summary:** Sonata/rondo/variation are large-scale *tonal drama*.
MusicXML represents structure via `<direction>`+`words`/`rehearsal`,
`<repeat>`/`<segno>` for navigation, and `<sound tempo>` for playback
parameters. Continue to the next Tier 1 module: [Basic Orchestration
(`01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/`)].
