---
title: "Struktur Root dan Score-Partwise"
tier: "MusicXML Masterclass"
subject: "Anatomi MusicXML"
xml_tags: ["score-partwise", "work", "identification", "part-list", "credit", "measure", "score-instrument"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Struktur Root & Score-Partwise

> **Buku panduan bab ini:** Michael Good, "MusicXML: An Internet-Friendly
> Format for Sheet Music" (makalah pendiri); *MusicXML W3C spec* 4.0
> (chapter *Quick Start*). Gould, *Behind Bars* (Bab 6 — score layout) untuk
> perspektif engraver. Fokus: hierarki dokumen `score-partwise` dan metadata
> untuk pertukaran antar-software.

## 4.1 Score-Partwise vs Score-Timewise

| Format | Struktur | Penggunaan |
|--------|----------|------------|
| `score-partwise` | `<part>` → seluruh `<measure>` per part | Dominan (semua app exporter) |
| `score-timewise` | `<measure>` → seluruh `<part>` | Alur waktu / layout transformasi |

> Dokumen partwise lebih natural untuk engraving; kebanyakan library parser
> (music21) multi-menyokong *partwise* terlebih dahulu.

## 4.2 Elemen Root dan Header

```xml
<?xml version="1.0" encoding="UTF-8"?>
<score-partwise version="4.0">
  <work>
    <work-title>Simfoni No. 1</work-title>
    <work-number>Op. 1</work-number>
  </work>
  <identification>
    <creator type="composer">J. S. Bach</creator>
    <creator type="poet">—</creator>
    <rights>Public Domain</rights>
    <encoding>
      <software>Dorico 5.0</software>
      <encoding-date>2026-01-15</encoding-date>
      <supports element="accidental" type="yes"/>
    </encoding>
  </identification>
  <defaults>
    <scaling>...</scaling>
    <page-layout>...</page-layout>
  </defaults>
</score-partwise>
```

### 4.2.1 Rutinitas `<work>` & `<identification>`

- `<work-title>` — judul besar.
- `<work-number>` / `<opus>` — nomor opus (opsional).
- `<creator type="...">` — composer/arranger/lyricist, bila pengisi.
- `<rights>` — copyright/license (mis. CC0/Public Domain).
- `<encoding>` — software producer + tanggal + `<supports>` (fitur yang
  didukung export).

> Praktik baik: selalu isi `<encoding>` dengan versi software & tanggal agar
> *round-trip* bisa di-debug lintas aplikasi.

## 4.3 `<part-list>` dan `<score-part>`

Daftar instrumen — urutan = urutan score staves. Gugus dipanggil
`<part-group>`.

```xml
<part-list>
  <part-group number="1" type="start">
    <group-name>Woodwinds</group-name>
    <group-symbol>bracket</group-symbol>
  </part-group>
  <score-part id="P1">
    <part-name>Flute</part-name>
    <part-abbreviation>Fl.</part-abbreviation>
    <score-instrument id="P1-I1">
      <instrument-name>Flute</instrument-name>
      <instrument-sound>pitched</instrument-sound>
      <virtual-instrument>
        <virtual-library>EastWest</virtual-library>
        <virtual-name>EW Flute</virtual-name>
      </virtual-instrument>
    </score-instrument>
    <midi-instrument id="P1-I1">
      <midi-channel>1</midi-channel>
      <midi-program>73</midi-program>
    </midi-instrument>
  </score-part>
  <score-part id="P2">
    <part-name>Oboe</part-name>
    <part-abbreviation>Ob.</part-abbreviation>
  </score-part>
  <part-group number="1" type="stop"/>
</part-list>
```

> `id` part (P1, P2, ...) adalah **kunci referensi** ke `<part id="P1">`.
> `score-instrument` boleh lebih dari satu untuk divisi/perkusi multi-sound.

## 4.4 Struktur `<part>` dan `<measure>`

```xml
<part id="P1">
  <measure number="1" implicit="no" non-controlling="no">
    <attributes>
      <divisions>2</divisions>
      <key><fifths>0</fifths></key>
      <time><beats>4</beats><beat-type>4</beat-type></time>
      <clef><sign>G</sign><line>2</line></clef>
    </attributes>
    <note>
      <pitch><step>C</step><octave>4</octave></pitch>
      <duration>2</duration>
      <type>quarter</type>
    </note>
  </measure>
  <measure number="2">
    ...
  </measure>
</part>
```

- `implicit="yes"` → birama tanpa nomor (pickup bar awal).
- `non-controlling="yes"` → birama yang tidak menambah progress (untuk
  highlighting / rehearsal numbering).
- `<attributes>` di awal tiap perubahan: divisions, key/time, clef.

## 4.5 `<credit>` dan Metadata Tambahan

Diukur dalam *tenths of staff space* relatif terhadap halaman. Format:

```xml
<credit page="1">
  <credit-type>title</credit-type>
  <credit-words default-x="300" default-y="600" font-size="24" font-style="bold">Judul Karya</credit-words>
</credit>
<credit page="1">
  <credit-type>composer</credit-type>
  <credit-words default-x="70" default-y="120">Diteliti & diarans.</credit-words>
</credit>
```

- `<credit-type>`: `title`, `subtitle`, `composer`, `arranger`, `lyricist`,
  `rights`, `part-name`.
- Multiple `<credit-words>` bisa dalam satu `<credit>`.

## 4.6 Urutan Elemen di Root (Schema-valid)

1. `<?xml ... ?>` (prolog opsional)
2. `<work>` (opsional)
3. `<movement-number>` / `<movement-title>` (opsional)
4. `<identification>` (opsional)
5. `<defaults>` (opsional)
6. `<music>` → `part-group`, `credit`, `part-list` ... (versi 4.0)
7. `<part>`* 
8. `</score-partwise>`

> **Catatan versi 4.0:** layout/credit sekarang boleh muncul di dalam elemen
> `<music>`; tetap urutan schema dipertahankan. Praktik: selalu `version="4.0"`
> agar tidak ambigu.

## 4.7 Validasi Mini (Round-Trip)

1. `version="4.0"` pada root.
2. `id` part-list konsisten dengan `<part id>`.
3. Jumlah `<part>` = jumlah `<score-part>`.
4. `measure number` unik per part, naik urut.
5. `divisions` konsisten per part.

### 4.7.1 Verifikasi dengan music21

```python
import music21
s = music21.converter.parse("file.mxl")
for p in s.parts:
    print(p.id, p.measureNumber)
```

## 4.8 Checklist Struktur Root

| Periksa | Ya/Tidak |
|---------|----------|
| Root `<score-partwise version="4.0">`? | |
| `<work>`/`<identification>`/`<credit>`? | |
| `<part-list>` meliputi semua part + instrumen? | |
| `id` konsisten? | |
| Setiap `<part>` punya blok `<measure>`? | |
| `divisions` konsisten + durasi valid? | |

## 4.9 Miskonsepsi

- **"Partwise & timewise bisa dicampur dalam satu file"** — Tidak; pilih salah
  satu untuk root.
- **"`<credit>` wajib untuk parse"** — Opsional; yang wajib hanya `part-list`
  & part.
- **"MIDI instrument cukup tanpa score-instrument"** — Untuk playback Ya; untuk
  engraving/id part ID butuh `score-instrument`.

## 4.10 Referensi Buku & Sumber

- Good, *Majors in the Mix* / W3C MusicXML 4.0 spec:
  https://www.w3.org/2021/06/musicxml40/
- music21 docs: https://web.mit.edu/music21/doc/
- MuseScore export internals (MXML writer): https://musescore.org/

---

**Rangkuman:** Dokumen `score-partwise` = header (work, identification,
defaults, credit) → `part-list` → satu `<part>` per instrumen, tiap part berisi
`<measure>`; `divisions`/`key`/`time`/`clef` di `<attributes>`. Lanjut ke
[The Note Element (`Ch2-The-Note-Element.md`)].