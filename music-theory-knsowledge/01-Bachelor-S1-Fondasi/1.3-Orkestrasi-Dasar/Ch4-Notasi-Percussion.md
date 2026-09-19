---
title: "Notasi Percussion"
tier: "Bachelor S1"
subject: "Orkestrasi Dasar"
xml_tags: ["<unpitched>", "<percussion>", "<score-instrument>", "<instrument-sound>", "<clef>", "<midi-unpitched>", "<midi-instrument>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 4 — Notasi Percussion

> **Buku panduan bab ini:** Adler, *The Study of Orchestration* (Bab 8–9 —
> percussion & battery, "Reading" mape); Rimsky-Korsakov (Bab IV — perale).
> Focus: membedakan pitched/unpitched, menulis `midi-unpitched` dengan benar
> agar lintas-software konsisten.

## 4.1 Jenis Perkusi

| Kategori | Contoh | Notasi MusicXML |
|----------|--------|------------------|
| **Pitched** | Timpani, Marimba, Vibraphone, Xylophone, Glockenspiel | `<pitch>` |
| **Unpitched** | Snare, Bass drum, Cymbal, Triangle | `<unpitched>` |
| **Hybrid (drum kit)** | kick, snare, hi-hat, tom, crash | `<unpitched>` + instrument attribution |

### 4.1.1 Klasifikasi Mallet/Bar Percussion

| Instrumen | Range sounding | Transposisi notation | GM-ish program (VST biasanya) |
|-----------|----------------|----------------------|-------------------------------|
| Timpani | D2 – F#3 | konser (F-clef) | — |
| Marimba | A2 – C7 | konser (G-clef) | 12 |
| Xylophone | F4 – C8 | ditulis 1 oktaf di bawah bunyi | 13 |
| Vibraphone | F3 – F6 | konser | 11 |
| Glockenspiel | G5 – C8 | ditulis 2 oktaf di bawah bunyi | 9 |

> Xylophone & Glockenspiel adalah *octave-transposing* — gunakan
> `<transpose>` (lihat `Ch2-Transposisi-Instrumen.md`).

## 4.2 Notasi Unpitched — Prinsip

- Tidak ada `<pitch>`; memakai `<unpitched>` dengan `display-step`/`display-octave`
  untuk posisi visual pada staff.
- Staff memakai clef `<sign>percussion</sign>`.
- **Satu `<score-instrument>` per bunyi berbeda** agar MIDI akurat
  (mis. snare vs kick dalam satu part).

### 4.2.1 GM Drum Mapping Standar (`<midi-unpitched>`)

| Instrumen | GM note | `<midi-unpitched>` |
|-----------|---------|--------------------|
| Acoustic Bass Drum (kick) | C2 (36) | 36 |
| Snare Drum | D1 (38) | 38 |
| Closed Hi-hat | F#1 (42) | 42 |
| Pedal Hi-hat | E1 (44) | 44 |
| Open Hi-hat | A#1 (46) | 46 |
| Low Tom | G1 (43) / A1 (45) | 45/47 |
| Ride Cymbal | D2 (51) | 51 |
| Crash Cymbal | C2 (49) | 49 |
| Triangle | E5 (81) | 81 |
| Tambourine | F#5 (54) | 54 |

### 4.2.2 Aplikasi MusicXML: Snare + Bass Drum dalam Satu Part

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P19">
      <part-name>Percussion</part-name>
      <part-abbreviation>Perc.</part-abbreviation>
      <score-instrument id="P19-S">
        <instrument-name>Snare Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <score-instrument id="P19-B">
        <instrument-name>Bass Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P19-S">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>38</midi-unpitched>
      </midi-instrument>
      <midi-instrument id="P19-B">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>36</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P19">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>2</duration>
        <instrument id="P19-S"/>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.2.3 Not dengan `<instrument>` Attribution

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P19">
      <part-name>Percussion</part-name>
      <part-abbreviation>Perc.</part-abbreviation>
      <score-instrument id="P19-S">
        <instrument-name>Snare Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <score-instrument id="P19-B">
        <instrument-name>Bass Drum</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P19-S">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>38</midi-unpitched>
      </midi-instrument>
      <midi-instrument id="P19-B">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>36</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P19">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>2</duration>
        <instrument id="P19-S"/>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>3</display-octave>
        </unpitched>
        <duration>2</duration>
        <instrument id="P19-B"/>
        <voice>2</voice>
        <type>eighth</type>
        <stem>down</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

> `<instrument>` menghubungkan not dengan salah satu `score-instrument` —
> wajib saat satu part punya banyak bunyi tak bernada.

## 4.3 Drum Kit Notation — Standar Posisi

Posisi staff yang umum (satu staff, clef percussion):

| Elemen | Posisi (umum) | GM |
|--------|---------------|-----|
| Kick | ruang di bawah (C3) | 36 |
| Snare | D4/E4 | 38 |
| Closed hi-hat | G5 (atas) | 42 |
| Open hi-hat | G5 + teknik | 46 |
| Tom high | B4 | 48 |
| Tom mid | A4 | 47 |
| Floor tom | F4/E4 | 43 |
| Ride | B5/F5 | 51 |
| Crash | B5 (atas, atau F#5) | 49 |

### 4.3.1 Contoh Hi-hat: 16-beat antara kick/snare

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P19">
      <part-name>Percussion</part-name>
      <part-abbreviation>Perc.</part-abbreviation>
      <score-instrument id="P19-H">
        <instrument-name>Hi-hat</instrument-name>
        <instrument-sound>unpitched</instrument-sound>
      </score-instrument>
      <midi-instrument id="P19-H">
        <midi-channel>10</midi-channel>
        <midi-program>0</midi-program>
        <midi-unpitched>42</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P19">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>G</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>1</duration>
        <instrument id="P19-H"/>
        <voice>1</voice>
        <type>16th</type>
        <stem>up</stem>
        <notations>
          <articulations>
            <staccato/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 4.4 Perkusi Bernada — Timpani & Mallet

### 4.4.1 Timpani

- Range per drum set di awal — tuning *ketetapan* via `<direction><words>`.
- F-clef, konser pitch.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P18">
      <part-name>Timpani</part-name>
    </score-part>
  </part-list>
  <part id="P18">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">D – A</words>
        </direction-type>
      </direction>
      <note>
        <pitch><step>D</step><octave>2</octave></pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.4.2 Timpani Note

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P18">
      <part-name>Timpani</part-name>
    </score-part>
  </part-list>
  <part id="P18">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
      <note>
        <pitch><step>D</step><octave>2</octave></pitch>
        <duration>4</duration>
        <instrument id="P18-I1"/>
        <voice>1</voice>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### 4.4.3 Mallet: Xylophone

- Notasi G-clef, konser tertulis 1 oktaf di bawah bunyi → `<transpose>` untuk
  playback (`diatonic -7`, `chromatic -12`).

## 4.5 Simbol Khusus & Teknik

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
        <duration>16</duration>
        <type>whole</type>
        <notations>
          <articulations>
            <accent/>
            <staccato/>
            <tenuto/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

Roll (buzz) snare — tremolo:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P20">
      <part-name>Snare Drum</part-name>
    </score-part>
  </part-list>
  <part id="P20">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <clef><sign>percussion</sign></clef>
      </attributes>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>16</duration>
        <type>whole</type>
        <notations>
          <ornaments>
            <tremolo type="start">2</tremolo>
          </ornaments>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 4.6 Percussion Map di Software

- **MuseScore:** Edit → Instruments → Drumset editor — map visual pitch.
- **Dorico:** playback templates; articulation per note.
- **Sibelius:** drum maps per part.
- **Import/export lintas-software:** pastikan `midi-unpitched` & `display-step`
  konsisten agar map tidak copot. Jangan membawa `<pitch>` pada not unpitched.

## 4.7 Checklist Percussion Engraving

| Periksa | Ya/Tidak |
|---------|----------|
| Clef percussion / timpani benar? | |
| Setiap unpitched punya `<midi-unpitched>` sesuai GM? | |
| Posisi display konsisten & dipahami pemain? | |
| Roll/teknik via articulations/tremolo tercatat? | |
| Timpani tertuning instruction? | |

## 4.8 Miskonsepsi

- **"Not unpitched boleh pakai `<pitch>`"** — Salah; pakai `<unpitched>` +
  `<midi-unpitched>` agar lintas-software benar.
- **"Satu part perc bisa mencampur banyak drum tanpa `<instrument>`"** — Akan
  terdengar satu program saja; wajib atribusi.
- **"Xylophone terdengar sesuai nota"** — Ia *transposes* 1 oktaf di atas;
  jangan lupa transposisi.

## 4.9 Latihan

1. **Dasar:** Tulis 4 bar drum kit standar (kick+snare+hat) dengan mapping GM.
2. **Menengah:** Buat part timpani 4 drum dengan tuning direction.
3. **Lanjut:** Export drum map dari MuseScore → import di Dorico; cek apakah
  posisi display & bunyi tetap konsisten; dokumentasikan perbedaan.

## 4.10 Repertoar Dengar

- Stravinsky, *The Rite of Spring* — perc section monumental.
- Ravel, *Bolero* — snare ostinato ikonik.
- Bartók, *Music for Strings, Percussion & Celesta*.

## 4.11 Referensi Buku & Sumber Web

**Buku:**
- Adler, *The Study of Orchestration*.
- Rimsky-Korsakov, *Principles of Orchestration*.

**Web:**
- General MIDI percussive family list:
  https://www.midi.org/specifications/
- MuseScore drumset handbook: https://musescore.org/en/handbook

---

**Rangkuman:** Perkusi dibedakan pitched/unpitched; MusicXML unpitched = 
`<unpitched>` + `<midi-unpitched>` + atribusi `<instrument>`, pitched = `<pitch>`
+ clef benar. Ini menutup Tier 1 [Orkestrasi Dasar]. Lanjut ke [Tier 2 —
Master S2 (`../../02-Master-S2-Lanjutan/`)].