---
title: "Extended Techniques — Percussion"
tier: "Master S2"
subject: "Extended Techniques"
xml_tags: ["<note>", "<unpitched>", "<percussion>", "<technical>", "<words>", "<direction>", "<notehead>", "<midi-unpitched>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Extended Techniques: Percussion

> **Buku panduan bab ini:** Gardner Read, *Contemporary Percussion*;
> John H. Beck, *Encyclopedia of Percussion*; John Cage, *prepared piano*
> notes. Fokus: instrumen tak biasa, prepared piano, teknik non-standar,
> setup/peta perkusi MusicXML.

## 3.1 Perkusi Tak Biasa & "Perkusi" Baru

Extended percussion mencakup:

- Eksploitasi bagian nonumum: rim, frame, rods.
- Instrumen nonkonvensional: logam, kayu, plastik, benda sehari-hari.
- Body percussion (tap, chest thump) — tanpa MIDI mapping; tulis instruksi.

## 3.2 Prepared Piano (Cage)

Objek diletakkan di senar piano mengubah timbre.

### 3.2.1 Notasi Umum

- Instruksi awal part; perubahan `prepared with ...` / `remove preparation`.

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">Prepared: 3 screws on C4–E4 str.</words>
  </direction-type>
</direction>
```

### 3.2.2 Teknik String Piano

- *String pizz.* — petik langsung.
- *Knock body* — rapan badan pianof.
- *Silent depression* — tahan senar tanpa bunyi.

## 3.3 Extended Percussion Techniques

| Teknik | Keterangan | Notasi |
|--------|------------|--------|
| Bowed cymbal/gong | gesek senar bow | `arco` |
| Rim shots | mallet + rim | `rim shot` (GM 37) |
| Mallet roll | tremolo cepat | tremolo |
| Double-stops | dua mallet | dua not / split |

### 3.3.1 Bowed Cymbal

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">bow cymbal (arco)</words>
  </direction-type>
</direction>
```

### 3.3.2 Tremolo Mallet

```xml
<note>
  <pitch><step>G</step><octave>5</octave></pitch>
  <duration>4</duration>
  <type>whole</type>
  <notations>
    <ornaments>
      <tremolo type="start">3</tremolo>
    </ornaments>
  </notations>
</note>
```

## 3.4 Stage Techniques

- **Dampened scrubbing** — tangan menutup head → buzz.
- **Cymbal stacks** — multi cymbal bertumpuk.
- **Choked crashes** — pencetan setelah bunyi.
- Bila simbol tak tersedia → `<technical>` + boxed text instruction.

## 3.5 Menulis Setup Perkusi (Percussion Map)

Setiap elemen punya `score-instrument` + `midi-unpitched` mapping GM:

```xml
<score-instrument id="P01-H">
  <instrument-name>Hi-hat (pedal)</instrument-name>
  <instrument-sound>unpitched</instrument-sound>
</score-instrument>
<midi-instrument id="P01-H">
  <midi-channel>10</midi-channel>
  <midi-program>0</midi-program>
  <midi-unpitched>44</midi-unpitched>
</midi-instrument>
```

> Kick=36, Snare=38, Hi-hat closed 42 / pedal 44, Ride=51, Crash=49, Tom
> 45/47/48/50.

### 3.5.1 Setup Dokumentasi di Awal Part

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">Setup: 4 drums + 3 cymbals (hi-hat, ride, crash)</words>
  </direction-type>
</direction>
```

## 3.6 Multi-Staff Percussion

Saat setup > 4 elemen, gunakan beberapa staf:

| Staf | Isi |
|------|-----|
| Staf 1 | Mallet / pitched (timpani/marimba) |
| Staf 2 | Battery (snare/kick/hihat) |

MusicXML: `<staves>2</staves>` + `staff` pada tiap note.

## 3.7 Repertoar

| Karya | Teknik |
|-------|--------|
| **Varèse — Ionisation** | drum + sirens; non-pitched |
| **Cage — Sonatas & Interludes** | prepared piano |
| **Reich — Music for 18 Musicians** | mallet phasing |
| **Xenakis — Psappha** | 6 percussion + frictions |

## 3.8 Checklist

| Periksa | Ya/Tidak |
|---------|----------|
| Setup unik didokumentasikan? | |
| Tiap elemen `midi-unpitched` benar? | |
| Tremolo/roll slash benar? | |
| Instruksi bow/arco di part jelas? | |
| Preparasi piano dijelaskan teks? | |

## 3.9 Miskonsepsi

- **"Prepared piano perlu MIDI khusus"** — Musik disimpan normal di pitch;
  prepared ge mapped oleh performer/teknis.
- **"Semua perkusi = unpitched"** — Timpani/marimba pitched; mapping berbeda.
- **"Setup satu staf cukup"** — Untuk kompleks memakai multi-staff.

## 3.10 Latihan

1. Tulis bentar bagian perc extended (bow cymbal + rim shot).
2. Buat setup prepared piano 3 objek → instruksi part.
3. Map 4 elemen perkusi ke MusicXML multi-staff.

## 3.11 Referensi

- Read, *Contemporary Percussion*.
- Beck, *Encyclopedia of Percussion*.
- Cage, *Sonatas & Interludes* (preparation notes).

---

**Rangkuman:** Ext. percussion = prepared piano, bowed/rim/roll, instrument
nonkonvensional; MusicXML via `score-instrument`/`midi-unpitched` map, `<words>`
instruksi, tremolo. Ini menutup Tier 2 ([Master S2]). Lanjut ke [Tier 3 —
Doctoral S3 (`../../03-Doctoral-S3-Riset/`)].