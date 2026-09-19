---
title: "Maqam Ornamentation"
pillar: "Ethnomusicology & Non-Western Systems"
level: "Level 4-5"
xml_tags: ["ornament", "grace", "trill", "mordent", "glissando"]
related_files: ["Ch2-Maqam-Raga.md", "Ch3-Colotomic-Structure.md"]
---

# Maqam Ornamentation

## 📖 Konsep Teoritis (Level 1-3)

Maqam adalah sistem modal dalam musik Arab yang memiliki karakter unik melalui **ornamentation** (hiasan) yang khas.

### Karakteristik Maqam

| Maqam | Interval Khas | Karakter |
|:---|:---|:---|
| **Bayati** | 3/4 tone | Romantis, penuh perasaan |
| **Hijaz** | Augmented 2nd | Timur Tengah, eksotis |
| **Rast** | 3/4 tone | Ceria, energik |
| **Saba** | Microtonal | Sedih, merintih |

### Jenis Ornamentation

1. **Mordent**: Nada cepat di atas/bawah
2. **Trill**: Getar cepat antar nada
3. **Glissando**: Perpindahan gradual
4. **Grace Notes**: Nada hias pendek
5. **Tremolo**: Pengulangan cepat

### Fungsi Ornamentation

- **Emotional Expression**: Ekspresi emosional
- **Melodic Elaboration**: Pengembangan melodi
- **Rhythmic Interest**: Variasi ritmis
- **Stylistic Identity**: Identitas gaya

## 🎼 Implementasi Praktis (Level 4)

### Ornament untuk Vokal

- **Melismatic**: Banyak nada per suku kata
- **Portamento**: Slide antar nada
- **Vibrato**: Getar nada
- **Crescendo/Decrescendo**: Dinamika

### Ornament untuk Instrumen

- **String**: Vibrato, glissando, harmonics
- **Woodwind**: Trills, mordents
- **Brass**: Falls, doits
- **Percussion**: Rolls, flams

## ⚙️ Level 5: Implementasi MusicXML

### Grace Notes

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Oud</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Oud</instrument-name>
        <instrument-sound>plucked.string</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>21</midi-program>
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
      <!-- Grace notes untuk maqam -->
      <note>
        <grace/>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>1</duration>
        <type>16th</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>

      <!-- Grace note dengan slash -->
      <note>
        <grace slash="yes"/>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>1</duration>
        <type>16th</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>

      <!-- Multiple grace notes -->
      <note>
        <grace/>
        <pitch>
          <step>E</step>
          <octave>5</octave>
        </pitch>
        <duration>1</duration>
        <type>32nd</type>
      </note>
      <note>
        <grace/>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>1</duration>
        <type>32nd</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
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

### Trills dan Mordents

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Oud</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Oud</instrument-name>
        <instrument-sound>plucked.string</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>21</midi-program>
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
      <!-- Trill -->
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <ornaments>
            <trill-mark/>
          </ornaments>
        </notations>
      </note>

      <!-- Mordent -->
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <ornaments>
            <mordent/>
          </ornaments>
        </notations>
      </note>

      <!-- Inverted mordent -->
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <ornaments>
            <inverted-mordent/>
          </ornaments>
        </notations>
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

### Glissando dan Portamento

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Oud</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Oud</instrument-name>
        <instrument-sound>plucked.string</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>21</midi-program>
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
      <!-- Glissando naik -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <glissando type="up" line-type="wavy"/>
        </notations>
      </note>

      <!-- Glissando turun -->
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <glissando type="down" line-type="wavy"/>
        </notations>
      </note>

      <!-- Portamento -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <slide type="up"/>
        </notations>
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

### Custom Ornaments

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Oud</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Oud</instrument-name>
        <instrument-sound>plucked.string</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>21</midi-program>
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
      <!-- Custom ornament dengan text -->
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <ornaments>
            <accidental-mark placement="above"/>
          </ornaments>
        </notations>
      </note>

      <!-- Tremolo -->
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
        <notations>
          <tremolo type="start" repetitions="4"/>
        </notations>
      </note>

      <!-- Custom text untuk maqam ornament -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-style="italic">Tahrir</words>
        </direction-type>
      </direction>

      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>4</duration>
        <type>quarter</type>
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

### Aturan Engraving

- **Grace notes**: Ukuran lebih kecil dari note utama
- **Ornaments**: Letakkan di atas note
- **Glissando**: Garis wavy atau straight
- **Portamento**: Garis dengan slide
- **Custom ornaments**: Gunakan text annotations

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Grace note tidak muncul | Gunakan `<grace/>` sebelum note |
| Trill tidak jelas | Tambahkan accidental pada trill |
| Glissando putus | Pastikan note connectivity |
| Ornament clash | Atur placement dengan hati-hati |

## 📚 Referensi

- **Buku**: *Maqam World* (Perry)
- **Buku**: *Arabic Music* (Maqam)
- **Audio**: Performance musik Arab tradisional