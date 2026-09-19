---
title: "Mikrotonal & Custom Tuning"
tier: "Doctoral S3"
subject: "Psikoakustik & Spektral"
xml_tags: ["<pitch>", "<alter>", "<accidental>", "<microtone>", "<transpose>", "<sound>", "<tuning>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore", "OpenMusic"]
---

# Bab 2 — Mikrotonal & Custom Tuning

> **Buku panduan bab ini:** Ivan Wyschnegradsky, *La loi de la pansonorité*;
> Wilson THC; James Tenney, *A History of Consonance and Dissonance*;
> aplikasi practical dari OpenMusic & Dorico.
> Fokus: interval < semitone, tuning non-12-TET, dan just intonation dalam
> partitur.

## 2.1 Dasar Mikrotonal

Mikrotonal = interval lebih kecil dari semitone: quarter-tone, sixth-tone,
third-tone. Digunakan dalam elektronik, spektral, dan sistem non-Barat
(lihat `../3.3-Sistem-NonBarat-Etno/`).

| Interval | Ukuran | Contoh |
|----------|--------|--------|
| Quarter-tone | 50 cents | ¼ kruis/mol |
| Sixth-tone | 33.33 cents | Kupas split |
| Third-tone | 66.67 cents | 3-way |
| Just intonation | rasio | rasio rasional |

## 2.2 Quarter-Tone dalam MusicXML

MusicXML mengizinkan `<alter>` non-integer:

- `<alter>0.5</alter>` = sharp quarter (D#¼).
- `<alter>-0.5</alter>` = flat quarter (D♭¼).
- `<alter>1.5</alter>` = sesquisharp (×).

### 2.2.1 Contoh

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
        <pitch>
          <step>D</step>
          <alter>0.5</alter>
          <octave>4</octave>
        </pitch>
        <duration>2</duration>
        <type>quarter</type>
        <accidental>quarter-sharp</accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Nilai `accidental`: `quarter-sharp`, `quarter-flat`,
> `three-quarter-sharp`, `three-quarter-flat`.

## 2.3 Sixth-Tone dan Tanda Tambahan

MusicXML tak punya simbol sixth-tone standar — gunakan kolaborasi:

1. Ekstensi `accidental-mark` di notation.
2. Teks `1/6 tone` di `<direction><words>`.
3. Grafis slash di atas nota.

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
          <words xml:space="preserve">1/6-tone sharp</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Custom Tuning di Software

- **Dorico:** microtonal accidentals (`MusicXML` round-trip memberatkan),
  tuning center pitch.
- **Sibelius:** `MIDI note tuning` (keyswitch / tuning setting).
- **MuseScore:** plugin microtonal.
- **OpenMusic:** `micropitch` port -> MusicXML.

> Untuk ketepatan cents, dorong kode metadata: `<miscellaneous-field>`.
> Beberapa software menekan semitone mapping — cek peta.

## 2.5 Just Intonation (JI)

Rasio interval murni dari deret harmonik:

| Interval | Rasio | Cents | vs 12-TET |
|----------|-------|-------|-----------|
| Unison | 1:1 | 0 | 0 |
| Major second | 9:8 | 203.9 | +3.9 |
| Major third | 5:4 | 386.3 | −13.7 |
| Perfect fourth | 4:3 | 498.0 | −2.0 |
| Perfect fifth | 3:2 | 702.0 | +2.0 |
| Major sixth | 5:3 | 884.4 | −15.6 |

> **JI** memberi kesan jernih pada harmoni berhenti, tapi mengubah interval
> melodi vs ET. Gunakan `<alter>` berkorelasi cents + `accidental` custom,
> metadata di `<miscellaneous>`.

## 2.6 Sistem Tuning Utama

- **Equal temperament (12-TET):** tiap semitone 100 cents.
- **Mean-tone:** semitone ~96–100 cents (untuk M3 murni).
- **Pythagorean:** semua dari rasio 3:2 (pure perfect fifth).
- **Werckmeister/Kirnberger:** well-temperaments historis.

## 2.7 Glissando Mikro & Tekstur

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
        <duration>2</duration><type>half</type>
        <notations><glissando type="start"/></notations>
      </note>
      <note>
        <pitch><step>D</step><alter>0.5</alter><octave>4</octave></pitch>
        <duration>2</duration><type>half</type>
        <notations><glissando type="stop"/></notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Tekstur spektral: kolom pitch menerus dengan quarter-flat/sharp gradual.

## 2.8 Checklist Mikrotonal

| Periksa | Ya/Tidak |
|---------|----------|
| `alter` bernilai .5/1.5 pada pitch microtonal? | |
| `accidental` sesuai (quarter/three-quarter)? | |
| Sixth-tone ditandai teks? | |
| Dukungan font/playback dicek? | |
| Tuning (ET/just) terdokumentasi? | |

## 2.9 Miskonsepsi

- **"Microtone = tuning gagal"** — Sistem musik non-Barat & spektral memang
  non-12-TET.
- **"Semua software memahami `<alter>0.5`"** — Tidak; cek dukungan font &
  accidental.
- **"JI hanya untuk sejarah"** — Sering dalam spektral modern.

## 2.10 Latihan

1. Tulis 4 quarter-tone melody (2 sharp + 2 flat) → render.
2. Buat tabel cents tiap interval JI → validasi 1 progresi.
3. Eksperimen `alter=0.33` sixth-tone → audio semitone.
4. Rujuk maqam/raga (3.3) untuk aplikasi.

## 2.11 Referensi

- Wyschnegradsky, *La loi de la pansonorité*.
- Tenney, *A History of Consonance*.
- Scala (tuning files): https://www.huygens-fokker.org/scala/

---

**Rangkuman:** Mikrotonal & custom tuning memperluas 12-TET. MusicXML
mendukung quarter-tone via `<alter>` non-integer + `<accidental>`;
interval lain via teks & ekstensi. Lanjut ke [Komposisi Algoritmik
(`../3.2-Komposisi-Algoritmik/`)].