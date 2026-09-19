---
title: "Parameter Genre Musik"
tier: "Bachelor S1"
subject: "Genre Fondasi"
xml_tags: ["<sound>", "<midi-instrument>", "<per-minute>", "<time>", "<metronome>", "<direction>", "<words>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore", "Daw (Logical Editor)"]
---

# Bab 1 — Parameter Genre Musik

## 1.1 Mengapa Genre Penting Bagi Arranger

Sebuah genre adalah **kumpulan konvensi bersama** — keputusan ritme, harmoni,
warna, bentuk, dan wilayah kerja — yang dikenali pendengar pertama kali.
Bagi arranger/komposer yang berorientasi MusicXML, memahami genre bukan soal
label, melainkan soal **prosedur penerjemahan**: pengetahuan tentang genre
langsung menentukan *bayo*, *voicing*, pilihan instrumen, bagian bentuk, dan
selanjutnya tag `<sound>`/`<direction>` yang ditulis ke file XML.

Rujukan silabus: silabus S1 menekankan *craft* — menyalin konvensi genre
adalah cara termurah untuk menjadi "cara berpikir" arranger (pendekatan
Walter Piston & Adler pada *style dictation*).

## 1.2 Parameter Pembeda Genre — "Dekoder Genre"

Saat mendengar/membaca musik, arranger dapat mendekode genre dengan enam
parameter ini. Urutasnya penting — tempo dan bayo adalah kunci paling cepat:

### 1.2.1 Tempo dan Groove

| Param | Pertanyaan | Contoh |
|-------|-----------|--------|
| Tempo (BPM) | Berapa kecepatan ketukan? | Ballad ≤80; Pop up-tempo 100–130; EDM 120–130; Rock 110–140 |
| Subdivisi | Ketukan terbagi 2, 3, atau *swing*? | Blues shuffle = triplet; Funk = 16th; Rock = 8th "straight" |
| Bakik (backbeat) | Di mana aksen 2 & 4? | Rock: snare on 2 & 4; Latin: clave; Jazz: ride cymbal |
| Mif chart sinkopasi | Di posisi berapa `off-beat`? | Funk: "1-e-&"; Pop: chorus kick 1&2&3&4& |

### 1.2.2 Sintaks Harmoni

Tiap genre memiliki kosakata akor dan aturan geraknya sendiri:

- **Klasik/tonal:** fungsi (T–S–D), modulasi, *secondary dominants*.
- **Blues:** harmoni **dominant 7** pada setiap derajat, *turnaround* I–IV–I–V.
- **Rock:** power chord (interval 5, tanpa 3rd), kadeng plagal IV–I.
- **Jazz:** ii–V–I, *substitution* (tritone sub), chord-scale, extension (9/11/13).
- **Funk/Soul:** akor *dominant* dengan 9th, *slash chords*, vamps pada satu harmoni.
- **Latin:** harmoni statis tetapi ritme kompeks; tonal umumnya mayor/minor dengan II–V.
- **EDM:** progresi ringkas (i–VI–III–VII), kadang hanya satu akor pada satu *drop*.

### 1.2.3 Bentuk (Form)

| Genre | Bentuk lazim |
|-------|--------------|
| Pop/rock | Intro–Verse–Pre-Chorus–Chorus–Bridge–Outro |
| Blues | 12-bar, 8-bar, 16-bar |
| Jazz | AABA, rhythm changes (AABA 32), 12-bar blues jazz |
| Funk/Soul | Vamp 4/8/16-bar, chorus ganda |
| Latin | Dal segno/coda, montuno, *coro* |
| EDM | Build–Drop–Break–Drop (4×8 bar) |
| March | I – Trio – I (modulasi ke subdominant di Trio) |

### 1.2.4 Matriks Instrumentasi

"Wajah" genre ditentukan ansambel intinya. Saat beradaptasi, arranger menyimpan
**fungsi suara**, bukan instrumen tertentu (lihat 1.5).

| Fungsi suara | Peran | Contoh instrumen lintas genre |
|--------------|-------|-------------------------------|
| Lead/Melodi | Kalimat utama | Vokal, terompet, sax, lead guitar, violin |
| Harmonic pad | Isian yang tidak bersaing | Piano-lhi, strings, guitar strum |
| Bass | Fondasi & bayo | Baterai-kick, bass upright, bass guitar, tuba |
| Rhythm/pump | Denyut & aksen | Baterai, cajón, djembe, gitar-ritme |
| Fill/email | Transisi & warna | Drums fill, horn stab, synth arpeggio |

