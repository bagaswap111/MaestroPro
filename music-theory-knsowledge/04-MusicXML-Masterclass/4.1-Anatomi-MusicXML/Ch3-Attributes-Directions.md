---
title: "Attributes & Directions"
tier: "MusicXML Masterclass"
subject: "Anatomi MusicXML"
xml_tags: ["<attributes>", "<divisions>", "<key>", "<time>", "<clef>", "<direction>", "<dynamics>", "<sound>", "<forward>", "<backup>", "<transpose>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Attributes & Directions

> **Buku panduan:** W3C MusicXML 4.0 — *The Attributes Element* & *The
> Direction Element*; Gould, *Behind Bars* (Bab 3–5: key, time, dynamics,
> tempo). Fokus: mengatur skala/key/clef & menyandikan instruksi di atas/bawah
> staff.

## 4.1 Elemen `<attributes>` (Divisions, Key, Time, Clef)

`<attributes>` menetapkan setting di awal measure — atau kapan pun berubah.

### 4.1.1 `<divisions>`

```xml
<attributes>
  <divisions>2</divisions>
</attributes>
```

> Semua `<duration>` dalam part dibaca terhadap divisions ini. Boleh berubah
> di tengah (bila subunits beat), dengan `divisions` baru.

### 4.1.2 `<staves>` (Multi-Staff Part)

```xml
<attributes>
  <staves>2</staves>
  <clef number="1"><sign>G</sign><line>2</line></clef>
  <clef number="2"><sign>F</sign><line>4</line></clef>
</attributes>
```

- Bila `<staves>` berubah ke 2, gunakan `number` di `clef` & `staff`.

### 4.1.3 `<key>` — `fifths`/`mode`/`cancel`

```xml
<attributes>
  <key>
    <cancel>2</cancel>
    <fifths>1</fifths>
    <mode>minor</mode>
  </key>
</attributes>
```

- `cancel` — jumlah aksiden yang dibatalkan (untuk pergantian kunci drastis).
- `fifths` — krus/mol; `mode` — `major`/`minor`.

### 4.1.4 `<time>` — Sederhana & Compound

```xml
<time symbol="cut">
  <beats>2</beats>
  <beat-type>2</beat-type>
</time>
```

```xml
<time>
  <beats>6</beats>
  <beat-type>8</beat-type>
</time>
```

> Compound (`6/8`, `9/8`) hanya butuh beats+beat-type; axis grouping biasanya
> dari metronome/beam. `symbol="cut"` untuk alla breve.

### 4.1.5 `<clef>` — G, F, C, Percussion, TAB

| `sign` | Pemakaian |
|--------|-----------|
| `G` | treble (line default 2) |
| `F` | bass (line default 4) |
| `C` | alto/tenor (line 3/4) |
| `percussion` | perkusi tak bernada |
| `TAB` | tabulatur gitar |
| `none` | tanpa clef (persussion ge container) |

```xml
<clef>
  <sign>G</sign>
  <line>2</line>
  <clef-octave-change>-1</clef-octave-change>
</clef>
```

- `clef-octave-change` — kurir 8va/8vb (±1 oktaf).

### 4.1.6 `<transpose>` — untuk instrumen transpos (lihat `Ch2-Transposisi`)

```xml
<transpose>
  <diatonic>-1</diatonic>
  <chromatic>-2</chromatic>
  <octave-change>0</octave-change>
</transpose>
```

## 4.2 `<direction>` — Instruksi di Atas/Bawah Staff

`<direction placement="above">` menaruh teks/gambar/dinamik di posisi
tertentu.

### 4.2.1 `<direction-type>` → `<words>`/`<dynamics>`/`<wedge>`

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">pp</words>
  </direction-type>
</direction>
```

Standar dinamik dinotasikan dengan elemen khusus:

```xml
<direction placement="above">
  <direction-type>
    <dynamics>
      <p/>
    </dynamics>
  </direction-type>
</direction>
```

> Elemen `dynamics` mendukung: `pppp`…`ppp`, `pp`, `p`, `mp`, `mf`, `f`,
> `ff`, `fff`, `ffff`, `fp`, `sf`, `sfz`, `rfz`, `rf`. Dinamik terpisah dari
> words (render di bawah dasar staff otomatis).

### 4.2.2 Wedge (Hairpin)

```xml
<direction placement="below">
  <direction-type>
    <wedge type="crescendo" number="1"/>
  </direction-type>
</direction>
...
<direction placement="below">
  <direction-type>
    <wedge type="stop" number="1"/>
  </direction-type>
</direction>
```

- `wedge type`: `crescendo`, `diminuendo`, `stop`, `continue`.

### 4.2.3 Tempo — Metronome + Sound

```xml
<direction placement="above">
  <direction-type>
    <metronome parentheses="no">
      <beat-unit>quarter</beat-unit>
      <per-minute>120</per-minute>
    </metronome>
    <words xml:space="preserve">Allegro</words>
  </direction-type>
  <sound tempo="120"/>
</direction>
```

> `<sound tempo>` = nilai BPM untuk playback; metronome adalah tampilan.

### 4.2.4 Atribut `<sound>` Lain

| atribut | Makna |
|---------|-------|
| `tempo` | BPM |
| `dynamics` | 0–100 |
| `dacapo` | da capo |
| `segno` | marker segno |
| `coda` | marker coda |
| `fine` | fine |
| `pizzicato` | string pizz |
| `pan` | stereo (0-90) |

## 4.3 `<forward>` & `<backup>` — Playback Position

Saat polyphony multi-voice dengan durasi berbeda, `forward`/`backup` menggerak
playback cursor.

### 4.3.1 `<forward>` (maju)

```xml
<note>
  <rest/>
  <duration>1</duration>
  <voice>2</voice>
  <type>eighth</type>
</note>
<forward>
  <duration>7</duration>
</forward>
```

> Mengisi kekosongan di tengah voice agar durasi total measure berimbang.

### 4.3.2 `<backup>` (mundur)

```xml
<backup>
  <duration>4</duration>
</backup>
```

> Kembali ke titik awal measure untuk menulis voice berikutnya. Umum di
> partisterta piano (staff 1 atas, kembali, staff 1 bawah).

## 4.4 Contoh Measure Lengkap

```xml
<measure number="1">
  <attributes>
    <divisions>2</divisions>
    <key><fifths>-1</fifths></key>
    <time><beats>3</beats><beat-type>4</beat-type></time>
    <clef><sign>G</sign><line>2</line></clef>
  </attributes>
  <direction placement="above">
    <direction-type>
      <dynamics><f/></dynamics>
    </direction-type>
    <sound dynamics="80"/>
  </direction>
  <note>
    <pitch><step>F</step><octave>4</octave></pitch>
    <duration>2</duration>
    <type>quarter</type>
  </note>
</measure>
```

## 4.5 Referensi Cepat Direction-Type

| Sub-elemen | Fungsi |
|------------|--------|
| `<words>` | Teks bebas |
| `<dynamics>` | Tanda dinamika |
| `<wedge>` | Hairpin |
| `<metronome>` | Tanda tempo |
| `<octave-shift>` | 8va/15ma display |
| `<dashes>` | garis putus (dash line) |
| `<bracket>` | kurung (menšur/teknik) |
| `<pedal>` | pedal piano |
| `<sound>` | parameter playback |

## 4.6 Checklist Attributes & Directions

| Periksa | Ya/Tidak |
|---------|----------|
| `<attributes>` di awal measure / tiap perubahan? | |
| `divisions`/`key`/`time`/`clef` benar? | |
| Dinamik & tempo via `<direction>`? | |
| `<forward>`/`<backup>` rapi utk multi-voice? | |
| `<sound>` diset sesuai software target? | |

## 4.7 Miskonsepsi

- **"Key signature boleh diabaikan jika tak ada aksen"** — Tetap wajib untuk
  parse & playback; jangan menghilangkan.
- **"`<dynamics>` = `<words>pp</words>`"** — Word works look-wise, tapi elemen
  `<dynamics><p/></dynamics>` memberi konvensi & rendering otomatis.
- **"Direction selalu satu suara"** — Satu `<direction>` untuk satu *span*;
  offset mengontrol posisi relatif.

## 4.8 Referensi

- W3C MusicXML 4.0: https://www.w3.org/2021/06/musicxml40/
- Gould, *Behind Bars* — dynamics/tempo chapter.
- music21: https://web.mit.edu/music21/doc/

---

**Rangkuman:** `<attributes>` menentukan divisions/key/time/clef/transpose di
awal (atau perubahan); `<direction>` menyandikan dinamik, tempo, wedge dll;
`<forward>`/`<backup>` menjaga cursor saat polyphony. Lanjut ke [Harmony &
Chord Symbols (`Ch4-Harmony-Chord-Symbols.md`)].