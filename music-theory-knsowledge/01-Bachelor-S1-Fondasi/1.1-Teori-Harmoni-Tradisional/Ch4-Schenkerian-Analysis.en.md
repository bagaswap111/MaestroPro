---
title: "Schenkerian Analysis & Tonal Prolongation"
pillar: "Deep Structure & Analytical Grammar"
level: "Level 4-5"
xml_tags: ["direction", "frame", "bracket", "voice"]
related_files: ["Ch1-Harmoni-Diatonik.md", "Ch3-Voice-Leading.md"]
---

# Schenkerian Analysis & Tonal Prolongation

## 📖 Theoretical Concepts (Level 1-3)

Schenkerian Analysis is a method of tonal music analysis developed by Heinrich Schenker. It views music as layers of hierarchical structure, in which the surface (foreground) of the music is elaborated from a simpler basic structure (background).

### Hierarchy of Tonal Musical Structure

```
Ursatz (Background)
├── Fundamental Line (Urlinie) - structural melody
├── Bass Arpeggiation (Bassbrechung) - basic harmony
│
Middleground
├── Prolongation techniques
├── Voice exchange
├── register transfer
│
Foreground
├── Surface elaboration
├── Passing tones, neighbor tones
├── Figuration
```

### Prolongation Techniques

1. **Consonant Support**: Consonant notes that support the harmonic structure
2. **Dissonant Prolongation**: Use of dissonance to prolong harmony
3. **Arpeggiation**: Broken chords extended across registers
4. **Register Transfer**: Movement of notes between octaves

## 🎼 Practical Implementation (Level 4)

### Analysis for Arrangers

In the context of arranging, Schenkerian Analysis helps:
- Identify essential harmonic structure vs surface elaboration
- Understand voice leading at the fundamental level
- Determine what should be emphasized in the arrangement
- Optimize instrument use based on structural register

### Score Reduction

When creating an orchestral score from a solo composition:
1. Identify the Ursatz (background structure)
2. Separate middleground from foreground
3. Distribute structural elements to the appropriate instruments
4. Maintain the hierarchy of voices in the orchestration

## ⚙️ Level 5: MusicXML Implementation

### XML Tags for Structural Analysis

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
        <staves>2</staves>
        <clef number="1">
          <sign>G</sign>
          <line>2</line>
        </clef>
        <clef number="2">
          <sign>F</sign>
          <line>4</line>
        </clef>
      </attributes>
      <!-- Direction to mark hierarchical structure -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-style="italic">Ursatz</words>
        </direction-type>
        <offset>0</offset>
      </direction>
      <!-- Bracket for analytical reduction -->
      <direction placement="above">
        <direction-type>
          <bracket type="start" line-end="down" default-y="25"/>
        </direction-type>
      </direction>
      <!-- Voice separation for multi-layer analysis -->
      <note>
        <voice>1</voice>
        <type>quarter</type>
        <stem>up</stem>
      </note>
      <note>
        <voice>2</voice>
        <type>quarter</type>
        <stem>down</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Notation for Multi-Layer Analysis

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
      <!-- Bracket notation for structural reduction -->
      <direction placement="above">
        <direction-type>
          <bracket default-y="30" line-end="down" line-type="dotted" type="start"/>
        </direction-type>
      </direction>
      <!-- Words for marking analysis levels -->
      <direction placement="above">
        <direction-type>
          <words default-y="35" font-size="9" font-style="italic">Middleground</words>
        </direction-type>
      </direction>
      <!-- Footnote for analytical explanation -->
      <direction placement="below">
        <direction-type>
          <words default-y="-30" font-size="8">^ Fundamental structure: I-V-I</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Engraving Rules

- Use a **bracket** (not a slur) to mark analytical sections
- **Italic font** for analytical terms (Ursatz, Urlinie, Bassbrechung)
- **Dotted line** for reductions not visible in performance
- **Wedge/bracket** to indicate register transfer
- Ensure **voice direction** is consistent for each analysis layer

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Bracket overlaps notes | Add a higher `default-y` |
| Inconsistent voice direction | Use the `<voice>` tag explicitly |
| Multi-staff analysis error | Ensure the `<staves>` count matches |
| Words not visible | Check `placement="above/below"` and `default-y` |

## 📚 References

- **Book**: *Harmonic Analysis* (Heinrich Schenker)
- **Book**: *Schenkerian Analysis* (Allen Cadwallader & David Gagné)
- **Book**: *The Musician's Guide to Analysis* (Janet Schmalfeldt)
