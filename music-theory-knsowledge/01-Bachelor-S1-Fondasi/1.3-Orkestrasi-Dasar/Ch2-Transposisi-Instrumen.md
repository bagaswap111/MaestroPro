---
title: "Transposisi Instrumen"
tier: "Bachelor S1"
subject: "Orkestrasi Dasar"
xml_tags: ["<transpose>", "<score-instrument>", "<attributes>", "<midi-instrument>", "<midi-channel>", "<octave-change>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Transposisi Instrumen

> **Buku panduan bab ini:** Rimsky-Korsakov, *Principles of Orchestration*
> (Bab "Instrumentation Tables"); Adler, *Study of Orchestration* (Bab 3–4,
> "Transposing Instruments"). Fokus: hubungan *written* vs *sounding*, rumus
> `<transpose>`, dan kesalahan umum saat templating.

## 4.1 Konsep: Konser vs Written

- **Konser (Sounding Pitch):** bunyi yang benar-benar terdengar — bahasa
  universal konduktor/analis.
- **Written (Notasi Pemain):** not yang ditulis — disesuaikan untuk klave/logika
  jari instrumen.

### 4.1.1 Rumus Dasar

```
Written = Konser + Interval (naik)
Sound   = Written − Interval (turun)   [untuk instrumen transpos]
```

| Instrumen | Jarak written vs konser |
|-----------|--------------------------|
| Clarinet/Trumpet in B♭ | written + Mayor2 (tonas+), sound − Mayor2 |
| Horn in F | written + Perfect5, sound − P5 |
| Alto Sax in E♭ | written + Major6 |
| Tenor Sax in B♭ | written + Major9 (oktaf + Mayor2) |
| Piccolo | sound + 1 oktaf atas written |
| Double Bass | sound − 1 oktaf written |

> Saat import partitur, matikan *concert pitch* untuk part-player; jelaskan
> perbedaannya saat menulis *score*.

## 4.2 Woodwind: Flute, Clarinet Bb, Alto Sax

### 4.2.1 Clarinet in Bb — Pemikiran Praktis

Clarinet in B♭ ditulis **+1 Mayor second**. Contoh konser C4 → written D4, dan
key signature naik satu flat/ruz:

| Konser | Clarinet Bb |
|--------|-------------|
| C major (0) | D major (+2♯) |
| G major (+1♯) | A major (+3♯) |
| F major (−1♭) | G major (+1♯) |

### 4.2.2 Struktur MusicXML untuk Clarinet Bb

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P3">
      <part-name>Clarinet in Bb</part-name>
      <part-abbreviation>Cl.</part-abbreviation>
      <score-instrument id="P3-I1">
        <instrument-name>Clarinet</instrument-name>
        <instrument-sound>pitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P3-I1">
        <midi-channel>4</midi-channel>
        <midi-program>71</midi-program>
        <volume>74.8031</volume>
        <pan>0</pan>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P3">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>2</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose>
          <diatonic>-1</diatonic>
          <chromatic>-2</chromatic>
          <octave-change>0</octave-change>
        </transpose>
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

### 4.2.3 Elemen `<transpose>` di dalam `<attributes>`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Clarinet in Bb</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>2</divisions>
        <key>
          <fifths>2</fifths>
        </key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose>
          <diatonic>-1</diatonic>
          <chromatic>-2</chromatic>
          <octave-change>0</octave-change>
        </transpose>
      </attributes>
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>8</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

- `<diatonic>-1</diatonic>` — turun 1 derajat skala (written→sound).
- `<chromatic>-2</chromatic>` — turun 2 semitone total (written D → sound C).
- `<octave-change>` — oktaf tambahan (untuk octave-transposing).

> **Ingat arah:** nilai **minus** = written lebih tinggi dari sound (dibunyikan
> lebih rendah). Clarinet Bb: written D terdengar C → `-2` semitone.

### 4.2.4 Cloning untuk Clarinet A, E♭, Bass Bass

| Alat | Interval (written → sound) | `<chromatic>` |
|------|----------------------------|---------------|
| Clarinet A | Minor3 (turun semitone 3) | -3 |
| Clarinet E♭ | Major6 (naik 9) | +9 (sound lebih tinggi) |
| Bass Clarinet B♭ | same as Bb | -2 |

## 4.3 Br sie (Horn F, Trumpet Bb)

### 4.3.1 French Horn in F

Ditulis +Perfect5 dari konser:

- Konser C3 → tertulis G3.
- Konser A4 → tertulis E5.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>French Horn in F</part-name>
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
          <diatonic>4</diatonic>
          <chromatic>7</chromatic>
          <octave-change>0</octave-change>
        </transpose>
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

> `+7` semitone = written lebih tinggi dari sound; horn F: tulis G terdengar C.
> Di MusicXML nilai **positif** menandakan sound lebih rendah dari written
> (instrumen "transposing down"). Verifikasi di software.

**Ledger line berlebih:** pindah ke register *notatable*:

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

### 4.3.2 Trumpet in Bb

Sama dengan klarinet B♭:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Trumpet in Bb</part-name>
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
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

- Range sounding: F#3 – C6; Range written: Ab4 – D7.
- Mute direpresentasikan per bagian `<direction><words>con sord.</words>`.

## 4.4 Octave-Transposing Instruments

| Instrumen | Tulisan vs bunyi | Clef |
|-----------|------------------|------|
| Double Bass | +1 oktaf (tulis lebih tinggi) | F |
| Piccolo | −1 oktaf (bunyi lebih tinggi) | G |
| Guitar | +1 oktaf | G |
| Celesta | −1 oktaf | G |

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
        <clef><sign>F</sign><line>4</line></clef>
        <transpose>
          <diatonic>-7</diatonic>
          <chromatic>-12</chromatic>
          <octave-change>-1</octave-change>
        </transpose>
      </attributes>
      <note>
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Contoh: bass guitar tertulis C3 → terbaca tengah 1 oktaf lebih rendah (C2);
> MusicXML `-12` semitone.

## 4.5 Transposisi dalam Praktik Orkestrasi (Rimsky)

- Klarinet B♭ dalam ensemble: registerual fleksibel; transposisi *automatic*
  di software namun keterampilan **menulis manual** penting saat pencil draft.
- Horn F: sistem notasi *traditional* bisa menggunakan × (old notation);
  waspada saat menggabungkan legacies.
- Trombone: **BC (bass clef non-transposing)** umum; TC (treble in B♭/cornet
  technique) dipakai brass band — selalu tandai di part-name.

## 4.6 Checklist Engraving Transposisi

| Langkah | Detail |
|---------|--------|
| 1 | Tentukan mode (concert vs written) |
| 2 | Salin transposisi per instrumen |
| 3 | Set clef + octave-change |
| 4 | Verifikasi via Concert Pitch toggle |
| 5 | Cek register ekstrem & ledger |

## 4.7 Miskonsepsi

- **"`<transpose>` mengubah note disimpan"** — Tidak; note disimpan *written*;
  `<transpose>` hanya dimakan saat playback/print.
- **"Horn F ditulis lebih rendah"** — Written selalu *lebih tinggi* (P5), tapi
  range rendah sulit notated.
- **"Semua instrumen transpos punya `<octave-change>`"** — Hanya octave
  transpos (bass, piccolo, guitar) yang perlu ±12.

## 4.8 Latihan

1. **Dasar:** Ubah C major melody 4 bar ke written clarinet (gunakan
   `<transpose>`).
2. **Menengah:** Buat part Horn F dari melodi konser, perhatikan register.
3. **Lanjut:** Tambah octave-change untuk double bass dan bandingkan
   *concert* vs *written* di playback.

## 4.9 Referensi Buku & Sumber Web

**Buku:**
- Rimsky-Korsakov, *Principles of Orchestration*.
- Adler, *Study of Orchestration*.

**Web:**
- MusicXML transpose spec:
  https://www.w3.org/2021/06/musicxml40/
- MuseScore handbook (transposition):
  https://musescore.org/en/handbook

---

**Rangkuman:** Transposisi = jembatan written↔sounding. MusicXML simpan
interval di `<transpose>` dalam `<attributes>`, didukung
`<score-instrument>`/`<midi-instrument>`. Lanjut: [Tekstur & Doubling
(`Ch3-Tekstur-Doubling.md`)].