### 1.2.5 Konvensi Notasi Musik

Setiap genre memiliki cara penulisan yang sudah dibakukan oleh praktisi:

- **Rock/pop:** notasi biasanya **interpretatif** — chord symbols di atas staf,
  gitar sebagai tab/rhythm box, drums pakai slash notation.
- **Jazz:** *lead sheet* (melodi + chords), notasi slash untuk comping,
  *head charts*, solos sebagai bagian tanpa not penuh.
- **Latin:** notasi clave eksplisit di cowbell/claves, part rhythm section
  lengkap dengan semua ketukan.
- **March/brass band:** tutti dinamis, not penuh, *palm-key/valve part*.
- **EDM:** part disusun oleh *grid* DAW; saat ditulis ke notasi perlu
  normalisasi 16th (lihat 4.3-MIDI-Quantization).

### 1.2.6 Bias Software

| Software | Kekuatan genre |
|----------|----------------|
| MuseScore | Notasi umum, cepat ekspor MusicXML, bagus untuk belajar |
| Dorico | Playback ekspresif, *engraving* terbaik, Layout versi paruh |
| Sibelius | Standard industri, plug-in; kuat untuk scoring orkestra & band |
| Finale | Legacy, macro; kini banyak beralih |
| DAW (Logic/Cubase) | Untuk EDM/groove → ekspor MIDI lalu bersihkan |

## 1.3 Representasi Genre dalam MusicXML

Genre **tidak diwakili satu tag khusus**. Sebagai gantinya, keputusan genre
menyebar ke banyak elemen:

### 1.3.1 Tempo — `<sound tempo>` dan `<metronome>`

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
          <words default-y="10">Swing</words>
        </direction-type>
        <sound tempo="126"/>
      </direction>
      <direction placement="above">
        <direction-type>
          <metronome>
            <beat-unit>quarter</beat-unit>
            <per-minute>126</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="126"/>
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

> Untuk *swing notation*, tetap tulis not sebagai 8th; swing di-handle playback
> lewat `<sound swing="eighth" first="third" second="third"/>` (dorico/XML 3.1)
> atau dengan *swing playback* DO-DO di MuseScore.

### 1.3.2 Warna — `<midi-instrument>` + `<sound>`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Electric Guitar</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Electric Guitar</instrument-name>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>27</midi-program>
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
        <rest/>
        <duration>16</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

Program MIDI 0–127 adalah "wajah" genre di playback (piano=0, e.bass=33,
strings=48, oboe=68, choir=52…). Konsistensi genre = konsistensi `instrument`
per part.

### 1.3.3 Notasi khusus genre

- **Slash notation (rock/jazz):** not dengan head `slash` (MuseScore/XML:
  `<notehead>slash</notehead>` di `<notehead>`), durasi sesuai ketukan.
- **Chord symbols (jazz/pop):** `<harmony>` — lihat `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch4-Harmony-Chord-Symbols.md`.
- **Percussion map (latin/march):** `unpitched` + `midi-unpitched` — lihat
  `../1.3-Orkestrasi-Dasar/Ch4-Notasi-Percussion.md`.
- **Ted berarti:** `<direction-type><words>"Swing 8ths"</words></direction-type>`
  sebelum bagian, dan lakukan *STC* (style-text-convert) di setiap software.

## 1.4 Roda Genre: Tujuh "Dial" Untuk Menulis Otomatis

Untuk menyusun draf genre cepat (dipakai di seluruh bab genre tier ini):

1. **Dial Tempo** → nilai BPM khas.
2. **Dial Groove** → pola 16th/8th triplet/straight + backbeat position.
3. **Dial Harmony** → kosakata akor + progresi model.
4. **Dial Form** → jumlah bar per bagian, layout section berulang.
5. **Dial Orchestration** → instrumen inti + register (matriks 1.2.4).
6. **Dial Dynamics** → rentang (pp–ff), aksen, *crescendo* awal.
7. **Dial Energy** → garis lengkung kepadatan (thinner intro → dense drop).

## 1.5 Adaptasi Lintas Instrumentasi — Metode "Fungsi Suara"

Kunci adaptasi genre (dipakai pada bab Ch2 setiap keluarga):

1. **Ekstrak 7 dial** dari genre sumber.
2. **Petakan 4 fungsi suara** (lead/pad/bass/rhythm) ke instrumen target.
3. **Terjemahkan idiom**: gitar-choke → string pizzicato; snare-backbeat →
   timpani-palstick; square-bass → tuba.
