---
title: "Vokal & Choral — Karakteristik & Notasi"
tier: "Bachelor S1"
subject: "Genre Vokal & Choral"
xml_tags: ["<voice>", "<lyric>", "<harmonic>", "<melisma>", "<tie>", "<staff>", "<direction>"]
software: ["MuseScore", "Dorico", "Sibelius", "Finale"]
---

# Bab 1 — Vokal & Choral: Karakteristik & Notasi

## 1.1 Dunia Suara Manusia

Untuk arranger, suara adalah instrumen paling luwes tapi paling terbatas
jangkauan dan transparansinya. Dasar:

| Jenis suara | Range mnemonic (hanya pendekatan tingkat A) | Catatan |
|-------------|---------------------------------------------|---------|
| Soprano | C4–C6 | Melodi tinggi, *coloratura* |
| Mezzo-soprano | A3–A5 | *contralto* sedikit lebih rendah |
| Tenor | C3–C5 (B2–C5 praktis) | Umum ditulis treble |
| Baritone | G2–G4 | |
| Bass | E2–E4, basso spesso hingga C2 | |

**Passaggio** (area transisi register) penting: soprano sekitar E4–F#4,
tenor sekitar D4–E4. Di notasi, hindari baris panjang di daerah passaggio berat
tanpa istirahat.

## 1.2 Tekstur Choral: Monofoni–Polifoni–Homofoni

- **Monofoni:** satu garis melodi (gregorian).
- **Homofoni:** semua suara ritme sama (hymn style) — *Note-against-note*.
- **Polifoni:** kontrapung — masing suara ritmik berbeda (motet, fugue
  vocal). Lihat bab [Species Counterpoint & Fugue
  (`../1.2-Kontrapung-Bentuk-Musik/`)].

### 1.2.1 Empat Suara SATB

| Suara | Clef & octave | Peran |
|-------|---------------|-------|
| Soprano | Treble | Melodi |
| Alto | Treble | Harmonik atas |
| Tenor | Treble (8vb) / tenor clef | Harmonik bawah |
| Bass | Bass clef | Fondasi (root), dsb. |

## 1.3 Menulis Lirik di MusicXML — `<lyric>`

Lirik menempel pada `<note>` melalui `<lyric>` dengan `syllabic`:

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
      <note>
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric number="1">
          <syllabic>begin</syllabic>
          <text>Count</text>
        </lyric>
      </note>
      <note>
        <pitch><step>D</step><octave>5</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
        <lyric number="1">
          <syllabic>end</syllabic>
          <text>ry</text>
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

**Melisma:** satu silabel pada beberapa not → letakkan `<extend/>` pada not
ke-dua dst (tanda `_`).

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
      <note>
        <pitch><step>A</step><octave>5</octave></pitch>
        <duration>2</duration>
        <type>8th</type>
        <lyric number="1"><syllabic>end</syllabic><text>la</text><extend/></lyric>
      </note>
      <note>
        <rest/>
        <duration>14</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
        <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Harmoni Vokal: Voicing dan Doubling

- **Doubling di SATB:** rangkap root/5th di terbaik; paralel oktaf & kuinta
  dihindari (Aldwell–Schachter).
- **Kadens khas choral:** *Amen* (IV–I plagal), *half cadence* Vě.
- **Chorus 3/4 suara pop:** 3rd 6th di atas melodi, coba downgrade oktaf di
  bass (closed voicing).

### 1.4.1 Contoh SATB pada Progressi I–V–I (C)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>SATB</part-name>
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
      <!-- Soprano E -->
      <note><pitch><step>E</step><octave>5</octave></pitch><duration>4</duration><voice>1</voice><type>quarter</type></note>
      <!-- Alto C -->
      <note><pitch><step>C</step><octave>4</octave></pitch><duration>4</duration><voice>2</voice><type>quarter</type></note>
      <!-- Tenor G -->
      <note><pitch><step>G</step><octave>3</octave></pitch><duration>4</duration><voice>3</voice><type>quarter</type></note>
      <!-- Bass C -->
      <note><pitch><step>C</step><octave>3</octave></pitch><duration>4</duration><voice>4</voice><type>quarter</type></note>
      <note>
        <rest/>
        <duration>16</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Teknik Vokal Khas Genre

| Genre | Kekhasan |
|-------|----------|
| Gregorian | Monofoni, free rhythm, *neum* |
| Renaisans/Barok | Kontrapung imitatif, *word painting* |
| Romantik | Cepat dissonansi, modulasi, *wide range* |
| Pop | Belting, falsetto, riff/run melisma, harmonies 3rd |
| Gospel | Call-response, choir antiphonal, *vamp* ride |
| Doo-wop | Chord block, roots+5th+3rd at tada, "bop-bop-bop" |
| Barbershop | 4-part *close harmony* (TTBB), *barbershop seventh* |

## 1.6 Miskonsepsi Umum

- **"Semua vokal dalam satu staf dua baris"** — Untuk skor paduan bisa 1 staf
  per suara atau 2 staf dengan `divisi`; pilih readability.
- **"Lirik otomatis di MusicXML"** — Harus manual `<lyric>`; hindari tooltip
  gulung.
- **"Range non penting"** — Range = musuh semua chorus; check tessitura on
  every verse.
- **"Barbershop = 4 baris di clef bass"** — TTBB = tenor 1/2 (treble), baritone,
  bass (bass). Range row, closed voicing.

## 1.7 Latihan

1. **Dasar:** Tulis himne 4 bar SATB (I–V–I) lengkap lirik "Amen".
2. **Menengah:** Buat *call-and-response* gospel 8 bar: soli choir vs full
   choir, part tersusun 2 staf.
3. **Lanjut:** Tulis 3-part pop harmony (closed voicing, root+5th+3rd),
   tambah melisma `<extend/>` pada kata "love" di bar 5.

## 1.8 Repertoar Dengar

- Renaissance: Palestrina, *Missa Papae Marcelli*.
- Barok: Bach, *Jesu, Joy of Man's Desiring* (chorale setting).
- Romantik: Brahms, *Ein deutsches Requiem*.
- Pop: Pentatonix, *Hallelujah* (cover); Queen, *Bohemian Rhapsody* (opera
  section).
- Gospel: Mahalia Jackson, *How Great Thou Art*.

## 1.9 Referensi Buku & Sumber Web

**Buku:**
- Kostka & Payne, *Tonal Harmony* (bab Choral Harmony).
- Tony Thornton, *Barbershop Music Theory* (aransemen).
- Robert Shaw, *On Music* / *Choral Workshop Guides*.

**Web:**
- CPDL (Choral Public Domain Library) — partitur bebas:
  https://www.cpdl.org/
- MuseScore vocal template:
  https://musescore.org/
- Barbershop Harmony Society:
  https://www.barbershop.org/

---

**Rangkuman:** Vokal/choral = range suara, tekstur (mono/homo/poly), penulisan
lirik via `<lyric>` dan melisma `<extend/>`. MusicXML mewakili tiap suara
`<voice>`, melodi dengan `#`, dan lirik dengan `lyric`. Lanjut ke [Adaptasi
Vokal & Choral Lintas Instrumentasi (`Ch2-Adaptasi-Instrumentasi.md`)].