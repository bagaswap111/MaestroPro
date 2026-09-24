---
title: "Just Intonation Tuning"
pillar: "Contemporary Harmony, Jazz & Post-Tonal"
level: "Level 4-5"
xml_tags: ["tuning", "pitch", "cents", "frequency"]
related_files: ["Ch1-Teori-Spektral.md", "Ch2-Mikrotonal-Tuning.md"]
---

# Just Intonation Tuning

## 📖 Theoretical Concepts (Level 1-3)

Just Intonation (JI) is a tuning system based on natural **frequency ratios** from the harmonic series, not equal division of the octave as in Equal Temperament.

### Tuning Comparison

| System | Basis | Character |
|:---|:---|:---|
| **Equal Temperament** | 12 equal octave divisions | Versatile, slightly out of tune |
| **Just Intonation** | Frequency ratios | Pure intervals, limited modulation |
| **Pythagorean** | Perfect 5ths | Bright, sharp 3rds |
| **Meantone** | Narrow 5ths | Pure 3rds, bad keys |

### Common JI Ratios

```
Unison:        1:1      (0 cents)
Minor 2nd:     16:15    (112 cents)
Major 2nd:     9:8      (204 cents)
Minor 3rd:     6:5      (316 cents)
Major 3rd:     5:4      (386 cents)
Perfect 4th:   4:3      (498 cents)
Tritone:       45:32    (590 cents)
Perfect 5th:   3:2      (702 cents)
Minor 6th:     8:5      (814 cents)
Major 6th:     5:3      (884 cents)
Minor 7th:     9:5      (1018 cents)
Major 7th:     15:8     (1088 cents)
Octave:        2:1      (1200 cents)
```

## 🎼 Practical Implementation (Level 4)

### For Arrangers

1. **Resonance Maximization**: Choose ratios for resonance
2. **Harmonic Clarity**: JI for clear chords
3. **Timbral Variation**: Ratios affect timbre
4. **Microtonal Composition**: Composition with JI

### Practical Applications

- **A cappella**: Natural JI for vocals
- **Gamelan**: Traditional JI system
- **Experimental**: Contemporary JI composition
- **Sound Design**: Sound synthesis with JI

## ⚙️ Level 5: MusicXML Implementation

### Tuning Definitions

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
        <!-- Tuning for the instrument -->
        <tuning>
          <tuning-step>C</tuning-step>
          <tuning-alter>0</tuning-alter>
          <tuning-octave>4</tuning-octave>
          <cents>0</cents>
        </tuning>
      </attributes>

      <attributes>
        <!-- Custom tuning for JI ratio 5:4 (Major 3rd) -->
        <tuning>
          <tuning-step>E</tuning-step>
          <tuning-alter>-14</tuning-alter>
          <tuning-octave>4</tuning-octave>
          <cents>-14</cents>
        </tuning>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

### Cents Deviation

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
      <!-- Cents deviation for microtones -->
      <note>
        <pitch>
          <step>C</step>
          <alter>0</alter>
          <octave>4</octave>
        </pitch>
        <accidental>natural</accidental>
      </note>

      <!-- JI adjustment -->
      <note>
        <pitch>
          <step>E</step>
          <alter>-14</alter>
          <octave>4</octave>
        </pitch>
      </note>

      <!-- Direction with cents annotation -->
      <direction placement="below">
        <direction-type>
          <words default-y="-15" font-size="8">-14 cents (JI 5:4)</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Custom Tuning XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <defaults>
    <scaling>
      <millimeters>6.35</millimeters>
      <tenths>40</tenths>
    </scaling>
  </defaults>
  <part-list>
    <score-part id="P1">
      <part-name>Ensemble</part-name>
      <part-abbreviation>Ens</part-abbreviation>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <!-- Per-note tuning -->
        <tuning>
          <tuning-step>G</tuning-step>
          <tuning-alter>2</tuning-alter>
          <tuning-octave>4</tuning-octave>
          <cents>2</cents>
        </tuning>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

### Engraving Rules

- **Cents markings**: Must be clear below or above the note
- **Ratio annotations**: Use text for frequency ratios
- **Tuning brackets**: Mark sections with different tunings
- **Accidental system**: Use a consistent system
- **Legend**: State the tuning system at the beginning of the score

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Cents are unreadable | Use a sufficiently large font size |
| Tuning conflict | Set `<concert-pitch>` as a reference |
| Complex ratio | Use decimal notation |
| Multiple tunings | Use separate staves or text markers |

## 📚 References

- **Book**: *The Structure of Atonal Music* (Allen Forte)
- **Book**: *Just Intonation Primer* (Neil Haverstick)
- **Journal**: *Computer Music Journal* - Tuning systems
