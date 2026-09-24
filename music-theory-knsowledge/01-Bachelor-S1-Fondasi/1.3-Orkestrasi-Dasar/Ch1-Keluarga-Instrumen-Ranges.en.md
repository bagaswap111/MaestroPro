---
title: "Instrument Families & Ranges"
tier: "Bachelor S1"
subject: "Basic Orchestration"
xml_tags: ["<score-instrument>", "<midi-instrument>", "<part-name>", "<part-abbreviation>", "<instrument-sound>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Instrument Families & Ranges

> **Textbook for this chapter:** Nikolai Rimsky-Korsakov, *Principles of
> Orchestration* (Chapters I–VI — families, range, register, tessitura); Samuel
> Adler, *The Study of Orchestration* (Chapters 1–4, *Range* Appendix). Focus:
> getting to know the four families, their actual ranges, and defining them correctly
> in MusicXML so that *midi* & *playback* are accurate.

## 1.1 The String Family

Sound source: strings vibrating, set in motion by the bow. Strengths: wide register, unlimited
*sustain*, *col legno*/*pizzicato*/*tremolo* offering extreme colors.
All are written at **sounding pitch** — no transposition (except the Double
Bass, which sounds one octave lower than written).

| Instrument | Written range (sounding) | Safe register | Core timbre |
|-----------|--------------------------|----------------|-------------|
| Violin | G3 – C7 | G3–E6 | Bright, flexible, soloistic |
| Viola | C3 – E6 | C3–A5 | Dark, warm, mid-range |
| Cello | C2 – A5 | C2–G4 | Deep, grand *tenor* |
| Double Bass | E1 – G4 | E1–D4 | Sub-bass, foundation |

### 1.1.1 Registers in Practical Use (Adler)

- **Violin:** G string = rich; E string = *piercing*.
- **Viola:** G string = soulful color; avoid long melodies on the C string
  (thick & *guttural*).
- **Cello:** A string = lyrical; D/G = texturally useful.
- **Double Bass:** open D/G — limited sustain in the upper register.

### 1.1.2 Technique Overview

| Technique | MusicXML artifact |
|--------|-------------------|
| Pizzicato | `<notations><technical><pluck/></technical></notations>` |
| Arco (return) | `<text>arco</text>` in `<direction>` |
| Tremolo | `<ornaments><tremolo type="start">2</tremolo></ornaments>` |
| Harmonics | `<technical><harmonic><natural/></harmonic></technical>` |
| Col legno | `<words>col legno</words>` |

### 1.1.3 MusicXML Application: Defining a Violin Part with Standard Techniques

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
      <part-abbreviation>Vln.</part-abbreviation>
      <score-instrument id="P1-I1">
        <instrument-name>Orchestral Violin</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>40</midi-program>
        <volume>78.7937</volume>
        <pan>0</pan>
      </midi-instrument>
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
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.2 The Woodwind Family

Comprising: Flute, Oboe, Clarinet, Bassoon + variants (Piccolo, Alto Flute, E♭
Clarinet, Contrabassoon). Each has its own **transposition** & **register**
(details in `Ch2-Transposisi-Instrumen.md`).

| Instrument | Range (sounding) | Character |
|-----------|--------------------|------|
| Flute | C4 – D7 | *pale* below, *silvery* above |
| Oboe | Bb3 – A6 | *piercing*, distinctive oboe melody |
| Clarinet in B♭ | D3 – A7 (low sounding) | *dark chalumeau* → *bright clarion* |
| Bassoon | Bb1 – Eb5 | *gruff* bass, cantando *tenor* |

### 1.2.1 Clarinet Register Divisions (Adler/Rimsky)

| Register | Character |
|----------|----------|
| Chalumeau (D3–G4) | dark, soft |
| Throat (G4–C5) | *pinched*, proceed with care |
| Clarion (C5–G5) | bright, soloistic |
| Altissimo (G5–C7) | sharp, virtuosic |

### 1.2.2 MusicXML: B♭ Clarinet with Correct `instrument-sound`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P4">
      <part-name>Clarinet in Bb</part-name>
      <part-abbreviation>Cl.</part-abbreviation>
      <score-instrument id="P4-I1">
        <instrument-name>B-flat Clarinet</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P4-I1">
        <midi-channel>5</midi-channel>
        <midi-program>71</midi-program>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P4">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
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

## 1.3 The Brass Family

Trumpet, Horn, Trombone, Tuba, Euphonium, Flugelhorn. Mostly transposing;
very wide *dynamic range*; solid *sustain* & *articulation*.

| Instrument | Range (sounding) | Notation |
|-----------|--------------------|--------|
| Trumpet in B♭ | F#3 – C6 | Transposing (Bb) |
| French Horn in F | Bb1 – F5 | Transposing (F); melodic register E4–Bb4 |
| Trombone (Tenor) | E2 – Bb4 | Concert (BC) |
| Bass Tuba | D1 – F4 | Concert (BC) |

### 1.3.1 MIDI Programs (General MIDI canonical)

| Instrument | GM program |
|------------|------------|
| Trumpet | 56 |
| French Horn | 60 |
| Trombone | 57 |
| Tuba | 58 |
| Violin | 40 |
| Cello | 42 |
| Flute | 73 |
| Oboe | 68 |
| Clarinet | 71 |
| Bassoon | 70 |

> General MIDI is only an *approximation* — for true orchestral accuracy
> use sampling libraries (VST); MIDI programs are enough for drafts.

## 1.4 The Percussion Family

| Instrument | Type | Range / notes |
|-----------|-------|-------------------|
| Timpani | Pitched (4 drums) | D2 – F♯3 (tuning varies) |
| Marimba | Pitched | A2 – C7 (concert C4→written note) |
| Xylophone | Pitched | F4 – C8 (written 1 octave below sound) |
| Vibraphone | Pitched | F3 – F6 |
| Glockenspiel | Pitched | G5 – C8 (written 2 octaves below) |
| Snare Drum | Unpitched | no pitch — `<unpitched>` |
| Bass Drum, Cymbal, Triangle | Unpitched | GM mapping |

### 1.4.1 MusicXML Application: Snare (Unpitched)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P20">
      <part-name>Snare Drum</part-name>
      <part-abbreviation>S.D.</part-abbreviation>
      <score-instrument id="P20-I1">
        <instrument-name>Snare Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P20-I1">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>38</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P20">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>2</duration>
        <instrument id="P20-I1"/>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
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
    <score-part id="P20">
      <part-name>Snare Drum</part-name>
      <part-abbreviation>S.D.</part-abbreviation>
    </score-part>
  </part-list>
  <part id="P20">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>2</duration>
        <instrument id="P20-I1"/>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<midi-unpitched>` assigns a drum/key to a specific GM degree. Snare=38,
> Kick=36, Hi-hat=42, Crash=49 (table details in `Ch4-Notasi-Percussion.md`).

## 1.5 Complete Comparative Range Table

| Instrument | Sounding | Clef | Transposition |
|-----------|----------|------|---------|
| Piccolo | D5 – C8 | G (read 8va) | Transposes 8 |
| Flute | C4 – D7 | G | – |
| Oboe | Bb3 – A6 | G | – |
| English Horn | E3 – A5 | G | F transposing |
| Clarinet B♭ | D3 – A6 | G | Bb |
| Bass Clarinet | D2 – B4 | G | Bb |
| Bassoon | Bb1 – Eb5 | F | – |
| Trumpet B♭ | F#3 – C6 | G | Bb |
| Horn in F | B1 – F5 | G | F |
| Trombone | E2 – Bb4 | F/BC | – |
| Tuba | D1 – F4 | F/BC | – |
| Harp | Cb1 – G#7 | brace (G4+F4) | – |

> Useful API (automatic range): Dorico/MuseScore *Note per instrument*
> for part-by-part validation when writing.

## 1.6 Engraving Considerations

1. **Clef management**: bass/strings/bassoon in F-clef; woodwind in G;
   *octave-clef* (`<clef-octave-change>`) for low registers.
2. **Percussion**: use `<sign>percussion</sign>` for unpitched —
   do not misattribute pitch.
3. **Range check**: the *instrument range* feature in Dorico/MuseScore validates
   notes outside the register.
4. **Transpose display**: turn on *concert pitch* to check the ensemble; turn it
   off for player parts.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Percussion</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef>
          <sign>percussion</sign>
        </clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
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

## 1.7 Common Misconceptions

- **"Alto Sax = a transposing clarinet"** — Playing an alto sax (E♭) melody always
  sounds a major 6th above concert; not B♭.
- **"Defining a part with just a name is enough"** — For correct playback you need
  `score-instrument` + `midi-instrument` (correct program).
- **"Actual range = whatever's on the internet"** — Written ranges differ from
  *practical* & *comfortable* registers; use the Adler/Rimsky tables.

## 1.8 Exercises

1. **Basic:** Write the actual ranges of Violin, Oboe, Horn in F (within 5 ledger lines).
2. **Intermediate:** Define 4 parts (Flute, Clarinet Bb, Trombone, Snare) in
   MusicXML with correct `midi-program`.
3. **Advanced:** Arrange register plans: 3 ways to double a melody (oboe+vln,
   clar+alto sax, horn 1+2) and compare them.

## 1.9 Listening Repertoire

- Ravel, *Daphnis et Chloé* — *divisi* violins + highly colorful woodwind.
- *The Rite of Spring* (Stravinsky) — high woodwind / low brass extremes.
- John Williams *Jurassic Park theme* — strong horn section.

## 1.10 Book & Web References

**Books:**
- Rimsky-Korsakov, *Principles of Orchestration* (Norton edition).
- Samuel Adler, *The Study of Orchestration*.

**Web:**
- Philip Saylor orchestration charts: https://philharmonia.co.uk/
- Vienna Symphonic Library *instrument guide*: https://www.vsl.co.at/en/

---

**Summary:** The four families — strings, woodwind, brass, percussion — each have
distinct ranges, transpositions, and registers. In MusicXML each instrument is defined
via `<score-instrument>` + `<midi-instrument>` (program). Further material:
[Instrument Transposition (`Ch2-Transposisi-Instrumen.md`)] and [Texture
(`Ch3-Tekstur-Doubling.md`)].
