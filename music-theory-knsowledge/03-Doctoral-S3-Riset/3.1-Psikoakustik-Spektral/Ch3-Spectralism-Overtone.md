---
title: "Spectralism & Overtone-Based Composition"
pillar: "Contemporary Harmony, Jazz & Post-Tonal"
level: "Level 4-5"
xml_tags: ["harmonic", "natural", "base-pitch", "partial", "microtonal"]
related_files: ["Ch1-Teori-Spektral.md", "Ch2-Mikrotonal-Tuning.md"]
---

# Spectralism & Overtone-Based Composition

## 📖 Konsep Teoritis (Level 1-3)

Spectralism adalah aliran komposisi yang dikembangkan oleh **Gérard Grisey** dan **Tristan Murail** di IRCAM pada tahun 1970-80an. Musik didasarkan pada **overtone series** (deret harmonik) sebagai sumber material harmonis dan melodis.

### Harmonic Series

```
Overtone:  1    2    3    4    5    6    7    8
Pitch:     C    C    G    C    E    G    Bb   C
Interval:  P8   P8   P5   P4   M3   m3   ~m3  P8
Cents:     0    1200 1902 2400 2786 3156 3437 3600
```

### Prinsip Spektral

1. **Timbre as Harmony**: Chord dari partial numbers
2. **Spectral Scale**: Skala dari overtone frequencies
3. **Morphing**: Transformasi gradual antar spektrum
4. **Resonance**: Simulasi resonansi alami

### Komponen Utama

- **Grisey**: *Partiels*, *Les espaces acoustiques*
- **Murail**: *Voyage*, *Les courants de l'espace*
- **Saariaho**: *L'amour de loin*

## 🎼 Implementasi Praktis (Level 4)

### Untuk Orkestrasi

1. **Harmonic Orchestration**: Distribusi partial ke instrumen
2. **Spectral Chords**: Akor dari harmonic series
3. **Morphing Orchestration**: Transformasi timbre gradual
4. **Resonance Simulation**: Imitasi resonansi ruangan

### Teknik Komposisi

- **Overtone Chord**: C-G-E-Bb dari partial 1-3-5-7
- **Spectral Scale**: Scale berdasarkan frequency ratios
- **Timbre Melody**: Melodi dari perubahan spektrum
- **Microtonal Tuning**: Tuning berdasarkan harmonic series

## ⚙️ Level 5: Implementasi MusicXML

### Tag XML untuk Harmonic Series

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
      <!-- Natural harmonics -->
      <note>
        <pitch>
          <step>A</step>
          <octave>4</octave>
        </pitch>
        <notations>
          <technical>
            <harmonic>
              <natural/>
              <base-pitch/>
            </harmonic>
          </technical>
        </notations>
      </note>

      <!-- Partial number notation -->
      <direction placement="above">
        <direction-type>
          <words default-y="15" font-size="8">Partial 5</words>
        </direction-type>
      </direction>

      <!-- Harmonic with sounding pitch -->
      <note>
        <pitch>
          <step>E</step>
          <octave>5</octave>
        </pitch>
        <notations>
          <technical>
            <harmonic>
              <natural/>
              <sounding-pitch/>
            </harmonic>
          </technical>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Microtonal Accidentals

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
      <!-- Quarter-tone sharp -->
      <note>
        <pitch>
          <step>C</step>
          <alter>0.5</alter>
          <octave>4</octave>
        </pitch>
        <accidental>quarter-sharp</accidental>
      </note>

      <!-- Three-quarter-tone flat -->
      <note>
        <pitch>
          <step>D</step>
          <alter>-0.75</alter>
          <octave>4</octave>
        </pitch>
        <accidental>three-quarters-flat</accidental>
      </note>

      <!-- Custom microtonal accidental -->
      <note>
        <pitch>
          <step>F</step>
          <alter>0.33</alter>
          <octave>4</octave>
        </pitch>
        <accidental>
          <accidental-mark smufl="accidentalQuarterToneSharp2ArrowUp"/>
        </accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Spectral Annotation

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
      <!-- Spectral analysis marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="25" font-size="9" font-style="italic">Spectral chord: partials 1-3-5-7</words>
        </direction-type>
      </direction>

      <!-- Frequency ratio notation -->
      <direction placement="below">
        <direction-type>
          <words default-y="-15" font-size="8">Ratio: 1:3:5:7</words>
        </direction-type>
      </direction>

      <!-- Timbre morphing marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-size="8">Morph: Bright → Dark</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- Gunakan **diamond notehead** untuk harmonics
- **Partial numbers** harus jelas di atas nota
- **Microtonal accidentals**: Gunakan SMUFL glyphs
- **Frequency annotations**: Letakkan di bawah staff
- **Spectral markings**: Gunakan italic font

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Diamond notehead tidak muncul | Gunakan `smufl="noteheadDiamond"` |
| Microtonal tidak terbaca | Eksplisitkan cents value |
| Partial number salah | Verifikasi dengan harmonic series calculator |
| Spectral chord complex | Gunakan multi-staff notation |

## 📚 Referensi

- **Buku**: *The Computer Music Tutorial* (Curtis Roads)
- **Buku**: *Temporal Sound and Spectra* (Gérard Grisey)
- **Jurnal**: *Computer Music Journal* - Spectral music articles
