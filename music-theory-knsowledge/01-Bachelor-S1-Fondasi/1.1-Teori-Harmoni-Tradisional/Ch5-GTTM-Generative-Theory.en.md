---
title: "GTTM - Generative Theory of Tonal Music"
pillar: "Deep Structure & Analytical Grammar"
level: "Level 4-5"
xml_tags: ["direction", "grouping", "metronome", "words"]
related_files: ["Ch1-Harmoni-Diatonik.md", "Ch2-Progresi-Akor-Modulasi.md"]
---

# GTTM - Generative Theory of Tonal Music

## 📖 Theoretical Concepts (Level 1-3)

The Generative Theory of Tonal Music (GTTM) was developed by Fred Lerdahl and Ray Jackendoff. This theory analyzes tonal music based on **grouping structure** and **meter structure** as its two main dimensions.

### Grouping Structure

Grouping structure divides music into segments based on:
- **Proximity**: Distance between notes (rests, dynamic changes)
- **Similarity**: Similarity of rhythmic/melodic patterns
- **Parallelism**: Repetition of patterns

### Meter Structure

Meter structure organizes hierarchical beats:
- **Pulse**: Basic beat
- **Beat**: Organized beat
- **Measure**: Group of beats
- **Hyper-measure**: Group of measures

### Preference Rules

GTTM uses **preference rules** to determine the most likely structure:
1. **Well-Formedness Rules**: Basic rules for valid structures
2. **Preference Rules**: Rules for choosing the best interpretation

## 🎼 Practical Implementation (Level 4)

### For Arrangers/Composers

GTTM helps with:
1. **Phrasing**: Identifying phrase boundaries for articulation
2. **Dynamic Shaping**: Adjusting dynamics based on grouping
3. **Rhythmic Clarity**: Ensuring meter structure is clear in notation
4. **Structural Emphasis**: Emphasizing important structural points

### Analysis for Orchestration

- Use grouping to determine **breath marks** for wind instruments
- Identify hyper-measures for orchestral **dynamic shaping**
- Use meter structure for effective **rhythmic layering**

## ⚙️ Level 5: MusicXML Implementation

### XML Tags for Grouping Structure

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
      <!-- Grouping start for a musical segment -->
      <direction placement="above">
        <direction-type>
          <grouping type="start" member-of="1"/>
        </direction-type>
      </direction>

      <!-- Grouping stop at the end of a segment -->
      <direction placement="above">
        <direction-type>
          <grouping type="stop" member-of="1"/>
        </direction-type>
      </direction>

      <!-- Multi-level grouping -->
      <direction placement="above">
        <direction-type>
          <grouping type="start" member-of="1"/>
        </direction-type>
      </direction>

      <direction placement="above">
        <direction-type>
          <grouping type="start" member-of="2"/>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### XML Tags for Meter Structure

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
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <!-- Metronome marking for tempo -->
      <direction placement="above">
        <direction-type>
          <metronome parentheses="no">
            <beat-unit>quarter</beat-unit>
            <per-minute>120</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="120"/>
      </direction>

      <!-- Hyper-measure marking with rehearsal marks -->
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="25" font-size="14">A</rehearsal>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Words for Analytical Marking

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
      <!-- Grouping level marking -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-style="italic">Phrase 1</words>
        </direction-type>
      </direction>

      <!-- Hyper-measure marking -->
      <direction placement="above">
        <direction-type>
          <words default-y="30" font-size="9">Hyper-measure 1</words>
        </direction-type>
      </direction>

      <!-- Breath mark at a grouping boundary -->
      <note>
        <notations>
          <breath-mark/>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Engraving Rules

- Use **rehearsal marks** (letters/numbers) for hyper-measure boundaries
- **Slur** to show grouping visually
- **Breath marks** at grouping boundaries for wind instruments
- **Fermata** at important structural points
- Use **dynamic markings** to follow the grouping contour

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Grouping not visible | Use a combination of slur + words |
| Meter ambiguity | Add an explicit metronome marking |
| Hyper-measure unclear | Use rehearsal marks with a large font |
| Breath mark too close | Minimum distance of 1 space between breath marks |

## 📚 References

- **Book**: *A Generative Theory of Tonal Music* (Lerdahl & Jackendoff, 1983)
- **Book**: *The Analysis of Tonal Music* (Jonathan Dunsby)
- **Journal**: *Music Theory Online* - articles on GTTM applications
