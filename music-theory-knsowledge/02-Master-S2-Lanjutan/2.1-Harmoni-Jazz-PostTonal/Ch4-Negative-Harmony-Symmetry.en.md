---
title: "Negative Harmony & Symmetrical Scales"
pillar: "Contemporary Harmony, Jazz & Post-Tonal"
level: "Level 4-5"
xml_tags: ["transpose", "degree", "accidental", "key"]
related_files: ["Ch1-Chord-Scale-Theory.md", "Ch2-Upper-Structures-Alterations.md"]
---

# Negative Harmony & Symmetrical Scales

## 📖 Theoretical Concepts (Level 1-3)

### Negative Harmony

Negative Harmony is a concept developed by Ernst Levy, explaining the mirror relationship between two harmonies. Every note has its "negative" based on an axis of symmetry.

```
C - D - E - F - G - A - B
  ↕   ↕   ↕   ↕   ↕   ↕   ↕
C - Bb - Ab - G - F - Eb - D
```

**Applications:**
- C major → C minor (negative)
- I-IV-V progression → I-ii-v (negative)
- Creating unexpected harmonic variations

### Symmetrical Scales

Symmetrical scales have intervals that repeat at regular intervals:
1. **Chromatic Scale**: Repeating semitone intervals
2. **Whole-Tone Scale**: Repeating whole-tone intervals
3. **Octatonic Scale**: Repeating whole-half intervals
4. **Augmented Scale**: Repeating minor 3rd intervals

### Mirror Chord Progressions

Progressions that use symmetry to create a mirror effect:
- **Axis Progression**: Uses a pivot chord
- **Tritone Substitution**: Replaces V with bII
- **Negative Counterpoint**: Harmonized mirror melodies

## 🎼 Practical Implementation (Level 4)

### For Arrangers

1. **Harmonic Variation**: Use negative harmony for variation
2. **Modal Interchange**: Negative of parallel modes
3. **Arranging Creativity**: Create unconventional voicings
4. **Transitional Harmony**: Bridge between sections with symmetry

### Analysis for Composition

- Identify the **axis** within the progression
- Use **tritone substitution** for variation
- Create a **mirror melody** for a counter-melody
- Explore **symmetrical voicing** for jazz chords

## ⚙️ Level 5: MusicXML Implementation

### XML Tags for Negative Harmony

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
      <!-- Transpose for negative -->
      <attributes>
        <transpose>
          <diatonic>-6</diatonic>
          <chromatic>-10</chromatic>
        </transpose>
      </attributes>
      
      <!-- Degree analysis for negative chord -->
      <harmony>
        <root>
          <root-step>C</root-step>
        </root>
        <kind text="m">minor</kind>
        <degree>
          <degree-value>3</degree-value>
          <degree-alter>0</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
      </harmony>
      
      <!-- Accidental for negative pitch -->
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
      </note>
    </measure>
  </part>
</score-partwise>
``

### XML Tags for Symmetrical Scales

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
      <!-- Key signature for atonal -->
      <attributes>
        <key>
          <key-accidental slash="yes"/>
          <key-step>A</key-step>
        </key>
      </attributes>
      
      <!-- Time signature for symmetrical -->
      <attributes>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
      </attributes>
      
      <!-- Cautionary accidental for symmetrical -->
      <note>
        <pitch>
          <step>E</step>
          <alter>0</alter>
          <octave>4</octave>
        </pitch>
        <accidental>
          <accidental-mark>natural</accidental-mark>
        </accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Transpose Tags for Mirror

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
      <!-- Mirror interval -->
      <direction placement="above">
        <direction-type>
          <transpose>
            <diatonic>3</diatonic>
            <chromatic>5</chromatic>
          </transpose>
        </direction-type>
      </direction>
      
      <!-- Axis marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-style="italic">Axis</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Engraving Rules

- Use **cautionary accidentals** for symmetry
- **Key signatures** may not be available for symmetrical scales
- Use **text markings** to explain negative harmony
- Maintain smooth **voice leading** even with complex harmony
- **Accidentals** must be clear for every note

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Negative chord not detected | Use `<kind>` with a text description |
| Symmetrical scale error | Make all accidentals explicit |
| Mirror interval wrong | Verify diatonic vs chromatic values |
| Enharmonic confusion | Use cautionary accidentals |

## 📚 References

- **Book**: *Negative Harmony* (Ernst Levy)
- **Book**: *The Jazz Theory Book* (Mark Levine)
- **Book**: *Twentieth-Century Harmony* (Vincent Persichetti)
