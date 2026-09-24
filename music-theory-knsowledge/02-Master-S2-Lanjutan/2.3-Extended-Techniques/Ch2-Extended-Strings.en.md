---
title: "Extended Techniques — Strings"
tier: "Master S2"
subject: "Extended Techniques"
xml_tags: ["<note>", "<notations>", "<technical>", "<articulations>", "<notehead>", "<words>", "<direction>", "<glissando>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — Extended Techniques: Strings

> **Guidebook for this chapter:** Gardner Read, *Contemporary Instrumental
> Techniques*; Penderecki/Xenakis scores; Patricia & Allen Strange,
> *The Modern Violin*. Focus: col legno, sul pont/tasto, snap pizz, advanced
> harmonics, extreme techniques — MusicXML notation.

## 2.1 Col Legno

**Col legno battuto** (strike with the wood) vs **tratto** (bow with the wood) —
both require an instruction + return to `arco`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Strings</part-name>
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
          <words xml:space="preserve">col legno battuto</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

Return:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Strings</part-name>
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
          <words xml:space="preserve">arco</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 2.2 Sul Ponticello & Sul Tasto

| Technique | Instruction | Sound |
|--------|-----------|-------|
| *Sul ponticello* | `sul pont.` | metallic, near the bridge |
| *Sul tasto* | `sul tasto` / `flautando` | soft, over the fingerboard |
| *Molto sul pont.* | `p.p.s.p.` | hysterical |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Strings</part-name>
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

> Combined techniques: `sul ponticello + tremolo` — stack the instructions,
> don't double the rests.

## 2.3 Bartók / Snap Pizzicato

The string is pressed and released — "snapping" onto the fingerboard.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Strings</part-name>
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
        <pitch><step>G</step><octave>3</octave></pitch>
        <duration>1</duration>
        <type>quarter</type>
        <notations>
          <articulations>
            <snap-pizzicato/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Behind-the-Bridge & Extreme Techniques

- **b.t.b. (behind the bridge)** — pluck between bridge and tailpiece.
- **Scordatura** — nonstandard tuning; notation: written vs sounding; MusicXML
  via `<transpose>` or string-tuning.
- **Bow knock** — tap the instrument body (≈ percussive).

Scordatura MusicXML pattern:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Strings</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <staff-tuning number="1">
    <tuning-step>G</tuning-step>
    <tuning-octave>3</tuning-octave>
  </staff-tuning>
      </attributes>

    </measure>
  </part>
</score-partwise>
```

## 2.5 Advanced Harmonics

### 2.5.1 Artificial

- Foundation (below) + diamond (above) connected.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Strings</part-name>
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
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>2</duration><type>half</type>
      </note>
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>2</duration><type>half</type>
        <notehead>diamond</notehead>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Natural harm. = single diamond; artificial = two notes + note position.

### 2.5.2 Glissando Harmonics

Often in spectralism — a series of harmonics ascending/descending.

## 2.6 Glissando on One String

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Strings</part-name>
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
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>3</duration><type>dotted-quarter</type>
        <notations><glissando type="start"/></notations>
      </note>
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
        <notations><glissando type="stop"/></notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Add `<technical><string>3</string></technical>` to clarify the string.

## 2.7 Unmeasured Tremolo & Divisi Mass

- **Unmeasured tremolo** — slashes without counting (Septimitus).
- Combine divisi + tremolo → dense texture.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Strings</part-name>
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
        <duration>4</duration><type>whole</type>
        <notations><ornaments><tremolo type="start">0</tremolo></ornaments></notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `tremolo type="start">0` = unmeasured (no slashes). Values 1–8 add
> beams/slashes.

## 2.8 Contemporary Repertoire

- **Penderecki — Threnody**: clusters, sul pont, col legno.
- **Xenakis — Metastasis**: large glissandi (tutti descending).
- **Lachenmann — Intérieur I**: string percussion (knock, scratch).

## 2.9 Checklist

| Check | Yes/No |
|---------|----------|
| Instructions written (sul pont, col legno)? | |
| Snap pizz/bow knock given articulation? | |
| Harmonics (natural/artificial) correct? | |
| Glissando start/stop `<glissando>`? | |
| Scordatura/staff-tuning documented? | |

## 2.10 Common Misconceptions

- **"Col legno must always be battuto"** — There is also tratto (bowed); specify.
- **"Artificial harmony uses just one diamond"** — Needs two notes (foundation +
  diamond).
- **"Glissando = direct slide"** — On strings it can be a smooth *portamento*;
  write what you intend.

## 2.11 Exercises

1. 2 bars: sul pont. tremolo on violin.
2. Cello snap pizz (G3) + 1-string glissando.
3. Cello scordatura (G→F) + successive notes.

## 2.12 References

- Read, *Contemporary Instrumental Techniques*.
- Strange, *The Contemporary Violin*.
- Penderecki, *Threnody* (score).

---

**Summary:** Ext. strings = col legno, sul pont/tasto, snap pizz, harmonics,
scordatura, unmeasured tremolo; MusicXML via `<technical>`, `<articulations>`,
`<notehead>`, `<glissando>`, `staff-tuning`. Continue to [Extended Percussion
(`Ch3-Extended-Percussion.md`)].
