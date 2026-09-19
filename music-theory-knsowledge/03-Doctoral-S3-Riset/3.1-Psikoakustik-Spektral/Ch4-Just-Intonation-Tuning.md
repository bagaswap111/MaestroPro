---
title: "Just Intonation Tuning"
pillar: "Contemporary Harmony, Jazz & Post-Tonal"
level: "Level 4-5"
xml_tags: ["tuning", "pitch", "cents", "frequency"]
related_files: ["Ch1-Teori-Spektral.md", "Ch2-Mikrotonal-Tuning.md"]
---

# Just Intonation Tuning

## 📖 Konsep Teoritis (Level 1-3)

Just Intonation (JI) adalah sistem tuning berdasarkan **frequency ratios** alami dari harmonic series, bukan equal division oktaf seperti Equal Temperament.

### Perbandingan Tuning

| Sistem | Basis | Karakter |
|:---|:---|:---|
| **Equal Temperament** | 12-oktaf divide equal | Versatile, sedikit out of tune |
| **Just Intonation** | Frequency ratios | Pure intervals, limited modulation |
| **Pythagorean** | Perfect 5ths | Bright, sharp 3rds |
| **Meantone** | Narrow 5ths | Pure 3rds, bad keys |

### Common JI Ratios

```
Unison:        1:1      (0 cents)
Minor 2nd:     16:15    (112 cents)
Major 2nd:     9:8      (204 cents)
Minor 3rd:     6:5      (316 cents)
Major 3rd:     5:4      (386 cents)
Perfect 4th:   4:3      (498 cents)
Tritone:       45:32    (590 cents)
Perfect 5th:   3:2      (702 cents)
Minor 6th:     8:5      (814 cents)
Major 6th:     5:3      (884 cents)
Minor 7th:     9:5      (1018 cents)
Major 7th:     15:8     (1088 cents)
Octave:        2:1      (1200 cents)
```

## 🎼 Implementasi Praktis (Level 4)

### Untuk Arranger

1. **Resonance Maximization**: Pilih ratios untuk resonance
2. **Harmonic Clarity**: JI untuk chord yang clear
3. **Timbral Variation**: Ratios mempengaruhi timbre
4. **Microtonal Composition**: Komposisi dengan JI

### Aplikasi Praktis

- **A cappella**: JI natural untuk vokal
- **Gamelan**: Sistem JI tradisional
- **Experimental**: Komposisi contemporary JI
- **Sound Design**: Sound synthesis dengan JI

## ⚙️ Level 5: Implementasi MusicXML

### Tuning Definitions

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
        <!-- Tuning untuk instrumen -->
        <tuning>
          <tuning-step>C</tuning-step>
          <tuning-alter>0</tuning-alter>
          <tuning-octave>4</tuning-octave>
          <cents>0</cents>
        </tuning>
      </attributes>

      <attributes>
        <!-- Custom tuning untuk JI ratio 5:4 (Major 3rd) -->
        <tuning>
          <tuning-step>E</tuning-step>
          <tuning-alter>-14</tuning-alter>
          <tuning-octave>4</tuning-octave>
          <cents>-14</cents>
        </tuning>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

### Cents Deviation

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
      <!-- Cents deviation untuk microtonal -->
      <note>
        <pitch>
          <step>C</step>
          <alter>0</alter>
          <octave>4</octave>
        </pitch>
        <accidental>natural</accidental>
      </note>

      <!-- JI adjustment -->
      <note>
        <pitch>
          <step>E</step>
          <alter>-14</alter>
          <octave>4</octave>
        </pitch>
      </note>

      <!-- Direction dengan cents annotation -->
      <direction placement="below">
        <direction-type>
          <words default-y="-15" font-size="8">-14 cents (JI 5:4)</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Custom Tuning XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <defaults>
    <scaling>
      <millimeters>6.35</millimeters>
      <tenths>40</tenths>
    </scaling>
  </defaults>
  <part-list>
    <score-part id="P1">
      <part-name>Ensemble</part-name>
      <part-abbreviation>Ens</part-abbreviation>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <!-- Per-note tuning -->
        <tuning>
          <tuning-step>G</tuning-step>
          <tuning-alter>2</tuning-alter>
          <tuning-octave>4</tuning-octave>
          <cents>2</cents>
        </tuning>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- **Cents markings**: Harus jelas di bawah atau atas note
- **Ratio annotations**: Gunakan text untuk frequency ratio
- **Tuning brackets**: Tandai section dengan tuning berbeda
- **Accidental system**: Gunakan system yang konsisten
- **Legend**: Cantumkan tuning system di awal partitur

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Cents tidak terbaca | Gunakan ukuran font cukup besar |
| Tuning conflict | Set `<concert-pitch>` untuk referensi |
| Ratio complex | Gunakan decimal notation |
| Multiple tunings | Gunakan staff terpisah atau text markers |

## 📚 Referensi

- **Buku**: *The Structure of Atonal Music* (Allen Forte)
- **Buku**: *Just Intonation Primer* (Neil Haverstick)
- **Jurnal**: *Computer Music Journal* - Tuning systems
