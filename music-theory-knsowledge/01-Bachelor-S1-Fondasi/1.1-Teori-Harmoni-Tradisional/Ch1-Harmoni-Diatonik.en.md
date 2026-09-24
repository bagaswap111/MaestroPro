---
title: "Diatonic Harmony"
tier: "Bachelor S1"
subject: "Traditional Harmony Theory"
xml_tags: ["<harmony>", "<root>", "<kind>", "<degree>", "<bass>", "<accidental>", "<note>", "<chord>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Diatonic Harmony

> **Textbook for this chapter:** Kostka & Payne, *Tonal Harmony* (McGraw-Hill);
> Aldwell & Schachter, *Harmony and Voice Leading* (Cengage). Both are
> the foundation of the undergraduate harmony syllabus and should be consulted
> as references when the rules here are disputed.

## 1.1 Triads: The Building Blocks of Tonal Harmony

Diatonic harmony is built on the degrees of the major/minor scale. Each
degree produces a triad with a different quality (Kostka & Payne, Chapter 3):

| Degree | Triad (C major) | Quality | General function |
|---------|------------------|----------|-------------|
| **I**   | C–E–G            | Major    | Tonic |
| **ii**  | D–F–A            | Minor    | Subdominant |
| **iii** | E–G–B            | Minor    | Weak tonic |
| **IV**  | F–A–C            | Major    | Subdominant |
| **V**   | G–B–D            | Major    | Dominant |
| **vi**  | A–C–E            | Minor    | Weak tonic (relative) |
| **vii°**| B–D–F            | Diminished | Dominant (D function) |

### 1.1.1 Intervals Making Up a Triad

| Quality | Arrangement (from root) | Symbol |
|----------|---------------------|--------|
| Major | M3 + m3 | C, Cmaj |
| Minor | m3 + M3 | Cm, Cmin |
| Diminished | m3 + m3 | C°, Cdim |
| Augmented | M3 + M3 | C+, Caug |

### 1.1.2 Major vs Minor vs Modal

- **Natural minor:** degrees i–ii°–III–iv–v–VI–VII (v = minor triad on
  5).
- **Harmonic minor (tonal):** raise degree 7 → creates **major V** and
  **vii°** → enables the dominant function (the raison d'être of tonal minor
  harmony).
- **Melodic minor (ascending):** raise 6 & 7, descend natural — useful for
  melodic lines and chords (i–ii–III... VI–vii°–I).

**Kostka–Payne rule of thumb:** in minor diatonic composition, use the
*harmonic minor* for V/vii°, and the *natural* for VII/III.

### 1.1.3 Inversions & Basso Continuo (Figures)

| Symbol | Chord | Bass | Abbreviation |
|--------|------|------|-----------|
| Root position | C–E–G | C | `5/3` (tbl) |
| First inversion | E–G–C | E | `6` |
| Second inversion | G–C–E | G | `6/4` |

Figures are used in Baroque basso continuo practice. In MusicXML: inversion is
stated via *actual notes* + the chord symbol; there is no "inversion" attribute —
the arranger writes it through the arrangement of notes on the staff.

### 1.1.4 Doubling Triads (Aldwell & Schachter, Chapter 4)

- In root position major/minor: **double the root** (most common), sometimes
  double the 3rd/5th.
- Avoid doubling the **leading tone** (degree 7, e.g. B in G major) — a chromatic
  element that must resolve.
- In diminished chords (vii°), rarely double the 3rd (which is the leading tone).
- "Over-doubling" rules are binding in strict SATB; in orchestration they are
  relaxed (see the Orchestration chapter).

### 1.1.5 MusicXML: Writing a Triad as a Vertical Chord

Write actual notes with the `<chord>` tag on the same staff:

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
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
        <chord/>
      </note>
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
        <chord/>
      </note>
    </measure>
  </part>
</score-partwise>
```

And as a **chord symbol** (lead sheet) on a separate staff:

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
        <root><root-step>C</root-step></root>
        <kind text="maj">major</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>G</root-step></root>
        <kind text="7">dominant</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.2 Seventh Chords

Adding a third interval above a triad produces a four-note chord
(Kostka & Payne, Chapter 14; Levine, Chapter 5 for jazz context):

| Chord | Notes | 7th Quality |
|------|-----|--------------|
| Cmaj7 | C–E–G–B | major 7 |
| Cm7 | C–E♭–G–B♭ | minor 7 |
| C7 | C–E–G–B♭ | dominant 7 (minor 7) |
| Cm7b5 (half-dim) | C–E♭–G♭–B♭ | minor 7 |
| C°7 (diminished) | C–E♭–G♭–B♭♭ | diminished 7 |
| Cmmaj7 | C–E♭–G–B | major 7 (exotic) |

### 1.2.1 Like Chords on Every Degree (C major)

| Degree | 7th Chord | Name |
|---------|--------|---------|
| I | Imaj7 | maj7 (tonic) |
| ii | ii7 | min7 |
| iii | iii7 | min7 |
| IV | IVmaj7 | maj7 |
| V | V7 | *dominant seventh* |
| vi | vi7 | min7 |
| vii° | viiø7 | half-diminished |

V7 is the most important seventh chord: the **tritone** (B–F) inside it is the
resolution engine (B→C, F→E). This is the core concept of Aldwell & Schachter
(Chapter 15) and the basis of tritone substitution in jazz.

### 1.2.2 MusicXML: Quality with `<kind>`

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
        <root><root-step>C</root-step></root>
        <kind text="maj7">major-seventh</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>D</root-step></root>
        <kind text="m7">minor-seventh</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>G</root-step></root>
        <kind text="7">dominant</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>B</root-step></root>
        <kind text="o7">diminished-seventh</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.3 Functional Harmony: T – S – D

Three central functions (Kostka & Payne Chapters 3–4; Riemann's theory):

- **Tonic (T):** I, iii (weak), vi (weak) — center, rest.
- **Subdominant (S):** IV, ii — moving away from the center, *pre-dominant*.
- **Dominant (D):** V, vii° — tension, *leading* back to I.

### 1.3.1 Strong Progression Principles

1. **Descending fifth** (ii→V→I) — the strongest progression, jazz's backbone.
2. **Descending third** (I→vi→IV→ii) — a painting-like progression, common in
   pop/folk.
3. Avoid *retrograde* IV–I motion that creates stasis (the plagal cadence
   is a controlled exception).

| Motion | Strength | Example |
|-------|------|--------|
| up 4 / down 5 | yes | V→I |
| down 3 | medium | I→vi |
| down 2 | medium–gliding | V→IV |
| up 2 | melodically weak | IV→V (dominant cadence) |

### 1.3.2 MusicXML: Complete I–IV–V–I

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
        <root><root-step>C</root-step></root><kind text="maj">major</kind>
      </harmony>
    </measure>
    <measure number="2">
      <harmony print-frame="no">
        <root><root-step>F</root-step></root><kind text="maj">major</kind>
      </harmony>
    </measure>
    <measure number="3">
      <harmony print-frame="no">
        <root><root-step>G</root-step></root><kind text="7">dominant</kind>
      </harmony>
    </measure>
    <measure number="4">
      <harmony print-frame="no">
        <root><root-step>C</root-step></root><kind text="maj">major</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Cadences and Embellishing 6/4

Cadences are the resting points of phrases (Kostka & Payne Chapter 7):

| Cadence | Formula | Character |
|--------|---------|----------|
| **PAC** (Perfect Authentic) | V → I, root position, tonic in the top melodic note | Strong final |
| **IAC** (Imperfect Authentic) | V → I, tonic in middle/top note but not the tonic pitch | Medium final |
| **HC** (Half Cadence) | ... → V | Suspended |
| **Plagal** | IV → I | "Amen" |
| **Deceptive (DC)** | V → vi | Avoids the tonic |

### 1.4.1 IAC in 6/4 → Boundary Case?

The *Cadential 6/4* `I6/4–V–I` (C: G–C–E → V7 → I) is a **delaying**
figure — the 6/4 is not a stable tonic but the dominant with a *pedal*.
Aldwell–Schachter call it *dominant preparation*.

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
    <measure number="10">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="6/4">major</kind>
      </harmony>
    </measure>
    <measure number="11">
      <harmony print-frame="no">
        <root><root-step>G</root-step></root>
        <kind text="7">dominant</kind>
      </harmony>
    </measure>
    <measure number="12">
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="maj">major</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 1.4.2 Authentic Cadence with Figured Bass in MusicXML

`<bass>` tells the *root symbol* there is a different bass (C/E):

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
        <bass>
          <bass-step>E</bass-step>
        </bass>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Early Chromaticism: Secondary Dominants

Enriching diatonic harmony without leaving the center (Kostka Chapter 18;
Aldwell Chapter 26):

```
C:   V7/V   V7    I
     D7  →  G7 →  C
```

**How to build:** *built as the dominant of the target* — the V7 of chord X,
starting from the leading tone of X (C# for D).

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
        <root><root-step>D</root-step></root>
        <kind text="7" use-symbols="yes">dominant</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

Also *secondary leading-tone*: vii°7/V → (D#dim) → V.

## 1.6 Early Modulation & the Concept of Tonal Region

Modulation = a **lasting** change of tonal center, supported by a *pivot chord*
and a new *rhythm* (full details are in `Ch2-Progresi-Akor-Modulasi.md`). Here we
note:

- **Pivot (common chord):** a chord that can be analyzed in two keys.
- **Close relationship:** keys within ±1 accidental of each other (C → G, F, Dm,
  Am, Em).
- **Direct modulation** (without a pivot) is legal at a *section break*.

## 1.7 Core Voice Leading (30 Seconds)

Non-negotiable rules (details: `Ch3-Voice-Leading.md`):

1. Preserve *common tones*.
2. Minimal stepwise motion.
3. The **tritone of V7 (B–F) must resolve:** B→C, F→E.
4. The leading tone rises to the tonic.
5. Avoid *parallel fifths/octaves*.
6. Double the root in root position; never double the leading tone.

## 1.8 Common Misconceptions

- **"vi = full tonic"** — vi is a *root-less* weak tonic; regarding it
  as S in a plagal context is sometimes more accurate.
- **"V7 is always a resolving dominant"** — V7 can be *deceptive* (→vi), or become
  *II7/V* in a modulation area.
- **"Cadences only occur at the end of a song"** — Cadences end *phrases*, including internal
  ones (species: PAC at the end of the 8-bar, etc.).
- **"Half-diminished must resolve to V"** — It can move on to V, vi, or ii;
  it depends on context.
- **"The symbol `<kind>=C7` is the same as the physical notes"** — Not always; a prolonged
  chromatic V7 can be voiced without literal notes (voice leading!).

## 1.9 Exercises

1. **Basic:** Write 3 triads (I, IV, V) in C in three positions.
2. **Intermediate:** Analyze the progression F–G–C–Am (mixed IAC–PAC):
   label the function of each chord, find the pivot to the ii area.
3. **Advanced:** Compose an 8-bar SATB phrase (I–vi–ii–V7–IAC) with doubled
   roots, write the *chord symbols* `<harmony>` + *actual notes* `<chord>` in MusicXML,
   and check in MuseScore.

## 1.10 Listening Repertoire

- Bach Chorales (BWV 294, 302) — perfect diatonic harmony.
- Beethoven, Piano Sonata *Pathétique* I — diminished V7/iv.
- Schubert, *Ständchen* — plagal color.
- Brahms, *Ein deutsches Requiem* — functions & inversions.

## 1.11 Book & Web References

**Books (syllabus):**
- Kostka & Payne, *Tonal Harmony* (Chapters 3–7, 14, 18).
- Aldwell & Schachter, *Harmony and Voice Leading* (Chapters 1–5, 15, 26).
- Walter Piston, *Harmony* (classic).

**Web:**
- MusicXML Tutorial (W3C) — `<harmony>`:
  https://www.w3.org/2021/06/musicxml40/tutorial/
- Hooktheory — pop progressions: https://www.hooktheory.com/
- OpenStax Music (free): https://openstax.org/books/understanding-music/

---

**Summary:** Diatonic harmony = triads + seventh chords + functions
(T–S–D) + cadences + inversions. Core voice-leading rules (tritone, common tone,
doubling) are the heart of Aldwell–Schachter; in MusicXML these concepts are
expressed both via *actual notes* `<chord>` and *symbols* `<harmony>/<root>/<kind>`.
Continue to [Chapter 2 — Chord Progressions & Modulation
(`Ch2-Progresi-Akor-Modulasi.md`)] and study voice leading details in
[`Ch3-Voice-Leading.md`].
