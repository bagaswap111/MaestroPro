---
title: "Negative Harmony & Symmetrical Scales"
pillar: "Contemporary Harmony, Jazz & Post-Tonal"
level: "Level 4-5"
xml_tags: ["transpose", "degree", "accidental", "key"]
related_files: ["Ch1-Chord-Scale-Theory.md", "Ch2-Upper-Structures-Alterations.md"]
---

# Negative Harmony & Symmetrical Scales

## 📖 Konsep Teoritis (Level 1-3)

### Negative Harmony

Negative Harmony adalah konsep yang dikembangkan oleh Ernst Levy, menjelaskan hubungan cermin (mirror) antara dua harmoni. Setiap nada memiliki "negatif"nya berdasarkan poros simetri.

```
C - D - E - F - G - A - B
  ↕   ↕   ↕   ↕   ↕   ↕   ↕
C - Bb - Ab - G - F - Eb - D
```

**Penerapan:**
- C major → C minor (negatif)
- Progressi I-IV-V → I-ii-v (negatif)
- Membuat variasi harmoni yang unexpected

### Symmetrical Scales

Skala simetris memiliki interval yang berulang secara teratur:
1. **Chromatic Scale**: Interval semitone berulang
2. **Whole-Tone Scale**: Interval whole tone berulang
3. **Octatonic Scale**: Interval whole-half berulang
4. **Augmented Scale**: Interval minor 3rd berulang

### Mirror Chord Progressions

Progressi yang menggunakan simetri untuk menciptakan efek cermin:
- **Axis Progression**: Menggunakan pivot chord
- **Tritone Substitution**: Menggantikan V dengan bII
- **Negative Counterpoint**: Melodi cermin harmonis

## 🎼 Implementasi Praktis (Level 4)

### Untuk Arranger

1. **Harmonic Variation**: Gunakan negative harmony untuk variasi
2. **Modal Interchange**: Negative dari mode paralel
3. **Arranging Creativity**: Buat voicing yang tidak konvensional
4. **Transitional Harmony**: Bridge antar section dengan simetri

### Analisis untuk Komposisi

- Identifikasi **axis** dalam progressi
- Gunakan **tritone substitution** untuk variasi
- Buat **mirror melody** untuk counter-melody
- Eksplorasi **symmetrical voicing** untuk jazz chord

## ⚙️ Level 5: Implementasi MusicXML

### Tag XML untuk Negative Harmony

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
      <!-- Transpose untuk negative -->
      <attributes>
        <transpose>
          <diatonic>-6</diatonic>
          <chromatic>-10</chromatic>
        </transpose>
      </attributes>
      
      <!-- Degree analysis untuk negative chord -->
      <harmony>
        <root>
          <root-step>C</root-step>
        </root>
        <kind text="m">minor</kind>
        <degree>
          <degree-value>3</degree-value>
          <degree-alter>0</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
      </harmony>
      
      <!-- Accidental untuk negative pitch -->
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
      </note>
    </measure>
  </part>
</score-partwise>
``

### Tag XML untuk Symmetrical Scales

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
      <!-- Key signature untuk atonal -->
      <attributes>
        <key>
          <key-accidental slash="yes"/>
          <key-step>A</key-step>
        </key>
      </attributes>
      
      <!-- Time signature untuk symmetrical -->
      <attributes>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
      </attributes>
      
      <!-- Cautionary accidental untuk symmetrical -->
      <note>
        <pitch>
          <step>E</step>
          <alter>0</alter>
          <octave>4</octave>
        </pitch>
        <accidental>
          <accidental-mark>natural</accidental-mark>
        </accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Transpose Tags untuk Mirror

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
      <!-- Mirror interval -->
      <direction placement="above">
        <direction-type>
          <transpose>
            <diatonic>3</diatonic>
            <chromatic>5</chromatic>
          </transpose>
        </direction-type>
      </direction>
      
      <!-- Axis marker -->
      <direction placement="above">
        <direction-type>
          <words default-y="20" font-style="italic">Axis</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- Gunakan **accidental cautionary** untuk simetri
- **Key signature** mungkin tidak tersedia untuk skala simetris
- Gunakan **text markings** untuk menjelaskan negatif harmony
- Pertahankan **voice leading** yang smooth meskipun harmoni kompleks
- **Accidentals** harus jelas untuk setiap nada

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Negative chord tidak terdeteksi | Gunakan `<kind>` dengan text description |
| Symmetrical scale error | Eksplisitkan semua accidentals |
| Mirror interval salah | Verifikasi diatonic vs chromatic values |
| Enharmonic confusion | Gunakan cautionary accidentals |

## 📚 Referensi

- **Buku**: *Negative Harmony* (Ernst Levy)
- **Buku**: *The Jazz Theory Book* (Mark Levine)
- **Buku**: *Twentieth-Century Harmony* (Vincent Persichetti)
