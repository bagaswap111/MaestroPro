---
title: "Fugue & Bentuk Kontrapunktal"
tier: "Bachelor S1"
subject: "Kontrapung & Bentuk Musik"
xml_tags: ["<score-part>", "<part-list>", "<measure>", "<direction>", "<words>", "<repeat>", "<rest>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Fugue & Bentuk Kontrapunktal

> **Buku panduan bab ini:** Alfred Mann, *The Study of Fugue* (terj./antologi,
> W.W. Norton — sumber primer Marpurg, Albrechtsberger, Fux, Cherubini di dalam
> terjemahan); Kent Kennan *Counterpoint*. Fokus: struktur subject–answer–
> countersubject, episode, stretto, dan pedal point.

## 2.1 Konsep Fugue

*Fugue* = komposisi polifonik satu subject yang dinyatakan bergantian oleh
beberapa suara, dipertahankan kontrapungnya, diakhiri pada tonika. Puncak
Barok: J.S. Bach, *Art of Fugue* (BWV 1080) dan *Well-Tempered Clavier*
(BWV 846–869, 870–893).

## 2.2 Anatomi Fugue

### 2.2.1 Terminologi Inti

| Istilah | Definisi |
|---------|----------|
| *Subject* | Tema utama, di tonika |
| *Answer* | Subject pada dominan — *real* (persis) atau *tonal* (disesuaikan) |
| *Countersubject* | Kontra-melodi yang menyertai subject/answer, biasanya konsisten |
| *Exposition* | Semua suara masuk bergantian T→D→T→D |
| *Episode* | Proses sequence tanpa pernyataan subject penuh |
| *Stretto* | Subject masuk sebelum selesai → kanon |
| *Pedal point* | Nada dominan/tonika panjang di bass |
| *Codetta* | Kalimat kecil di antara entri exposition |
| *Augmentation/Diminution* | Perubahan nilai durasi subject |

### 2.2.2 Tiga Bagian Menyeluruh

1. **Exposition** — T, D, T, D (masing-masing) + countersubject.
2. **Middle section** — entri pada kunci relatif/dominant, dipisah episode.
3. **Final section** — stretto + pedal point + kadens tonika.

## 2.3 Exposition — Rule Setup

- **S0 (T)** mulai tonika; **S1 (D)** *answer* di dominan.
- **S2 (T)** kembali tonika dengan countersubject.
- **S3 (D)** dan seterusnya — ketat dalam "order depan /is".

### 2.3.1 MusikXML: Susunan Part per Suara

Fugue dalam MusicXML sebaiknya satu `<score-part>` per suara (vokal/instrumen),
bukan per instrumen fisik:

```xml
<part-list>
  <score-part id="P1">
    <part-name>Soprano</part-name>
  </score-part>
  <score-part id="P2">
    <part-name>Alto</part-name>
  </score-part>
  <score-part id="P3">
    <part-name>Tenor</part-name>
  </score-part>
  <score-part id="P4">
    <part-name>Bass</part-name>
  </score-part>
</part-list>
```

### 2.3.2 Tonal vs Real Answer

- **Real answer:** interval subject dipertahankan persis (beberapa medio-bench
  fugue). 
- **Tonal answer:** penyesuaian untuk menghindari *dominant key jump* yang
  drastic; umum bila subject melompat dari tonik ke dominan (V) atau ke
  subdominant (IV).

| Subject dimulai | Answer yang umum |
|-----------------|------------------|
| Tonika→Tonika | Real di dominan |
| Tonika→Dominan | Tonal (dorong ke subdom.) |
| Tonika→Subdom. | Tonal (kembali tonik) |

## 2.4 Episode dan Perlakuan Subject

- **Episode:** memakai *sequence* (naik/turun) yang *modulates* menuju kunci
  berikutnya. Episode sebaiknya **dipisahkan** dari entri subject dengan
  *cadence* ringan.
- **Perlakuan subject:**
  - *Inversion* — arah interval dibalik.
  - *Retrograde* — subject mundur.
  - *Augmentation/Diminution* — durasi dua kali / separuh.
  - *Stretto* — tumpang tindih.
- **Pedal point** pada dominan menciptakan *expectation* kembali ke tonika.

### 2.4.1 MusicXML: Menandai Entri Subject

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">Subject</words>
  </direction-type>
  <offset>0</offset>
</direction>
```

> Letakkan marka ini di awal setiap entri; untuk *answer* tulis "Answer".

## 2.5 Stretto dan Puncak

*Stretto* masuknya subject berikutnya *sebelum* yang sebelumnya selesai —
jarak 1–2 birama; semakin rapat semakin kuat tensinya. Dalam fugue Bach,
stretto terakhir biasanya diiringi kadens pedal point di dominan; suara
dipadatkan hingga *canon* sempurna (mis. *Art of Fugue*, Contrapunctus).

### 2.5.1 Cek via MusicXML/Penulisan

Untuk merencanakan stretto, buat *timeline* tabel:

| Birama | S1 (subject) | S2 (answer) | S3 (countersubject) |
|--------|--------------|--------------|---------------------|
| 1    | entri tonika | – | – |
| 3    | lanjut (real) | entri dominan | – |
| ... | – | – | entri |

## 2.6 Nada Diam antar Entri (Rests)

Suara yang belum masuk diberi `<rest/>` konsisten sampai entrinya:

```xml
<note>
  <rest measure="yes"/>
  <duration>4</duration>
  <voice>4</voice>
  <type>whole</type>
  <staff>4</staff>
</note>
```

## 2.6a Pengulangan Episoda (repeat)

```xml
<barline location="right">
  <bar-style>light-heavy</bar-style>
  <repeat direction="backward"/>
</barline>
<barline location="left">
  <repeat direction="forward"/>
</barline>
```

## 2.7 Analisis Fugue Bach (WTK I, BWV 846)

Prosedur analitik (Mann) yang bisa dipakai di score apa pun:

1. Tulis *subject* lengkap (not pertama).
2. Identifikasi *answer* dan jenisnya (real/tonal).
3. Temukan *countersubject* yang menyertai entri.
4. Petakan tiap entri subject + kunci (buat diagram jalur).
5. Tandai *episode*, *sequence*, dan *stretto*.
6. Catat *pedal* dan kadens puncak.

## 2.8 Kontrapung Lanjut: Inversi, Kanon, Triple Fugue

- **Inversi** — interval kebalikan dengan axis (contoh *Art of Fugue*).
- **Kanon** — entri imitatif identik mengejar (bisa tanpa modulasi).
- **Double/triple fugue** — dua/lebih subject diperlakukan setara; konflik
  disinegra menggunakan *countersubjects* masing-masing.

## 2.9 Miskonsepsi

- **"Fugue harus kompleks"** — Fugue dasar hanya satu subject dengan aturan
  ketat eksposisi; kompleksitas datang dari kontrapung yang hemat.
- **"Answer sempre tonal"** — Banyak fugue memakai *real answer*; tonal
  digunakan ketika subject mengutip nada dominan penting.
- **"Episode boleh sembarang = filler"** — Episode adalah *engine* modulasi;
  plotnya sequence yang diawasi dengan kadens.
- **"MusicXML menandai fugue otomatis"** — Tidak; hanya part/voice/repeat/
  direction. Analisis manual tetap komponen inti.

## 2.10 Latihan

1. **Dasar:** Tulis subject 8 not di C mayor; buat *real answer* di G.
2. **Menengah:** Bangun eksposisi 3-suara (T–D–T) dengan countersubject
   konsisten; susun part-list MusicXML.
3. **Lanjut:** Susun stretto interval 1 birama; tandai dalam score sebagai
   `<direction>`; bandingkan efek kepaduannya dengan versi non-stretto.

## 2.11 Repertoar Dengar

- Bach, *WTK I/II* — BWV 846, 847, 869.
- Bach, *Art of Fugue* BWV 1080 (Contrapunctus 1, 4, 9).
- Handel, *Fugue* dari *Suites* keyboard (HWV 426–433).
- Shostakovich, *24 Preludes & Fugues*, Op. 87 — fugue modern.

## 2.12 Referensi Buku & Sumber Web

**Buku:**
- Alfred Mann, *The Study of Fugue*.
- Kent Kennan, *Counterpoint*.

**Web:**
- IMSLP (score sumber): https://imslp.org/
- Music21 counterpoint: https://web.mit.edu/music21/doc/

---

**Rangkuman:** Fugue = satu subject (answer/real-tonal) + countersubject dan
struktur Eksposisi→Episode→Stretto→Pedal→Kadens. Dalam MusicXML layout-nya
adalah beberapa `<score-part>` + `<direction><words>` untuk entri + `<rest>`
untuk suara kosong + `<repeat>` untuk episode. Lanjut: [Bentuk Sonata & Rondo
(`Ch3-Bentuk-Sonata-Rondo.md`)].