---
title: "Blues — Karakteristik & Notasi"
tier: "Bachelor S1"
subject: "Genre Blues"
xml_tags: ["<harmony>", "<kind>", "<degree>", "<slur>", "<tie>", "<accidental>", "<glissando>"]
software: ["MuseScore", "Dorico", "Sibelius", "Finale"]
---

# Bab 1 — Blues: Karakteristik & Notasi

## 1.1 Akar dan Bahasa Blues

Blues lahir dari budayanya di Delta Mississippi dan berbagi DNA dengan
*work songs* serta *field holler* Afro-Amerika. Sebagai **bahasa musik**, esensi
aplikatifnya bagi arranger adalah:

1. **Blue notes** — b3, b5, b7 sebagai *flexible intonation* (sengaja
   "kotor"/blur), bukan harmoni kaku.
2. **Call-and-response** — melodi menjawab diri sendiri/pertanyaan.
3. **Shuffle feel** — ketukan terbagi triplet (long-short).
4. **Form responsif** — 12/16/24 bar dengan turnaround.

## 1.2 Forma Blues 12-Bar (Kanon)

Progresi standar (mayor):

| Bar | I | II | III | IV | V | VI | VII | VIII | IX | X | XI | XII |
|-----|---|---|----|----|---|---|-----|------|----|----|-----|-----|
| Akor | I7 | I7 | I7 | I7 | IV7 | IV7 | I7 | I7 | V7 | IV7 | I7 | V7 |
| C mayor | C7 | C7 | C7 | C7 | F7 | F7 | C7 | C7 | G7 | F7 | C7 | G7 |

**Turnaround** (bar 11–12) adalah mesin blues: I7–VI7–ii7–V7 (di C: C7–A7–Dm7–G7) yang
melemparkan ke awal. Dalam jazz blues, bar 9–10 menjadi **ii–V**: Dm7–G7 pakai
*substitution* C#dim7/Am7–D7 (lihat Levine, *The Jazz Theory Book*, bab 9).

### 1.2.1 Variasi: 8-bar & 16-bar

- **8-bar:** sering di gospel/R&B — I–IV–I–V per set pertama.
- **16-bar:** jazz/Dixieland (mis. *Basin Street Blues*).
- **Minor blues:** i7–iv7–i7–iv7–♭VII–i7 (i–iv–♭VII) dengan perubahan
  turnarounds; scale minor blues i–♭III–iv–♭V–♭VII.

## 1.3 Harmoni & Voice Leading Blues

Bahkan ketika harmoni 12-bar sederhana, *voice leading* (Aldwell–Schachter)
tetap dipakai: resolusi b7→3 di tiap *dominant*; pergerakan bass I–IV–I–V4–2?

- **Bentuk dominan penuh:** C7 = C–E–G–♭B. 3rd & 7th adalah *guide tones*
  (dieksekusi dengan cara yang sama di gitar, saksofon, piano).
- **Tritone substitution** (jazz blues): G7→D♭7 (bass turun setengah).
- **Chromatic approach** di baseline: C–B–♭B–A untuk transisi ke F7.

### 1.3.1 Contoh Voice-Leading pada Bar 9–10 (Jazz Blues)

Base line: D7 (bar 9) – C# (approach) – C7 (bar 10) – G7 (turnaround).
Voice 1: A–C#–E–G (D9) → G–A (C6). Menulis pakai `<harmony>` + `<degree>`.

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
    <measure number="9">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <harmony>
        <root><root-step>D</root-step></root>
        <kind>dominant</kind>
        <degree>
          <degree-value>9</degree-value>
          <degree-alter>0</degree-alter>
          <degree-type>add</degree-type>
        </degree>
      </harmony>
      <note>
        <rest/>
        <duration>16</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
    </measure>
    <measure number="10">
      <note>
        <rest/>
        <duration>16</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
    </measure>
    <measure number="11">
      <harmony>
        <root><root-step>G</root-step></root>
        <kind>dominant</kind>
      </harmony>
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

## 1.4 Blue Notes, Bends dan Glissando di Notasi

Blue notes **tidak selalu ditulis** di partitur asli (kontrol vokal/gitar tidak
pasti). Arranger menuliskan:

- **Dipilih (grace):** not kecil sebelum target — `grace` + `steal-time`.
- **Bend (gitar/bass):** `<glissando>` atau custom text `bend`.
- **Slur/fall-off:** `<slur>` (per not) + `falloff` articulation.
- **Half-valve/teknik:** text expression.

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
        <grace steal-time-previous="1/3"/>
        <pitch><step>E</step><alter>-1</alter><octave>4</octave></pitch>
        <duration>1</duration>
        <type>16th</type>
        <accidental>flat</accidental>
        <notations>
          <slur type="start" number="1"/>
        </notations>
      </note>
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>1</duration>
        <type>16th</type>
        <notations>
          <slur type="stop" number="1"/>
          <glissando type="start" number="1" line-type="wavy"/>
        </notations>
      </note>
      <note>
        <rest/>
        <duration>14</duration>
        <voice>1</voice>
        <type>half</type>
        <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Shuffle vs Straight — Menulis Swing Blues

