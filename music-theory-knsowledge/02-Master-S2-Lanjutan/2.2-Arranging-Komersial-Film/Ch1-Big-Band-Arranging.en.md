---
title: "Big Band Arranging"
tier: "Master S2"
subject: "Commercial & Film Arranging"
xml_tags: ["<part-list>", "<score-part>", "<harmony>", "<transpose>", "<direction>", "<words>", "<articulations>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Big Band Arranging

> **Guidebook for this chapter:** Russell Garcia, *The Professional Arranger
> Composer* (the classic big-band voicing bible); Dave Wolpe, *Instrumental
> Jazz Arranging*; Berklee, *Modern Jazz Voicings*. Focus: organizing
> sax/brass/rhythm sections, cluster voicing, soli, kicks.

## 1.1 Standard Big Band Instrumentation

| Group | Instruments | Common count |
|----------|-----------|-------------|
| Saxophone | Alto 1–2, Tenor 1–2, Baritone | 5 |
| Trumpet | Trumpet 1–3 (+ flugelhorn) | 3–4 |
| Trombone | Trombone 1–3, Bass Trombone | 4 |
| Rhythm | Piano, Bass, Drums (guitar ad lib.) | 3–4 |

> **Notation:** Alto/Baritone sax transpose in E♭; Tenor sax in B♭; Trumpet in B♭;
> Trombone in concert pitch (BC). (See
> `../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`.)

## 1.2 Saxophone Voicing — The 5-Part System

### 1.2.1 Close & Drop 2 Techniques

| Formation | Arrangement |
|---------|---------|
| *Close position* | all chord tones within one octave |
| *Drop 2* | the 2nd voice from the top is dropped an octave |
| *Semi-close* | mixed intervals |
| *Spread / open* | wide range (for register division) |

Example of **Drop 2 on C7**: chord tones C E G Bb → close E G Bb C → lower
**G** (2nd from the top) an octave → **G3, E4, Bb4, C5**.

Choosing each sax according to *tessitura*:

| Sax | Comfortable range |
|-----|---------------|
| Alto | Bb3–F5 |
| Tenor | Ab2–E5 |
| Baritone | C2–F4 |

### 1.2.2 Using "Slots" & Clusters

- **Cluster voicing** (Hughes, NEST): each player takes the nearest
  note — the top merges into one.
- **Internal soli**: 5 saxes + section; give each a small independent
  direction so they don't *skit* an octave.

### 1.2.3 MusicXML: Drop 2 in the Sax Part (concert pitch)

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
    </measure>
    <measure number="2">
      <note><pitch><step>G</step><octave>3</octave></pitch><duration>4</duration><type>whole</type><voice>1</voice></note>
    </measure>
    <measure number="3">
      <note><pitch><step>E</step><octave>4</octave></pitch><duration>4</duration><type>whole</type><voice>2</voice></note>
    </measure>
    <measure number="4">
      <note><pitch><step>B</step><accidental>flat</accidental><octave>4</octave></pitch><duration>4</duration><type>whole</type><voice>3</voice></note>
    </measure>
    <measure number="5">
      <note><pitch><step>C</step><octave>5</octave></pitch><duration>4</duration><type>whole</type><voice>4</voice></note>
    </measure>
  </part>
</score-partwise>
```

> Write in *concert pitch* while drafting voicings, then each sax part is given
> a `<transpose>` (E♭/B♭) automatically in software.

## 1.3 Brass Writing

### 1.3.1 Trumpet Section

- Trumpet 1 (lead): melody, high register.
- Trumpet 2–3: harmonization & fills.
- Range: up to C6 is comfortable; **don't stay long** in the upper register (fatigue).

### 1.3.2 Trombone Section

- Trombone 1–2: harmony.
- Bass Trombone: bass.
- **Shout chorus** — all brass (tpt+tbn) together → peak energy.

### 1.3.3 MusicXML: Shout Chorus Direction

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
          <words xml:space="preserve">Shout Chorus</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Rhythm Section

### 1.4.1 Piano Voicings

- **4-way close** (rootless): 3rd–7th–9th–13th.
- Compact notation: harmony symbol + slash rhythm.

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
        <kind text="m9">minor-ninth</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 1.4.2 Walking Bass

- Movement about 120-ish per beat, *approach tones* (diatonic/chromatic) toward
  the root/target of the next note.
- Written in concert pitch (double bass sounds an octave lower than notation — see
  `../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`).

### 1.4.3 Drums / Kit

- Percussion notation (see
  `../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch4-Notasi-Percussion.md`).
- Style templates (swing, shuffle, latin) on the chart ease the players.

## 1.5 Soli, Fill, Kicks — Hierarchy of Peaks

| Technique | Description | MusicXML |
|--------|-----------|----------|
| *Soli* | whole section in one rhythm | place `<accent/>` |
| *Fill* | fill-in figure | normal notes |
| *Kicks* | unison accents + rhythm | `<articulations><accent/>` |
| *Head arrangement* | opening melody of the improvisation | plain |

### 1.5.1 Kick Accent Notation

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
        <duration>1</duration>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.6 Background vs Foreground

- **Background figures** (tutti strings? No—big band background): sax pads
  beneath the soloist.
- **Foreground** (lead sax / trumpet), `a2` divisi.
- Dynamic balance: background `mf` while the soloist is `ff` — balanced.

## 1.7 Software Templates

1. Kit: 5 sax + 4 tpt + 4 tbn + rhythm = 13+ parts.
2. Set clef & transpose (`transposing instrument` per part).
3. Concert pitch off when printing parts.
4. Layout without unnecessary long rests (`cue`/`cutaway`).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="sx1"><part-abbreviation>S.1</part-abbreviation></score-part>
    <score-part id="sx2"><part-abbreviation>S.2</part-abbreviation></score-part>
    <score-part id="trp1"><part-abbreviation>Tpt.1</part-abbreviation></score-part>
    <score-part id="tbn1"><part-abbreviation>Tbn.1</part-abbreviation></score-part>
    <score-part id="bs"><part-abbreviation>Bass</part-abbreviation></score-part>
    <score-part id="dr"><part-abbreviation>Drs.</part-abbreviation></score-part>
  </part-list>
  <part id="sx1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

## 1.8 Arranging Checklist

| Check | Yes/No |
|---------|----------|
| Sax voicings close, within each sax's range? | |
| Trumpet 1 not fatigued (register)? | |
| Brass not excessively shifting? | |
| Rhythm section clear (symbols + rhythm)? | |
| Feel changes marked in the parts? | |

## 1.9 Common Misconceptions

- **"All saxes in the same register"** — No; baritone on bass, alto on lead.
- **"Soli = everyone plays the same melody"** — Soli is block harmony; only the
  lead follows the melody; the rest are harmonized.
- **"Bass written like guitar written"** — Walking bass = concert notation;
  guitar (on the chart) is written an octave higher.

## 1.10 Exercises

1. Write **Drop 2** for C7 across 4 saxes (alto1, alto2, tenor1, tenor2).
2. Create a 4-bar **shout chorus**: trumpet 1 melody + block harmonization.
3. Arrange an 8-bar **walking bass** for ii–V–I in F.
4. Build a 13-part big band **template** in MusicXML with correct transposition.

## 1.11 Listening Repertoire

- Duke Ellington, *Take the A Train*.
- Count Basie, *April in Paris* (shout chorus).
- Sammy Nestico, big band charts.

## 1.12 References

- Garcia, *The Professional Arranger Composer*.
- Wolpe, *Instrumental Jazz Arranging*.
- DiNovi/Levine sampling: arrangement resources online:
  https://www.arrangerstab.com/

---

**Summary:** Big band = section language: sax clusters, brass lead/punch,
rhythm fills. MusicXML: multiple `<score-part>` with transpose,
`<harmony>` symbols, kick articulations. Continue to [String Section
Techniques (`Ch2-String-Section-Techniques.md`)].
