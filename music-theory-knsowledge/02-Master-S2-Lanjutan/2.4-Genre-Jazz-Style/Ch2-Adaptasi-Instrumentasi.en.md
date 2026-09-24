---
title: "Jazz Style — Cross-Instrumentation Adaptation"
tier: "Master S2"
subject: "Jazz Style Genre"
xml_tags: ["<score-part>", "<midi-instrument>", "<transpose>", "<swing>", "<glissando>", "<harmony>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — Jazz Style: Cross-Instrumentation Adaptation

## 2.1 Method: Jazz Idiom to Non-Jazz Ensembles

Changing *idiom* doesn't mean *identity* is lost — it's lost when
*swing/feel/harmony* are dropped. Mapping the functions:

| Jazz function | Original instruments | Non-jazz targets |
|-------------|----------------|-----------------|
| *Head* melody (swing) | Trumpet/Alto | Violin (fiddle-jazz), flute, oboe |
| Comp (voicing) | Piano/guitar | Harp, horn pad, divisi strings |
| *Walking bass* | Acoustic bass | Cello pizz., bassoon (low register) |
| Drums (ride/swing) | Kit | Light cajón, brushes kit |
| Horn section stabs | Sax/Brass | Classical trumpet, woodwind choir |

## 2.2 Adaptation 1: Jazz Lead Sheet → String Quartet "Jazz Quartet"

*"String jazz"* style (e.g. Turtle Island String Quartet, Kronos (jazz
program)).

- **Violin 1:** *head* melody — use *glissando* (bend string), *grace
  note approach*, *vibrato*.
- **Violin 2:** pad/driving 8ths (swing) with *pizz* accents.
- **Viola:** rootless comp — pluck the chord (muted), 3rd+7th.
- **Cello:** walking bass — pizzicato groove, chromatic approach.

### 2.2.1 Example Rootless Comp in Strings (mm 1, ii–V–I)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>String Quartet</part-name>
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
      <!-- Vln1: pickup downbeat D played as swing eighth -->
      <note>
        <pitch><step>D</step><octave>6</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>8th</type>
        <notations><glissando type="start"/></notations>
      </note>
      <!-- Cello: walking D -->
      <note>
        <pitch><step>D</step><octave>3</octave></pitch>
        <duration>2</duration>
        <voice>4</voice>
        <type>8th</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.3 Adaptation 2: Big Band → Symphonic Wind Band

Ellington/Basie transcriptions for wind band (a common competitive format):

- **Sax section** → clarinet choir/portable baritone sax.
- **Trumpet section** → cornet section + flugelhorn (soft melody).
- **Trombones** → keep 3–4, substitute euphonium on the melody.
- **Rhythm** → piano/harp replaced by piano alone; drum kit to percussion kit.

Rule: swing tunes → **stay swing** (don't go *straight*), because *feel* is
identity.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Piano</part-name>
    </score-part>
    <score-part id="P2">
      <part-name>Flugelhorn</part-name>
    </score-part>
  </part-list>
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose><diatonic>-1</diatonic><chromatic>-2</chromatic></transpose>
      </attributes>
      <score-instrument id="P2-I1">
        <instrument-name>Flugelhorn</instrument-name>
      </score-instrument>
      <midi-instrument id="P2-I1">
        <midi-channel>2</midi-channel>
        <midi-program>57</midi-program>
      </midi-instrument>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Adaptation 3: Jazz-Funk → Brass Band / Percussion Ensemble

- Synth/fretless bass → **tuba slap-tongue** or staccato bassoon.
- E-piano comp → **horn section** (rootless voicing, divisi).
- *Ride cymbal* words → **tambourine/cowbell** on the swing beats.
- Wah guitar → **trumpet wah-wa mute** (`Harmon`).

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
      <direction placement="below">
        <direction-type>
          <words>with Harmon mute — wah</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 2.5 Jazz Vocal → Solo Sax (Instrumental Lead)

*Vocal scat → sax* techniques:
- Write the melodic contour, not the lyrics.
- *Bends* → lip glissandi; *fall* → falloff.
- Scat 8ths → swing feel.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Saxophone</part-name>
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
        <duration>2</duration>
        <type>8th</type>
        <notations>
          <articulations><falloff/></articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.6 Jazz Adaptation Checklist

| Check | Result |
|-----|-------|
| Swing <sound> retained (not straightened)? | |
| ii–V–I & substitutions retained (identity)? | |
| Voicing moved — rootless/tight? | |
| Walking bass connected (approach)? | |
| Head/melody in jazz articulation phrases (tongue/slur)? | |
| Horn section stabs consistent | |
| `score-part`+`transpose` correct for target ensemble | |

## 2.7 Exercises

1. **Basic:** Write an 8-bar ii–V–I *lead* for flute + string quartet.
2. **Intermediate:** Convert rootless piano comp → horn section (3 horns) for 4 bars.
3. **Advanced:** Arrange *So What* (modal) for string quartet: modal vamps,
   vln1 head; cello bass = dorian line.

## 2.8 Adaptation Repertoire

- **Turtle Island String Quartet** — standard jazz for strings.
- **Gordon Goodwin / Big Phat Band** — popular big band.
- **Brass Brazil** — bossa/funk for brass.

## 2.9 Book References & Web Sources

**Books:**
- Mark Levine (theory + piano book).
- Jerry Bergonzi, *Inside Improvisation* series.
- Ted Pease, *Jazz Composition: Theory and Practice*.

**Web:**
- Jazzadvice — approach/enclosure: https://www.jazzadvice.com/
- Learnjazzstandards: https://www.learnjazzstandards.com/
- Universal Edition — string jazz repertoire.

---

**Summary:** Jazz adaptation = keep swing & ii–V harmony (identity) while
transferring functions (lead/head, comp, walking bass, rhythm) to target
instruments with equivalent idiomatic techniques (gliss/wah/mute). Return to [Jazz
Characteristics (`Ch1-Karakteristik-Notasi.md`)] or continue to [Funk/Soul/R&B
(`../2.5-Genre-Funk-Soul-RnB/`)].
