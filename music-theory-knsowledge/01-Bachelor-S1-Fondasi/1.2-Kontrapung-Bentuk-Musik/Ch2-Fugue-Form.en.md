---
title: "Fugue & Contrapuntal Form"
tier: "Bachelor S1"
subject: "Counterpoint & Musical Form"
xml_tags: ["<score-part>", "<part-list>", "<measure>", "<direction>", "<words>", "<repeat>", "<rest>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — Fugue & Contrapuntal Form

> **Textbook for this chapter:** Alfred Mann, *The Study of Fugue* (trans./anthology,
> W.W. Norton — primary sources from Marpurg, Albrechtsberger, Fux, Cherubini in
> translation); Kent Kennan, *Counterpoint*. Focus: the structure of subject–answer–
> countersubject, episode, stretto, and pedal point.

## 2.1 Fugue Concepts

A *fugue* = a polyphonic composition with a single subject stated alternately by
several voices, with its counterpoint maintained, ending on the tonic. The peak of
the Baroque: J.S. Bach, *Art of Fugue* (BWV 1080) and *Well-Tempered Clavier*
(BWV 846–869, 870–893).

## 2.2 Anatomy of a Fugue

### 2.2.1 Core Terminology

| Term | Definition |
|---------|----------|
| *Subject* | The main theme, in the tonic |
| *Answer* | The subject on the dominant — *real* (exact) or *tonal* (adjusted) |
| *Countersubject* | The counter-melody accompanying the subject/answer, usually consistent |
| *Exposition* | All voices entering in turn T→D→T→D |
| *Episode* | Sequential passage without a full subject statement |
| *Stretto* | The subject enters before the previous one finishes → canon |
| *Pedal point* | A long dominant/tonic note in the bass |
| *Codetta* | A short phrase between exposition entries |
| *Augmentation/Diminution* | Alteration of the subject's note values |

### 2.2.2 The Three Large Sections

1. **Exposition** — T, D, T, D (each) + countersubject.
2. **Middle section** — entries in the relative/dominant keys, separated by episodes.
3. **Final section** — stretto + pedal point + tonic cadence.

## 2.3 Exposition — Rule Setup

- **S0 (T)** starts in the tonic; **S1 (D)** gives the *answer* on the dominant.
- **S2 (T)** returns to the tonic with a countersubject.
- **S3 (D)** and so on — strictly following the entry order.

### 2.3.1 MusicXML: Part Layout per Voice

A fugue in MusicXML is best represented with one `<score-part>` per voice (vocal/instrument),
not per physical instrument:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Soprano</part-name>
    </score-part>
    <score-part id="P2">
      <part-name>Alto</part-name>
    </score-part>
    <score-part id="P3">
      <part-name>Tenor</part-name>
    </score-part>
    <score-part id="P4">
      <part-name>Bass</part-name>
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
    </measure>
  </part>
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
    </measure>
  </part>
  <part id="P3">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
    </measure>
  </part>
  <part id="P4">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

### 2.3.2 Tonal vs Real Answer

- **Real answer:** the subject's intervals are preserved exactly (some mid-level
  fugues).
- **Tonal answer:** an adjustment to avoid a drastic *dominant key jump*; common
  when the subject leaps from tonic to dominant (V) or to
  subdominant (IV).

| Subject begins | Common answer |
|-----------------|------------------|
| Tonic→Tonic | Real on the dominant |
| Tonic→Dominan | Tonal (push to the subdominant) |
| Tonic→Subdom. | Tonal (return to the tonic) |

## 2.4 Episodes and Treatment of the Subject

- **Episode:** uses an *sequence* (ascending/descending) that *modulates* toward the next
  key. An episode should be **separated** from the subject entries by a
  light *cadence*.
- **Treatment of the subject:**
  - *Inversion* — the direction of the intervals is reversed.
  - *Retrograde* — the subject is played backwards.
  - *Augmentation/Diminution* — note values doubled / halved.
  - *Stretto* — overlapping entries.
- A *pedal point* on the dominant creates an *expectation* of returning to the tonic.

### 2.4.1 MusicXML: Marking Subject Entries

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
          <words xml:space="preserve">Subject</words>
        </direction-type>
        <offset>0</offset>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> Place this mark at the start of every entry; for the *answer* write "Answer".

