---
title: "Twelve-Tone Serialism"
pillar: "Contemporary Harmony, Jazz & Post-Tonal"
level: "Level 4-5"
xml_tags: ["accidental", "pitch", "alter", "key-accidental"]
related_files: ["Ch1-Chord-Scale-Theory.md", "Ch3-Harmoni-PostTonal.md"]
---

# Twelve-Tone Serialism

## 📖 Theoretical Concepts (Level 1-3)

Twelve-Tone Serialism (Dodecaphony) was developed by Arnold Schoenberg in the 1920s. The system uses a **tone row** — an ordered sequence of 12 non-repeating chromatic pitches — as the basis of composition.

### Tone Row Construction

A tone row has 4 basic forms:
1. **Prime (P)**: The original form
2. **Inversion (I)**: Vertical mirror
3. **Retrograde (R)**: Reversed order
4. **Retrograde Inversion (RI)**: Mirror + reversed

### Matrix (Magic Square)

The matrix is used to calculate all tone-row transformations:
- Rows = Prime (P0–P11)
- Columns = Inversion (I0–I11)
- Diagonals = Retrograde

### Principles of Serialism

1. **No Repetition**: No pitch is repeated within the order
2. **Chromatic Completion**: All 12 pitches must appear
3. **Interval Invariance**: Intervals between pitches are preserved
4. **Row Partitioning**: The tone row can be divided for textural needs

## 🎼 Practical Implementation (Level 4)

### For Arrangers/Composers

1. **Structural Foundation**: The tone row as the harmonic basis
2. **Melodic Generation**: Transformations for melody
3. **Harmonic Language**: Chords drawn from the tone row
4. **Rhythmic Independence**: Rhythm is not bound to the serial system

### Orchestration Techniques

- **Voice Exchange**: Distributing the tone row across instruments
- **Klangfarbenmelodie**: Color melody through timbre
- **Row Partitioning**: Divide the tone row among multiple instruments
- **Density Control**: Manage the number of active instruments

## ⚙️ Level 5: MusicXML Implementation

### XML Tags for Tone Row

``xml
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
      <!-- Tone row Prime -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
      </note>
      <!-- ... 12 notes total -->
      
      <!-- Row form marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9">P-0</words>
        </direction-type>
      </direction>
      
      <!-- Interval marking -->
      <direction placement="below">
        <direction-type>
          <words default-y="-15" font-size="8">+4, -6, +5...</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
``

### Explicit Accidentals for Atonal Writing

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
      <!-- Every note requires an explicit accidental -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <accidental>natural</accidental>
      </note>
      
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <accidental>natural</accidental>
      </note>
      
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <accidental>flat</accidental>
      </note>
      
      <!-- Atonal key signature (empty) -->
      <attributes>
        <key>
          <key-accidental slash="yes"/>
          <key-step>A</key-step>
        </key>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

### Row Form Markers

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
      <!-- P (Prime) -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-weight="bold">P-0</words>
        </direction-type>
      </direction>
      
      <!-- I (Inversion) -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-weight="bold">I-5</words>
        </direction-type>
      </direction>
      
      <!-- R (Retrograde) -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-weight="bold">R-3</words>
        </direction-type>
      </direction>
      
      <!-- RI (Retrograde Inversion) -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-weight="bold">RI-7</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Engraving Rules

- **Atonal context**: No key signature; all accidentals explicit
- **Cautionary accidentals**: Use them for readability
- **Row form markers**: Use text annotations for analysis
- **Voice leading**: Maintain it even when atonal
- **Beaming**: Follow standard rhythmic rules

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Accidental ambiguity | Use a natural before flat/sharp |
| Row form not visible | Add an explicit text annotation |
| Enharmonic confusion | Be consistent in enharmonic choice |
| Incorrect playback | Set `<concert-pitch>` if needed |

## 📚 References

- **Book**: *Twelve-Tone Serialism* (George Perle)
- **Book**: *The Structure of Atonal Music* (Allen Forte)
- **Book**: *Introduction to Twelve-Tone Theory* (George Perle)
