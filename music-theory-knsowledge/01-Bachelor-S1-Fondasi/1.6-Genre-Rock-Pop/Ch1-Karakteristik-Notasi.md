---
title: "Rock & Pop — Karakteristik & Notasi"
tier: "Bachelor S1"
subject: "Genre Rock & Pop"
xml_tags: ["<sound>", "<midi-instrument>", "<notehead>", "<stem>", "<direction>", "<words>", "<slur>"]
software: ["MuseScore", "Dorico", "Sibelius", "Guitar Pro", "TuxGuitar"]
---

# Bab 1 — Rock & Pop: Karakteristik & Notasi

## 1.1 Bahasa Rock-Pop: Kesederhanaan yang Presisi

Rock/pop membuktikan bahwa keterbatasan kosakata harmoni **tidak** berarti
keterbatasan efet. Dedicasi pada **groove, timbre, dan bentuk** menghasilkan
kekuatan emosi. Metrik: bentuk pop 32-bar, power chords, backbeat snare 2&4,
melodi *membumi pada ketukan* — beda dengan jazz (syncopated, 3rd tinggi).

### 1.1.1 Komponen Inti

1. **Backbeat** — snare/pad pada 2 & 4; pada drum `side stick`/`rimshot`.
2. **Elektro timbre** — distorsi gitar, synth pad, vocoder, auto-tune.
3. **Form ulang** — verse–pre-chorus–chorus–bridge–outro.
4. **Hook** — frase pendek mengulang (catchy riff) pada *instrumental figure*.
5. **Vokal sentral** — melodi prima (betah di tessitura), harmonisa pada chorus.

## 1.2 Power Chord dan Aplikasi MusicXML

Power chord = interval **root + 5th** (plus ±oktaf) tanpa 3rd → netral nada
mayor/minor. Ditulis dengan staf gitar/bass sebagai dua atau empat not.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Electric Guitar</part-name>
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
        <pitch><step>E</step><octave>2</octave></pitch>
        <duration>4</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations><technique><double-tongue/></technique></notations>
      </note>
      <note>
        <pitch><step>B</step><octave>2</octave></pitch>
        <duration>4</duration>
        <voice>1</voice>
        <type>quarter</type>
        <chord/>
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

> **Gitar akor box:** tulis small `chord frame` di atas staf (MuseScore:
> `Note → Fretboard`); representasi MusicXML `<frame>` di `<harmony>` untuk
> diagram.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Electric Guitar</part-name>
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
        <frame>
          <frame-strings>6</frame-strings>
          <frame-frets>5</frame-frets>
          <frame-note string="6" fret="0"/>
          <frame-note string="5" fret="2"/>
          <frame-note string="4" fret="2"/>
          <!-- E5 power chord shape -->
        </frame>
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

## 1.3 Groove Baterai — Notasi Rock

Pola dasar rock (ketukan = 8th di hi-hat, 2&4 snare, 1&3 bass drum):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P2">
      <part-name>Drums</part-name>
    </score-part>
  </part-list>
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <unpitched display-step="C" display-octave="5"/>
        <duration>1</duration>
        <voice>1</voice>
        <type>8th</type>
        <instrument id="P2-I1"/>
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

**Fungsi potongan (fundamental drum chart):**
- Bass drum (kick) — 1 & 3, plus *syncopation* di intro.
- Snare — 2 & 4 (`rimshot` articulation).
- Hi-hat — 8th/16th *closed* (ditulis < notehead "x" ).
- Crash/ride — aksen video (crash) awal *section*, ride = *swing*.

### 1.3.1 Half-Time Feel & Shuffle Rock

- **Half-time:** snare hanya pada ketuk 3 → bass drum pad pada 1&3 (feel lebih
  hei, fitur "slowed" pada metal-ballad).
- **Shuffle:** DC 2:1 pada hi-hat; dipakai pada *blues-rock* (Led Zeppelin).

## 1.4 Harmoni Pop — Progresi Universal

Studi Hooktheory (data ribuan lagu pop/EDM) menunjukkan progresi yang paling
sering: **I–V–vi–IV** (C–G–Am–F), yaitu "Axis of Awesome" (sebutan *four chord
song*). Variasi umum:

| Progresi | Suasana | Contoh |
|----------|---------|--------|
| I–V–vi–IV | Optimis/kelana | *Don't Stop Believin'* (Journey) |
| vi–IV–I–V | Terbalik, minor-lead | *Someone Like You* (Adele) |
| I–vi–IV–V | Nostalgik (50s) | *Earth Angel* |
| I–V–♭VII–IV | Borrowed (Mixolydian) | *Sweet Child O' Mine* (intro) |
| i–VI–III–VII | Minor rock (Epic) | *Zombie* (Cranberries) |

### 1.4.1 *Borrowed chords* & Mode

