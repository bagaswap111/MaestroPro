---
title: "Page & System Breaks"
pillar: "Music Engraving & Typography Mastery"
level: "Level 4-5"
xml_tags: ["print", "new-system", "new-page"]
related_files: ["Ch4-Collision-Avoidance.md", "Ch1-Engraving-Fundamentals.md"]
---

# Page & System Breaks

## 📖 Konsep Teoritis (Level 1-3)

Page dan system breaks mengatur layout partitur dalam halaman.

### System Breaks

- **New System**: Baris baru dalam halaman yang sama
- **System Spacing**: Jarak antar system
- **Staff Grouping**: Pengelompokan staff

### Page Breaks

- **New Page**: Halaman baru
- **Page Margins**: Margin halaman
- **Page Size**: Ukuran kertas

## 🎼 Implementasi Praktis (Level 4)

### Strategic Page Turns

- **Jangan putus frasa**: Halaman baru di akhir frasa
- **Istirahat musisi**: Page turn untuk solo
- **Page turn gap**: Beri jarak untuk balik halaman
- **Rehearsal marks**: Letakkan di awal halaman

## ⚙️ Level 5: Implementasi MusicXML

### New System

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
    <measure number="8">
      <print new-system="yes"/>
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
    </measure>
    <measure number="16">
      <print new-system="yes" spacing="12"/>
    </measure>
  </part>
</score-partwise>
```

### New Page

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
    <measure number="16">
      <print new-page="yes"/>
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
    </measure>
    <measure number="32">
      <print new-page="yes" spacing="15"/>
    </measure>
  </part>
</score-partwise>
```

### Page Layout

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <defaults>
    <page-layout>
      <page-height>1683</page-height>
      <page-width>1190</page-width>
      <page-margins type="both">
        <left-margin>70</left-margin>
        <right-margin>70</right-margin>
        <top-margin>88</top-margin>
        <bottom-margin>88</bottom-margin>
      </page-margins>
    </page-layout>
    <system-layout>
      <system-distance>137</system-distance>
      <top-system-distance>73</top-system-distance>
    </system-layout>
  </defaults>
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
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- **Page turn**: Minimal 2-3 bar sebelum page turn
- **System break**: Di akhir frasa/section
- **Spacing**: Konsisten antar system
- **Margins**: Sama untuk semua halaman

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Page turn terlalu cepat | Tambahkan rest bars |
| System terlalu rapat | Increase system-distance |
| Margin tidak konsisten | Set page-margins eksplisit |
| Layout overflow | Kurangi konten per system |

## 📚 Referensi

- **Buku**: *Behind Bars* (Elaine Gould) - Layout
- **Spesifikasi**: MusicXML print elements