## 2.5 Stretto and the Climax

In *stretto*, the next subject entry begins *before* the previous one has finished —
a distance of 1–2 measures; the tighter the spacing, the stronger the tension. In Bach's
fugues, the final stretto is usually accompanied by a pedal-point cadence on the
dominant; the voices are compressed into a perfect *canon* (e.g. *Art of Fugue*,
Contrapunctus).

### 2.5.1 Checking via MusicXML/Writing

To plan a stretto, create a timeline table:

| Measure | S1 (subject) | S2 (answer) | S3 (countersubject) |
|--------|--------------|--------------|---------------------|
| 1    | tonic entry | – | – |
| 3    | continuation (real) | dominant entry | – |
| ... | – | – | entry |

## 2.6 Rests Between Entries

Voices that have not yet entered are given a consistent `<rest/>` until their entry:

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
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
      <note>
        <rest measure="yes"/>
        <duration>4</duration>
        <voice>4</voice>
        <type>whole</type>
        <staff>4</staff>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.6a Episode Repetition (repeat)

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
      <barline location="right">
        <bar-style>light-heavy</bar-style>
        <repeat direction="backward"/>
      </barline>
      <barline location="left">
        <repeat direction="forward"/>
      </barline>
    </measure>
  </part>
</score-partwise>
```

## 2.7 Analysis of a Bach Fugue (WTC I, BWV 846)

An analytic procedure (Mann) applicable to any score:

1. Write out the complete *subject* (first notes).
2. Identify the *answer* and its type (real/tonal).
3. Find the *countersubject* that accompanies the entries.
4. Map every subject entry + key (create a path diagram).
5. Mark the *episodes*, *sequences*, and *strettos*.
6. Note the *pedal* and the climactic cadence.

## 2.8 Advanced Counterpoint: Inversion, Canon, Triple Fugue

- **Inversion** — intervals mirrored about an axis (example from *Art of Fugue*).
- **Canon** — identical imitative entries chasing each other (can be without modulation).
- **Double/triple fugue** — two or more subjects treated as equals; conflicts
  are integrated using their respective *countersubjects*.

## 2.9 Misconceptions

- **"A fugue must be complex"** — A basic fugue is just one subject with strict
  exposition rules; complexity comes from economical counterpoint.
- **"The answer is always tonal"** — Many fugues use a *real answer*; a tonal
  answer is used when the subject emphasizes important dominant notes.
- **"Episodes can be anything = filler"** — The episode is the modulation *engine*;
  its plot is a sequence monitored by cadences.
- **"MusicXML marks fugues automatically"** — No; only parts/voices/repeats/
  directions. Manual analysis remains a core component.

## 2.10 Exercises

1. **Basic:** Write an 8-note subject in C major; create a *real answer* in G.
2. **Intermediate:** Build a 3-voice exposition (T–D–T) with a consistent
   countersubject; arrange the MusicXML part-list.
3. **Advanced:** Compose a stretto at a 1-measure distance; mark it in the score as
   `<direction>`; compare its cohesive effect with a non-stretto version.

## 2.11 Listening Repertoire

- Bach, *WTC I/II* — BWV 846, 847, 869.
- Bach, *Art of Fugue* BWV 1080 (Contrapunctus 1, 4, 9).
- Handel, *Fugues* from keyboard *Suites* (HWV 426–433).
- Shostakovich, *24 Preludes & Fugues*, Op. 87 — modern fugues.

## 2.12 Book & Web References

**Books:**
- Alfred Mann, *The Study of Fugue*.
- Kent Kennan, *Counterpoint*.

**Web:**
- IMSLP (source scores): https://imslp.org/
- Music21 counterpoint: https://web.mit.edu/music21/doc/

---

**Summary:** A fugue = one subject (answer/real-tonal) + countersubject and
the structure Exposition→Episode→Stretto→Pedal→Cadence. In MusicXML the layout is
several `<score-part>`s + `<direction><words>` for entries + `<rest>` for
empty voices + `<repeat>` for episodes. Next: [Sonata & Rondo Form
(`Ch3-Bentuk-Sonata-Rondo.md`)].
