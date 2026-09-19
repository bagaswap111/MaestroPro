---
title: "Twelve-Tone Serialism"
pillar: "Contemporary Harmony, Jazz & Post-Tonal"
level: "Level 4-5"
xml_tags: ["accidental", "pitch", "alter", "key-accidental"]
related_files: ["Ch1-Chord-Scale-Theory.md", "Ch3-Harmoni-PostTonal.md"]
---

# Twelve-Tone Serialism

## 📖 Konsep Teoritis (Level 1-3)

Twelve-Tone Serialism (Dodecaphony) dikembangkan oleh Arnold Schock pada tahun 1920-an. Sistem ini menggunakan **tone row** - urutan 12 nada chromatic yang tidak berulang sebagai dasar komposisi.

### Tone Row Construction

Tone row memiliki 4 bentuk dasar:
1. **Prime (P)**: Bentuk asli
2. **Inversion (I)**: Cermin vertikal
3. **Retrograde (R)**: Urutan terbalik
4. **Retrograde Inversion (RI)**: Cermin + terbalik

### Matrix (Magic Square)

Matrix digunakan untuk menghitung semua transformasi tone row:
- Baris = Prime (P0-P11)
- Kolom = Inversion (I0-I11)
- Diagonal = Retrograde

### Principles of Serialism

1. **No Repetition**: Tidak ada nada yang diulang dalam urutan
2. **Chromatic Completion**: Semua 12 nada harus muncul
3. **Interval Invariance**: Interval antar nada dipertahankan
4. **Row Partitioning**: Tone row bisa dibagi untuk kebutuhan tekstural

## 🎼 Implementasi Praktis (Level 4)

### Untuk Arranger/Composer

1. **Structural Foundation**: Tone row sebagai dasar harmoni
2. **Melodic Generation**: Transformasi untuk melodi
3. **Harmonic Language**: Chord dari tone row
4. **Rhythmic Independence**: Rhythm tidak terikat serial

### Teknik Orkestrasi

- **Voice Exchange**: Distribusi tone row ke instrumen
- **Klangfarbenmelodie**: Color melody melalui timbre
- **Row Partitioning**: Bagi tone row untuk multiple instruments
- **Density Control**: Atur jumlah instrumen aktif

## ⚙️ Level 5: Implementasi MusicXML

### Tag XML untuk Tone Row

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
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <!-- Tone row Prime -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
      </note>
      <!-- ... 12 notes total -->
      
      <!-- Row form marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9">P-0</words>
        </direction-type>
      </direction>
      
      <!-- Interval marking -->
      <direction placement="below">
        <direction-type>
          <words default-y="-15" font-size="8">+4, -6, +5...</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
``

### Explicit Accidentals untuk Atonal

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
      <!-- Setiap nada membutuhkan accidental eksplisit -->
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <accidental>natural</accidental>
      </note>
      
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <accidental>natural</accidental>
      </note>
      
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <accidental>flat</accidental>
      </note>
      
      <!-- Atonal key signature (kosong) -->
      <attributes>
        <key>
          <key-accidental slash="yes"/>
          <key-step>A</key-step>
        </key>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

### Row Form Markers

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
      <!-- P (Prime) -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-weight="bold">P-0</words>
        </direction-type>
      </direction>
      
      <!-- I (Inversion) -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-weight="bold">I-5</words>
        </direction-type>
      </direction>
      
      <!-- R (Retrograde) -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-weight="bold">R-3</words>
        </direction-type>
      </direction>
      
      <!-- RI (Retrograde Inversion) -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="9" font-weight="bold">RI-7</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- **Atonal context**: Tidak ada key signature, semua accidentals eksplisit
- **Cautionary accidentals**: Gunakan untuk keterbacaan
- **Row form markers**: Gunakan text annotations untuk analisis
- **Voice leading**: Pertahankan meskipun atonal
- **Beaming**: Ikuti aturan ritmik standar

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Accidental ambiguity | Gunakan natural sebelum flat/sharp |
| Row form tidak terlihat | Tambahkan text annotation eksplisit |
| Enharmonic confusion | Konsisten dalam pemilihan enharmonic |
| Playback incorrect | Set `<concert-pitch>` jika diperlukan |

## 📚 Referensi

- **Buku**: *Twelve-Tone Serialism* (George Perle)
- **Buku**: *The Structure of Atonal Music* (Allen Forte)
- **Buku**: *Introduction to Twelve-Tone Theory* (George Perle)
