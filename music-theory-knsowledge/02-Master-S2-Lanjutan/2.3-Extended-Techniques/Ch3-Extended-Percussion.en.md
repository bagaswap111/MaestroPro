---
title: "Extended Techniques — Percussion"
tier: "Master S2"
subject: "Extended Techniques"
xml_tags: ["<note>", "<unpitched>", "<percussion>", "<technical>", "<words>", "<direction>", "<notehead>", "<midi-unpitched>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — Extended Techniques: Percussion

> **Guidebook for this chapter:** Gardner Read, *Contemporary Percussion*;
> John H. Beck, *Encyclopedia of Percussion*; John Cage, *prepared piano*
> notes. Focus: unusual instruments, prepared piano, non-standard techniques,
> MusicXML percussion setup/map.

## 3.1 Unusual Percussion & New "Percussion"

Extended percussion includes:

- Exploiting uncommon parts: rim, frame, rods.
- Nonconventional instruments: metal, wood, plastic, everyday objects.
- Body percussion (tap, chest thump) — no MIDI mapping; write instructions.

## 3.2 Prepared Piano (Cage)

Objects placed on the piano strings alter the timbre.

### 3.2.1 Common Notation

- Instructions at the start of the part; changes as `prepared with ...` / `remove preparation`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Percussion</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>percussion</sign><line>2</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">Prepared: 3 screws on C4–E4 str.</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### 3.2.2 String Piano Techniques

- *String pizz.* — direct pluck.
- *Knock body* — tap the piano body.
- *Silent depression* — hold the string without sound.

## 3.3 Extended Percussion Techniques

| Technique | Description | Notation |
|--------|------------|--------|
| Bowed cymbal/gong | bow the string on the cymbal | `arco` |
| Rim shots | mallet + rim | `rim shot` (GM 37) |
| Mallet roll | rapid tremolo | tremolo |
| Double-stops | two mallets | two notes / split |

### 3.3.1 Bowed Cymbal

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Percussion</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>percussion</sign><line>2</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">bow cymbal (arco)</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### 3.3.2 Mallet Tremolo

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Percussion</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>percussion</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>G</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
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

## 3.4 Stage Techniques

- **Dampened scrubbing** — hand covering the head → buzz.
- **Cymbal stacks** — multiple cymbals stacked.
- **Choked crashes** — pressing after the sound.
- If a symbol isn't available → `<technical>` + boxed text instruction.

## 3.5 Writing the Percussion Setup (Percussion Map)

Each element has a `score-instrument` + `midi-unpitched` GM mapping:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Percussion</part-name>
      <score-instrument id="P01-H">
        <instrument-name>Hi-hat (pedal)</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P01-H">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>44</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>percussion</sign><line>2</line></clef>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

> Kick=36, Snare=38, Hi-hat closed 42 / pedal 44, Ride=51, Crash=49, Tom
> 45/47/48/50.

### 3.5.1 Documenting the Setup at the Start of the Part

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Percussion</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>percussion</sign><line>2</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">Setup: 4 drums + 3 cymbals (hi-hat, ride, crash)</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 3.6 Multi-Staff Percussion

When the setup has more than 4 elements, use multiple staves:

| Staff | Contents |
|------|-----|
| Staff 1 | Mallet / pitched (timpani/marimba) |
| Staff 2 | Battery (snare/kick/hi-hat) |

MusicXML: `<staves>2</staves>` + `staff` on each note.

## 3.7 Repertoire

| Work | Technique |
|-------|--------|
| **Varèse — Ionisation** | drums + sirens; non-pitched |
| **Cage — Sonatas & Interludes** | prepared piano |
| **Reich — Music for 18 Musicians** | mallet phasing |
| **Xenakis — Psappha** | 6 percussionists + friction |

## 3.8 Checklist

| Check | Yes/No |
|---------|----------|
| Unique setup documented? | |
| Every element's `midi-unpitched` correct? | |
| Tremolo/roll slashes correct? | |
| Bow/arco instructions clear in the part? | |
| Piano preparation explained in text? | |

## 3.9 Common Misconceptions

- **"Prepared piano needs special MIDI"** — The music is stored normally in pitch;
  preparations are mapped by the performer/technician.
- **"All percussion = unpitched"** — Timpani/marimba are pitched; mapping differs.
- **"One staff is enough for the setup"** — For complex setups use multi-staff.

## 3.10 Exercises

1. Write a short extended percussion part (bow cymbal + rim shot).
2. Create a 3-object prepared piano setup → part instructions.
3. Map 4 percussion elements to MusicXML multi-staff.

## 3.11 References

- Read, *Contemporary Percussion*.
- Beck, *Encyclopedia of Percussion*.
- Cage, *Sonatas & Interludes* (preparation notes).

---

**Summary:** Ext. percussion = prepared piano, bowed/rim/roll, nonconventional
instruments; MusicXML via `score-instrument`/`midi-unpitched` map, `<words>`
instructions, tremolo. This closes Tier 2 ([Master S2]). Continue to [Tier 3 —
Doctoral S3 (`../../03-Doctoral-S3-Riset/`)].
