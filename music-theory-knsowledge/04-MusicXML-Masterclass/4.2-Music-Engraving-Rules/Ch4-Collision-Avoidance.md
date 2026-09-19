---
title: "Collision Avoidance"
pillar: "Music Engraving & Typography Mastery"
level: "Level 4-5"
xml_tags: ["direction", "offset", "default-y", "position"]
related_files: ["Ch1-Engraving-Fundamentals.md", "Ch5-Page-System-Breaks.md"]
---

# Collision Avoidance

## 📖 Konsep Teoritis (Level 1-3)

Collision avoidance adalah teknik untuk mencegah tumpang tindih antar elemen notasi dalam partitur.

### Jenis Collision

1. **Note-Note Collision**: Nada yang tumpang tindih
2. **Note-Articulation**: Nada dengan artikulasi
3. **Note-Lyrics**: Nada dengan teks
4. **Dynamics-Notes**: Dinamika dengan nada
5. **Ledger Lines**: Garis bantu yang tumpang tindih

### Faktor yang Mempengaruhi

- **Interval Distance**: Jarak antar nada
- **Stem Direction**: Arah stem
- **Beam Position**: Posisi beam
- **Articulation Placement**: Posisi artikulasi

## 🎼 Implementasi Praktis (Level 4)

### Teknik Collision Avoidance

1. **Horizontal Offset**: Geser elemen horizontal
2. **Vertical Offset**: Geser elemen vertikal
3. **Stem Direction**: Ubah arah stem
4. **Beam Grouping**: Kelompokkan beam
5. **Ledger Lines**: Atur panjang ledger lines

### Aturan untuk Berbagai Elemen

- **Second intervals**: Gunakan offset horizontal
- **Chord collisions**: Pisahkan noteheads
- **Artikulasi**: Letakkan di luar notehead
- **Lyrics**: Letakkan di bawah staff

## ⚙️ Level 5: Implementasi MusicXML

### Horizontal Offset

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
      <!-- Offset untuk collision avoidance -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <offset>-1</offset>
      </note>
      <!-- Direction dengan offset -->
      <direction placement="above">
        <direction-type>
          <words default-y="20">f</words>
        </direction-type>
        <offset>2</offset>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Vertical Offset

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
      <!-- Default-y untuk vertical positioning -->
      <direction placement="above">
        <direction-type>
          <words default-y="25" font-size="12">ff</words>
        </direction-type>
      </direction>
      <!-- Dynamics dengan offset -->
      <direction placement="below">
        <direction-type>
          <dynamics default-y="-20">
            <f/>
          </dynamics>
        </direction-type>
      </direction>
      <!-- Artikulasi dengan offset -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <articulations>
            <accent default-y="5"/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Stem Direction

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
      <!-- Stem up untuk menghindari collision -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <stem>up</stem>
      </note>
      <!-- Stem down untuk menghindari collision -->
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <stem>down</stem>
      </note>
      <!-- Voice direction untuk multi-voice -->
      <note>
        <voice>1</voice>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <stem>up</stem>
      </note>
      <note>
        <voice>2</voice>
        <pitch>
          <step>E</step>
          <octave>4</octave>
        </pitch>
        <stem>down</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Ledger Lines

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
      <!-- Ledger lines dengan offset -->
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <ledger-lines>3</ledger-lines>
        </notations>
      </note>
      <!-- Octave shift untuk high/low notes -->
      <direction placement="above">
        <direction-type>
          <octave-shift type="down" size="8"/>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- **Minimum distance**: 1 spasi antar elemen
- **Offset values**: Gunakan dalam satuan tenths
- **Default-y**: Untuk positioning vertikal
- **Stem direction**: Ikuti aturan stem
- **Ledger lines**: Panjang yang tepat

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Note overlap | Gunakan horizontal offset |
| Artikulasi clash | Gunakan vertical offset |
| Lyrics terlalu dekat | Tambahkan spacing |
| Ledger lines panjang | Gunakan octave shift |

## 📚 Referensi

- **Buku**: *Behind Bars* (Elaine Gould) - Collision avoidance
- **Spesifikasi**: MusicXML offset elements
- **Software**: Dorico/Sibelius - Auto collision avoidance
