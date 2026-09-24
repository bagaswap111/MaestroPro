---
title: "Duration & Rhythm Encoding"
pillar: "MusicXML Architecture & Computational Music"
level: "Level 4-5"
xml_tags: ["duration", "divisions", "type", "time-modification", "tuplet"]
related_files: ["Ch2-The-Note-Element.md", "Ch5-Score-Timewise-vs-Partwise.md"]
---

# Duration & Rhythm Encoding

## 📖 Theoretical Concepts (Level 1-3)

Duration in MusicXML is encoded using **divisions** as the reference. Every note
has a duration in divisions units.

### Divisions System

```
Divisions = 4 (default)
Quarter note = 4 divisions
Eighth note = 2 divisions
Sixteenth note = 1 division
Half note = 8 divisions
Whole note = 16 divisions
```

### Note Types

| Type | Duration (divisions=4) |
|:---|:---|
| whole | 16 |
| half | 8 |
| quarter | 4 |
| eighth | 2 |
| 16th | 1 |
| 32nd | 0.5 |
| 64th | 0.25 |

### Tuplets

Tuplets use **time-modification** to indicate duration changes:

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
      <time-modification>
      <actual-notes>3</actual-notes>
      <normal-notes>2</normal-notes>
      </time-modification>
    </measure>
  </part>
</score-partwise>
```

## 🎼 Practical Implementation (Level 4)

### Correct Durations

1. **Calculate Divisions**: Set divisions at the start
2. **Calculate Duration**: Duration = type value × divisions
3. **Tuplets**: Use time-modification
4. **Rest**: Rests have the same duration

### Rhythm Patterns

- **Dotted notes**: Duration × 1.5
- **Tied notes**: Sum of durations
- **Grace notes**: Duration = 0
- **Cue notes**: Small duration

## ⚙️ Level 5: MusicXML Implementation

### Basic Duration Encoding

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
      <!-- Divisions declaration -->
      <attributes>
      <divisions>4</divisions>
      </attributes>

      <!-- Quarter note -->
      <note>
      <pitch>
      <step>C</step>
      <octave>4</octave>
      </pitch>
      <duration>4</duration>
      <type>quarter</type>
      </note>

      <!-- Eighth note -->
      <note>
      <pitch>
      <step>D</step>
      <octave>4</octave>
      </pitch>
      <duration>2</duration>
      <type>eighth</type>
      </note>

      <!-- Sixteenth note -->
      <note>
      <pitch>
      <step>E</step>
      <octave>4</octave>
      </pitch>
      <duration>1</duration>
      <type>16th</type>
      </note>

      <!-- Half note -->
      <note>
      <pitch>
      <step>F</step>
      <octave>4</octave>
      </pitch>
      <duration>8</duration>
      <type>half</type>
      </note>

      <!-- Whole note -->
      <note>
      <pitch>
      <step>G</step>
      <octave>4</octave>
      </pitch>
      <duration>16</duration>
      <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Dotted Notes

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
      <!-- Dotted quarter note -->
      <note>
      <pitch>
      <step>C</step>
      <octave>4</octave>
      </pitch>
      <duration>6</duration>
      <type>quarter</type>
      <dot/>
      </note>

      <!-- Double dotted half note -->
      <note>
      <pitch>
      <step>D</step>
      <octave>4</octave>
      </pitch>
      <duration>14</duration>
      <type>half</type>
      <dot/>
      <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Tuplets

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
      <!-- Triplet -->
      <note>
      <pitch>
      <step>C</step>
      <octave>4</octave>
      </pitch>
      <duration>2</duration>
      <type>eighth</type>
      <time-modification>
      <actual-notes>3</actual-notes>
      <normal-notes>2</normal-notes>
      </time-modification>
      <notations>
      <tuplet type="start" bracket="yes"/>
      </notations>
      </note>

      <!-- Tuplet continued -->
      <note>
      <pitch>
      <step>D</step>
      <octave>4</octave>
      </pitch>
      <duration>2</duration>
      <type>eighth</type>
      <time-modification>
      <actual-notes>3</actual-notes>
      <normal-notes>2</normal-notes>
      </time-modification>
      </note>

      <!-- Tuplet end -->
      <note>
      <pitch>
      <step>E</step>
      <octave>4</octave>
      </pitch>
      <duration>2</duration>
      <type>eighth</type>
      <time-modification>
      <actual-notes>3</actual-notes>
      <normal-notes>2</normal-notes>
      </time-modification>
      <notations>
      <tuplet type="stop"/>
      </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Complex Tuplets

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
      <!-- Quintuplet -->
      <note>
      <pitch>
      <step>C</step>
      <octave>4</octave>
      </pitch>
      <duration>2</duration>
      <type>eighth</type>
      <time-modification>
      <actual-notes>5</actual-notes>
      <normal-notes>4</normal-notes>
      </time-modification>
      <notations>
      <tuplet type="start" bracket="yes" show-number="actual"/>
      </notations>
      </note>

      <!-- Septuplet -->
      <note>
      <pitch>
      <step>D</step>
      <octave>4</octave>
      </pitch>
      <duration>2</duration>
      <type>eighth</type>
      <time-modification>
      <actual-notes>7</actual-notes>
      <normal-notes>4</normal-notes>
      </time-modification>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Grace Notes (Duration = 0)

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
      <!-- Grace note -->
      <grace/>
      <note>
      <pitch>
      <step>C</step>
      <octave>5</octave>
      </pitch>
      <duration>0</duration>
      <type>eighth</type>
      </note>

      <!-- Main note after grace -->
      <note>
      <pitch>
      <step>D</step>
      <octave>5</octave>
      </pitch>
      <duration>4</duration>
      <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Engraving Rules

- **Divisions**: Must be consistent throughout one score
- **Duration**: Must be accurate per type
- **Tuplets**: Use time-modification
- **Dots**: Add duration according to the rules
- **Grace notes**: Duration = 0

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Wrong duration | Recalculate based on divisions |
| Tuplet not read | Add bracket and number |
| Rhythm clash | Check the time signature |
| Note overflow | Reduce duration or use a tie |

## 📚 References

- **Specification**: MusicXML 4.0 - Duration elements
- **DTD**: Note element specification
- **Book**: *Behind Bars* (Elaine Gould) - Rhythmic notation
