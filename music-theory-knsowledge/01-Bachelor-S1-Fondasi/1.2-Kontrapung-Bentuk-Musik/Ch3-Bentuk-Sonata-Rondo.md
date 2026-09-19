---
title: "Bentuk Sonata, Rondo, Tema & Variasi"
tier: "Bachelor S1"
subject: "Kontrapung & Bentuk Musik"
xml_tags: ["<direction>", "<words>", "<repeat>", "<rehearsal>", "<barline>", "<sound>", "<segno>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 3 — Bentuk Sonata, Rondo, Tema & Variasi

> **Buku panduan bab ini:** Percy Goetschius, *The Homophonic Forms of Musical
> Composition* (sumber teori bentuk klasik) dan *Lessons in Music Form*;
> Charles Rosen, *Sonata Forms* (sudut pandang modern). Fokus: drama harmonik
> skala besar — eksposisi, development, rekapitulasi, rondo, variasi.

## 3.1 Bentuk Sonata (Sonata-Allegro)

Bentuk yang mendominasi gerak pertama simfoni, sonata, kuartet, dan sonata solo
sejak Haydn→Beethoven. Keunikan: **konflik tonal** antara tema 1 (tonika) dan
tema 2 (key kedua), disinergi pada rekapitulasi.

### 3.1.1 Struktur Umum (Rosen / Goetschius)

| Bagian | Konten | Kunci |
|--------|--------|-------|
| **Exposition** | Tema 1 → *transition* → Tema 2 → *codetta* | I → V (atau relatif mayor) |
| **Development** | Fragmentasi motif, modulasi jauh, retransisi (dominant pedal) | bebas |
| **Recapitulation** | Tema 1→2 (kini di tonika) + coda | I |

### 3.1.2 Terminologi Pendukung

- **Bridge/Transition** — konektor sekaligus modulasi dari I ke II key.
- **Codetta** — penutup *small* eksposisi sebelum *repeat*.
- **Retransition** — jembatan kembali, biasanya *dominant pedal* (getaran).
- **Coda** — perluasan penutup (bisa mengembangkan tema).

### 3.1.3 Kunci Tema 2 pada Mode Minor

Dalam minor, tema 2 umumnya berada di **relatif mayor (III)** atau **dominan
minor (v)** — bukan dominant mayor seperti mayor.

### 3.1.4 MusicXML: Menandai Struktur + Repeat

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
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">Exposition</words>
        </direction-type>
        <sound tempo="120"/>
      </direction>
      <barline location="right">
        <bar-style>heavy-light</bar-style>
        <repeat direction="forward"/>
      </barline>
    </measure>
  </part>
</score-partwise>
```

> *Repeat* eksposisi lazim (klasik). Gunakan `<repeat direction="forward"/>`
> di awal, `direction="backward"` di akhir.

### 3.1.5 Variasi Klasik & Modern

- **Sonata-rondo** (Mozart, Beethoven): A–B–A–C–A–B'–A (rondo + sonata).
- **Slow-movement sonata** (tanpa development, A–B–A' pendek).
- **Ternary-like** recapitulation bisa memiringkan; Rosen menekankan pentingnya
  *arrival* tema 2 di tonika sebagai "resolution of the tonal drama".

## 3.2 Rondo

Struktur A–B–A–C–A–…–A dengan *refrain* berulang di antara couplets.

### 3.2.1 Contoh Mapping

| Birama | Bagian | Kunci |
|--------|--------|-------|
| 1–16 | A (Refrain) | I |
| 17–32 | B (First couplet) | V atau relatif mayor |
| 33–40 | A' | I |
| 41–64 | C (Second couplet) | vi / kunci jauh |
| 65–80 | A'' | I |
| 81–96 | Coda | I |

### 3.2.2 Prinsip Pengubahan Couplet

- *Contrast* setinggi ritme, register, orkestrasi.
- Jaga *transition* singkat ke couplet; *refrain* kembali tegas.
- Pada *sonata-rondo*, couplet B/S biasanya ditulis di dominan (bisa menjadi
  *tema 2*).

### 3.2.3 MusicXML: Refrain + Coda Navigation

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
      <barline location="left">
        <repeat direction="forward"/>
      </barline>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">Coda</words>
        </direction-type>
      </direction>
      <direction placement="below">
        <direction-type>
          <words xml:space="preserve">Da Capo al Coda</words>
        </direction-type>
      </direction>
      <barline location="right">
        <bar-style>dotted</bar-style>
        <segno/>
      </barline>
    </measure>
  </part>
</score-partwise>
```

## 3.3 Tema & Variasi

Pertahankan kerangka harmoni/melodi tema sambil mengubah tempat parameter.

### 3.3.1 Pendekatan Bergenre (Goetschius bab "Variation")

| Jenis variasi | Yang berubah |
|---------------|--------------|
| **Melodik / ornamentasi** | periasan kecil di melodi |
| **Harmonik** | reharmonisasi (tapi kerap mempertahankan *contour*) |
| **Ritmik** | triplet, turba, isorhythm |
| **Tekstural** | suara berganti (melodi+bass → akor padat) |
| **Register & mode** | oktav/mode (mayor→minor) |
| **Karakter** | tempo/agregat (Bach *Goldberg*) |

### 3.3.2 Struktur Variasi Umum (Classical)

- Varian menjaga **durasi total** dan **kadens** utama (langsung dipetakan).
- Beethoven (*Eroica* finale) mengurangi-becomes kontras; modern bebas.

### 3.3.3 MusicXML: Menandai Nomor Variasi

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
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">Var. III</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 3.4 Bentuk Terkait

| Bentuk | Struktur | Contoh |
|--------|----------|--------|
| **Ternary** | A–B–A | dikenal luas |
| **Binary** | A–B | suite dance |
| **Rounded binary** | A–B: A' | sonata-scale kecil |
| **Minuet & Trio** | A (minuet) B (trio) A (da capo) | Haydn Minuets |
| **Theme & Variations** | A–A1–A2–… | Mozart K.265 "Ah vous dirai-je" |
| **Passepied/Gigue** | Binary dgn karakter figuration | Bach suites |

## 3.5 Form Markers & Engraving Workflow

Saran hasil dari era dorico (integrity joints):

1. **Namai tiap section** — `<words>`, `<rehearsal>` di awal.
2. **Set tempo** literal di `<sound tempo>` (tak hanya tempo mark visual).
3. **Gunakan repeat/dc/segno** secara konsisten — jangan menumpuk DC manual.
4. **Cek "jump" solver** di software — pastikan `D.S. al Coda` benar.

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
      <direction placement="above">
        <direction-type>
          <rehearsal letters="A">A</rehearsal>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 3.6 Studi Kasus

- **Mozart, Piano Sonata K.545 I** — eksposisi jelas; tema 2 di G; development
  pendek — model pengajaran.
- **Mozart, Rondo alla Turca (K.331 III)** — A–B–A–C–…–A dengan coda virtuosik.
- **Beethoven, Symph. No.5 II** — *double variation* (dua tema bergantian,
  salah satunya lirik).
- **Bach, Goldberg Variations** — tessitura sistematis antar variasi.

## 3.7 Miskonsepsi Umum

- **"Sonata form = 3 bagian dengan repeat ganda"** — Repeat *tambahan*, bukan
  wajib; inti adalah kunci tema 2 + rekap konsiliasi.
- **"Rondo selalu di akhir"** — Sebagai *finale* umum, tetapi sonata-rondo
  bisa di mana saja.
- **"Variasi hanya melodi berornamen"** — Ada variasi tekstur/harmoni/mode;
  di Beethoven karakter/register yang didorong.
- **"MusicXML punya elemen section"** — Tidak ada `<section>`; gunakan
  `direction`+`words`/`rehearsal` dan repeat/segno untuk navigasi.

## 3.8 Latihan

1. **Dasar:** Petakan Rondo Mozart K.331 (III) dengan tabel 2.1 di 3.2.
2. **Menengah:** Tulis eksposisi sonata mini 16 bar: I–transition–V (+ repeat
   di `<barline>`).
3. **Lanjut:** Buat 3 variasi tema 8 bar (melodik, ritmik, tekstural); tandai
   `Var.` di MusicXML; pastikan server *playback* seamless.

## 3.9 Repertoar Dengar

- Mozart: K.545 I, K.331 III, String Quartet K.387 (sonata).
- Beethoven: *Waldstein*, *Eroica* II (double variation), Op. 111 II.
- Schumann, *Carnaval* — bentuk karakter pendek.
- Brahms, *Variations on a Theme of Haydn* (Op. 56a) — orkestra.

## 3.10 Referensi Buku & Sumber Web

**Buku:**
- Goetschius, *Lessons in Music Form* & *Homophonic Forms*.
- Charles Rosen, *Sonata Forms*.
- Wallace-Branham? pelajari untuk laju umum.

**Web:**
- Open Music Theory (form sections):
  https://openmusictheory.github.io/form/
- IMSLP: https://imslp.org/

---

**Rangkuman:** Sonata/rondo/variasi adalah *drama tonal* berskala besar.
MusicXML merepresentasikan struktur via `<direction>`+`words`/`rehearsal`,
`<repeat>`/`<segno>` untuk navigasi, dan `<sound tempo>` untuk parameter
playback. Lanjut ke Tier 1 berikutnya: [Orkestrasi Dasar
(`01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/`)].
