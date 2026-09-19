---
title: "Timecode & SMPTE Synchronization"
pillar: "Industrial Workflow & Specialized Applications"
level: "Level 4-5"
xml_tags: ["direction", "words", "rehearsal", "frame"]
related_files: ["Ch3-Film-Scoring-Notation.md", "Ch4-Click-Tracks-Streamers.md"]
---

# Timecode & SMPTE Synchronization

## 📖 Konsep Teoritis (Level 1-3)

SMPTE (Society of Motion Picture and Television Engineers) timecode adalah standar untuk menandai waktu dalam video dan audio.

### Format Timecode

```
HH:MM:SS:FF
│  │  │  │
│  │  │  └── Frame (00-29 untuk 30fps)
│  │  └───── Second (00-59)
│  └──────── Minute (00-59)
└─────────── Hour (00-23)
```

### Frame Rates Umum

| Frame Rate | Digunakan untuk |
|:---|:---|
| 23.976 fps | Film (NTSC) |
| 24 fps | Film (standar) |
| 25 fps | PAL/SECAM |
| 29.97 fps | NTSC drop-frame |
| 30 fps | Video HD |

### Drop-Frame Timecode

Drop-frame timecode mengkompensasi perbedaan frame rate NTSC:
- **Non-drop-frame**: Setiap detik = 30 frame
- **Drop-frame**: Skip frame tertentu untuk akurasi

## 🎼 Implementasi Praktis (Level 4)

### Timecode dalam Film Scoring

1. **Spotting Session**: Menentukan tempat musik mulai/berhenti
2. **Hit Points**: Titik-titik penting yang harus di-sync
3. **Streamers**: Penanda visual untuk sinkronisasi
4. **Bar Mapping**: Menghubungkan bar dengan timecode

### Konversi Timecode

- **TC ke Bar**: Gunakan tempo dan time signature
- **Bar ke TC**: Hitung berdasarkan beat dan frame
- **Tempo Mapping**: Sesuaikan tempo untuk sync

## ⚙️ Level 5: Implementasi MusicXML

### Tag XML untuk Timecode Markers

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
      <!-- Rehearsal mark dengan timecode -->
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
      <!-- Rehearsal mark dengan bar number -->
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
      <!-- Hit point dengan timecode -->
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

### Aturan Engraving

- **Timecode**: Gunakan format HH:MM:SS:FF
- **Frame rate**: Cantumkan frame rate yang digunakan
- **Hit points**: Kombinasikan timecode + rehearsal marks
- **Bar mapping**: Hubungkan bar number dengan timecode
- **Cue notes**: Tambahkan timecode untuk setiap cue

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Timecode clash | Gunakan placement yang berbeda |
| Frame rate confusion | Cantumkan frame rate secara eksplisit |
| Sync drift | Gunakan tempo marking yang presisi |
| Drop-frame error | Periksa format timecode |

## 📚 Referensi

- **Buku**: *On the Track* (Fred Karlin & Rayburn Wright)
- **Buku**: *Scoring for Film, TV, and the Internet* (Timothy Brophy)
- **Software**: Pro Tools, Cubase - Timecode integration
