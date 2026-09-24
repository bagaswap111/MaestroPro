---
title: "Timecode & SMPTE Synchronization"
pillar: "Industrial Workflow & Specialized Applications"
level: "Level 4-5"
xml_tags: ["direction", "words", "rehearsal", "frame"]
related_files: ["Ch3-Film-Scoring-Notation.md", "Ch4-Click-Tracks-Streamers.md"]
---

# Timecode & SMPTE Synchronization

## 📖 Theoretical Concepts (Level 1-3)

SMPTE (Society of Motion Picture and Television Engineers) timecode is the standard for marking time in video and audio.

### Timecode Format

```
HH:MM:SS:FF
│  │  │  │
│  │  │  └── Frame (00-29 for 30fps)
│  │  └───── Second (00-59)
│  └──────── Minute (00-59)
└─────────── Hour (00-23)
```

### Common Frame Rates

| Frame Rate | Used for |
|:---|:---|
| 23.976 fps | Film (NTSC) |
| 24 fps | Film (standard) |
| 25 fps | PAL/SECAM |
| 29.97 fps | NTSC drop-frame |
| 30 fps | HD video |

### Drop-Frame Timecode

Drop-frame timecode compensates for the NTSC frame-rate difference:
- **Non-drop-frame**: Every second = 30 frames
- **Drop-frame**: Skips certain frames for accuracy

## 🎼 Practical Implementation (Level 4)

### Timecode in Film Scoring

1. **Spotting Session**: Determining where music starts/stops
2. **Hit Points**: Important points that must be synced
3. **Streamers**: Visual markers for synchronization
4. **Bar Mapping**: Connecting bars to timecode

### Timecode Conversion

- **TC to Bar**: Use the tempo and time signature
- **Bar to TC**: Calculate based on beats and frames
- **Tempo Mapping**: Adjust tempo for sync

## ⚙️ Level 5: MusicXML Implementation

### XML Tags for Timecode Markers

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
      <!-- Timecode marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="25" font-size="9">TC: 01:02:15:12</words>
        </direction-type>
      </direction>
    </measure>
    <measure number="2">
      <!-- Rehearsal mark with timecode -->
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="30" font-size="14">A (TC: 01:02:15:12)</rehearsal>
        </direction-type>
      </direction>
    </measure>
    <measure number="3">
      <!-- Frame-accurate marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="8">Frame: 1876</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Bar-to-Timecode Mapping

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
      <!-- Bar mapping notation -->
      <direction placement="above">
        <direction-type>
          <words default-y="15" font-size="8">Bar 45 = TC: 01:02:15:12</words>
        </direction-type>
      </direction>
    </measure>
    <measure number="2">
      <!-- Rehearsal mark with bar number -->
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="25" font-size="12">Bar 45</rehearsal>
        </direction-type>
      </direction>
    </measure>
    <measure number="3">
      <!-- Cue marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-style="italic">[Cue: Hit at TC 01:02:15:12]</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### SMPTE Reference

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
      <!-- SMPTE offset marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="30" font-size="8">SMPTE Offset: 01:00:00:00</words>
        </direction-type>
      </direction>
    </measure>
    <measure number="2">
      <!-- Frame rate indicator -->
      <direction placement="above">
        <direction-type>
          <words default-y="25" font-size="8">24 fps</words>
        </direction-type>
      </direction>
    </measure>
    <measure number="3">
      <!-- Hit point with timecode -->
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
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="8">HIT: TC 01:02:15:12</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Engraving Rules

- **Timecode**: Use the format HH:MM:SS:FF
- **Frame rate**: State the frame rate being used
- **Hit points**: Combine timecode + rehearsal marks
- **Bar mapping**: Connect bar numbers with timecode
- **Cue notes**: Add timecode for every cue

### Edge Cases & Troubleshooting

| Problem | Solution |
|:---|:---|
| Timecode clash | Use a different placement |
| Frame-rate confusion | State the frame rate explicitly |
| Sync drift | Use precise tempo markings |
| Drop-frame error | Check the timecode format |

## 📚 References

- **Book**: *On the Track* (Fred Karlin & Rayburn Wright)
- **Book**: *Scoring for Film, TV, and the Internet* (Timothy Brophy)
- **Software**: Pro Tools, Cubase — Timecode integration
