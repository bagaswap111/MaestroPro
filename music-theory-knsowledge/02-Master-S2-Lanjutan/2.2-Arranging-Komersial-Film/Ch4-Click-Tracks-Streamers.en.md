---
title: "Click Tracks & Streamers"
pillar: "Industrial Workflow & Specialized Applications"
level: "Level 4-5"
xml_tags: ["direction", "metronome", "words", "rehearsal"]
related_files: ["Ch3-Film-Scoring-Notation.md", "Ch1-Big-Band-Arranging.md"]
---

# Click Tracks & Streamers

## 📖 Theoretical Concepts (Level 1-3)

In film scoring, the **click track** and **streamer** are crucial synchronization aids between the music and the picture.

### Click Track

A click track is a recorded metronome click that maintains tempo during recording:
- **Subdivision**: Usually a 1/4 note or 1/8 note
- **Tempo**: Determined by the picture editor
- **Count-in**: Usually 2-4 bars before starting

### Streamer

A streamer is a visual marker in the score indicating **hit points** (important points):
- **Forward streamer**: Diagonal line upward (toward the hit)
- **Pop**: A beat marker right at the hit point
- **Vertical line**: Vertical line for synchronization

### Types of Hit Points

1. **Hard Hit**: Abrupt scene change
2. **Soft Hit**: Gradual transition
3. **Bridge**: Connecting point between scenes
4. **In/Out Point**: Start and end of a scene

## 🎼 Practical Implementation (Level 4)

### Click Track Management

1. **Tempo Map**: Create a precise tempo map
2. **Subdivision**: Choose an appropriate subdivision
3. **Count-in**: Add a sufficient count-in
4. **Bar Numbers**: Bar numbers must be clear

### Streamer Notation

1. **Forward Streamer**: Diagonal line upward
2. **Backward Streamer**: Diagonal line downward
3. **Vertical Line**: Dashed line for the hit point
4. **Pop**: Diamond or asterisk at the hit point

## ⚙️ Level 5: MusicXML Implementation

### XML Tags for Click Track

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
      <!-- Click track metronome -->
      <direction placement="above">
        <direction-type>
          <metronome parentheses="no" font-size="10">
            <beat-unit>quarter</beat-unit>
            <per-minute>120</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="120"/>
      </direction>
    </measure>
    <measure number="2">
      <!-- Count-in notation -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="12" font-weight="bold">1   2   3   4</words>
        </direction-type>
      </direction>
    </measure>
    <measure number="3">
      <!-- Subdivision indicator -->
      <direction placement="above">
        <direction-type>
          <metronome parentheses="yes">
            <beat-unit>quarter</beat-unit>
            <beat-unit-dot/>
            <per-minute>120</per-minute>
          </metronome>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### XML Tags for Streamers

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
      <!-- Forward streamer -->
      <direction placement="above">
        <direction-type>
          <words default-y="15" font-size="8">>>>  </words>
        </direction-type>
      </direction>
    </measure>
    <measure number="2">
      <!-- Vertical line / hit point -->
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="20" font-size="14">HIT</rehearsal>
        </direction-type>
      </direction>
    </measure>
    <measure number="3">
      <!-- Pop marker -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>whole</type>
        <notations>
          <articulations>
            <accent/>
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="4">
      <!-- Streamer words -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-style="italic">forward streamer</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Tempo Changes

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
      <!-- Tempo ramp for gradual change -->
      <direction placement="above">
        <direction-type>
          <metronome>
            <beat-unit>quarter</beat-unit>
            <per-minute>100</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="100"/>
      </direction>
    </measure>
    <measure number="2">
      <!-- Tempo change -->
      <direction placement="above">
        <direction-type>
          <metronome>
            <beat-unit>quarter</beat-unit>
            <per-minute>120</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="120"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Engraving Rules

- **Click track**: Metronome marking must be prominent
- **Streamers**: Use words/direction, not standard notation
- **Hit points**: Rehearsal marks at a large size
- **Bar numbers**: Every bar must have a number
- **Tempo changes**: Clear and prominent

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Streamer not visible | Use a sufficiently high default-y |
| Click track clash | Hide it in the performance score |
| Hit point unclear | Combine rehearsal mark + accent |
| Tempo ramp error | Use a gradual tempo change |

## 📚 References

- **Book**: *On the Track* (Fred Karlin & Rayburn Wright)
- **Book**: *Film Scoring* (Emmanuel Chabrier)
- **Software**: Dorico, Sibelius — Film Scoring Templates
