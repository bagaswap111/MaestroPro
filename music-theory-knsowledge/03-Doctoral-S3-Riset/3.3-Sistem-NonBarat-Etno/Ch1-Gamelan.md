---
title: "Gamelan: Slendro & Pelog"
tier: "Doctoral S3"
subject: "Sistem Non-Barat & Etno"
xml_tags: ["<score-instrument>", "<instrument-sound>", "<transpose>", "<pitch>", "<per-time>", "<ornament>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Gamelan: Slendro & Pelog

> **Buku panduan bab ini:** Colin McPhee, *Music in Bali*; Sumarsam,
> *Gamelan: Cultural Interaction, and Musical Development in Central Java*;
> Kunst, *Music in Java*. Fokus: laras/interval, pathet (mode), notasi
> kepatihan, dan penerjemahan ke partitur Barat.

## 1.1 Laras Gamelan

| Laras | Jumlah Nada | Karakter | Notasi Cipher |
|-------|-------------|----------|----------------|
| **Slendro** | 5 | interval hampir rata | 1 2 3 5 6 |
| **Pelog** | 7 | interval tidak rata | 1 2 3 4 5 6 7 |

> Interval Slendro tak sama antar *set* gamelan — bersifat *tunable* per
> kraton. Pelog memiliki beberapa *pathet* (jenis mode).

## 1.2 Pathet (Mode)

| Pathet | Laras | Karakter |
|--------|-------|----------|
| Pathet Nem | Slendro/Pelog | tengah, bergerak |
| Pathet Sanga | Slendro | ringan, terbuka |
| Pathet Manyura | Slendro | klimaks, akhir |

> Pathet mengatur *penggunaan nada* dan hierarki nada penting — mirip mode
> tapi berbasis laras spesifik.

## 1.3 Notasi Gamelan — Kepatihan

Gamelan memakai **notasi ciphers** (kepatihan): angka 1–7 di atas baris,
tanda `-` untuk istirahat, titik `.` untuk oktaf. Tidak menggunakan staff.

Contoh baris slendro `1 2 3 - 5 6 5 3`.

### 1.3.1 Menerjemahkan ke Staff Barat

1. Pilih approksimasi laras ke 12-ET (atau set tuning custom).
2. Buat *custom instrument definitions* (gamelan tak ada di General MIDI).
3. Tandai laras & pathet di awal part.

## 1.4 Render Gamelan di MusicXML

### 1.4.1 Custom Instrument

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Saron</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Saron (Jawa)</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>0</midi-program>
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
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 1.4.2 Approksimasi Tuning

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Saron</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Saron (Jawa)</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>0</midi-program>
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
        <transpose>
          <chromatic>0</chromatic>
        </transpose>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Slendro tak bisa direpresentasi sempurna dalam 12-ET; gunakan sample
> gamelan khusus / tuning microtonal bila presisi dibutuhkan.

### 1.4.3 Menandai Laras/Pathet

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Saron</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Saron (Jawa)</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>0</midi-program>
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
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">Laras Slendro · Pathet Nem</words>
        </direction-type>
      </direction>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>quarter</type>
      </note>
      <note>
        <rest/>
        <duration>4</duration>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Struktur Form Gamelan

| Bagian | Fungsi |
|--------|--------|
| *Buka* | Pembuka (saron/bonang) |
| *Inggah* | Pergantian bagian |
| *Gongan* | Periode gong (tanda gong besar) |
| *Suwuk* | Penutup |

## 1.6 Aransemen Gamelan untuk Orkestra Barat

1. Terjemahkan: saron→celesta/xylophone, demung→bassoon, bonang→bell.
2. Tulis **key signature** approksimasi laras.
3. Gunakan *ornament* khas (gong strokes, kempul hits, graces).

## 1.7 Repertoar/Program

- **McPhee — Tabuh-Tabuhan** (1936): gamelan dalam orkestra.
- **Lou Harrison** — works with gamelan ensemble.
- **Bartók** — kutipan elemen modal (approksimasi).

## 1.8 Checklist Notasi Gamelan

| Check | Ya/Tidak |
|-------|----------|
| Laras/pathet dicantumkan? | |
| Custom instrument dibuat (bukan General MIDI)? | |
| Approksimasi tuning dinegosiasikan? | |
| Ornament gong/kempul ditandai? | |
| Terminologi form lokal diterjemahkan? | |

## 1.9 Miskonsepsi

- **"Slendro = pentatonik minor"** — Interval Slendro lebih mendekati
  ekuiton; bukan sekadar pentatonik Barat.
- **"Bisa dibuat dengan instrumen GM"** — Tubuh & teknik (mallet) tak
  terwakili GM.
- **"Pathet = key signature Barat"** — Ia lebih tentang fungsi nada dalam
  struktur, bukan sekadar skala.

## 1.10 Latihan

1. Tulis 8-bar slendro pathet manyura di MusicXML (cipher → staff).
2. Terjemahkan Saron→xylophone → bandingkan warna.
3. Susun peta custom instrument 5 instrumen gamelan.

## 1.11 Referensi

- McPhee, *Music in Bali*.
- Sumarsam, *Gamelan in Central Java*.
- Kunst, *Music in Java*.

---

**Rangkuman:** Gamelan memakai laras slendro/pelog non-Barat dan notasi
cipher. Di MusicXML salin lewat custom instrument, tanda laras, dan
approksimasi tuning — layak, meski tak instan. Lanjut ke [Maqam & Raga
(`Ch2-Maqam-Raga.md`)].