---
title: "Click Tracks & Streamers"
pillar: "Industrial Workflow & Specialized Applications"
level: "Level 4-5"
xml_tags: ["direction", "metronome", "words", "rehearsal"]
related_files: ["Ch3-Film-Scoring-Notation.md", "Ch1-Big-Band-Arranging.md"]
---

# Click Tracks & Streamers

## 📖 Konsep Teoritis (Level 1-3)

Dalam film scoring, **click track** dan **streamer** adalah alat bantu sinkronisasi yang krusial antara musik dengan gambar (picture).

### Click Track

Click track adalah ketukan metronom yang direkam untuk menjaga tempo selama rekaman:
- **Subdivision**: Biasanya 1/4 note atau 1/8 note
- **Tempo**: Ditentukan oleh picture editor
- **Count-in**: Biasanya 2-4 takbir sebelum mulai

### Streamer

Streamer adalah penanda visual dalam partitur yang menunjukkan **hit points** (titik penting):
- **Forward streamer**: Garis diagonal ke atas (menuju hit)
- **Pop": Penanda ketukan tepat di hit point
- **Vertical line**: Garis vertikal untuk synchronization

### Jenis Hit Points

1. **Hard Hit**: Perubahan adegan tiba-tiba
2. **Soft Hit**: Transisi gradual
3. **Bridge**: Titik penghubung antar adegan
4. **In/Out Point**: Awal dan akir scene

## 🎼 Implementasi Praktis (Level 4)

### Click Track Management

1. **Tempo Map**: Buat peta tempo yang presisi
2. **Subdivision**: Pilih subdivisi yang sesuai
3. **Count-in**: Tambahkan count-in yang cukup
4. **Bar Numbers**: Nomor takbir harus jelas

### Streamer Notation

1. **Forward Streamer**: Garis diagonal ke atas
2. **Backward Streamer**: Garis diagonal ke bawah
3. **Vertical Line**: Garis putus-putus untuk hit point
4. **Pop**: Diamond atau asterisk di titik hit

## ⚙️ Level 5: Implementasi MusicXML

### Tag XML untuk Click Track

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

### Tag XML untuk Streamers

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
      <!-- Tempo ramp untuk gradual change -->
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

### Aturan Engraving

- **Click track**: Metronome marking harus prominent
- **Streamers**: Gunakan words/direction, bukan notasi standar
- **Hit points**: Rehearsal marks dengan ukuran besar
- **Bar numbers**: Setiap bar harus ada nomor
- **Tempo changes**: Jelas dan prominent

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Streamer tidak terlihat | Gunakan default-y yang cukup tinggi |
| Click track clash | Sembunyikan di partitur performa |
| Hit point unclear | Kombinasikan rehearsal + accent |
| Tempo ramp error | Gunakan gradual tempo change |

## 📚 Referensi

- **Buku**: *On the Track* (Fred Karlin & Rayburn Wright)
- **Buku**: *Film Scoring* (Emmanuel Chabrier)
- **Software**: Dorico, Sibelius - Template Film Scoring