4. **Tulis ulang ritme**: sinkopasi 16th funk → divisi 16th di string, dll.
5. **Urutan register** agar tidak saling menutupi (penting di ansambel padat).
6. **Sesuaikan notasi**: chord symbols tetap, tapi menu rutin voicing dipindah.

Contoh singkat: **Blues 12-bar → String Quartet**

- Lead: Violin 1 (blues bends via glissando).
- Pad: Viola + Celli (voicing dominan 7 tanpa 3rd di register rendah).
- Bass: Cello (pizzicato walking — not `bend`).
- Rhythm: Violin 2 (off-beat accents, 8th straight).
- Notasi: tulis swing dengan `equal` sharps; play back dengan swing dll.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>String Ensemble</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <!-- Contoh: turnarounds blues dalam string (fragmen) -->
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <key><fifths>0</fifths></key>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>6</duration>
        <voice>2</voice>
        <type>quarter</type>
        <dot/>
      </note>
      <note>
        <pitch><step>D</step><octave>3</octave></pitch>
        <duration>4</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.6 Miskonsepsi Umum

- **"Genre = instrumen"** — Backbeat dua genre bisa sama, tapi warna berbeda.
  Genre ditentukan konvesi (tempo+bayo+harmoni+form), bukan hanya alat.
- **"Tempo tinggi = energik"** — Energi tidak selalu BPM; groove syncopation dan
  *density* juga menentukan. Funk sering "medan" di 90–110 BPM.
- **"Semua audio → MIDI = genre sama"** — Hasil transkripsi selalu netral;
  genre muncul saat arranger menerapkan kembali konvensi tempo/bayo.
- **"MusicXML tidak tahu genre"** — Betul, tapi arranger harus menanam genre lewat
  `tempo`, `instrument`, dan `direction text` agar software playback/siswa paham.

## 1.7 Latihan

1. **Dasar:** Sebutkan 7 dial untuk country (tempo, bayo, harmoni, dsb.).
2. **Menengah:** Pindahkan *idiom* piano boogie dari blues ke brass band:
   identifikasi 4 fungsi suara dan usulkan instrumen.
3. **Lanjut:** Tulis 4 bar *funk groove* (E9) di MusicXML: bass bass syncopation,
   klavin stabs, snare backbeat, dan tambahkan `<direction word>"Funk"` pada awal.

## 1.8 Repertoar Dengar

- Blues: Muddy Waters, *Hoochie Coochie Man* (1954).
- Rock: AC/DC, *Back in Black*; The Beatles, *Come Together*.
- Funk: James Brown, *Sex Machine*; Tower of Power, *What is Hip*.
- Jazz: Duke Ellington, *It Don't Mean a Thing*; Charlie Parker, *Ornithology*.
- Latin: Antonio Carlos Jobim, *Wave*; Tito Puente, *Oye Como Va*.
- EDM: Daft Punk, *One More Time*; Avicii, *Levels*.
- March: John Philip Sousa, *El Capitan*; Takashi Yoshimatsu, *Symphony*.
- Choral: Tallis, *Spem in Alium* (40 suara); Eric Whitacre, *Sleep*.

## 1.9 Referensi Buku & Sumber Web

**Buku (sesuai silabus):**
- Kostka & Payne, *Tonal Harmony* (McGraw-Hill) — kerangka fungsi/progresi lintas genre.
- Walter Piston, *Orchestration* (Norton) — fungsi suara instrumen.
- Samuel Adler, *The Study of Orchestration* (Norton) — matriks instrumentasi.
- Jack Wheaton, *Pro Sessions* (unsur) — genre populer.

**Web:**
- W3C MusicXML: https://www.w3.org/2021/06/musicxml40/
- MuseScore Handbook — swing & playback: https://musescore.org/en/handbook/
- Dorico Help — swing playback & MIDI: https://www.steinberg.net/help/dorico/
- Hooktheory (analisis harmoni progressions pop): https://www.hooktheory.com/

---

**Rangkuman:** Genre = konvensi tempo-bayo-harmoni-form-instrumentasi-notasi.
Ke dekat MusicXML tidak ada tag "genre", tapi arranger menanamnya lewat
`<metronome>`, `<sound>`, `<midi-instrument>`, dan teks `<direction>`. Semua bab
genre tier ini (1.5–1.8, 2.4–2.7) memakai kerangka 7-dial + 6-fungsi-suara yang
dibahas di sini. Lanjut ke [Blues (`1.5-Genre-Blues/`)].