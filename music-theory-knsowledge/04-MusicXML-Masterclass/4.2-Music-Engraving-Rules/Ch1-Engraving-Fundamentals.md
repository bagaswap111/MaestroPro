---
title: "Music Engraving — Fundamentals"
tier: "MusicXML Masterclass"
subject: "Music Engraving Rules"
xml_tags: ["<note>", "<stem>", "<beam>", "<notations>", "<slur>", "<direction>", "<print>", "<octave-shift>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Engraving Fundamentals

> **Buku panduan bab ini:** Elaine Gould, *Behind Bars: The Definitive Guide to
> Music Notation* (Bab 1–8) — standar engraving modern; Roemer *The Art of
> Music Copying*. Focus: spacing, stem, beam, slur, ledger — prinsip dasar agar
> partitur terbaca cepat.

## 1.1 Apa Itu Engraving?

*Engraving* = seni mengatur elemen visual partitur: spacing, arah stem,
grup beaming, penempatan tanda. Tujuannya **readability** — minimal gerakan
mata, maksimal informasi.

Hubungan dengan MusicXML: MusicXML menyimpan *hint* layout; mesin layout
terakhir di software. Sebagai penulis XML, kita memberikan *structural*
petunjuk agar hasil render konsisten.

## 1.2 Structure `<note>` untuk Engraving

| Elemen | Fungsi visual |
|--------|---------------|
| `<stem>` | arah tangkai |
| `<beam>` | pengelompokan not cepat |
| `<notations>` | slur, tie, fingering, articulations |
| `<dot>` | titik nada |
| `<accidental>` | aksiden tampilan |

```xml
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>2</duration>
  <voice>1</voice>
  <type>quarter</type>
  <stem>down</stem>
  <beam number="1">begin</beam>
</note>
```

## 1.3 Spacing — Gould

| Elemen | Aturan |
|--------|--------|
| Horizontal | Semakin panjang nilai, semakin besar jarak antar-akor |
| Vertikal | Jarak staff disesuaikan agar tidak bertabrakan dengan ledger |
| Ties/tuplets | Tidak mendorong teks tajam; proper offset |
| Lyrics | spacing direncanakan bersama teks |

### 1.3.1 Kontrol Spacing di MusicXML

MusicXML tidak menyimpan *absolute* spacing; layout dihitung. `width` pada
measure memberikan sinyal lebar:

```xml
<measure number="1" implicit="no" width="640">
  ...
</measure>
```

> `width` dalam *tenths* — 10 tenths = 1 staff space. Gunakan konsisten bila
> Anda ingin memengaruhi *line break*.

## 1.4 Stem Direction (Arah Tangkai)

Aturan klasik (Gould ch. notes):

- Nada di bawah garis tengah → stem **up**.
- Nada di atas garis tengah → stem **down**.
- Pada garis → bergantung voice/konteks.
- Voice 1 umumnya up; Voice 2 down (dalam satu staff).

```xml
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>quarter</type>
  <stem>up</stem>
</note>
```

Nilai `<stem>`: `up`, `down`, `double`, `none`.

## 1.5 Beam Grouping (Grup Beaming)

*Beaming* harus mencerminkan meter:

| Meter | Grouping alami |
|-------|----------------|
| 4/4 | quarter per beat; 8ths boleh beamed 2 |
| 6/8 | per 3 eighths (beat) |
| 3/4 | beamed per beat (atau per half) |

### 1.5.1 Eighth pairs dalam 4/4

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>1</duration>
  <type>eighth</type>
  <stem>up</stem>
  <beam number="1">begin</beam>
</note>
<note>
  <pitch><step>D</step><octave>4</octave></pitch>
  <duration>1</duration>
  <type>eighth</type>
  <stem>up</stem>
  <beam number="1">end</beam>
</note>
```

- `beam number="1"` — primary (paling dekat nota head).
- `begin|continue|end|backward hook|forward hook`.
- 16th memakai `number="2"`, 32nd `number="3"`.

## 1.6 Slur dan Tie

| Simbol | Fungsi | MusicXML |
|--------|--------|----------|
| Slur | Legato antar pitch berbeda | `<slur>` |
| Tie | Nilai diperpanjang pitch sama | `<tied>` |

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>half</type>
  <notations>
    <tied type="start"/>
    <slur type="start" placement="above"/>
  </notations>
</note>
```

- `<slur>` & `<tied>` dalam `<notations>`; `type` start/stop.
- Slur placement: `above`/`below`, `number` untuk paralel.

## 1.7 Ledger Lines (Garis Bantu)

- Batas readability ~4 ledger lines.
- Solusi lebih baik: `8va`/`8vb`, ganti clef, atau *sub-staff*.

```xml
<direction placement="above">
  <direction-type>
    <octave-shift type="down" size="8"/>
  </direction-type>
</direction>
...
<direction placement="above">
  <direction-type>
    <octave-shift type="stop" size="8"/>
  </direction-type>
</direction>
```

- `octave-shift` display-only; pitch tidak berubah.

## 1.8 Engraving di Software (Gould-model practices)

| Software | Gaya |
|----------|------|
| **MuseScore** | manual power; default readable |
| **Dorico** | *engraving-first* logic; otomatis cerdas |
| **Sibelius** | plugins untuk spacing/manx |

Periksa selalu: pimp broom → zoom 100%, cek collision, alasan spacing antar
systems.

## 1.9 Checklist Fundamentals

| Periksa | Ya/Tidak |
|---------|----------|
| Stem direction konsisten register/voice? | |
| Beam grouping ikut meter? | |
| Slur/tie di `notations`+ placement benar? | |
| Ledger dibatasi (maks ~4)? | |
| Spacing width masuk akal? | |

## 1.10 Miskonsepsi

- **"MusicXML menyimpan spacing absolusi per not"** — Sebagian besar dihitung
  engine; XML hanya hint.
- **"`<stem>` wajib"** — Opsional; bila tidak ada, software menghitung sendiri.
- **"Tie boleh tanpa notations"** — Kali (belum) harus berpasangan.

## 1.11 Referensi

- Gould, *Behind Bars*.
- MusicXML W3C: https://www.w3.org/2021/06/musicxml40/
- MuseScore engraving handbook: https://musescore.org/en/handbook

---

**Rangkuman:** Fundamental engraving (spacing, stem, beam, slur, ledger)
dikendalikan di MusicXML lewat `<stem>`, `<beam>`, `<notations>` (`slur`/`tied`),
`<octave-shift>`, dan `width` pada measure. Lanjut ke [Engraving — Advanced
(`Ch2-Engraving-Advanced.md`)].