Rock sering berbagi **borrowed chords** dari mode paralel (C mayor ↔ C minor):
- ♭VII (Bb) — dorongan Mixolydian, sangat rock (Aeolian rock).
- ♭VI (Ab) — drama emosional.
- iv (Fm) — melankolis dalam konteks mayor.

Menulis di MusicXML: `<harmony>` + `<degree>` untuk alterasi; mode dinyatakan
lewat *accidental* pada melodi & progresi.

## 1.5 Aransemen Pop — Peta *Stacking*

Aransemen pop mengikuti aturan *spectral stacking*:

1. **Bass** di bawah, sederhana (root/5th, oktaf).
2. **Harmonik isi** ada di *mid* (piano/gitar/string pad).
3. **Lead** selalu di atas — bisa double 1 oktaf.

Urutan *intensity per section* ("build"):
- Verse: bass + vokal + cahaya pad, kompak.
- Pre-chorus: tambah snare 8th/16th, riser (crash roll).
- Chorus: penuh — drums, oktav lead, double vocal, busuk.

### 1.5.1 Replica Drop — Menulis *Fills* Transisi

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
    <measure number="32">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type><words>build — riser to bar 33</words></direction-type>
      </direction>
      <note>
        <rest/>
        <duration>4</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest/>
        <duration>12</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.6 Vokal Pop — Notasi dan Tessitura

- Jangkauan kerja pop: **A3–C5** (tenor-to-soprano umum), untuk solo sopran
  dengran luas hingga E5.
- **Harmoni chorus:** 3rd di atas melodi, kadang 5th change.
- **Bahasa melodi:** kata prosa di posisi 1-3 (kata penting di aksen kuat).
- Notasi melodi pakai *lead sheet*: melody only + chords (tidak lengkap vocal)

### 1.6.1 Double Tracking Vokal

Jika DAW vokal *double-tracked* (2 lagu), di MusicXML cukup 1 staf dengan `8vb`,
populasikan `<sound volume>` sesuai di klik. Label "vox doubled" di direction.

## 1.7 Miskonsepsi Umum

- **"Rock lemah harmoni"** — Lihat *borrowed ♭VII*, *minor 4th*, modulasi area
  — Rock punya harmoni khas (bukan less, lain).
- **"Power chord = 2 gitar saja"** — Bisa *1 atau 2 oktaf* (root+5th+octave);
  pada bass-guitar register rendah.
- **"Tempo pop selalu 100–120"** — Intro bisa 6/8; *half-time* mengubah feel.
- **"Notasi rock tidak penting"** — Notasi chord chart penting utk *live band*
  — arranger menulis konvensi alur semua bagian.

## 1.8 Latihan

1. **Dasar:** Tulis 4 bar *power chord* E5–A5–B5 untuk 2 gitar (AkorKings).
2. **Menengah:** Tulis pola drum 8-bar: intro (kitchen) → verse → fill bar 5.
3. **Lanjut:** Tulis *chorus doubling* (lead + harmony 3rd) + chorus hooks di
   MusicXML, tambah `<words>Build</words>` di bar penutup verse.

## 1.9 Repertoar Dengar

- Beatles, *Come Together*; *Hey Jude* (form + chorus hook).
- Led Zeppelin, *Whole Lotta Love* (riff + half-time break).
- AC/DC, *Back in Black* (straight 8th + riff).
- Radiohead, *Creep* (I–III–IV–iv borrowed).
- Taylor Swift, *Blank Space* / Adele, *Someone Like You* (progresi pop scalar).
- Billie Eilish, *bad guy* (bass 16th + half-time).

## 1.10 Referensi Buku & Sumber Web

**Buku:**
- Jörn Dietrich & medi, *The Pop Music Manual* (arranging).
- Don Muro, *The Art of Sequencing* (MIDI pop).
- Rikky Rooksby, *How to Write Songs on Guitar* (pop/rock progressions).
- Jack Wheaton, *Pro Sessions*.

**Web:**
- Hooktheory (analisis progresi): https://www.hooktheory.com/
- Hookpad visual (progresi + melodi):
  https://www.hooktheory.com/hookpad
- MuseScore Drum Notation (notasi drum standar):
  https://musescore.org/en/handbook/notation/drumset
- Dorico — playback/drum setup:
  https://www.steinberg.net/help/dorico/

---

**Rangkuman:** Rock/pop = kesederhanaan harmoni + presisi groove + bentuk
ulang + timbre. MusicXML menangani lewat `<frame>` untuk power chord guitar,
notasi perkusi `<unpitched>` untuk drum, `<harmony>` untuk progresi,
`<direction>` untuk marking build/drop. Lanjut ke [Adaptasi Rock/Pop Lintas
Instrumentasi (`Ch2-Adaptasi-Instrumentasi.md`)].