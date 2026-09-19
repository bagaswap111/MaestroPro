---
title: "Kotekan & Interlocking Patterns"
pillar: "Ethnomusicology & Non-Western Systems"
level: "Level 4-5"
xml_tags: ["note", "voice", "beam", "tuplet", "articulation"]
related_files: ["Ch1-Gamelan.md", "Ch3-Colotomic-Structure.md"]
---

# Kotekan & Interlocking Patterns

## 📖 Konsep Teoritis (Level 1-3)

Kotekan adalah teknik interlocking pattern dalam musik Gamelan Bali, di mana dua atau lebih instrumen memainkan pola yang saling melengkapi untuk menghasilkan melodi cepat yang tidak bisa dimainkan satu instrumen.

### Pola Interlocking

```
Polos (dasar):    X . X . X . X . X . X . X . X . X .
Sangsih (tanggung): . X . X . X . X . X . X . X . X . X
Resultant:        X X X X X X X X X X X X X X X X X X
```

### Jenis Kotekan

1. **Kotekan Reong**: Pola untuk instrumen reong
2. **Kotekan Gangsa**: Pola untuk gangsa
3. **Kotekan Ceng-Ceng**: Pola untuk ceng-ceng
4. **Kotekan Saron**: Pola untuk saron

### Prinsip Interlocking

- **Complementary**: Pola saling melengkapi
- **Even Distribution**: Pembagian merata
- **Speed**: Menghasilkan kecepatan tinggi
- **Precision**: Ketepatan ritmis sangat penting

## 🎼 Implementasi Praktis (Level 4)

### Notasi Interlocking

- **Two-voice notation**: Notasi dua suara
- **Single-line resultant**: Hasil gabungan
- **Practice parts**: Parts untuk latihan
- **Score layout**: Layout untuk ensemble

### Orkestrasi Interlocking

- Distribusi ke instrumen berbeda
- Pemilihan register yang kontras
- Dynamic balance antar parts
- Articulation yang konsisten

## ⚙️ Level 5: Implementasi MusicXML

### Two-Voice Interlocking

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Polos</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Gangsa</instrument-name>
        <instrument-sound>pitched.metal</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>0</midi-program>
      </midi-instrument>
    </score-part>
    <score-part id="P2">
      <part-name>Sangsih</part-name>
      <score-instrument id="P2-I1">
        <instrument-name>Gangsa</instrument-name>
        <instrument-sound>pitched.metal</instrument-sound>
      </score-instrument>
      <midi-instrument id="P2-I1">
        <midi-channel>2</midi-channel>
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
        <clef><sign>G</sign><line>2</line></clef>
        <staves>2</staves>
      </attributes>
      <!-- Interlocking pattern: Polos -->
      <note>
        <voice>1</voice>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>2</duration>
        <type>eighth</type>
        <stem>up</stem>
        <beam number="1">begin</beam>
      </note>
      <note>
        <voice>1</voice>
        <rest/>
        <duration>2</duration>
        <type>eighth</type>
        <stem>up</stem>
        <beam number="1">end</beam>
      </note>
      <note>
        <voice>1</voice>
        <rest/>
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
      <!-- Interlocking pattern: Sangsih -->
      <note>
        <voice>2</voice>
        <rest/>
        <duration>2</duration>
        <type>eighth</type>
        <stem>down</stem>
      </note>
      <note>
        <voice>2</voice>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>2</duration>
        <type>eighth</type>
        <stem>down</stem>
        <beam number="1">begin</beam>
      </note>
      <note>
        <voice>2</voice>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Multi-Part Interlocking

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <!-- Part list untuk interlocking -->
  <part-list>
    <score-part id="P1">
      <part-name>Polos</part-name>
      <part-abbreviation>Pol</part-abbreviation>
      <score-instrument id="P1-I1">
        <instrument-name>Gangsa</instrument-name>
        <instrument-sound>pitched.metal</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>0</midi-program>
      </midi-instrument>
    </score-part>
    <score-part id="P2">
      <part-name>Sangsih</part-name>
      <part-abbreviation>San</part-abbreviation>
      <score-instrument id="P2-I1">
        <instrument-name>Gangsa</instrument-name>
        <instrument-sound>pitched.metal</instrument-sound>
      </score-instrument>
      <midi-instrument id="P2-I1">
        <midi-channel>2</midi-channel>
        <midi-program>0</midi-program>
      </midi-instrument>
    </score-part>
  </part-list>

  <!-- Polos part -->
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>2</duration>
        <type>eighth</type>
      </note>
      <note>
        <rest/>
        <duration>2</duration>
        <type>eighth</type>
      </note>
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>

  <!-- Sangsih part -->
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <rest/>
        <duration>2</duration>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>2</duration>
        <type>eighth</type>
      </note>
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Beaming untuk Interlocking

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Polos</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Gangsa</instrument-name>
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
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <!-- Fast interlocking dengan beaming -->
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>1</duration>
        <type>16th</type>
        <stem>up</stem>
        <beam number="1">begin</beam>
        <beam number="2">begin</beam>
      </note>
      <note>
        <rest/>
        <duration>1</duration>
        <type>16th</type>
        <stem>up</stem>
        <beam number="1">end</beam>
        <beam number="2">end</beam>
      </note>
      <note>
        <rest/>
        <duration>6</duration>
        <type>eighth</type>
      </note>

      <!-- Articulation untuk precision -->
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>1</duration>
        <type>16th</type>
        <stem>up</stem>
        <notations>
          <articulations>
            <staccatissimo/>
          </articulations>
        </notations>
      </note>
      <note>
        <rest/>
        <duration>3</duration>
        <type>16th</type>
      </note>
      <note>
        <rest/>
        <duration>8</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- **Voice separation**: Gunakan stem direction berbeda
- **Beaming**: Konsisten untuk interlocking
- **Articulation**: Staccato untuk clarity
- **Part layout**: Terpisah untuk practice
- **Resultant melody**: Tandai sebagai guide

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Voice clash | Gunakan stem direction berbeda |
| Beaming rancu | Pisahkan beaming per voice |
| Tempo terlalu cepat | Kurangi note value |
| Precision rendah | Tambahkan articulations |

## 📚 Referensi

- **Buku**: *Gamelan Bali* (Michael Tenzer)
- **Buku**: *Music of Indonesia* (Sumarsam)
- **Video**: Performance Gamelan Bali