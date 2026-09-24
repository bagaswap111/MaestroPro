---
title: "Species Counterpoint"
tier: "Bachelor S1"
subject: "Counterpoint & Musical Form"
xml_tags: ["<note>", "<duration>", "<type>", "<rest>", "<voice>", "<notations>", "<tied>", "<pitch>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Species Counterpoint

> **Textbook for this chapter:** Johann Joseph Fux, *Gradus ad Parnassum* (1725;
> trans. Alfred Mann, Norton); Marcus Santa, *Counterpoint: A Species Approach*
> ; Kent Kennan, *Counterpoint*. The *species* method is a disciplined exercise that
> trains independent, point-by-point melodic ability — the foundation of fugue, chorale,
> and part-writing.

## 1.1 Introduction to Counterpoint

*Counterpoint* (Latin *punctus contra punctum* = "note against note") is
the art of combining two or more melodies that are independent yet harmonious.
Created as *exercises* by Fux (in dialogue with Palestrina) in five
levels:

| Species | Rhythmic ratio (against the C.F.) |
|---------|--------------------------|
| **First** | 1:1 — *note-against-note* |
| **Second** | 2:1 — two notes against one |
| **Third** | 4:1 — four notes against one |
| **Fourth** | Syncopation (tie, *suspension*) |
| **Fifth** | *Florid* — a complete mixture |

### 1.1.1 Cantus Firmus (C.F.)

The C.F. is a basic melody (generally 8–16 *whole* notes, diatonic, ending
leading-tone-to-tonic or subtonic-to-tonic). Rules for writing a good C.F.:

1. Every note connected *stepwise* for the most part (small octave leaps).
2. Avoid large upward leaps, especially intervals of 7/9.
3. The melodic climax occurs only once.
4. The cadence ends *2 → 1* (or *7 → 1*).

## 1.2 First Species: Note-Again-Note

### 1.2.1 Rules (Fux, ed. Mann)

1. Begin/end on a *perfect consonance* (P1, P8) — cadences with harmonious notes.
2. Permitted intervals: **P1, m3, M3, P5, m6, M6, P8**.
3. **Forbidden:** ascending P4 (considered *dissonant* in the Baroque), 2nd, 7th, tritone.
4. **Parallel fifths/octaves** are forbidden (in succession).
5. *Contrary motion* is recommended; *similar* motion toward a *perfect* interval is avoided.
6. Both melodies stay within an **octave** range from the start.
7. No ***hidden* (direct) leaps** — the upper voice must not move *similar*
   toward a *perfect* interval in a conspicuous unison.

### 1.2.2 Consonant vs Dissonant Patterns (Intervals)

| Type | Interval |
|-------|----------|
| Perfect | P1, P5, P8 (open) |
| Imperfect | M3, m3, M6, m6 |
| Dissonant | 2nd, 7th, P4 (in context), tritone |

### 1.2.3 MusicXML: Two-Voice First Species

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
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>4</duration>
        <voice>2</voice>
        <type>whole</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>4</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
      <note>
        <pitch><step>A</step><octave>3</octave></pitch>
        <duration>4</duration>
        <voice>2</voice>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> **Quick check:** for every measure, the scale difference between the voices =
> a consonant interval; and there are no two consecutive measures with the same
> P5/P8 interval.

## 1.3 Second Species: Two Notes Against One

### 1.3.1 Rules

- Two *half notes* against one *whole* C.F. → the *unaccented* beat (2nd of the pair)
  may be **dissonant as a *passing tone* (PT)**.
- The first *accented* beat must be consonant.
- A new PT may appear only when it lies between two adjacent harmonies, one step apart.
- Avoid *parallel fifths/octaves* between successive *downbeats*.
- Do not: have both unaccented notes be PTs with no accented consonance between them.

### 1.3.2 MusicXML: Second Species

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
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>half</type>
      </note>
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>half</type>
      </note>
      <note>
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> In the example: the 2nd note (D) is a PT from E→C (consonant→consonant). Make sure
> to use different `<voice>` elements so playback is explicit.

## 1.4 Third Species: Four Notes Against One

### 1.4.1 Rules

- Four *quarter notes* per *whole* C.F.
- *Passing tones* on *unaccented* beats; *neighbor tones* allowed (ascending/descending
  and back).
- Certain *cambiata* leaps are allowed; avoid serial *disjunction*.
- **The requirement that every *quarter* create a strong accent** is binding — the
  first accent of each group must be consonant.
- More than 3 consecutive PTs is risky; leaps must open the contour.

### 1.4.2 Example

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
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>B</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Fourth Species: Syncopation (Ties)

### 1.5.1 Rules — *Suspension*

- A note begins on the *weak* beat, is **extended (tied)** to the next *strong* beat →
  creating a *suspension*.
- The cycle: **consonant (preparation) → dissonant (suspension) → consonant
  (resolution).**
- Note patterns: usually **7–6, 4–3, 9–8** (counting above the C.F.); resolution descends.
- Perfect parallels are forbidden between *suspensions*.

The three phases of a suspension:

| Phase | Beat | Interval to C.F. |
|------|---------|------------------|
| Preparation | weak | consonant |
| Suspension | strong | dissonant |
| Resolution | weak | consonant (descending) |

### 1.5.2 MusicXML: Tie + Tied

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
        <pitch><step>F</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>half</type>
        <tie type="start"/>
        <notations>
          <tied type="start"/>
        </notations>
      </note>
      <note>
        <pitch><step>F</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>half</type>
        <tie type="stop"/>
        <notations>
          <tied type="stop"/>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<tie>` = playback; `<tied>` inside `<notations>` = the displayed curve. Both
> must be synchronized when a passage is tied.

## 1.6 Fifth Species: Florid Counterpoint

### 1.6.1 Rules

- All *species* may be mixed within the same measure — *quarter, half, whole*,
  plus ornaments (PT, NT, suspension, cambiata).
- Main principle: **balance of motion** — direct the climax and cadence.
- When mixing, preserve the root rules (accent, decay, parallels).

### 1.6.2 Mixed Rhythmic Example

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
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>2</duration><type>half</type>
      </note>
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.7 Counterpoint in Modern Contexts & Orchestration

- Two-voice counterpoint appears in: flute+oboe duo, string quartet
  (1st+2nd), wind choir doubling.
- Engraving *software*: give each melody a different `<voice>` so the lines are
  independent; use solo playback to check the contour of each part.
- Music21: the `counterpoint` module (Schubert) offers automatic *species exercises*
  for validation.

## 1.8 Common Misconceptions

- **"Species = only Palestrina exercises"** — Species principles (accent, PT,
  parallels) carry over to all tonal writing & film content.
- **"P4 is always considered dissonant"** — In *vertical* species, P4 against a lower
  C.F. is considered dissonant; against the *bass* the context differs.
- **"Counter-melodies may be entirely rhythmically identical"** — In *first species*, yes; for
  a modern feel use *independent rhythm* (species 4).
- **"A tie doesn't need `<tied>`"** — Wrong; both (playback+visual) are required for
  correct software behavior.

## 1.9 Exercises

1. **Basic:** Write First Species for 2 voices (8-note C.F. + counterpoint).
2. **Intermediate:** Compose a Second Species with one dissonant *passing tone*.
3. **Advanced:** Combine species 2–4 in an 8-bar *florid* passage, achieve a consonant
   cadence; validate via music21.

## 1.10 Listening Repertoire

- Palestrina, *Missa Papae Marcelli* — species in vocal polyphony.
- Bach, Two-Part Inventions BWV 772–786 (counter-melodies).
- Fux selections: *Gradus ad Parnassum* examples.

## 1.11 Book & Web References

**Books:**
- Fux, *Gradus ad Parnassum* (trans. Alfred Mann).
- Santa, *Counterpoint: A Species Approach*.
- Kennan, *Counterpoint* (modern).

**Web:**
- Music21 counterpoint module:
  https://web.mit.edu/music21/doc/
- MuseScore — braces/voices tutorial:
  https://musescore.org/en/handbook/

---

**Summary:** Species 1–5 provide progressive discipline: consonant intervals,
accents, passing tones, suspensions, and florid writing. MusicXML represents
each melody with consistent `<voice>`/`<staff>`; ties use `<tie>` +
`<tied>`. Further material: [Fugue & Contrapuntal Form
(`Ch2-Fugue-Form.md`)].
