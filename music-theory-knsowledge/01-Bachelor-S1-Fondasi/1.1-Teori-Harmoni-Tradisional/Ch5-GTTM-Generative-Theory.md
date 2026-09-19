---
title: "GTTM - Generative Theory of Tonal Music"
pillar: "Deep Structure & Analytical Grammar"
level: "Level 4-5"
xml_tags: ["direction", "grouping", "metronome", "words"]
related_files: ["Ch1-Harmoni-Diatonik.md", "Ch2-Progresi-Akor-Modulasi.md"]
---

# GTTM - Generative Theory of Tonal Music

## 📖 Konsep Teoritis (Level 1-3)

Generative Theory of Tonal Music (GTTM) dikembangkan oleh Fred Lerdahl dan Ray Jackendoff. Teori ini menganalisis musik tonal berdasarkan **grouping structure** dan **meter structure** sebagai dua dimensi utama.

### Grouping Structure

Grouping structure membagi musik menjadi segmen-segmen berdasarkan:
- **Proximity**: Jarak antar nada (jeda, perubahan dinamika)
- **Similarity**: Kemiripan pola ritmis/melodis
- **Parallelism**: Pengulangan pola

### Meter Structure

Meter structure mengatur ketukan hierarkis:
- **Pulse**: Ketukan dasar
- **Beat**: Ketukan yang terorganisir
- **Measure**: Kelompok ketukan
- **Hyper-measure**: Kelompok takbir

### Preferensi Rules

GTTM menggunakan **preferensi rules** untuk menentukan struktur yang paling mungkin:
1. **Well-Formedness Rules**: Aturan dasar struktur yang valid
2. **Preference Rules**: Aturan untuk memilih interpretasi terbaik

## 🎼 Implementasi Praktis (Level 4)

### Untuk Arranger/Composer

GTTM membantu dalam:
1. **Phrasing**: Mengidentifikasi batas frasa untuk artikulasi
2. **Dynamic Shaping**: Menyesuaikan dinamika berdasarkan grouping
3. **Rhythmic Clarity**: Memastikan meter structure jelas dalam notasi
4. **Structural Emphasis**: Menekankan titik-titik struktural penting

### Analisis untuk Orkestrasi

- Gunakan grouping untuk menentukan **breath marks** pada instrumen tiup
- Identifikasi hyper-measure untuk **dynamic shaping** orkestra
- Gunakan meter structure untuk **rhythmic layering** yang efektif

## ⚙️ Level 5: Implementasi MusicXML

### Tag XML untuk Grouping Structure

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
      <!-- Grouping start untuk segmen musikal -->
      <direction placement="above">
        <direction-type>
          <grouping type="start" member-of="1"/>
        </direction-type>
      </direction>

      <!-- Grouping stop untuk akhir segmen -->
      <direction placement="above">
        <direction-type>
          <grouping type="stop" member-of="1"/>
        </direction-type>
      </direction>

      <!-- Multi-level grouping -->
      <direction placement="above">
        <direction-type>
          <grouping type="start" member-of="1"/>
        </direction-type>
      </direction>

      <direction placement="above">
        <direction-type>
          <grouping type="start" member-of="2"/>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Tag XML untuk Meter Structure

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
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <!-- Metronome marking untuk tempo -->
      <direction placement="above">
        <direction-type>
          <metronome parentheses="no">
            <beat-unit>quarter</beat-unit>
            <per-minute>120</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="120"/>
      </direction>

      <!-- Hyper-measure marking dengan rehearsal marks -->
      <direction placement="above">
        <direction-type>
          <rehearsal default-y="25" font-size="14">A</rehearsal>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Words untuk Penandaan Analisis

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
      <!-- Penandaan grouping level -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-style="italic">Phrase 1</words>
        </direction-type>
      </direction>

      <!-- Penandaan hyper-measure -->
      <direction placement="above">
        <direction-type>
          <words default-y="30" font-size="9">Hyper-measure 1</words>
        </direction-type>
      </direction>

      <!-- Breath mark untuk grouping boundary -->
      <note>
        <notations>
          <breath-mark/>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- Gunakan **rehearsal marks** (huruf/angka) untuk hyper-measure boundaries
- **Slur** untuk menunjukkan grouping secara visual
- **Breath marks** pada batas grouping untuk instrumen tiup
- **Fermata** pada titik-titik struktural penting
- Gunakan **dynamic markings** untuk mengikuti contour grouping

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Grouping tidak terlihat | Gunakan combination slur + words |
| Meter ambiguity | Tambahkan metronome marking eksplisit |
| Hyper-measure unclear | Gunakan rehearsal marks dengan font besar |
| Breath mark terlalu dekat | Jarak minimum 1 spasi antar breath marks |

## 📚 Referensi

- **Buku**: *A Generative Theory of Tonal Music* (Lerdahl & Jackendoff, 1983)
- **Buku**: *The Analysis of Tonal Music* (Jonathan Dunsby)
- **Jurnal**: *Music Theory Online* - articles on GTTM applications
