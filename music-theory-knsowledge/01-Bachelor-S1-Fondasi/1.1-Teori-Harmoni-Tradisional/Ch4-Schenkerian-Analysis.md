---
title: "Schenkerian Analysis & Tonal Prolongation"
pillar: "Deep Structure & Analytical Grammar"
level: "Level 4-5"
xml_tags: ["direction", "frame", "bracket", "voice"]
related_files: ["Ch1-Harmoni-Diatonik.md", "Ch3-Voice-Leading.md"]
---

# Schenkerian Analysis & Tonal Prolongation

## 📖 Konsep Teoritis (Level 1-3)

Schenkerian Analysis adalah metode analisis musik tonal yang dikembangkan oleh Heinrich Schenker. Metode ini memandang musik sebagai lapisan struktur hierarkis, di mana permukaan (foreground) musik dielaborasi dari struktur dasar (background) yang lebih sederhana.

### Hierarki Struktur Musik Tonal

```
Ursatz (Background)
├── Fundamental Line (Urlinie) - melodi struktural
├── Bass Arpeggiation (Bassbrechung) - harmoni dasar
│
Middleground
├── Prolongation techniques
├── Voice exchange
├── register transfer
│
Foreground
├── Surface elaboration
├── Passing tones, neighbor tones
├── Figuration
```

### Prolongation Techniques

1. **Consonant Support**: Nada konsonan yang mendukung struktur harmonis
2. **Dissonant Prolongation**: Penggunaan disonansi untuk memperpanjang harmoni
3. **Arpeggiation**: Pecahan akor yang diperluas melintasi register
4. **Register Transfer**: Perpindahan nada antar oktaf

## 🎼 Implementasi Praktis (Level 4)

### Analisis untuk Arranger

Dalam konteks arranging, Schenkerian Analysis membantu:
- Mengidentifikasi struktur harmonis yang esensial vs elaborasi permukaan
- Memahami voice leading pada level fundamental
- Menentukan mana yang harus ditekankan dalam aransemen
- Mengoptimalkan penggunaan instrumen berdasarkan register struktural

### Reduksi Partitur

Ketika membuat partitur orkestra dari komposisi solo:
1. Identifikasi Ursatz (struktur background)
2. Pisahkan middleground dari foreground
3. Distribusikan elemen struktural ke instrumen yang tepat
4. Pertahankan hierarki suara dalam orchestrasi

## ⚙️ Level 5: Implementasi MusicXML

### Tag XML untuk Analisis Struktural

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
        <staves>2</staves>
        <clef number="1">
          <sign>G</sign>
          <line>2</line>
        </clef>
        <clef number="2">
          <sign>F</sign>
          <line>4</line>
        </clef>
      </attributes>
      <!-- Direction untuk menandai struktur hierarkis -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-style="italic">Ursatz</words>
        </direction-type>
        <offset>0</offset>
      </direction>
      <!-- Bracket untuk reduksi analisis -->
      <direction placement="above">
        <direction-type>
          <bracket type="start" line-end="down" default-y="25"/>
        </direction-type>
      </direction>
      <!-- Voice separation untuk analisis multi-layer -->
      <note>
        <voice>1</voice>
        <type>quarter</type>
        <stem>up</stem>
      </note>
      <note>
        <voice>2</voice>
        <type>quarter</type>
        <stem>down</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Notasi untuk Analisis Multi-Layer

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
      <!-- Bracket notation untuk structural reduction -->
      <direction placement="above">
        <direction-type>
          <bracket default-y="30" line-end="down" line-type="dotted" type="start"/>
        </direction-type>
      </direction>
      <!-- Words untuk penandaan level analisis -->
      <direction placement="above">
        <direction-type>
          <words default-y="35" font-size="9" font-style="italic">Middleground</words>
        </direction-type>
      </direction>
      <!-- Footnote untuk penjelasan analisis -->
      <direction placement="below">
        <direction-type>
          <words default-y="-30" font-size="8">^ Struktur fundamental: I-V-I</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- Gunakan **bracket** (bukan slur) untuk menandai bagian analisis
- **Italic font** untuk istilah analisis (Ursatz, Urlinie, Bassbrechung)
- **Dotted line** untuk reduksi yang tidak terlihat dalam performa
- **Wedge/bracket** untuk menunjukkan register transfer
- Pastikan **voice direction** konsisten untuk setiap layer analisis

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Bracket overlap dengan not | Tambahkan `default-y` yang lebih tinggi |
| Voice direction tidak konsisten | Gunakan `<voice>` tag secara eksplisit |
| Multi-staff analysis error | Pastikan `<staves>` count sesuai |
| Words tidak terlihat | Cek `placement="above/below"` dan `default-y` |

## 📚 Referensi

- **Buku**: *Harmonic Analysis* (Heinrich Schenker)
- **Buku**: *Schenkerian Analysis* (Allen Cadwallader & David Gagné)
- **Buku**: *The Musician's Guide to Analysis* (Janet Schmalfeldt)
