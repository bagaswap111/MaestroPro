---
title: "Harmoni Diatonik"
tier: "Bachelor S1"
subject: "Teori Harmoni Tradisional"
xml_tags: ["<harmony>", "<root>", "<kind>", "<degree>", "<bass>", "<accidental>", "<note>", "<chord>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Harmoni Diatonik

> **Buku panduan bab ini:** Kostka & Payne, *Tonal Harmony* (McGraw-Hill);
> Aldwell & Schachter, *Harmony and Voice Leading* (Cengage). Keduanya adalah
> fondasi silabus harmoni S1 untuk menjadi rujukan ketika aturan di sini
> diperdebatkan.

## 1.1 Triada: Bata Dasar Harmoni Tonal

Harmoni diatonik dibangun di atas derajat tangga nada mayor/minor. Tiap
derajat menghasilkan triada dengan kualitas berbeda (Kostka & Payne, Bab 3):

| Derajat | Triada (C mayor) | Kualitas | Fungsi umum |
|---------|------------------|----------|-------------|
| **I**   | C–E–G            | Mayor    | Tonika |
| **ii**  | D–F–A            | Minor    | Subdominan |
| **iii** | E–G–B            | Minor    | Tonika lemah |
| **IV**  | F–A–C            | Mayor    | Subdominan |
| **V**   | G–B–D            | Mayor    | Dominan |
| **vi**  | A–C–E            | Minor    | Tonika lemah (relative) |
| **vii°**| B–D–F            | Diminished | Dominan (fungsi D) |

### 1.1.1 Interval Penyusun Triada

| Kualitas | Susunan (dari root) | Simbol |
|----------|---------------------|--------|
| Mayor | M3 + m3 | C, Cmaj |
| Minor | m3 + M3 | Cm, Cmin |
| Diminished | m3 + m3 | C°, Cdim |
| Augmented | M3 + M3 | C+, Caug |

### 1.1.2 Mayor vs Minor vs Modal

- **Natural minor:** derajat i–ii°–III–iv–v–VI–VII (v = minor triad pada
  5).
- **Harmonic minor (tonal):** raise derajat 7 → membuat **V mayor** dan
  **vii°** → memampukan fungsi dominan (raison d'être harmoni minor tonal).
- **Melodic minor (ascending):** naik 6 & 7, turun natural — berguna untuk
  garis melodi dan akor (i–ii–III... VI–vii°–I).

**Aturan praktis Kostka-Payne:** dalam komposisi diatonik minor, rujuklah
*harmonic minor* untuk akor V/vii°, dan *natural* untuk VII/III.

### 1.1.3 Inversi & Basso Continuo (Figur)

| Simbol | Akor | Bawah | Singkatan |
|--------|------|------|-----------|
| Root position | C–E–G | C | `5/3` (tbl) |
| First inversion | E–G–C | E | `6` |
| Second inversion | G–C–E | G | `6/4` |

Figur dalam praktik basso continuo era Barok. MusicXML: inversi dinyatakan
lewat *actual notes* + simbol akor; tidak ada atribut "inversion" — arranger
menuliskannya lewat susunan nada staf.

### 1.1.4 Doubling Triada (Aldwell & Schachter, Bab 4)

- Pada root position mayor/minor: **rangkap root** (paling umum), kadang
  rangkap 3rd/5th.
- Hindari rangkap **leading tone** (derajat 7, mis. B pada G mayor) — elemen
  kromatik yang harus beresolusi.
- Pada diminished (vii°), jarang rangkap 3rd (yang merupakan leading tone).
- Aturan "over-doubling" mengikat dalam SATB ketat; di orkestrasi dilonggarkan
  (lihat bab Orkestrasi).

### 1.1.5 MusicXML: Menulis Triada sebagai Akor Vertikal

Menulis not aktual dengan tag `<chord>` pada staf yang sama:

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
        <divisions>2</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
        <chord/>
      </note>
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
        <chord/>
      </note>
    </measure>
  </part>
</score-partwise>
```

Dan sebagai **chord symbol** (lead sheet) di staf terpisah:

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
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="maj">major</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>G</root-step></root>
        <kind text="7">dominant</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.2 Seventh Chords (Akor Ke-7)

Menambahkan interval ketiga di atas triada menghasilkan akor empat not
(Kostka & Payne, Bab 14; Levine, Bab 5 untuk konteks jazz):

| Akor | Not | Kualitas 7th |
|------|-----|--------------|
| Cmaj7 | C–E–G–B | major 7 |
| Cm7 | C–E♭–G–B♭ | minor 7 |
| C7 | C–E–G–B♭ | dominant 7 (minor 7) |
| Cm7b5 (half-dim) | C–E♭–G♭–B♭ | minor 7 |
| C°7 (diminished) | C–E♭–G♭–B♭♭ | diminished 7 |
| Cmmaj7 | C–E♭–G–B | major 7 (eksotis) |

### 1.2.1 Seperti Chord di Setiap Derajat (C mayor)

| Derajat | Akor 7 | Sebutan |
|---------|--------|---------|
| I | Imaj7 | maj7 (tonika) |
| ii | ii7 | min7 |
| iii | iii7 | min7 |
| IV | IVmaj7 | maj7 |
| V | V7 | *dominant seventh* |
| vi | vi7 | min7 |
| vii° | viiø7 | half-diminished |

V7 adalah akor ke-7 paling penting: **tritone** (B–F) di dalamnya adalah mesin
resolusi (B→C, F→E). Ini konsep inti Aldwell & Schachter (Bab 15) dan dasar
tritone substitution di jazz.

### 1.2.2 MusicXML: Kualitas dengan `<kind>`

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
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="maj7">major-seventh</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>D</root-step></root>
        <kind text="m7">minor-seventh</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>G</root-step></root>
        <kind text="7">dominant</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>B</root-step></root>
        <kind text="o7">diminished-seventh</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.3 Harmoni Fungsional: T – S – D

Tiga fungsi pusat (Kostka & Payne Bab 3–4; teori Riemann):

- **Tonika (T):** I, iii(lemah), vi(lemah) — pusat, istirahat.
- **Subdominan (S):** IV, ii — menjauh dari pusat, *pre-dominant*.
- **Dominan (D):** V, vii° — ketegangan, *leading* back ke I.

### 1.3.1 Kaidah Progresi Kuat

1. **Descending fifth** (ii→V→I) — progresi terkuat, backbone jazz.
2. **Descending third** (I→vi→IV→ii) — progresi lukis, umum pop/folk.
3. Hindari gerak *retrograde* IV–I yang menciptakan stasis (kadens plagal
   adalah pengecualian terkendali).

| Gerak | Kuat | Contoh |
|-------|------|--------|
| naik 4 / turun 5 | ya | V→I |
| turun 3 | sedang | I→vi |
| turun 2 | sedang–luncur | V→IV |
| naik 2 | melolia/plik | IV→V (dominant cadence) |

### 1.3.2 MusicXML: I–IV–V–I Lengkap

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
      <harmony print-frame="no">
        <root><root-step>C</root-step></root><kind text="maj">major</kind>
      </harmony>
    </measure>
    <measure number="2">
      <harmony print-frame="no">
        <root><root-step>F</root-step></root><kind text="maj">major</kind>
      </harmony>
    </measure>
    <measure number="3">
      <harmony print-frame="no">
        <root><root-step>G</root-step></root><kind text="7">dominant</kind>
      </harmony>
    </measure>
    <measure number="4">
      <harmony print-frame="no">
        <root><root-step>C</root-step></root><kind text="maj">major</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Kaden (Cadences) dan 6/4 Embellishing

Kadens adalah titik jeda frase (Kostka & Payne Bab 7):

| Kadens | Formula | Karakter |
|--------|---------|----------|
| **PAC** (Perfect Authentic) | V → I, root position, tonik di nada atas melodi | Final kuat |
| **IAC** (Imperfect Authentic) | V → I, tonik di nada tengah/atas bukan tonik | Final sedang |
| **HC** (Half Cadence) | ... → V | Tergantung |
| **Plagal** | IV → I | "Amen" |
| **Deceptive (DC)** | V → vi | Menghindari tonika |

### 1.4.1 IAC di 6/4 → Perbatasan?

*Cadential 6/4* `I6/4–V–I` (C: G–C–E → V7 → I) adalah figur **retardasi** —
6/4 bukan tonika stabil, melainkan dominan dengan *pedal*. Aldwell-Schachter
menyebutnya *dominant preparation*.

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
    <measure number="10">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="6/4">major</kind>
      </harmony>
    </measure>
    <measure number="11">
      <harmony print-frame="no">
        <root><root-step>G</root-step></root>
        <kind text="7">dominant</kind>
      </harmony>
    </measure>
    <measure number="12">
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="maj">major</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 1.4.2 Kadens Authentic dengan Figured Bass di MusicXML

`<bass>` untuk memberitahu *root symbol* dengan bass berbeda (C/E):

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
      <harmony>
        <root><root-step>C</root-step></root>
        <kind>major</kind>
        <bass>
          <bass-step>E</bass-step>
        </bass>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Kromatisme Dini: Secondary Dominants

Memperkaya harmoni diatonik tanpa meninggalkan pusat (Kostka Bab 18;
Aldwell Bab 26):

```
C:   V7/V   V7    I
     D7  →  G7 →  C
```

**Cara membangun:** *built as dominant of target* — V7 dari akor X, dimulai
dari leading tone X (C# untuk D).

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
      <harmony print-frame="no">
        <root><root-step>D</root-step></root>
        <kind text="7" use-symbols="yes">dominant</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

Also *secondary leading-tone*: vii°7/V → (D#dim) → V.

## 1.6 Modulasi Dini & Konsep Tonal Region

Modulasi = perubahan pusat tonal **yang bertahan**, didukung *pivot chord* dan
*irama* baru (detail penuh ada di `Ch2-Progresi-Akor-Modulasi.md`). Di sini kita
catat:

- **Pivot (common chord):** akor yang bisa dianalisis dalam dua kunci.
- **Close relationship:** kunci dalam jarak ±1 oktaf signatura (C → G, F, Dm,
  Am, Em).
- **Direct modulation** (tanpa pivot) legal saat *section break*.

## 1.7 Voice Leading Inti (30 Detik)

Aturan non-negosiable (detail: `Ch3-Voice-Leading.md`):

1. Pertahankan *common tones*.
2. Gerak stepwise minimal.
3. **Tritone V7 (B–F) harus beresolusi:** B→C, F→E.
4. Leading tone naik ke tonika.
5. Hindari *parallel fifths/octaves*.
6. Rangkap root pada root position; jangan rangkap leading tone.

## 1.8 Miskonsepsi Umum

- **"vi = tonika penuh"** — vi adalah *root-less* tonika lemah; memandangnya
  sebagai S dalam konteks plagal kadang lebih akurat.
- **"V7 selalu dominan beresolusi"** — V7 bisa *deceptive* (→vi), atau menjadi
  *II7/V* di area modulasi.
- **"Kadens hanya di akhir lagu"** — Kadens mengakhiri *frase*, internal
  (species: PAC di akhir 8-bar, dsb).
- **"Half-diminished harus diselesaikan V"** — Bisa maju ke V, vi, atau ii;
  tergantung konteks.
- **"Symbol <kind>=C7 sama dengan fisik not"** — Tidak selalu; prolonged
  kromatis V7 dapat disusun tanpa not literal (voice leading!).

## 1.9 Latihan

1. **Dasar:** Tulis 3 triada (I, IV, V) di C dalam tiga posisi.
2. **Menengah:** Analisis progresi F–G–C–Am (IAC-PAC campuran):
   labeli fungsi tiap akor, cari pivot ke area ii.
3. **Lanjut:** Susun 8-bar frase SATB (I–vi–ii–V7–IAC) dengan rangkap root,
   tulis *chord symbols* `<harmony>` + *actual notes* `<chord>` di MusicXML,
   cek di MuseScore.

## 1.10 Repertoar Dengar

- Bach Chorale (BWV 294, 302) — harmoni diatonik sempurna.
- Beethoven, Piano Sonata *Pathetique* I — V7/iv diminution.
- Schubert, *Ständchen* — plagal color.
- Brahms, *Ein deutsches Requiem* — fungsi & inversi.

## 1.11 Referensi Buku & Sumber Web

**Buku (silabus):**
- Kostka & Payne, *Tonal Harmony* (Bab 3–7, 14, 18).
- Aldwell & Schachter, *Harmony and Voice Leading* (Bab 1–5, 15, 26).
- Walter Piston, *Harmony* (klasik).

**Web:**
- MusicXML Tutorial (W3C) — `<harmony>`:
  https://www.w3.org/2021/06/musicxml40/tutorial/
- Hooktheory — progresi pop: https://www.hooktheory.com/
- OpenStax Music (gratis): https://openstax.org/books/understanding-music/

---

**Rangkuman:** Harmoni diatonik = triada + seventh chords + fungsi
(T–S–D) + kadens + inversi. Aturan voice-leading inti (tritone, common tone,
rangkap) adalah pokok Aldwell-Schachter; di MusicXML konsep ini dinyatakan
baik lewat *actual notes* `<chord>` maupun *symbols* `<harmony>/<root>/<kind>`.
Lanjut ke [Bab 2 — Progresi Akor & Modulasi
(`Ch2-Progresi-Akor-Modulasi.md`)] dan pelajari detail voice leading di
[`Ch3-Voice-Leading.md`].
