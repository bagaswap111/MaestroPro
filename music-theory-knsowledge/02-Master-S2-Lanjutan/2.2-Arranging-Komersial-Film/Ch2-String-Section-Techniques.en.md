---
title: "String Section Techniques"
tier: "Master S2"
subject: "Commercial & Film Arranging"
xml_tags: ["<note>", "<notations>", "<divisi>", "<tremolo>", "<articulations>", "<direction>", "<words>", "<bowing>", "<glissando>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — String Section Techniques

> **Guidebook for this chapter:** Samuel Adler, *The Study of Orchestration*
> (strings chapters); Walter Piston, *Orchestration* (Chapters 5–6); divisi
> writing in Dorico. Focus: divisi/unison, bowing, tremolo, harmonics,
> pizzicato — how to write a living string section.

## 2.1 String Section Layout

| Group | Range (concert) | Role |
|----------|----------------|-------|
| Violin I | G3 – C7 | melody/top |
| Violin II | G3 – C7 | harmony, counter |
| Viola | C3 – E6 | middle color |
| Cello | C2 – A5 | lower melody/expressive bass |
| Double Bass | E1 – G4 | bass (notated one octave above sounding) |

### 2.1.1 Registers per staff

- Vln/Vla: treble.
- Vlc: bass (sometimes tenor clef for the upper register).
- Db: bass (octave-transposing, see Tier 1 Ch2 transposition).

## 2.2 Divisi (div.) and Unison

**Divisi** = splitting the group into two or more lines; **a2/unison** = all the same.

- Mark `div.` above the staff (sometimes `a2`).
- Example: Divisi into 2 lines: notes in voice 1 & voice 2.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
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
          <words xml:space="preserve">div.</words>
        </direction-type>
      </direction>
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
      <part-name>Violin</part-name>
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
      <note>
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>2</duration><voice>1</voice><type>half</type>
      </note>
    </measure>
    <measure number="3">
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>2</duration><voice>2</voice><type>half</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Return to `unison`: `<direction><words>unison</words>`. Dorico has native
> *divisi management*; we keep `<voice>` consistent.

## 2.3 Tremolo & Vamp

- **Tremolo** — rapid alternation; `tremolo type="start"` + number of slashes.
- **Vamp** — repetition.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
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
        <notations>
          <ornaments>
            <tremolo type="start">3</tremolo>
          </ornaments>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> 3 slashes → 32nd-note tremolo (very fast). Tremolo should end with
> `<tremolo type="stop">`.

## 2.4 Harmonics

- **Natural**: touch the node (octave, fifth...); diamond notehead.
- **Artificial**: pressure + fingerboard; normal notation below + diamond.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
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
        <duration>4</duration>
        <type>whole</type>
        <notehead>diamond</notehead>
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
      <part-name>Violin</part-name>
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
          <words xml:space="preserve">harm.</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 2.5 Bowing Techniques

| Technique | Symbol | MusicXML |
|--------|--------|----------|
| Up-bow | ⌄ | `<up-bow/>` |
| Down-bow | ⌃ | `<down-bow/>` |
| Col legno | — | `<words>col legno</words>` |
| Sul ponticello | — | `<words>sul pont.</words>` |
| Sul tasto | — | `<words>sul tasto</words>` |
| Sulla punta (at the tip) | — | `<words>sulla punta</words>` |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
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
        <duration>4</duration><type>whole</type>
        <notations>
          <technical>
            <down-bow/>
          </technical>
        </notations>
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
      <part-name>Violin</part-name>
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
          <words xml:space="preserve">sul pont.</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> **Notation tip:** repeat the technique at every change — don't assume it continues.

## 2.6 Pizzicato & Bartók Pizz

- Pizz = pluck; return with `arco`.
- Bartók pizz = hard pluck (string snaps back onto the fingerboard).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
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
        <pitch><step>A</step><octave>3</octave></pitch>
        <duration>1</duration>
        <type>quarter</type>
        <notations>
          <articulations>
            <pizzicato/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Pizzicato via `<articulations><pizzicato/>`. Return to arco:
> `<direction><words>arco</words>`.

## 2.7 String Writing in Film

1. **Homophonic stroke** — all together → warm.
2. **Melodic doubling** — octaves (vln+cello) → projection.
3. **Contrapuntal** — several counter lines (viola/cello) → climax.
4. **Tremolo/glissando** — suspense.

### 2.7.1 Glissando

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
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
        <notations>
          <glissando type="start"/>
        </notations>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch><step>D</step><octave>5</octave></pitch>
        <duration>2</duration><type>half</type>
        <notations>
          <glissando type="stop"/>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.8 String Orchestra Template

1. Parts: Vln I, Vln II, Vla, Vlc, Cb.
2. Clefs: G/G/G/F/F.
3. Enable divisi.
4. Bowing mapped for playback.

## 2.9 Checklist

| Check | Yes/No |
|---------|----------|
| Divisi marked div./a2? | |
| String ranges within limits? | |
| pizz/arco/sul pont/harm technique written? | |
| Tremolo note-value slashes correct? | |
| Unique bowing per phrase? | |

## 2.10 Common Misconceptions

- **"Divisi is always 2 parts"** — Can be 2–3 (divisi a3).
- **"`harmonic` uses only a diamond notehead"** — Diamond marks a
  natural harmonic; artificial needs two pitches.
- **"Glissando must be a large interval"** — Can also be a small step (portamento).

## 2.11 Exercises

1. Write 4 bars of homophonic divisi (vln I a3) in MusicXML voices 1–3.
2. Create a violin glissando from G4 to B5 + sul pont.
3. Arrange 8 bars of string counterpoint (vla+vlc counter).

## 2.12 References

- Adler, *The Study of Orchestration* — strings.
- Piston, *Orchestration*.
- Dorico divisi docs.

---

**Summary:** String section = divisi + bowing + tremolo + harmonics +
pizzicato; MusicXML via `<voice>`/`<divisi words>`, `<articulations>`,
`<technical>` (bow), `<tremolo>`, and `<glissando>`. Continue to [Film
Scoring Notation (`Ch3-Film-Scoring-Notation.md`)].
