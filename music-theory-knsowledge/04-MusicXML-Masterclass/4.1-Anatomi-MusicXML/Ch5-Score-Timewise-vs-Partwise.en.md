---
title: "Score-Timewise vs Score-Partwise"
pillar: "MusicXML Architecture & Computational Music"
level: "Level 4-5"
xml_tags: ["score-partwise", "score-timewise", "part", "measure"]
related_files: ["Ch1-Struktur-Root-Partwise.md", "Ch6-Duration-Rhythm-Encoding.md"]
---

# Score-Timewise vs Score-Partwise

## 📖 Theoretical Concepts (Level 1-3)

MusicXML has two root element formats: **Score-Partwise** and **Score-Timewise**.
The choice of format affects how the musical data is organized.

### Score-Partwise

A format that organizes data by **part** first:

```xml
<score-partwise>
  <part-list>...</part-list>
  <part id="P1">
    <measure number="1">...</measure>
    <measure number="2">...</measure>
  </part>
  <part id="P2">
    <measure number="1">...</measure>
    <measure number="2">...</measure>
  </part>
</score-partwise>
```

**Characteristics:**
- Part is the top level
- Each part contains all measures
- Ideal for individual parts
- Default format for most software

### Score-Timewise

A format that organizes data by **measure** first:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<part-list>...</part-list>
  <part id="P1">
    <measure number="1">
      ...
    </measure>
    <measure number="2">
      ...
    </measure>
  </part>
  <part id="P2">
    <measure number="1">
      ...
    </measure>
    <measure number="2">
      ...
    </measure>
  </part>
</score-partwise>
```

**Characteristics:**
- Measure is the top level
- Each measure contains all parts
- Ideal for simultaneous analysis
- Useful for comparing parts

## 🎼 Practical Implementation (Level 4)

### When to Use Partwise

1. **Part Extraction**: Extract individual parts
2. **Part Processing**: Process per-part
3. **Score Editing**: Editing scores
4. **Export per Part**: Export per instrument

### When to Use Timewise

1. **Score Analysis**: Simultaneous analysis
2. **Comparison**: Comparing parts
3. **Beat Analysis**: Analysis per beat
4. **Synchronization**: Synchronizing parts

## ⚙️ Level 5: MusicXML Implementation

### Score-Partwise Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC
  "-//Recordare//DTD MusicXML 4.0 Partwise//EN"
  "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <work>
    <work-title>Contoh Partwise</work-title>
  </work>
  <identification>
    <creator type="composer">Composer Name</creator>
  </identification>
  <part-list>
    <score-part id="P1">
      <part-name>Violin I</part-name>
      <part-abbreviation>Vln. I</part-abbreviation>
    </score-part>
    <score-part id="P2">
      <part-name>Violin II</part-name>
      <part-abbreviation>Vln. II</part-abbreviation>
    </score-part>
  </part-list>
  
  <!-- Part 1: Violin I -->
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
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
  
  <!-- Part 2: Violin II -->
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>G</step><octave>3</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Score-Timewise Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<part-list>
    <score-part id="P1">
      <part-name>Violin I</part-name>
    </score-part>
    <score-part id="P2">
      <part-name>Violin II</part-name>
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
      <duration>4</duration>
      <type>quarter</type>
      </note>
    </measure>
  </part>
  <part id="P2">
    <measure number="1">
      <attributes>
      <divisions>4</divisions>
      <key><fifths>0</fifths></key>
      <time><beats>4</beats><beat-type>4</beat-type></time>
      <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
      <pitch><step>G</step><octave>3</octave></pitch>
      <duration>4</duration>
      <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Conversion with Python music21

```python
import music21

# Read partwise
score = music21.converter.parse('partwise.xml')

# Convert to timewise
timewise = score.toTimewise()

# Or vice versa
partwise = timewise.toPartwise()
```

### Engraving Rules

- **Partwise**: Default for export
- **Timewise**: For analysis
- **Part-list**: Must be identical in both formats
- **Measure numbers**: Must be consistent
- **Attributes**: Must be in the first part/measure

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Part not read | Check the part-list |
| Measures out of sync | Use timewise to verify |
| Export fails | Use partwise for export |
| Import error | Convert to the correct format |

## 📚 References

- **Specification**: MusicXML 4.0 Standard
- **DTD**: partwise.dtd and timewise.dtd
- **Tool**: music21 Python library
