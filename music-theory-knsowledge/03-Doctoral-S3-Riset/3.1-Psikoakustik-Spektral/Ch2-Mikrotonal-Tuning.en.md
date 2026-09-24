---
title: "Microtonal & Custom Tuning"
tier: "Doctoral S3"
subject: "Psychoacoustics & Spectral"
xml_tags: ["<pitch>", "<alter>", "<accidental>", "<microtone>", "<transpose>", "<sound>", "<tuning>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore", "OpenMusic"]
---

# Chapter 2 — Microtonal & Custom Tuning

> **Guide books for this chapter:** Ivan Wyschnegradsky, *La loi de la pansonorité*;
> Wilson THC; James Tenney, *A History of Consonance and Dissonance*;
> practical applications of OpenMusic & Dorico.
> Focus: intervals < semitone, non-12-TET tuning, and just intonation in
> scores.

## 2.1 Microtonal Foundations

Microtonal = intervals smaller than a semitone: quarter-tone, sixth-tone,
third-tone. Used in electronic, spectral, and non-Western systems
(see `../3.3-Sistem-NonBarat-Etno/`).

| Interval | Size | Example |
|----------|--------|--------|
| Quarter-tone | 50 cents | ¼ sharp/flat |
| Sixth-tone | 33.33 cents | Split accidental |
| Third-tone | 66.67 cents | 3-way |
| Just intonation | ratio | rational ratio |

## 2.2 Quarter-Tones in MusicXML

MusicXML allows non-integer `<alter>`:

- `<alter>0.5</alter>` = quarter sharp (D#¼).
- `<alter>-0.5</alter>` = quarter flat (D♭¼).
- `<alter>1.5</alter>` = sesquisharp (×).

### 2.2.1 Example

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
          <step>D</step>
          <alter>0.5</alter>
          <octave>4</octave>
        </pitch>
        <duration>2</duration>
        <type>quarter</type>
        <accidental>quarter-sharp</accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `accidental` values: `quarter-sharp`, `quarter-flat`,
> `three-quarter-sharp`, `three-quarter-flat`.

## 2.3 Sixth-Tones and Additional Symbols

MusicXML has no standard sixth-tone symbol — use a combination:

1. Extend `accidental-mark` in notation.
2. Text `1/6 tone` in `<direction><words>`.
3. Slash graphic above the note.

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
          <words xml:space="preserve">1/6-tone sharp</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Custom Tuning in Software

- **Dorico:** microtonal accidentals (`MusicXML` round-trip is problematic),
  tuning center pitch.
- **Sibelius:** `MIDI note tuning` (keyswitch / tuning setting).
- **MuseScore:** microtonal plugins.
- **OpenMusic:** `micropitch` port → MusicXML.

> For cents accuracy, push metadata code: `<miscellaneous-field>`.
> Some software compresses semitone mapping — check the map.

## 2.5 Just Intonation (JI)

Pure interval ratios from the harmonic series:

| Interval | Ratio | Cents | vs 12-TET |
|----------|-------|-------|-----------|
| Unison | 1:1 | 0 | 0 |
| Major second | 9:8 | 203.9 | +3.9 |
| Major third | 5:4 | 386.3 | −13.7 |
| Perfect fourth | 4:3 | 498.0 | −2.0 |
| Perfect fifth | 3:2 | 702.0 | +2.0 |
| Major sixth | 5:3 | 884.4 | −15.6 |

> **JI** gives a clear impression on stopped chords, but changes melodic intervals
> vs ET. Use `<alter>` correlated to cents + custom `accidental`,
> metadata in `<miscellaneous>`.

## 2.6 Main Tuning Systems

- **Equal temperament (12-TET):** every semitone 100 cents.
- **Mean-tone:** semitone ~96–100 cents (for pure M3).
- **Pythagorean:** all from the ratio 3:2 (pure perfect fifth).
- **Werckmeister/Kirnberger:** historical well-temperaments.

## 2.7 Micro Glissandi & Textures

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
        <duration>2</duration><type>half</type>
        <notations><glissando type="start"/></notations>
      </note>
      <note>
        <pitch><step>D</step><alter>0.5</alter><octave>4</octave></pitch>
        <duration>2</duration><type>half</type>
        <notations><glissando type="stop"/></notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Spectral texture: continuous pitch columns with gradual quarter-flat/sharp.

## 2.8 Microtonal Checklist

| Check | Yes/No |
|---------|----------|
| Does `alter` have .5/1.5 values on microtonal pitches? | |
| Is `accidental` appropriate (quarter/three-quarter)? | |
| Are sixth-tones marked with text? | |
| Are font/playback capabilities checked? | |
| Is tuning (ET/just) documented? | |

## 2.9 Misconceptions

- **"Microtone = failed tuning"** — Non-Western & spectral music systems are
  indeed non-12-TET.
- **"All software understands `<alter>0.5`"** — No; check font &
  accidental support.
- **"JI is only for history"** — Often used in modern spectral music.

## 2.10 Exercises

1. Write a 4-quarter-tone melody (2 sharp + 2 flat) → render.
2. Create a cents table for each JI interval → validate 1 progression.
3. Experiment with `alter=0.33` sixth-tone → semitone audio.
4. Refer to maqam/raga (3.3) for applications.

## 2.11 References

- Wyschnegradsky, *La loi de la pansonorité*.
- Tenney, *A History of Consonance*.
- Scala (tuning files): https://www.huygens-fokker.org/scala/

---

**Summary:** Microtonal & custom tuning extend 12-TET. MusicXML
supports quarter-tones via non-integer `<alter>` + `<accidental>`;
other intervals via text & extensions. Continue to [Algorithmic Composition
(`../3.2-Komposisi-Algoritmik/`)].
