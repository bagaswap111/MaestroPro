---
title: "Brass Band & March — Karakteristik & Notasi"
tier: "Bachelor S1"
subject: "Genre Brass Band & March"
xml_tags: ["<transpose>", "<score-part>", "<midi-instrument>", "<direction>", "<words>", "<dynamics>", "<unpitched>"]
software: ["MuseScore", "Dorico", "Sibelius", "Finale"]
---

# Bab 1 — Brass Band & March: Karakteristik & Notasi

## 1.1 Dua Dunia yang Sering Disandingkan

- **March band / wind band:** ansambel campuran (woodwind+brass+percussion)
  dengan tradisi *marching* dan form **Trio-Subdominant**.
- **Brass band Inggris:** *semua brass* (cornet, tenor horn, baritone,
  euphonium, tuba) + percussion, dengan skor terkhusus, notasi transposisi
  tradisional Inggris.

Penting bagi arranger: kedua tradisi punya **notasi transposisi dengan budaya
berbeda** (brass band Inggris: semua tenor/baritone/euphonium di treble clef
transpos B♭; orkestra: konser pitch / BC).

## 1.2 Forma March Klasik

Mengikuti model John Philip Sousa:

| Bagian | Karakter | Kunci |
|--------|----------|-------|
| **Intro** (2–4 bar) | Fanfare pendek, drumroll | Tonik |
| **1st Strain** (8) | Melodi | Tonik |
| **2nd Strain** (8) | Melodi | Tonik |
| **Trio** (16) | Lembut (contohnya kereta), kontras | Umumnya subdominant (F kalau B♭) |
| **Break-strain/Grandioso** | Fanfare besar / *grandioso* | Subdominant |
| **Repeats** | D.C. dan Trio alternatif | — |

Template notasi: tanda *segno*, *D.S.*, dan *coda* lazim di March.

## 1.3 Notasi Transposisi Brass Band Inggris

Telah dibakukan (Gilmore–Besson tradition):

| Instrumen | Clef & notasi | Transpos |
|-----------|---------------|----------|
| Soprano Cornet | Treble | B♭ |
| Cornet (solo/repiano/2/3) | Treble | B♭ |
| Flugelhorn | Treble | B♭ |
| Tenor Horn | Treble | E♭ |
| Baritone | Treble | B♭ |
| Euphonium | Treble (tradisi) | B♭ |
| Bass (Eb/BBb tuba) | Treble (tradisi) atau konser | transpos |
| Trombone | Konser (BC) | C |

**Aturan:** semua kecuali trombone/tuba ditulis treble transpos; composer
menulis konser lalu nada → transposisi naik 1 langkah (B♭) atau turun 1 langkah
better (E♭).

### 1.3.1 MusicXML: Transposisi B♭ di `<attributes>`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Cornet in Bb</part-name>
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
          <diatonic>-1</diatonic>
          <chromatic>-2</chromatic>
        </transpose>
      </attributes>
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

> **MusicXML menyimpan:** pitch di file harus ditulis **di apa yang dilihat
> pemain** (written), dan ada `<transpose>` yang memberitahu *written→concert*.
> Ketika music21/Dorico mengeluarkan part, mereka meng-hitung konser dari
> `score-instrument` + `transpose`.

## 1.4 Notasi Perkusi (Snare/Tamburin/Marching)

- **Snare:** staff satu baris, notehead `x` untuk rimshot, `o` untuk *open*,
  `•` untuk center; *roll* ditulis tremolo (`<tremolo>`).
- **Bass drum:** 5 karakter pada baris 1; *march bass* cenderung pada catatan
  (bass drum parts) — 2nd & 4th, disinkop.
- **Cymbal:** crash note panjang `<tie>`; *choke* text.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Snare Drum</part-name>
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
        <unpitched display-step="C" display-octave="5"/>
        <duration>3</duration>
        <type>8th</type>
        <dot/>
        <notations>
          <articulations><accent/></articulations>
        </notations>
      </note>
      <note>
        <rest/>
        <duration>13</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
        <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Harmoni March — Kesederhanaan Luas

Kosakata march adalah **tonal wajib**: I, IV, V, vi, ii, V7, kadang
`ff`-dominan. Modulasi halus (Veiner) di strain: dari tonik ke **subdominant**
di Trio.

Karakter timbral:
- **Bass brass** mendukung harmoni (tuba) + ritme (bass drum).
- **Cornet/trombone** membawa melodi dan *countermelodies*.
- **Woodwind** di band campur menulis *legato* embel (mendukung).

## 1.6 Aransemen: Menulis March yang Berlari

1. Pilih tempo 110–130 BPM duple (atau 6/8 avec) — march = **2-beat feel**.
2. Tulis melody 1st strain dalam 8 bar; gunakan *pickup* (upkeen).
3. Tambah *countermelody* di 2nd strain (Euph/BSn melawan cornet).
4. Trio = kontras (staccato, p, jump register).
5. Orchestrate: melodi+harmoni+kontra+bass dengan layout brass band.

### 1.6.1 Menulis Pickup (Anacrusis)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Cornet</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>2</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>B</step><octave>4</octave></pitch>
        <duration>1</duration>
        <voice>1</voice>
        <type>8th</type>
        <notations>
          <slur type="start" number="1"/>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.7 Miskonsepsi Umum

- **"Trombone part sama di semua band"** — Di tradisi Inggris trombone BC; di
  band marching ada 1–2 tenor treble. Cek convention satuan.
- **"March = fool tempo 120"** — Sousa 120–126; banyak march ditulis 114–120,
  slow-march 60–90.
- **"Brass band = fanfare trumpet semua"** — ansambel cornet/flugel/tenor
  horn; cornet 2/3 berperan pengisi harmoni.
- **"Kunci Trio = subdominant selalu"** — *Sering* tapi bukan hukum; kerajaan
  penggunaan *relative major/minor* juga muncul.

## 1.8 Latihan

1. **Dasar:** Tulis 8-bar 1st strain di B♭ major (2/4), tambah pickup.
2. **Menengah:** Buat *countermelody* 4 bar untuk euphonium melawan cornet lead.
3. **Lanjut:** Modulasi dari B♭ ke F di Trio (12 bar), tulis semua transposisi:
   cornet written vs concert.

## 1.9 Repertoar Dengar

- Sousa, *Stars and Stripes Forever*, *El Capitan*.
- Alexandra Fillmore, *Americans We*.
- Beethoven, *March Militaire* / Schubert marches.
- Brass band Inggris: Granada, Peter Graham.

## 1.10 Referensi Buku & Sumber Web

**Buku:**
- Samuel Adler, *The Study of Orchestration* (bab Brass Band).
- Mogens Ellegaard *Brass Band Composers Guide* (modern).
- David Whitwell, *A Concise History of the Wind Band*.

**Web:**
- Sousa Archives (partitur field):
  https://www.sousafoundation.net/
- Brass Band Scores (free contest):
  https://www.brassbandresults.co.uk/
- MuseScore March templates:
  https://musescore.org/

---

**Rangkuman:** Brass band/march = form strain–trio (subdominant), transposisi
tradisi Inggris (cornet B♭ treble), perceakan not unsurj 2-beat, dan notasi
perkusi. Di MusicXML transposisi dinyatakan `<transpose>` per part; layout part
masing-masing melodi/kompetensi/bass. Lanjut ke [Adaptasi Brass Band & March
(`Ch2-Adaptasi-Instrumentasi.md`)].