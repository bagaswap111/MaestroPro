---
title: "Post-Tonal Harmony"
tier: "Master S2"
subject: "Jazz & Post-Tonal Harmony"
xml_tags: ["<note>", "<pitch>", "<alter>", "<accidental>", "<rest>", "<direction>", "<words>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 3 — Post-Tonal Harmony

> **Guidebook for this chapter:** Joseph N. Straus, *Introduction to Post-Tonal
> Theory* (set theory, serialism); Miguel A. Roig-Francolí, *Understanding
> Post-Tonal Music*; Grisey/Murail journals (spectral). Focus: impressionism,
> atonality, 12-tone, and spectral — all in MusicXML representation.

## 3.1 From Tonal to Post-Tonal

The 20th century moved beyond tonal function:

| Movement | Representatives | Style |
|-------|-----------|------|
| Impressionism | Debussy, Ravel | whole-tone, parallel |
| Atonality | Schoenberg | freedom of center |
| Serialism/12-tone | Schoenberg, Webern, Berg | tone rows |
| Spectral | Grisey, Murail | overtone & microstructure |
| Neotonal?ality | Copland, Bartók | guided return |

## 3.2 Impressionism & Parallel Harmony

### 3.2.1 Characteristics

- Whole-tone scale, pentatonic, ancient modes.
- Parallel chords (*same voicing* moving).
- No functional cadence; **color > function**.
- Bass often moves tritone? no — small movement & ostinato.

### 3.2.2 MusicXML: Parallel Chords

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
      <note><pitch><step>C</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
      <note><pitch><step>E</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
      <note><pitch><step>G</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
    </measure>
    <measure number="2">
      <note><pitch><step>D</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
      <note><pitch><step>F</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
      <note><pitch><step>A</step><octave>4</octave></pitch><duration>2</duration><type>half</type></note>
    </measure>
  </part>
</score-partwise>
```

## 3.3 Pitch-Class & Set Theory (Straus)

### 3.3.1 Basic Concepts

- **Pitch class (PC):** C=0, C#=1, …, B=11.
- **Interval class (IC):** shortest distance between two PCs (0–6).
- **Pitch-class set:** a collection of PCs; transposition/inversion share structure.
- **Tn / In / TnI:** class transformations.

### 3.3.2 MusicXML: Writing Free Chromaticism

- Key signature may have 0 fifths; each note gets an explicit `<alter>` +
  full `<accidental>` (StudioPraktik set notation).

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
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>2</duration>
        <type>eighth</type>
        <accidental>flat</accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 3.4 Serialism (12-Tone)

### 3.4.1 Principles

- Use **all 12 PCs** before repeating.
- Basic matrix: Prime (P), Retrograde (R), Inversion (I), Retrograde-Inversion
  (RI).

| Transformation | Definition |
|--------------|----------|
| P | original row |
| R | reversed |
| I | intervals flipped in direction |
| RI | I then reversed |

### 3.4.2 MusicXML: Writing a Serial Score

1. Key 0 fifths; all notes with explicit alters.
2. `<midi-instrument>` per *row* if different colors are wanted.
3. `<direction><words>` for P/R/I/RI marks.

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
          <words xml:space="preserve">Row P</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 3.5 Spectral Harmony (Grisey, Murail)

Principle: harmony is drawn from the **overtones** of a single fundamental.

- Chord = overtone-series notation (harmonics 1–n).
- Microtones often appear outside 12-ET.
- Integration with the whole *continuum* (practical engraving limits:
  24-tone microtonal default; see
  `../../03-Doctoral-S3-Riset/3.1-Psikoakustik-Spektral/Ch1-Teori-Spektral.md`).

### 3.5.1 MusicXML: Spectral Harmony (12-ET approximation)

Overtone stack from C2 (16.35 Hz); sequential harmonics ≈ major triad plus 7th/9th:

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
      <note><pitch><step>C</step><octave>2</octave></pitch><duration>4</duration><type>whole</type></note>
      <note><pitch><step>C</step><octave>3</octave></pitch><duration>4</duration><type>whole</type></note>
      <note><pitch><step>G</step><octave>3</octave></pitch><duration>4</duration><type>whole</type></note>
      <note><pitch><step>C</step><octave>4</octave></pitch><duration>4</duration><type>whole</type></note>
      <note><pitch><step>E</step><octave>4</octave></pitch><duration>4</duration><type>whole</type></note>
    </measure>
  </part>
</score-partwise>
```

## 3.6 Advanced Set Theory (Straus)

### 3.6.1 Normal Form & Prime Form

| Set | Normal Form | Prime Form |
|-----|-------------|------------|
| {C,Eb,G} (0,3,7) | [0,3,7] | (037) |
| {C,E,G,Bb} (0,4,7,10) | [0,4,7,10] | (0247) |

- Normal form = most compact permutation (least circular span).
- Prime form = the normal form starting at 0, smaller between T & I.

### 3.6.2 Interval Vector (IV)

For (027): pairs → each IC; count 6 vector slots `[v1..v6]`.

| Set | IV |
|-----|----|
| (012) | [210000] |
| (027) | [011010] |
| (037) | [001110] |

IV helps compare character and *focal* centers.

### 3.6.3 Note on Z-relation

Two different sets can share an IV — e.g. (014) vs (013) etc.; see Straus
for the complete table.

## 3.7 Neotonal & Modal (Bartók, Copland)

- Uses **modal** centers (not chordal function).
- *Mirror-symmetric* chords (axes), folk modes.
- Standard MusicXML representation (key + alter) — only the interpretation changes.

## 3.8 Exercises

1. Create your own 12-tone row; write P, I, R, RI with key 0 fifths.
2. Identify the pitch-class sets of a Debussy motif (*Voiles*).
3. Build a 5-note spectral harmony from C2 + MusicXML spelling.
4. Analyze Webern op.21 — find the row & fragmentation.
5. Calculate the IV of set (0146) and compare with (0137/4).

## 3.9 Post-Tonal Checklist

| Check | Yes/No |
|---------|----------|
| Explicit alter on every note? | |
| Key signature appropriate (0 or neutral)? | |
| Row transformation marked? | |
| Set/prime/IV analyzed? | |
| Spectral calculated via overtones? | |

## 3.10 Listening Repertoire

- Debussy, *Voiles / Pelléas*.
- Schoenberg, *Pierrot Lunaire*, Op. 21 (Webern).
- Grisey, *Partiels / Vortex Temporum*.
- Strauss, examples in *Intro to Post-Tonal Theory*.

## 3.11 References

**Books:**
- Straus, *Introduction to Post-Tonal Theory*.
- Roig-Francolí, *Understanding Post-Tonal Music*.
- Grisey, *Structuration des timbres* (journal).

**Web:**
- emusician set theory tools: https://www.mta.ca/~rrosebrugh/set-theory/
- Laitz, *The Complete Musician* (post-tonal ch).

---

**Summary:** Post-tonal opens impressionist color, atonality (set theory),
serial rows, and spectral overtones. MusicXML writes all of it with
explicit chromaticism (`<alter>`+`<accidental>`), neutral keys, and structural
marks in `<direction>`; analysis remains in human hands.
Continue to [Commercial & Film Arranging (`../2.2-Arranging-Komersial-Film/`)].