| Gaya | Subdivisi | Contoh |
|------|-----------|--------|
| **Shuffle** | Triplet (8th = 2:1) | Muddy Waters, John Lee Hooker |
| **Straight 8th** | Dua 8th sama | Texas blues, some rock-blues |
| **Slow blues (12/8)** | Notasi dalam 12/8 | B.B. King, *The Thrill is Gone* |

Notasi shuffle: tulis 8th triplet (atau not 8th + `swing` dalam playback).
Di software: MuseScore `Swing playback %`; Dorico `Swing` text directive.

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
          <words>Shuffle (J = 104)</words>
        </direction-type>
        <sound tempo="104"/>
      </direction>
      <direction placement="above">
        <direction-type>
          <metronome>
            <beat-unit>quarter</beat-unit>
            <per-minute>104</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="104"/>
      </direction>
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

## 1.6 Ansambel Inti Blues

| Instrumen | Fungsi |
|-----------|--------|
| Gitar (lead/rhythm) | Riff, bends, comping |
| Harmonica | Melodi berjeda, blue notes (bend draw) |
| Piano/B3 | Barre chords, comping shuffle |
| Bass (upright/el.) | Walking/two-feel, riff |
| Drum | Shuffle, ca /* 2&4 pada snare* |
| Vokal | Call-and-response |
| Horn section (optional) | Riffs jawab — "stabs" dan "shouts" |

### 1.6.1 Horn Stabs (Riff Jawab) — Notasi

Stab = akor pendek 8th/16th pada *off-beat*. Tulis semua part bersam waktu
birama, tandai `staccatissimo` + `accent`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Trumpet</part-name>
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
        <duration>1</duration>
        <voice>1</voice>
        <type>16th</type>
        <notations>
          <articulations>
            <accent/>
            <staccatissimo/>
          </articulations>
        </notations>
      </note>
      <note>
        <rest/>
        <duration>15</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
        <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.7 Transkripsi Cepat Blues (Workflow)

1. Tentukan length form (12/16/24-bar) & grip (shuffle/straight).
2. Tulis bass pada bar 1–12 (walking/if lebih dari 8 bar).
3. Tambah *guide tones* (3rd/7th) di kiri-tengah register piano/horn.
4. Tambah stabs/accents pada *off-beat*.
5. Tambah *turnaround* dengan *substitution*.
6. Cek playback di MuseScore:
   `Playback → Swing → 55–66%`.

## 1.8 Miskonsepsi Umum

- **"Blues selalu 12 bar"** — Minor blues & 8/16-bar umum; beberapa blues (miss.
  Dallas blues) memakai 12 bar dengan komplikasi.
- **"Shuffle = triplet selalu"** — Shuffle swing dan *dotted-eighth* adalah
  pendekatan berbeda; pilih sesuai penampil.
- **"Chord 7 pada setiap derajat otomatis"** — Jazz blues menyuntikkan ii–V dan
  *secondary dominants*; notasi partitur modern menulis lebih dari 3 akor.
- **"Blue note = b3 selalu dimainkan halus"** — Blue note adalah *pitch flexible*;
  buatnya dengan *approach*, *bend*, bukan notaton antep-kaku.

## 1.9 Latihan

1. **Dasar:** Tulis 12-bar C blues (I7–IV7–I7–V7) ke MusicXML lengkap dengan `<harmony>`.
2. **Menengah:** Ganti bar 9–10 menjadi ii–V (Dm7–G7) dan tulis *turnaround*
   A7–Dm7–G7 di final bar.
3. **Lanjut:** Tambah bass walking (chromatic approach) di 4 bar terakhir dan
   tunjukkan dengan entry `<pitch><step>D</step><alter>1</alter>` + `approach`.

## 1.10 Repertoar Dengar

- Muddy Waters, *Hoochie Coochie Man* (1954) — shuffle Delta.
- B.B. King, *The Thrill is Gone* — slow 12/8.
- John Lee Hooker, *Boogie Chillen* — boogie, minimal changes.
- Duke Ellington, *C Jam Blues* — jazz blues instrumental.
- John Coltrane, *Blues by Five* — jazz blues dengan turnaround kompleks.

## 1.11 Referensi Buku & Sumber Web

**Buku:**
- Mark Levine, *The Jazz Theory Book* (Sher Music) — bab Blues & Trane Changes.
- Kostka & Payne, *Tonal Harmony* — bentuk & progresi dasar.
- Bill Evans, *The Universal Mind of Bill Evans* (transkrip) — blues approach.
- David Baker, *The BB&J Blues Suite* — für arranging blues.

**Web:**
- Hooktheory — analisis progresi blues:
  https://www.hooktheory.com/theorytab/artists
- Jazzadvice "Minor Blues Playbook":
  https://www.jazzadvice.com/
- Freelib — koleksi MIDI blues untuk dianalisis: https://freemididownload.com/

---

**Rangkuman:** Blues = 12-bar + shuffle + blue notes + call-and-response.
Di MusicXML wujudnya adalah `<harmony>` yang jelas, `<slur>`/`<glissando>` untuk
bends, `swing` text untuk blues feel, dan notasi ``staccatissimo`` untuk stabs.
Lanjut ke [Adaptasi Blues Lintas Instrumentasi (`Ch2-Adaptasi-Instrumentasi.md`)].