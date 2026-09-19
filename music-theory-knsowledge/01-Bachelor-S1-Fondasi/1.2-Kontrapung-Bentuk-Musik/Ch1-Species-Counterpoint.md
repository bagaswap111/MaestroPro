---
title: "Species Counterpoint"
tier: "Bachelor S1"
subject: "Kontrapung & Bentuk Musik"
xml_tags: ["<note>", "<duration>", "<type>", "<rest>", "<voice>", "<notations>", "<tied>", "<pitch>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Species Counterpoint

> **Buku panduan bab ini:** Johann Joseph Fux, *Gradus ad Parnassum* (1725;
> terj. Alfred Mann, Norton); Marcus Santa, *Counterpoint: A Species Approach*
> ; Kent Kennan, *Counterpoint*. Metode *species* adalah latihan disiplin yang
> melatih kemampuan melodi independen dan punctual — fondasi fugue, chorale,
> dan tulis bagian.

## 1.1 Pengantar Kontrapung

*Counterpoint* (Latin *punctus contra punctum* = "not melawan not") adalah
seni menggabungkan dua melodi atau lebih yang independen namun harmonis.
Diciptakan sebagai *exercises* oleh Fux (dialog dengan Palestrina) dalam lima
tingkatan:

| Species | Rasio irama (lawan C.F.) |
|---------|--------------------------|
| **First** | 1:1 — *note-against-note* |
| **Second** | 2:1 — dua nada lawan satu |
| **Third** | 4:1 — empat nada lawan satu |
| **Fourth** | Sinkopasi (ligasi, *suspension*) |
| **Fifth** | *Florid* — campuran seluruhnya |

### 1.1.1 Cantus Firmus (C.F.)

C.F. adalah melodi dasar (umumnya 8–16 not *whole*, diatonis, diakhiri *leading
tone*-ke-tonik atau subtonik-ke-tonik). Aturan membuat C.F. yang baik:

1. Tiap nada terhubung *stepwise* mayoritas (lompat kecil oktaf).
2. Hindari lompat besar naik, terutama interval 7/9.
3. Puncak melodi (climax) hanya sekali.
4. Kadens diakhiri *2 → 1* (atau *7 → 1*).

## 1.2 First Species: Note-Again-Note

### 1.2.1 Aturan (Fux, Mann ed.)

1. Mulai/akhiri *perfect consonance* (P1, P8) — kadan dengan nada harmonis.
2. Interval yang diizinkan: **P1, m3, M3, P5, m6, M6, P8**.
3. **Dilarang:** P4 naik (dianggap *dissonant* di barok), 2nd, 7th, tritone.
4. **Parallel fifths/octaves** dilarang (berurutan).
5. *Contrary motion* disarankan; *similar* menuju *perfect* dihindari.
6. Kedua melodi tetap dalam takaran **oktaf** dari awal-awal.
7. Tidak ***samar* (hidden)** — suara keduanya tidak boleh bergerak *similar*
   menuju interval *perfect* *unisono* menonjol.

### 1.2.2 Pola Konsonan vs Disonan (Interval)

| Jenis | Interval |
|-------|----------|
| Perfect | P1, P5, P8 (open) |
| Imperfect | M3, m3, M6, m6 |
| Disonan | 2nd, 7th, P4 (konteks), tritone |

### 1.2.3 MusicXML: First Species Dua Suara

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
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>4</duration>
        <voice>2</voice>
        <type>whole</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>4</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
      <note>
        <pitch><step>A</step><octave>3</octave></pitch>
        <duration>4</duration>
        <voice>2</voice>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> **Verifikasi cepat:** untuk tiap birama, selisih skala antara suara =
> interval konsonan; dan tidak ada dua birama berturut-turut dengan interval
> P5/P8 yang sama.

## 1.3 Second Species: Dua Nada Lawan Satu

### 1.3.1 Aturan

- Dua *half notes* melawan satu *whole* C.F. → *unaccented* beat (2nd of pair)
  boleh **disonan sebagai *passing tone* (PT)**.
- *Accented* beat pertama harus konsonan.
- PT baru boleh muncul bila antara dua akor berdekatan, satu langkah.
- Hindari *parallel fifths/octaves* antar tiap *downbeat*.
- Jangan: dua nada *unaccented* sama-sama PT tanpa konsonan acakten di antara.

### 1.3.2 MusicXML: Second Species

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
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>half</type>
      </note>
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>half</type>
      </note>
      <note>
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Pada contoh: nada 2 (D) adalah PT dari E→C (konsonan→konsonan). Pastikan
> pengguna `<voice>` berbeda agar playback eksplisit.

## 1.4 Third Species: Empat Nada Lawan Satu

### 1.4.1 Aturan

- Empat *quarter notes* per *whole* C.F.
- *Passing tones* pada *unaccented* beats; boleh *neighbor* (atas/bawah
  kembali).
- *Cambiata* (lompat) tertentu diizinkan; hindari *disjunction* serial.
- **Perlunya seluruh *quarter* menimbulkan aksen-kuat** yang nyekat — aksen
  pertama tiap grup harus konsonan.
- Lebih dari 3 PT berturut-turut berbahaya; lompat harus membuka kontur.

### 1.4.2 Contoh

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
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>B</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Fourth Species: Sinkopasi (Ligasi)

### 1.5.1 Aturan — *Suspension*

- Nada mulai *weak*, **diperpanjang (ligated)** ke *strong* berikutnya →
  akhirnya *suspension*.
- Siklus: **konsonan (preparation) → dissonan (suspension) → konsonan
  (resolution, *tep*).**
- Susunan not: biasanya **7–6, 4–3, 9–8** (dari atas C.F.); resolusi turun.
- Dilarang paralel perfect di antara *suspensions*.

Tiga fase suspension:

| Fase | Ketukan | Interval ke C.F. |
|------|---------|------------------|
| Preparation | weak | konsonan |
| Suspension | strong | dissonan |
| Resolution | weak | konsonan (turun) |

### 1.5.2 MusicXML: Tie + Tied

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
      <note>
        <pitch><step>F</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>half</type>
        <tie type="start"/>
        <notations>
          <tied type="start"/>
        </notations>
      </note>
      <note>
        <pitch><step>F</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>half</type>
        <tie type="stop"/>
        <notations>
          <tied type="stop"/>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<tie>` = playback; `<tied>` dalam `<notations>` = kurva tampilan. Keduanya
> wajib sinkron bila bagian diligasi.

## 1.6 Fifth Species: Florid Counterpoint

### 1.6.1 Aturan

- Boleh mencampur semua *species* dalam birama sama — *quarter, half, whole*,
  plus ornamenti (PT, NT, suspension, cambiate).
- Prinsip utama: **kesetimbangan gerak** — arahkan puncak dan kadens.
- Saat mencampur, pertahankan aturan akar (aksen, decay, paralel).

### 1.6.2 Contoh Ritmik Campur

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
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>2</duration><type>half</type>
      </note>
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>1</duration><type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.7 Kontrapung dalam Konteks Modern & Orkestrasi

- Dua suara kontrapungter penting muncul di: flute+oboe duo, string quartet
  (1st+2nd), wind choir doubling.
- Software *engraving*: setiap melodi diberikan `<voice>` berbeda agar garis
  independen; gunakan playback solo untuk memeriksa kontur tiap bagian.
- Music21: modul `counterpoint` (Schubert) menawarkan *species exercise*
  otomatis untuk validasi.

## 1.8 Miskonsepsi Umum

- **"Species = hanya latihan Palestrina"** — Prinsip species (aksen, PT,
  paralel) merambat ke semua tulisan tonal & film content.
- **"P4 dianggap disonan selalu"** — Dalam *vertical* species P4 ke C.F. bawah
  dianggap disonan; terhadap *bass* konteks berbeda.
- **"Kontra-melodi boleh sama ritme penuh"** — Pada *first species* ya; untuk
  kesan modern gunakan *independent rhythm* (species 4).
- **"Tie tidak perlu <tied>"** — Salah; keduanya (playback+visual) wajib agar
  software benar.

## 1.9 Latihan

1. **Dasar:** Tulis First Species 2-suara (8 not C.F. + counterpoint).
2. **Menengah:** Buat Second Species dengan satu *passing tone* disonan.
3. **Lanjut:** Gabungkan species 2–4 dalam 8 bar *florid*, capai kadens
   konsonan; validasi lewat music21.

## 1.10 Repertoar Dengar

- Palestrina, *Missa Papae Marcelli* — species dalam polifoni vokal.
- Bach, Two-Part Inventions BWV 772–786 (kontra-melodi).
- Fux curation: *Gradus ad Parnassum* examples.

## 1.11 Referensi Buku & Sumber Web

**Buku:**
- Fux, *Gradus ad Parnassum* (terj. Alfred Mann).
- Santa, *Counterpoint: A Species Approach*.
- Kennan, *Counterpoint* (modern).

**Web:**
- Music21 counterpoint module:
  https://web.mit.edu/music21/doc/
- MuseScore — braces/voices tutorial:
  https://musescore.org/en/handbook/

---

**Rangkuman:** Species 1–5 memberikan disiplin progresif: interval konsonan,
aksen, passing tone, suspension, dan florid. MusicXML mewakili tiap melodi
dengan `<voice>`/`<staff>` yang konsisten; ligasi menggunakan `<tie>` +
`<tied>`. Materi lanjutan: [Fugue & Bentuk Kontrapunktal
(`Ch2-Fugue-Form.md`)].
