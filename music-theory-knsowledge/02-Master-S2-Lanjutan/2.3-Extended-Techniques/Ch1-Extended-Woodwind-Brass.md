---
title: "Extended Techniques — Woodwind & Brass"
tier: "Master S2"
subject: "Extended Techniques"
xml_tags: ["<note>", "<notations>", "<articulations>", "<technical>", "<words>", "<direction>", "<ornaments>", "<notehead>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Extended Techniques: Woodwind & Brass

> **Buku panduan bab ini:** Gardner Read, *Contemporary Instrumental
> Techniques*; libretto kontemporer (Berio, Sequenza); adopsi praktik dari
> IRCAM. Fokus: multiphonics, flutter, key clicks, mutes, microtonal —
> representasinya di MusicXML.

## 1.1 Konsep Extended Technique

*Extended technique* = cara bermain di luar kebiasaan untuk timbre baru;
pilar musik kontemporer & film design. Prinsip notasi: **jelas bagi pemain**,
karena banyak teknik tidak memiliki simbol baku — instruksi teks wajib.

## 1.2 Woodwind

### 1.2.1 Multiphonics

Dua+ nada berbunyi serentak via fingering khusus.

- Tulis kedua pitch (atau ritme diagonal) + `<words>multiph.</words>`.
- Fingering optional di bawah staff (angka/tabel).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
      <direction placement="below">
        <direction-type>
          <words xml:space="preserve">multiph.</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
        <pitch><step>D</step><octave>5</octave></pitch>
        <duration>2</duration><type>half</type>
      </note>
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>2</duration><type>half</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Pastikan dua not --- satu staff --- memakai `<voice>` berbeda; bila
> dibutuhkan durasi lebih pendek untuk salah-satu, gunakan chord semantic.

### 1.2.2 Flutter Tongue

Instruksi `flutter` / `frullato`; beberapa software mengenali
`<technical><tonguing>`; fallback words.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
      <notations>
        <articulations>
          <ornamental/>
        </articulations>
      </notations>
    </measure>
  </part>
</score-partwise>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
      <notations>
        <technical>
          <tonguing>flutter-tongue</tonguing>
        </technical>
      </notations>
    </measure>
  </part>
</score-partwise>
```

### 1.2.3 Key Clicks (Klak Tuts)

- Suara mekanis; `×` notehead pada tinggi tuts.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>1</duration>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
    </measure>
  </part>
</score-partwise>
```

> bila bunyi tak bernada, tambahkan `<technical><mute on="yes"/>`? Tidak —
> gunakan kata kunci `keyclick` dan posisi display.

### 1.2.4 Overblown & Singing While Playing

- **Overblown:** pitch + dynamic tinggi (`ff`), false harmonic.
- **Sing while playing:** dua baris — satu untuk whistle, satu untuk sengau.

## 1.3 Brass

### 1.3.1 Half-Valve / False Tones

Setengah valve = *false tones* (nada rendah nonharmonic). Tulis pitch terdengar
+ instruksi `half-valve`.

### 1.3.2 Mutes (Sordino)

| Mute | Efek | Instruksi |
|------|------|-----------|
| Straight | terang tajam | `con sord.` |
| Cup | lembut | `cup` |
| Harmon (wah) | nasal | `harmon` / `+ pedal` |
| Plunger | wah-wah | `plunger` |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
          <words xml:space="preserve">con sord.</words>
        </direction-type>
      </direction>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">senza sord.</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### 1.3.3 Lip/Valve Trill

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
        <duration>2</duration>
        <type>half</type>
        <notations>
          <ornaments>
            <trill/>
          </ornaments>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 1.3.4 Trombone Glissandi (Slide)

Glissando trombone = perubahan posisi slide kromatik:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
        <pitch><step>F</step><octave>3</octave></pitch>
        <duration>2</duration><type>half</type>
        <notations><glissando type="start"/></notations>
      </note>
      <note>
        <pitch><step>B</step><octave>3</octave></pitch>
        <duration>2</duration><type>half</type>
        <notations><glissando type="stop"/></notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Microtonal

- `<alter>0.5</alter>` → quarter-tone.
- Accidental custom `quarter-flat`/`quarter-sharp` saat dukungan font.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Woodwind</part-name>
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
          <step>E</step>
          <alter>0.5</alter>
          <octave>4</octave>
        </pitch>
        <duration>2</duration>
        <type>quarter</type>
        <accidental>quarter-flat</accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Di MusicXML sebagai `<accidental>`; rumus: alter 0.5 = quarter sharp,
> -0.5 = quarter flat. Beberapa font (SMuFL) mendukung simbol microtonal.

## 1.5 Penanganan di Software

| Software | Fitur Ext. |
|----------|------------|
| Dorico | symbol browser; playback skip |
| Sibelius | plugin ExtraTechniques |
| MuseScore | notehead ×, ornament simbol |

**Tip:** bila simbol tak ada, gunakan `<words>` + catatan kaki untuk teknik;
konsistensi paling penting daripada simbol unik.

## 1.6 Repertoar

- **Berio — Sequenza I** (flute): multiphonics, flutter, gliss.
- **Ligeti — Horn Trio**: harmonics & mutes.
- **Penderecki — Threnody**: teknik kluster brass.
- **Hindemith / Takemitsu** — wind colors.

## 1.7 Checklist

| Periksa | Ya/Tidak |
|---------|----------|
| Instruksi teknik jelas (teks)? | |
| × notehead key clicks benar? | |
| Multiphonics punya pitch + `multiph.`? | |
| Mute/una-mute diindikasikan? | |
| Microtone alter & accidental konsisten? | |

## 1.8 Miskonsepsi

- **"Mute didukung playback"** — TIDAK; hanya tulisan; sound via korpse map
  custom.
- **"Key click harus pakai pitch benar"** — sebaiknya display tujuan, bukan
  sounding necessarily.
- **"Flutter = ornament simbol cukup"** — pemain butuh kata `flutter` — 
  simbol tanpa kata ambigu.

## 1.9 Latihan

1. Tulis multiphonic flute (2 pitch) + `flutter` pada satu birama.
2. Buat mutes switching sequence pada trumpet (straight→cup→open).
3. Tulis microtonal E♭ quarter-flat di part clarinet, verifikasi.

## 1.10 Referensi

- Read, *Contemporary Instrumental Techniques*.
- Berio, *Sequenzas* (scores).
- SMuFL detail: https://www.smufl.org/

---

**Rangkuman:** Ext. woodwind/brass = multiphonics, flutter, key clicks, mutes,
microtonal. MusicXML via `<direction><words>`, `<notehead>`, `<technical>`,
`<ornaments>`, dan accidental microtonal (`alter=.5`). Lanjut ke [Extended
Strings (`Ch2-Extended-Strings.md`)].