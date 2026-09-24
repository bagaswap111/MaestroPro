---
title: "Percussion Notation"
tier: "Bachelor S1"
subject: "Basic Orchestration"
xml_tags: ["<unpitched>", "<percussion>", "<score-instrument>", "<instrument-sound>", "<clef>", "<midi-unpitched>", "<midi-instrument>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 4 — Percussion Notation

> **Textbook for this chapter:** Adler, *The Study of Orchestration* (Chapters 8–9 —
> percussion & battery, "Reading" mape); Rimsky-Korsakov (Chapter IV — instruments).
> Focus: distinguishing pitched/unpitched, writing `midi-unpitched` correctly
> for cross-software consistency.

## 4.1 Types of Percussion

| Category | Example | MusicXML Notation |
|----------|--------|------------------|
| **Pitched** | Timpani, Marimba, Vibraphone, Xylophone, Glockenspiel | `<pitch>` |
| **Unpitched** | Snare, Bass drum, Cymbal, Triangle | `<unpitched>` |
| **Hybrid (drum kit)** | kick, snare, hi-hat, tom, crash | `<unpitched>` + instrument attribution |

### 4.1.1 Mallet/Bar Percussion Classification

| Instrument | Sounding range | Notation transposition | GM-ish program (usually VST) |
|-----------|----------------|----------------------|-------------------------------|
| Timpani | D2 – F#3 | concert (F-clef) | — |
| Marimba | A2 – C7 | concert (G-clef) | 12 |
| Xylophone | F4 – C8 | written 1 octave below sound | 13 |
| Vibraphone | F3 – F6 | concert | 11 |
| Glockenspiel | G5 – C8 | written 2 octaves below sound | 9 |

> Xylophone & Glockenspiel are *octave-transposing* — use
> `<transpose>` (see `Ch2-Transposisi-Instrumen.md`).

## 4.2 Unpitched Notation — Principles

- No `<pitch>`; use `<unpitched>` with `display-step`/`display-octave`
  for the visual position on the staff.
- The staff uses clef `<sign>percussion</sign>`.
- **One `<score-instrument>` per distinct sound** for accurate
  MIDI (e.g. snare vs kick in one part).

### 4.2.1 Standard GM Drum Mapping (`<midi-unpitched>`)

| Instrument | GM note | `<midi-unpitched>` |
|-----------|---------|--------------------|
| Acoustic Bass Drum (kick) | C2 (36) | 36 |
| Snare Drum | D1 (38) | 38 |
| Closed Hi-hat | F#1 (42) | 42 |
| Pedal Hi-hat | E1 (44) | 44 |
| Open Hi-hat | A#1 (46) | 46 |
| Low Tom | G1 (43) / A1 (45) | 45/47 |
| Ride Cymbal | D2 (51) | 51 |
| Crash Cymbal | C2 (49) | 49 |
| Triangle | E5 (81) | 81 |
| Tambourine | F#5 (54) | 54 |

### 4.2.2 MusicXML Application: Snare + Bass Drum in One Part

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P19">
      <part-name>Percussion</part-name>
      <part-abbreviation>Perc.</part-abbreviation>
      <score-instrument id="P19-S">
        <instrument-name>Snare Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <score-instrument id="P19-B">
        <instrument-name>Bass Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P19-S">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>38</midi-unpitched>
      </midi-instrument>
      <midi-instrument id="P19-B">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>36</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P19">
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
        <instrument id="P19-S"/>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.2.3 Notes with `<instrument>` Attribution

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P19">
      <part-name>Percussion</part-name>
      <part-abbreviation>Perc.</part-abbreviation>
      <score-instrument id="P19-S">
        <instrument-name>Snare Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <score-instrument id="P19-B">
        <instrument-name>Bass Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P19-S">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>38</midi-unpitched>
      </midi-instrument>
      <midi-instrument id="P19-B">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>36</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P19">
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
        <instrument id="P19-S"/>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>3</display-octave>
        </unpitched>
        <duration>2</duration>
        <instrument id="P19-B"/>
        <voice>2</voice>
        <type>eighth</type>
        <stem>down</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<instrument>` connects a note to one of the `score-instrument`s —
> mandatory when one part contains many unpitched sounds.

## 4.3 Drum Kit Notation — Standard Positions

Common staff positions (single staff, percussion clef):

| Element | Position (common) | GM |
|--------|---------------|-----|
| Kick | space below (C3) | 36 |
| Snare | D4/E4 | 38 |
| Closed hi-hat | G5 (above) | 42 |
| Open hi-hat | G5 + technique | 46 |
| Tom high | B4 | 48 |
| Tom mid | A4 | 47 |
| Floor tom | F4/E4 | 43 |
| Ride | B5/F5 | 51 |
| Crash | B5 (above, or F#5) | 49 |

### 4.3.1 Hi-hat Example: 16-beat Between Kick/Snare

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P19">
      <part-name>Percussion</part-name>
      <part-abbreviation>Perc.</part-abbreviation>
      <score-instrument id="P19-H">
        <instrument-name>Hi-hat</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P19-H">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>42</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P19">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>G</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>1</duration>
        <instrument id="P19-H"/>
        <voice>1</voice>
        <type>16th</type>
        <stem>up</stem>
        <notations>
          <articulations>
            <staccato/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 4.4 Pitched Percussion — Timpani & Mallet

### 4.4.1 Timpani

- Range of each drum noted at the start — tuning instructions via `<direction><words>`.
- F-clef, concert pitch.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P18">
      <part-name>Timpani</part-name>
    </score-part>
  </part-list>
  <part id="P18">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">D – A</words>
        </direction-type>
      </direction>
      <note>
        <pitch><step>D</step><octave>2</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.4.2 Timpani Note

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P18">
      <part-name>Timpani</part-name>
    </score-part>
  </part-list>
  <part id="P18">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
      <note>
        <pitch><step>D</step><octave>2</octave></pitch>
        <duration>4</duration>
        <instrument id="P18-I1"/>
        <voice>1</voice>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.4.3 Mallet: Xylophone

- Notated in G-clef, concert written 1 octave below sound → `<transpose>` for
  playback (`diatonic -7`, `chromatic -12`).

## 4.5 Special Symbols & Techniques

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
        <duration>16</duration>
        <type>whole</type>
        <notations>
          <articulations>
            <accent/>
            <staccato/>
            <tenuto/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

Snare roll (buzz) — tremolo:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P20">
      <part-name>Snare Drum</part-name>
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
        <duration>16</duration>
        <type>whole</type>
        <notations>
          <ornaments>
            <tremolo type="start">2</tremolo>
          </ornaments>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 4.6 Percussion Maps in Software

- **MuseScore:** Edit → Instruments → Drumset editor — visual pitch mapping.
- **Dorico:** playback templates; articulation per note.
- **Sibelius:** drum maps per part.
- **Cross-software import/export:** make sure `midi-unpitched` & `display-step`
  are consistent so the mapping does not break. Do not carry `<pitch>` on unpitched notes.

## 4.7 Percussion Engraving Checklist

| Check | Yes/No |
|---------|----------|
| Percussion / timpani clef correct? | |
| Does every unpitched note have a GM-appropriate `<midi-unpitched>`? | |
| Display positions consistent & understood by players? | |
| Roll/techniques recorded via articulations/tremolo? | |
| Timpani tuning instruction present? | |

## 4.8 Misconceptions

- **"Unpitched notes may use `<pitch>`"** — Wrong; use `<unpitched>` +
  `<midi-unpitched>` for correct cross-software behavior.
- **"One percussion part can mix many drums without `<instrument>`"** — It will
  sound as one program only; attribution is mandatory.
- **"Xylophone sounds as written"** — It *transposes* 1 octave above;
  do not forget the transposition.

## 4.9 Exercises

1. **Basic:** Write 4 bars of standard drum kit (kick+snare+hat) with GM mapping.
2. **Intermediate:** Create a 4-drum timpani part with tuning directions.
3. **Advanced:** Export a drum map from MuseScore → import into Dorico; check whether
   display positions & sounds stay consistent; document the differences.

## 4.10 Listening Repertoire

- Stravinsky, *The Rite of Spring* — monumental percussion section.
- Ravel, *Bolero* — iconic snare ostinato.
- Bartók, *Music for Strings, Percussion & Celesta*.

## 4.11 Book & Web References

**Books:**
- Adler, *The Study of Orchestration*.
- Rimsky-Korsakov, *Principles of Orchestration*.

**Web:**
- General MIDI percussive family list:
  https://www.midi.org/specifications/
- MuseScore drumset handbook: https://musescore.org/en/handbook

---

**Summary:** Percussion is divided into pitched/unpitched; MusicXML unpitched =
`<unpitched>` + `<midi-unpitched>` + `<instrument>` attribution, pitched = `<pitch>`
+ correct clef. This concludes Tier 1 [Basic Orchestration]. Continue to [Tier 2 —
Master S2 (`../../02-Master-S2-Lanjutan/`)].
