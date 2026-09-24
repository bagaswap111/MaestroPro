---
title: "Film Scoring Notation"
tier: "Master S2"
subject: "Commercial & Film Arranging"
xml_tags: ["<direction>", "<words>", "<sound>", "<offset>", "<metronome>", "<bracket>", "<barline>", "<miscellaneous>"]
software: ["Dorico", "Sibelius", "Finale"]
---

# Chapter 3 — Film Scoring Notation

> **Guidebook for this chapter:** Derrick Bang, *The Score* (journal); Mark Snow &
> Richard Davis, *On the Track: A Guide to Contemporary Film Scoring*
> (revised edition); Berklee film scoring material. Focus: video synchronization,
> tempo maps, hit points, cue notes, and conductor-score practice.

## 3.1 Marking Video Time in the Score

| Element | Role |
|--------|-------|
| Bar numbers & frame marks | part margins |
| Click track | boxed metronome BPM |
| Streamers / pops | visual signals |
| Hit points (stings) | action → harmony |

## 3.2 Click Track & Tempo Mapping

### 3.2.1 Tempo Freeze

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
          <metronome parentheses="no">
            <beat-unit>quarter</beat-unit>
            <per-minute>120</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="120"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### 3.2.2 Tempo Map Deployment (Snow)

- Place expression hits on *beat 0* of each cue.
- Tempo changes before the next bar — `<offset>` divisions.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
          <words xml:space="preserve">accel. to 168</words>
        </direction-type>
        <offset>2</offset>
        <sound tempo="168"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 3.3 Conductor Score Format

| Element | Details |
|--------|--------|
| Header | title, film, cue number/length |
| BPM | initial value + changes |
| Bar numbers | every 4 bars (system) |
| Cue name | "M21 — Jungle Chase" |
| Navigation | D.S. al Coda, segno, da capo |

### 3.3.1 MusicXML: Cue Name

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
          <words xml:space="preserve">M21 — Jungle Chase</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### 3.3.2 Bar numbering

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
      <print>
        <measure-numbering>system</measure-numbering>
      </print>
    </measure>
  </part>
</score-partwise>
```

## 3.4 Hit Points & Streamers

- **Hit point** — `H` above the bar (text), like a "sting" on the downbeat.
- **Streamer** — a vertical line; text representation.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
          <words xml:space="preserve">H! (hit on downbeat)</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

Practice: create a mapping table like this:

| SMPTE | Bar | Beat | Action |
|-------|-----|------|------|
| 01:00:12:00 | 34 | 1 | Explosion |
| 01:01:04:12 | 56 | 3 | Lockdown cue |

## 3.5 Orchestral Template for Film

1. Part-list: perc + (piano/celesta) + WW + Brass + Strings.
2. Concert pitch off for transposing parts (B♭/F/E♭).
3. Harp on its own part (bracket for pedal).

## 3.6 Cues in the Score

`<cue/>` marks a note as a cue (displayed small, not sounded).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
        <duration>1</duration>
        <type>eighth</type>
        <cue/>
        <stem>up</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Some software displays a ghost notehead behind; cue names fail in
> MusicXML — using a semi-transparent (ghost) approach is common.

## 3.7 Synchronization with DAW/Video

| Parameter | MusicXML | Video ref |
|-----------|----------|-----------|
| Tempo | `<sound tempo>` | timebase |
| Bar | `number="N"` | frame |
| Offset | `<offset>` | frame grid |
| Hit | `<words>H</words>` | frame mark |

### 3.7.1 Frame Rate (SMPTE) — extension

MusicXML has no SMPTE element; software puts extensions in
`<miscellaneous>`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
      <miscellaneous>
        <miscellaneous-field name="frame-rate">24</miscellaneous-field>
      </miscellaneous>
    </measure>
  </part>
</score-partwise>
```

### 3.7.2 Frame→Beat Conversion

```
smpte_beat = (video_seconds * frame_rate - bar_start_frame) * tempo / 60
```

Store the *tempo map* of all BPM changes — important for DAW import.

## 3.8 Film Scoring Checklist

| Check | Yes/No |
|---------|----------|
| Complete tempo map (BPM + changes)? | |
| Hit points on the right bars? | |
| Cue notes used for entries? | |
| Frame rate/format noted? | |
| Bar numbers visible (system)? | |

## 3.9 Common Misconceptions

- **"Film scores are always rubato"** — Often click-track + straight; rubato
  is for individual moments.
- **"`<offset>` is in seconds"** — `offset` = divisions (notes), not time;
  convert via tempo.
- **"Crucial hits must be notes"** — H as in "sting"; visual text is enough.

## 3.10 Exercises

1. **Tempo map**: write cue M21 going 100→140→150 in MusicXML.
2. **Hit point**: place `H!` on the downbeat of bar 34 + `chord symbol`.
3. **Cue notes**: give 2 bars of flute cue for a woodwind entry.
4. **Round-trip**: export → DAW, check synchronization.

## 3.11 References

- Snow & Davis, *On the Track*.
- Bang, *The Score*.
- Berklee film scoring class material;
  https://online.berklee.edu/

---

**Summary:** Film notation = tempo map, hit points, cue notes, navigation;
represented via `<direction>`, `<offset>`, `<sound>`, `<cue/>`, and
`<miscellaneous-field>` frame rate. Continue to [Extended Techniques
(`../2.3-Extended-Techniques/`)].
