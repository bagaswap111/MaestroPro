---
title: "Keluarga Instrumen & Ranges"
tier: "Bachelor S1"
subject: "Orkestrasi Dasar"
xml_tags: ["<score-instrument>", "<midi-instrument>", "<part-name>", "<part-abbreviation>", "<instrument-sound>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Keluarga Instrumen & Ranges

> **Buku panduan bab ini:** Nikolai Rimsky-Korsakov, *Principles of
> Orchestration* (Bab I–VI — keluarga, range, register, tessitura); Samuel
> Adler, *The Study of Orchestration* (Bab 1–4, Appendiks *Range*). Fokus:
> mengenal empat keluarga, rentang aktual, dan mendefinisikannya dengan benar
> di MusicXML agar *midi* & *playback* akurat.

## 1.1 Keluarga Strings (Alat Gesek)

Sumber bunyi: senar bergetar ditiup busur. Kekuatan: register luas, *sustain*
tanpa batas, *col legno*/*pizzicato*/*tremolo* menunjukkan warna ekstrem.
Semua ditulis pada **sounding pitch** — tidak ada transposisi (kecuali Double
Bass yang bunyi satu oktaf lebih rendah dari notasi).

| Instrumen | Rentang tulis (sounding) | Register aman | Timbre inti |
|-----------|--------------------------|----------------|-------------|
| Violin | G3 – C7 | G3–E6 | Terang, fleksibel, solo |
| Viola | C3 – E6 | C3–A5 | Gelap, hangat, tengah |
| Cello | C2 – A5 | C2–G4 | Dalam, *tenor* agung |
| Double Bass | E1 – G4 | E1–D4 | Sub-bass, fondasi |

### 1.1.1 Register dalam Ms Use (Adler)

- **Violin:** G string = kaya; E string = *piercing*.
- **Viola:** G string = nyawa-warnai; hindari melodi lama di C string
  (tebal & *gutural*).
- **Cello:** A string = lirik; D/G = texturally useful.
- **Double Bass:** buka di D/G — sustain kurang di register atas.

### 1.1.2 Rangkaian Teknik

| Teknik | MusicXML artifact |
|--------|-------------------|
| Pizzicato | `<notations><technical><pluck/></technical></notations>` |
| Arco (balik) | `<text>arco</text>` di `<direction>` |
| Tremolo | `<ornaments><tremolo type="start">2</tremolo></ornaments>` |
| Harmonics | `<technical><harmonic><natural/></harmonic></technical>` |
| Col legno | `<words>col legno</words>` |

### 1.1.3 Aplikasi MusicXML: Definisi Part Violin dengan Teknik Standar

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
      <part-abbreviation>Vln.</part-abbreviation>
      <score-instrument id="P1-I1">
        <instrument-name>Orchestral Violin</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>40</midi-program>
        <volume>78.7937</volume>
        <pan>0</pan>
      </midi-instrument>
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
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.2 Keluarga Woodwind (Tiup Kayu)

Teridri: Flute, Oboe, Clarinet, Bassoon + variasi (Piccolo, Alto Flute, E♭
Clarinet, Contrabassoon). Tiap alat punya **transposisi** & **register** khas
(detail di `Ch2-Transposisi-Instrumen.md`).

| Instrumen | Rentang (sounding) | Ciri |
|-----------|--------------------|------|
| Flute | C4 – D7 | *pale* di bawah, *silvery* di atas |
| Oboe | Bb3 – A6 | *piercing*, oboe khas melodi |
| Clarinet in B♭ | D3 – A7 (sounding rendah) | *dark chalumeau* → *bright clarion* |
| Bassoon | Bb1 – Eb5 | *gruff* bass, *tenor* cantando |

### 1.2.1 Pembagian Register Clarinet (Adler/Rimsky)

| Register | Karakter |
|----------|----------|
| Chalumeau (D3–G4) | gelap, lembut |
| Throat (G4–C5) | *pinched*, hati-hati |
| Clarion (C5–G5) | terang, solo |
| Altissimo (G5–C7) | tajam, virtuosik |

### 1.2.2 MusikXML: Clarinet Bb dengan `instrument-sound` benar

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P4">
      <part-name>Clarinet in Bb</part-name>
      <part-abbreviation>Cl.</part-abbreviation>
      <score-instrument id="P4-I1">
        <instrument-name>B-flat Clarinet</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P4-I1">
        <midi-channel>5</midi-channel>
        <midi-program>71</midi-program>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P4">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.3 Keluarga Brass (Tiup Logam)

Trumpet, Horn, Trombone, Tuba, Euphonium, Flugelhorn. Kebanyakan transpos;
*dynamic range* sangat luas; *sustain* & *articulation* patent.

| Instrumen | Rentang (sounding) | Notasi |
|-----------|--------------------|--------|
| Trumpet in B♭ | F#3 – C6 | Transpos (Bb) |
| French Horn in F | Bb1 – F5 | Transpos (F); register melodi E4–Bb4 |
| Trombone (Tenor) | E2 – Bb4 | Konser (BC) |
| Bass Tuba | D1 – F4 | Konser (BC) |

### 1.3.1 MIDI Program (General MIDI canonical)

| Instrument | GM program |
|------------|------------|
| Trumpet | 56 |
| French Horn | 60 |
| Trombone | 57 |
| Tuba | 58 |
| Violin | 40 |
| Cello | 42 |
| Flute | 73 |
| Oboe | 68 |
| Clarinet | 71 |
| Bassoon | 70 |

> General MIDI hanya *approximation* — untuk akurasi orkestra sejati
> gunakan library sampling (VST); MIDI program cukup untuk draft.

## 1.4 Keluarga Percussion

| Instrumen | Jenis | Rentang / catatan |
|-----------|-------|-------------------|
| Timpani | Pitched (4 drum) | D2 – F♯3 (tuning bervariasi) |
| Marimba | Pitched | A2 – C7 (konduktor C4→nada tertulis) |
| Xylophone | Pitched | F4 – C8 (tulis 1 oktaf di bawah bunyi) |
| Vibraphone | Pitched | F3 – F6 |
| Glockenspiel | Pitched | G5 – C8 (tulis 2 oktaf di bawah) |
| Snare Drum | Unpitched | no pitch — `<unpitched>` |
| Bass Drum, Cymbal, Triangle | Unpitched | GM mapping |

### 1.4.1 Aplikasi MusicXML: Snare (Unpitched)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P20">
      <part-name>Snare Drum</part-name>
      <part-abbreviation>S.D.</part-abbreviation>
      <score-instrument id="P20-I1">
        <instrument-name>Snare Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P20-I1">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>38</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P20">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>2</duration>
        <instrument id="P20-I1"/>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P20">
      <part-name>Snare Drum</part-name>
      <part-abbreviation>S.D.</part-abbreviation>
    </score-part>
  </part-list>
  <part id="P20">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>2</duration>
        <instrument id="P20-I1"/>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<midi-unpitched>` menetapkan drum/kim ke derajat GM tertentu. Snare=38,
> Kick=36, Hi-hat=42, Crash=49 (detail tabel di `Ch4-Notasi-Percussion.md`).

## 1.5 Tabel Range Lengkap (Komparatif)

| Instrumen | Sounding | Clef | Transit |
|-----------|----------|------|---------|
| Piccolo | D5 – C8 | G (8va dibaca) | Transpos 8 |
| Flute | C4 – D7 | G | – |
| Oboe | Bb3 – A6 | G | – |
| English Horn | E3 – A5 | G | F transpos |
| Clarinet B♭ | D3 – A6 | G | Bb |
| Bass Clarinet | D2 – B4 | G | Bb |
| Bassoon | Bb1 – Eb5 | F | – |
| Trumpet B♭ | F#3 – C6 | G | Bb |
| Horn in F | B1 – F5 | G | F |
| Trombone | E2 – Bb4 | F/BC | – |
| Tuba | D1 – F4 | F/BC | – |
| Harp | Cb1 – G#7 | brace (G4+F4) | – |

> API berguna (range otomatis): Dorico/MuseScore *Note per instrument*.
> untuk validasi perpart saat menulis.

## 1.6 Pertimbangan Engraving

1. **Clef management**: bass/strings/bassoon di F-clef; woodwind di G;
   *octave-clef* (`<clef-octave-change>`) untuk register rendah.
2. **Percussion**: gunakan `<sign>percussion</sign>` untuk unpitched —
   jangan salah atribusi pitch.
3. **Range check**: fitur *instrument range* di Dorico/MuseScore memvalidasi
   not di luar register.
4. **Transpose display**: aktifkan *concert pitch* untuk cek ensemble; off
   untuk part player.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Percussion</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef>
          <sign>percussion</sign>
        </clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Double Bass</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef>
          <sign>G</sign>
          <line>2</line>
          <clef-octave-change>-1</clef-octave-change>
        </clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.7 Miskonsepsi Umum

- **"Alto Sax = clarinet transposisi"** — Bermain melodi alto sax (E♭) selalu
  major 6 lebih tinggi dari konser; bukan B♭.
- **"Definisi part dengan nama saja cukup"** — Untuk playback benar, Butuh
  `score-instrument` + `midi-instrument` (program benar).
- **"Range aktual = key di internet"** — Range tulisan berbeda dengan
  register *practical* & *comfortable*; gunakan tabel Adler/Rimsky.

## 1.8 Latihan

1. **Dasar:** Tulis range aktual Violin, Oboe, Horn F (dalam 5 ledger lines).
2. **Menengah:** Definisikan 4 part (Flute, Clarinet Bb, Trombone, Snare) di
   MusicXML dengan `midi-program` benar.
3. **Lanjut:** Susun paduan register: 3 cara menggandakan melodi (oboe+vln,
   clar+alto sax, horn 1+2) dan bandingkan.

## 1.9 Repertoar Dengar

- Ravel, *Daphnis et Chloé* — violins *divisi* + woodwind sangat berwarna.
- *The Rite of Spring* (Stravinsky) — high woodwind / low brass extremes.
- John Williams *Jurassic Park theme* — horn section kuat.

## 1.10 Referensi Buku & Sumber Web

**Buku:**
- Rimsky-Korsakov, *Principles of Orchestration* (edisi Norton).
- Samuel Adler, *The Study of Orchestration*.

**Web:**
- Philip Saylor orchestration charts: https://philharmonia.co.uk/
- Vienna symphonic library *instrument guide*: https://www.vsl.co.at/en/

---

**Rangkuman:** Empat keluarga — gesek, woodwind, brass, percussion — memiliki
range, transposisi, dan register khas. Di MusicXML tiap instrumen didefinisikan
via `<score-instrument>` + `<midi-instrument>` (program). Materi lanjut:
[Transposisi Instrumen (`Ch2-Transposisi-Instrumen.md`)] dan [Tekstur
(`Ch3-Tekstur-Doubling.md`)].