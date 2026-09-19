---
title: "Colotomic Structure (Gamelan)"
pillar: "Ethnomusicology & Non-Western Systems"
level: "Level 4-5"
xml_tags: ["rehearsal", "barline", "measure", "direction"]
related_files: ["Ch1-Gamelan.md", "Ch4-Kotekan-Interlocking.md"]
---

# Colotomic Structure (Gamelan)

## 📖 Konsep Teoritis (Level 1-3)

Colotomic structure adalah prinsip organisasi musik dalam Gamelan, di mana instrumen berbeda menandai siklus waktu yang berbeda.

### Hierarki Instrumen

```
Gong Ageng (paling rendah, paling lambat)
├── Kempur (menengah)
├── Kenong (cepat)
├── Kempli (pulse)
└── Saron/Demung (melodi utama)
```

### Siklus Colotomic

```
Gong:  |X . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|
Kempur:|X . . . . . . . . . . . . . . . . X . . . . . . . . . . . . .|
Kenong:|X . . . . . . . . X . . . . . . . X . . . . . . . . X . . . .|
Kempli:|X . X . X . X . X . X . X . X . X . X . X . X . X . X . X . X|
```

### Fungsi Colotomic

1. **Structural Marker**: Menandai struktur siklus
2. **Temporal Framework**: Memberikan kerangka waktu
3. **Hierarchical Organization**: Organisasi hierarkis
4. **Ceremonial Function**: Fungsi upacara

## 🎼 Implementasi Praktis (Level 4)

### Notasi Gamelan

- **Numbered Notation**: Angka untuk pitch
- **Colotomic Markers**: X untuk ketukan
- **Cyclical Notation**: Siklus berulang
- **Kotekan Parts**: Parts untuk interlocking

### Arranging untuk Orkestra

- Distribusi colotomic ke instrumen Barat
- Simulasi gong dengan bass drum/timpani
- Kenong dengan tenor drums
- Kempli dengan snare/triangle

## ⚙️ Level 5: Implementasi MusicXML

### Gong Cycle Markers

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Gong Ageng</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Gong</instrument-name>
        <instrument-sound>pitched.metal</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>0</midi-program>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>Percussion</sign><line>2</line></clef>
      </attributes>
      <!-- Gong ageng - structural marker -->
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="30" font-size="16" font-weight="bold">GONG</rehearsal>
        </direction-type>
      </direction>

      <!-- Kenong marker -->
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="25" font-size="12">K</rehearsal>
        </direction-type>
      </direction>

      <!-- Colotomic cycle notation -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9">Siklus 1</words>
        </direction-type>
      </direction>

      <note>
        <rest/>
        <duration>16</duration>
        <type>whole</type>
      </note>

      <!-- Heavy barline untuk gong -->
      <barline location="right">
        <bar-style>heavy-light</bar-style>
      </barline>
    </measure>
  </part>
</score-partwise>
```

### Rehearsal Marks untuk Colotomic

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Gong Ageng</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Gong</instrument-name>
        <instrument-sound>pitched.metal</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>0</midi-program>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>Percussion</sign><line>2</line></clef>
      </attributes>
      <note>
        <rest/>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
    <!-- Gong cycle boundary -->
    <measure number="2">
      <attributes>
        <divisions>4</divisions>
      </attributes>
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="35" font-size="18" enclosure="rectangle">G</rehearsal>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>16</duration>
        <type>whole</type>
        <notations>
          <fermata type="upright"/>
        </notations>
      </note>
    </measure>

    <!-- Kenong subdivisions -->
    <measure number="3">
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="25" font-size="12">Kenong</rehearsal>
        </direction-type>
      </direction>
      <note>
        <rest/>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Barline Styles untuk Colotomic

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Gong Ageng</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Gong</instrument-name>
        <instrument-sound>pitched.metal</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>0</midi-program>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>Percussion</sign><line>2</line></clef>
      </attributes>
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <!-- Regular barline -->
      <barline location="right">
        <bar-style>regular</bar-style>
      </barline>
    </measure>
    <measure number="2">
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <!-- Heavy-light untuk siklus besar -->
      <barline location="right">
        <bar-style>heavy-light</bar-style>
      </barline>
    </measure>
    <measure number="3">
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <!-- Double barline untuk subdivisi -->
      <barline location="right">
        <bar-style>light-light</bar-style>
      </barline>
    </measure>
    <measure number="4">
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <!-- Dashed untuk structural analysis -->
      <barline location="right">
        <bar-style>dashed</bar-style>
      </barline>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- **Gong markers**: Gunakan rehearsal marks besar
- **Colotomic notation**: Konsisten untuk setiap siklus
- **Barline styles**: Bedakan untuk level berbeda
- **Rehearsal letters**: Untuk setiap gong cycle
- **System breaks**: Pada gong cycle boundary

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Gong marker tidak prominent | Gunakan font size lebih besar |
| Colotomic confusion | Tambahkan numbering |
| Barline clash | Gunakan barline yang tepat |
| Cycle boundary unclear | Kombinasikan rehearsal + barline |

## 📚 Referensi

- **Buku**: *The Gamelan* (Sutton)
- **Buku**: *Music in Java* (Jaap Kunst)
- **Audio**: Recording Gamelan Jawa dan Bali