---
title: "Text Setting & Diction"
pillar: "Industrial Workflow & Specialized Applications"
level: "Level 4-5"
xml_tags: ["lyric", "syllabic", "elision", "extend", "breath-mark"]
related_files: ["Ch1-Karakteristik-Notasi.md", "Ch2-Adaptasi-Instrumentasi.md"]
---

# Text Setting & Diction

## 📖 Konsep Teoritis (Level 1-3)

Text setting adalah proses mencocokkan not musik dengan teks (lirik). Dalam vokal dan choral arranging, pemahaman tentang syllabic vs melismatic setting sangat krusial.

### Syllabic vs Melismatic

| Aspek | Syllabic | Melismatic |
|:---|:---|:---|
| **Definisi** | Satu nada per suku kata | Banyak nada per suku kata |
| **Karakter** | Jelas, langsung | Ekspresif, mengalir |
| **Contoh** | "A-ma-zing Grace" | "Aaaaa-men" (melisma pada "a") |
| **Diction** | Lebih mudah dipahami | Membutuhkan vokalis terampil |

### Elision

Elision adalah penggabungan dua suku kata dari dua kata berbeda menjadi satu nada:
- "love and" → "lov'and" (satu nada)
- "him always" → "him'al-ways" (satu nada)

### Breath Management

- **Breath marks** harus ditempatkan pada jeda frase alami
- Hindari memotong kata atau frasa penting
- Pertahankan **vowel purity** saat bernapas

## 🎼 Implementasi Praktis (Level 4)

### Untuk Choral Arranging

1. **SATB Writing**: Pastikan teks terbaca jelas di semua voce
2. **Divisi Teks**: Saat divisi, pastikan semua bagian mendapat teks yang sama
3. **Text Underlay**: Teks harus tepat di bawah nada yang sesuai
4. **Hyphenation**: Gunakan hyphen untuk memisahkan suku kata

### Diction untuk Berbagai Bahasa

- **Indonesian**: Vocal vowels harus jelas (a, e, i, o, u)
- **English**: Perhatikan schwa sound dan dipthongs
- **Latin**: Vowel pure, consonants sharp
- **Italian**: Open vowels, clear consonants

## ⚙️ Level 5: Implementasi MusicXML

### Tag XML untuk Syllabic Setting

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Soprano</part-name>
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
      <!-- Syllabic: satu nada per suku kata -->
      <note>
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>single</syllabic>
          <text>A-</text>
        </lyric>
      </note>
      <!-- Syllabic: suku kata pertama -->
      <note>
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>begin</syllabic>
          <text>A-</text>
        </lyric>
      </note>
      <!-- Syllabic: suku kata tengah -->
      <note>
        <pitch><step>D</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>middle</syllabic>
          <text>ma-</text>
        </lyric>
      </note>
      <!-- Syllabic: suku kata terakhir -->
      <note>
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>end</syllabic>
          <text>zing</text>
        </lyric>
      </note>
    </measure>
    <measure number="2">
      <!-- Melismatic: banyak nada, satu suku kata -->
      <note>
        <pitch><step>F</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>single</syllabic>
          <text>A</text>
          <extend/>
        </lyric>
      </note>
      <note>
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>single</syllabic>
          <text></text>
          <extend/>
        </lyric>
      </note>
      <note>
        <rest/>
        <duration>8</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Tag XML untuk Elision

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Soprano</part-name>
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
      <!-- Elision: gabungan dua kata -->
      <note>
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>end</syllabic>
          <text>lov'</text>
          <elision/>
          <syllabic>begin</syllabic>
          <text>and</text>
        </lyric>
      </note>
      <!-- Elision dalam satu nada -->
      <note>
        <pitch><step>D</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>single</syllabic>
          <text>lov'</text>
          <elision/>
          <syllabic>single</syllabic>
          <text>and</text>
        </lyric>
      </note>
      <note>
        <rest/>
        <duration>8</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Tag XML untuk Breath Marks

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Soprano</part-name>
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
      <!-- Breath mark setelah frasa -->
      <note>
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>12</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
        <notations>
          <breath-mark/>
        </notations>
      </note>
      <note>
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>4</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="2">
      <!-- Breath mark dengan custom text -->
      <direction placement="above">
        <direction-type>
          <words default-y="15" font-size="10">[breath]</words>
        </direction-type>
      </direction>
      <note>
        <pitch><step>G</step><octave>5</octave></pitch>
        <duration>12</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
      </note>
      <note>
        <rest/>
        <duration>4</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="3">
      <!-- Cautionary breath untuk choral -->
      <note>
        <pitch><step>F</step><octave>5</octave></pitch>
        <duration>12</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
        <notations>
          <breath-mark type="comma"/>
        </notations>
      </note>
      <note>
        <rest/>
        <duration>4</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving untuk Text Underlay

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <defaults>
    <lyric-font font-family="Times New Roman" font-size="12"/>
  </defaults>
  <part-list>
    <score-part id="P1">
      <part-name>Soprano</part-name>
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
      <!-- Text alignment yang benar -->
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>begin</syllabic>
          <text>A-</text>
          <extend/>
        </lyric>
      </note>
      <note>
        <pitch><step>B</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric>
          <syllabic>end</syllabic>
          <text>maz</text>
        </lyric>
      </note>
      <note>
        <rest/>
        <duration>8</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### Aturan Engraving

- **Font**: Gunakan serif font (Times New Roman) untuk lyrics
- **Ukuran**: 10-12pt untuk solo, 8-10pt untuk choral
- **Hyphen**: Gunakan `-` untuk memisahkan suku kata
- **Extend line**: Gunakan `_` untuk melisma yang berlanjut
- **Placement**: Lyrics selalu di **bawah** staff
- **Centering**: Teks harus centered di bawah notehead

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| Teks terlalu panjang | Kurangi ukuran font atau gunakan abbreviations |
| Elision tidak terlihat | Gunakan `<elision>` tag secara eksplisit |
| Extend line putus | Pastikan `<extend/>` di setiap nada melisma |
| Breathing mark clash | Jarak minimum 2 spasi dari note terakhir |
| Multi-language text | Gunakan `<language>` tag jika didukung software |

## 📚 Referensi

- **Buku**: *Behind Bars* (Elaine Gould) - Chapter: Lyrics
- **Buku**: *The Diagnosis and Correction of Vocal Faults* (James C. McKinney)
- **Buku**: *Diction for Singers* (Joan Wall)
