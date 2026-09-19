---
title: "Film Scoring Notation"
tier: "Master S2"
subject: "Arranging Komersial & Film"
xml_tags: ["<direction>", "<words>", "<sound>", "<offset>", "<metronome>", "<bracket>", "<barline>", "<miscellaneous>"]
software: ["Dorico", "Sibelius", "Finale"]
---

# Bab 3 — Film Scoring Notation

> **Buku panduan bab ini:** Derrick Bang, *The Score* (jurnal); Mark Snow &
> Richard Davis, *On the Track: A Guide to Contemporary Film Scoring*
> (edisi revisi); Berklee film scoring material. Fokus: sinkronisasi video,
> tempo map, hit points, cue notes, dan praktik partitur konduktor.

## 3.1 Menandai Waktu Video dalam Partitur

| Elemen | Peran |
|--------|-------|
| Bar numbers & frame marks | margin part |
| Click track | metronome BPM terkotak |
| Streamers / pops | isyarat visual |
| Hit points (stings) | aksi → harmoni |

## 3.2 Click Track & Tempo Mapping

### 3.2.1 Tempo Freeze

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
          <metronome parentheses="no">
            <beat-unit>quarter</beat-unit>
            <per-minute>120</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="120"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### 3.2.2 Tempo Map Deployment (Snow)

- Hit ungkapan di *ketukan ke 0* tiap cue.
- Perubahan tempo sebelum bar berikutnya — `<offset>` divisions.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
          <words xml:space="preserve">accel. to 168</words>
        </direction-type>
        <offset>2</offset>
        <sound tempo="168"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 3.3 Format Partitur Konduktor

| Elemen | Detail |
|--------|--------|
| Header | title, film, cue number/length |
| BPM | nilai awal + perubahan |
| Bar numbers | per 4 bar (system) |
| Cue name | "M21 — Jungle Chase" |
| Navigation | D.S. al Coda, segno, da capo |

### 3.3.1 MusicXML: Cue Name

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
          <words xml:space="preserve">M21 — Jungle Chase</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

### 3.3.2 Bar numbering

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
      <print>
        <measure-numbering>system</measure-numbering>
      </print>
    </measure>
  </part>
</score-partwise>
```

## 3.4 Hit Points & Streamers

- **Hit point** — `H` di atas bar (teks), diibarat "sting" di downbeat.
- **Streamer** — garis vertikal; representasi teks.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
          <words xml:space="preserve">H! (hit on downbeat)</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

Praktik: buat tabel mapping this:

| SMTPE | Bar | Beat | Aksi |
|-------|-----|------|------|
| 01:00:12:00 | 34 | 1 | Explosion |
| 01:01:04:12 | 56 | 3 | Lockdown cue |

## 3.5 Sablona Orchestral untuk Film

1. Part-list: perc + (piano/celesta) + WW + Brass + Strings.
2. Concert pitch off di parts transpos (B♭/F/E♭).
3. Harp di part sendiri (bracket for pedal).

## 3.6 Cues dalam Partitur

`<cue/>` menandai not sebagai cue (tampil kecil, tidak dibunyikan).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
        <pitch><step>G</step><octave>4</octave></pitch>
        <duration>1</duration>
        <type>eighth</type>
        <cue/>
        <stem>up</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Beberapa software menampilkan cabe nota di belakang; name gagal di
> MusicXML — umum memakai sem dimensi.

## 3.7 Sinkronisasi dengan DAW/Video

| Parameter | MusicXML | Video ref |
|-----------|----------|-----------|
| Tempo | `<sound tempo>` | timebase |
| Bar | `number="N"` | frame |
| Offset | `<offset>` | frame grid |
| Hit | `<words>H</words>` | frame mark |

### 3.7.1 Frame Rate (SMPTE) — ekstensi

MusicXML tak memiliki elemen SMPTE; software menaruh ekstensi di
`<miscellaneous>`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Conductor</part-name>
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
      <miscellaneous>
        <miscellaneous-field name="frame-rate">24</miscellaneous-field>
      </miscellaneous>
    </measure>
  </part>
</score-partwise>
```

### 3.7.2 Konversi Frame→Beat

```
smpte_beat = (video_seconds * frame_rate - bar_start_frame) * tempo / 60
```

Simpan *tempo map* dari semua perubahan BPM — penting untuk import DAW.

## 3.8 Checklist Film Scoring

| Periksa | Ya/Tidak |
|---------|----------|
| Tempo map lengkap (BPM + perubahan)? | |
| Hit points di bar yang tepat? | |
| Cue notes dipakai untuk masuk? | |
| Frame rate/format dicatat? | |
| Bar numbers terlihat (system)? | |

## 3.9 Miskonsepsi

- **"Film score selalu rubato"** — Sering click-track + straights; rubato
  untuk momen individu.
- **"`<offset>` adalah detik"** — `offset` = divisions (nada), bukan saat;
  konversi via tempo.
- **"Crucial hits wajib not"** — H alias sting lawyer; visual text cukup.

## 3.10 Latihan

1. **Tempo map**: tulis cue M21 dari 100→140→150 dalam MusicXML.
2. **Hit point**: letakkan `H!` pada bar 34 downbeat + `chord symbol`.
3. **Cue notes**: beri 2 bar cue flute untuk masuk woodwind.
4. **Round-trip**: export → DAW, cek sinkronisasi.

## 3.11 Referensi

- Snow & Davis, *On the Track*.
- Bang, *The Score*.
- Berklee film scoring class material;
  https://online.berklee.edu/

---

**Rangkuman:** Notasi film = tempo map, hit points, cue notes, navigation;
direpresentasi via `<direction>`, `<offset>`, `<sound>`, `<cue/>`, dan
`<miscellaneous-field>` frame rate. Lanjut ke [Extended Techniques
(`../2.3-Extended-Techniques/`)].