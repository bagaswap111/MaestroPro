---
title: "Funk, Soul & R&B — Characteristics & Notation"
tier: "Master S2"
subject: "Funk Soul R&B Genre"
xml_tags: ["<harmony>", "<kind>", "<degree>", "<notehead>", "<stem>", "<ghost>", "<direction>", "<slur>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Funk, Soul & R&B: Characteristics & Notation

## 1.1 Funk/Soul DNA: One-Chord Groove and Syncopation

Funk/Soul/R&B are kings of **groove** and *harmonic stasis*:

- **Single-chord harmony** (vamp) or compact ii–V — blocks of 8/16 bars.
- **Groove is everything** — 16th grid, syncopation on the *"&a"* of the beat.
- **Backbeat** on 2&4 of the snare, *kick* placed in the empty pocket.
- **Timbral:** clavinet ("clav"), wah-guitar, slap/pop bass, horn stabs,
  lush string pads, vocal hooks.

### 1.1.1 Subgenre Matrix

| Subgenre | Tempo | Vibe |
|----------|-------|---------|
| **Funk** (60s–70s) | 90–115 | Clav + 16th bass lines, drum *power pocket* (Sly Stone, James Brown) |
| **Soul** (60s) | 110–130 | Deepest backbeat, *string pads*, gospel feel |
| **R&B / Contemporary** | 60–100 | *trap-hihat 16ths*, sub-bass, vocoder/auto-tune, *swingy 16ths* |
| **Disco** (70s) | 116–128 | 4-on-floor kick, *strings*, horns, female vocal |
| **Boogie / early R&B** | 100 | Clavinet, octave bass |

## 1.2 Groove Notation: 16th Grid + Ghost Notes

Write funk on a *grid* of 16ths — *ghost notes* (sounded very softly)
use `notehead` `ghost` in MusicXML (percussion) or `<ghost>` text in bass.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Bass</part-name>
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
        <pitch><step>G</step><octave>2</octave></pitch>
        <duration>2</duration>
        <voice>2</voice>
        <type>16th</type>
      </note>
      <note>
        <pitch><step>G</step><octave>2</octave></pitch>
        <duration>2</duration>
        <voice>2</voice>
        <type>16th</type>
        <notehead>ghost</notehead>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 1.2.1 Classic 16th Bass Patterns

Funk bass: rhythmic weight at once — built from *octaves + fifths*, with a
*pickup into* the **key phrase**. Example (G, in 16ths):

```
Beat:  1  &  2  &  3  &  4  &
Pitch:  G  G  D  G  G  Bb G  G
```

You can use `<articulations><staccato/></articulations>` on
*syncopated* targets.

## 1.3 Harmony: Light, Sticky Chords

Funk rarely changes chords; **stabs** provide *color change*:

| Function | Type | Example |
|--------|-------|--------|
| Base vamp | One-chord | E9 (E7 + 9) |
| Stab | Quick ii7–V7 | C#m7–F#7 on bar 3 |
| *Slash* | 3rd in bass | D/F# |
| Dependent | *Dominant + 9* + *♭7* | A7#9 (Jimi) |

### 1.3.1 Writing Chord Stabs in the Rhythm Section

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
        <root><root-step>E</root-step></root>
        <kind text="9">dominant</kind>
        <degree>
          <degree-value>9</degree-value><degree-alter>0</degree-alter>
          <degree-type>add</degree-type>
        </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Horns & String Pads (R&B Arranging)

**Horn stabs** — layered into the groove:

- Write all parts together (unison rhythm), `staccatissimo`+accent.
- Example 2 bars for trombone (lead), peaking in the middle register.

**String pads** — R&B uses *string arrangements* with 4th/6th spreads,
*tremolo marcato*:
- Too thick → mount 3-note (root 5th 7th 9th), divisi.
- Hold in the chorus (*staccato notes* without thickness inside the chorus).

### 1.4.1 Example Horn Stab Bar

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Trumpet</part-name>
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
        <duration>2</duration>
        <voice>1</voice>
        <type>16th</type>
        <notations><articulations><accent/><staccatissimo/></articulations></notations>
      </note>
      <note>
        <rest/>
        <duration>2</duration>
        <voice>1</voice>
        <type>16th</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.5 R&B Vocals: Runs, Melisma, Ad-libs

- **Runs/melisma:** 16th lines — write every note (or `<extend/>` on one
  slur). Typical R&B: the phrase "You" → 8 notes.
- **Ad-lib tails:** at the end of chorus lines — written small (`8va`),
  *improvised ornament*, `[ad lib.]`.
- **Harmony stack:** 3rd/5th; the higher harmony follows the same lyrics.

## 1.6 Common Misconceptions

- **"Funk is always fast"** — Many funk standards sit at 90–110 (Sly); slow-jam
  can be at 60.
- **"R&B = chord-heavy"** — Harmonic elements are minor; *groove+timbre* are more
  crucial.
- **"Ghost notes don't need writing"** — For *notation playback* and
  *section unity*, they're important.
- **"Horns are only staccato"** — There are *swells*, *falls*, *fills*; color variety.

## 1.7 Exercises

1. **Basic:** Write an 8-bar funk vamp (E9): 16th bass + snare backbeat on 2&4.
2. **Intermediate:** Add a 2-bar horn stab run and a 3-note string pad.
3. **Advanced:** Double the chorus vocal hook with *ad-lib* & harmony stack;
   write melisma with `<extend/>`.

## 1.8 Listening Repertoire

- James Brown, *Sex Machine* / *Cold Sweat* (bass, vamp).
- Sly & Family Stone, *Thank You (Falettinme Be Mice Elf Agin)*.
- Stevie Wonder, *Superstition* (clav riff).
- Chic, *Le Freak* (muted funk guitar).
- Drake/Orange, *Hotline Bling* (trap R&B 16th hi-hat).

## 1.9 Book References & Web Sources

**Books:**
- David Garibaldi, *Future Sounds* (funk drum chops).
- Stu Hunt, *Funk Bass Bible*.
- Jerry Coker, *Elements of the Jazz Language* (R&B).

**Web:**
- Funk bass transcriptions: https://www.oktav.com/
- DRUMMER funk notation: https://webdrummer.com/
- Hooktheory (R&B progressions): https://www.hooktheory.com/

---

**Summary:** Funk/Soul/R&B = 16th groove + ghost notes + horn stabs + light
pads. MusicXML: `<notehead>ghost`, `articulations`, `<harmony>` key classes,
vocal melisma `<extend/>`. Continue to [Funk/Soul/R&B Adaptation
(`Ch2-Adaptasi-Instrumentasi.md`)].
