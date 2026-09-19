---
title: "Score-Timewise vs Score-Partwise"
pillar: "MusicXML Architecture & Computational Music"
level: "Level 4-5"
xml_tags: ["score-partwise", "score-timewise", "part", "measure"]
related_files: ["Ch1-Struktur-Root-Partwise.md", "Ch6-Duration-Rhythm-Encoding.md"]
---

# Score-Timewise vs Score-Partwise

## 📖 Konsep Teoritis (Level 1-3)

MusicXML memiliki dua format root element: **Score-Partwise** dan **Score-Timewise**. Pemilihan format mempengaruhi cara data musik diorganisir.

### Score-Partwise

Format yang mengorganisir data berdasarkan **part** terlebih dahulu:

```xml
<score-partwise>
  <part-list>...</part-list>
  <part id="P1">
    <measure number="1">...</measure>
    <measure number="2">...</measure>
  </part>
  <part id="P2">
    <measure number="1">...</measure>
    <measure number="2">...</measure>
  </part>
</score-partwise>
```

**Karakteristik:**
- Part adalah level teratas
- Setiap part berisi semua measures
- Ideal untuk part individual
- Format default kebanyakan software

### Score-Timewise

Format yang mengorganisir data berdasarkan **measure** terlebih dahulu:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<part-list>...</part-list>
  <part id="P1">
    <measure number="1">
      ...
    </measure>
    <measure number="2">
      ...
    </measure>
  </part>
  <part id="P2">
    <measure number="1">
      ...
    </measure>
    <measure number="2">
      ...
    </measure>
  </part>
</score-partwise>
```

**Karakteristik:**
- Measure adalah level teratas
- Setiap measure berisi semua parts
- Ideal untuk analisis simultan
- Berguna untuk comparison parts

## 🎼 Implementasi Praktis (Level 4)

### Kapan Menggunakan Partwise

1. **Part Extraction**: Ekstrak part individual
2. **Part Processing**: Proses per-part
3. **Score Editing**: Editing partitur
4. **Export per Part**: Export per instrumen

### Kapan Menggunakan Timewise

1. **Score Analysis**: Analisis simultan
2. **Comparison**: Perbandingan parts
3. **Beat Analysis**: Analisis per ketukan
4. **Synchronization**: Sinkronisasi parts

## ⚙️ Level 5: Implementasi MusicXML

### Struktur Score-Partwise

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC
  "-//Recordare//DTD MusicXML 4.0 Partwise//EN"
  "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <work>
    <work-title>Contoh Partwise</work-title>
  </work>
  <identification>
    <creator type="composer">Composer Name</creator>
  </identification>
  <part-list>
    <score-part id="P1">
      <part-name>Violin I</part-name>
      <part-abbreviation>Vln. I</part-abbreviation>
    </score-part>
    <score-part id="P2">
      <part-name>Violin II</part-name>
      <part-abbreviation>Vln. II</part-abbreviation>
    </score-part>
  </part-list>
  
  <!-- Part 1: Violin I -->
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
  
  <!-- Part 2: Violin II -->
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>G</step><octave>3</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Struktur Score-Timewise

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
<part-list>
    <score-part id="P1">
      <part-name>Violin I</part-name>
    </score-part>
    <score-part id="P2">
      <part-name>Violin II</part-name>
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
      <note>
      <pitch><step>C</step><octave>4</octave></pitch>
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
      <note>
      <pitch><step>G</step><octave>3</octave></pitch>
      <duration>4</duration>
      <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Konversi dengan Python music21

```python
import music21

# Baca partwise
score = music21.converter.parse('partwise.xml')

# Konversi ke timewise
timewise = score.toTimewise()

# Atau sebaliknya
partwise = timewise.toPartwise()
```

### Aturan Engraving

- **Partwise**: Default untuk export
- **Timewise**: Untuk analisis
- **Part-list**: Harus identik di kedua format
- **Measure numbers**: Harus konsisten
- **Attributes**: Harus di setiap part/measure pertama

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Part tidak terbaca | Periksa part-list |
| Measure tidak sinkron | Gunakan timewise untuk verify |
| Export gagal | Gunakan partwise untuk export |
| Import error | Konversi ke format yang benar |

## 📚 Referensi

- **Spesifikasi**: MusicXML 4.0 Standard
- **DTD**: partwise.dtd dan timewise.dtd
- **Tool**: music21 Python library
