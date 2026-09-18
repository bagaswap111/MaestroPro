---
title: "The Note Element"
tier: "MusicXML Masterclass"
subject: "Anatomi MusicXML"
xml_tags: ["<note>", "<pitch>", "<rest>", "<unpitched>", "<duration>", "<type>", "<chord>", "<tie>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — The Note Element

> **Buku panduan:** MusicXML W3C 4.0 spec, *The Note Element* dan *The Global
> Note Element*; Gould *Behind Bars* (Bab 8 rhythm). Fokus: pitch, durasi,
> chord, tie/grace — blok atom penyusun segala partitur.

## 4.1 Elemen `<pitch>` (Step, Octave, Alter)

Setiap nada bernada punya `<pitch>`:

| Sub-elemen | Jenis | Contoh |
|------------|-------|--------|
| `<step>` | A–G (huruf besar) | `C` |
| `<alter>` | int (0 natural; 1 kres; −1 mol; ...) | `1`, `-1` |
| `<octave>` | 0–9 (umum 1–7) | `4` |

```xml
<note>
  <pitch>
    <step>F</step>
    <alter>1</alter>
    <octave>4</octave>
  </pitch>
  <duration>2</duration>
  <type>quarter</type>
</note>
```

> `<alter>` menentukan *sounding pitch*; `<accidental>` hanya **tampilan**
> (redundant hint / cautionary). Sering alat tulis akan menyesuaikan
> `<accidental>` otomatis dari key+alter.

### 4.1.1 Senarai Jenis


| Elemen | Fungsi |
|--------|--------|
| `<pitch>` | Nada bernada (pitch class + octave) |
| `<rest>` | Nada diam (`measure="yes"` untuk rest okbo penuh) |
| `<unpitched>` | Perkusi tanpa pitch (display-step/octave) |

## 4.2 Rest & Unpitched

### 4.2.1 `<rest>`

```xml
<note>
  <rest/>
  <duration>4</duration>
  <voice>1</voice>
  <type>whole</type>
</note>
```

```xml
<note>
  <rest measure="yes">
    <display-step>C</display-step>
    <display-octave>4</display-octave>
  </rest>
  <duration>4</duration>
  <type>whole</type>
</note>
```

> `measure="yes"` = *full-measure rest*; posisi visual boleh diatur dengan
> display-step/octave.

### 4.2.2 `<unpitched>`

```xml
<note>
  <unpitched>
    <display-step>C</display-step>
    <display-octave>5</display-octave>
  </unpitched>
  <duration>2</duration>
  <instrument id="P1-S"/>
  <type>eighth</type>
</note>
```

## 4.3 Durasi & Type

### 4.3.1 `<duration>` — unit dalam `divisions`

`<divisions>` di `<attributes>` menyatakan quarter = N unit.

| Not | Durasi (divisions=2) | `<type>` |
|-----|----------------------|----------|
| Whole | 8 | `whole` |
| Half | 4 | `half` |
| Quarter | 2 | `quarter` |
| Eighth | 1 | `eighth` |
| 16th | 0.5 (gunakan divisions lbh besar) | `16th` |

### 4.3.2 Dotted Values

```xml
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>3</duration>
  <type>quarter</type>
  <dot/>
</note>
```

> `<dot/>` boleh berulang (double-dot). MusicXML menghitung durasi, sedangkan
> `<type>`+`<dot>` memberi *visual*; keduanya harus konsisten.

## 4.4 `<chord/>` — Notasi Akor Vertikal

- Nada pertama TANPA `<chord/>`.
- Nada ke-2 dst diberi `<chord/>`.

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>quarter</type>
</note>
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>quarter</type>
  <chord/>
</note>
<note>
  <pitch><step>G</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>quarter</type>
  <chord/>
</note>
```

> Aturan: semua nilah seri `<chord/>` harus **durasi sama** dan tidak boleh ada
> `<chord/>` pada not pertama dari seri.

## 4.5 Tie, Grace, Fermata

### 4.5.1 Tie

```xml
<note>
  <pitch><step>F</step><octave>4</octave></pitch>
  <duration>2</duration>
  <tie type="start"/>
  <notations>
    <tied type="start"/>
  </notations>
</note>
<note>
  <pitch><step>F</step><octave>4</octave></pitch>
  <duration>2</duration>
  <tie type="stop"/>
  <notations>
    <tied type="stop"/>
  </notations>
</note>
```

> `<tie>` = playback; `<tied>` (dalam `<notations>`) = kurva visual. Keduanya
> wajib sinkron.

### 4.5.2 Grace Notes

```xml
<note>
  <grace slash="yes"/>
  <pitch><step>D</step><octave>5</octave></pitch>
  <type>eighth</type>
  <stem>up</stem>
</note>
<note>
  <pitch><step>C</step><octave>5</octave></pitch>
  <duration>2</duration>
  <type>quarter</type>
</note>
```

- `grace` boleh punya `slash="yes"`, `make-time="half"` (mencuri separuh),
  dan `steal-time-previous/next` di MusicXML 3.1+.

## 4.6 Voice/Staff/Normal & Musis

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>2</duration>
  <voice>1</voice>
  <type>quarter</type>
  <staff>1</staff>
</note>
```

- `<voice>` — indeks suara (polyphony).
- `<staff>` — nomor staff dalam part multi-staff (1=atas, 2=bawah).

### 4.6.1 `<normal-notes>` & dopp. dalam aksen

Dalam hitungan bersamaan, `<time-modification>` dipakai:

```xml
<norm k>
  <time-modification>
    <actual-notes>3</actual-notes>
    <normal-notes>2</normal-notes>
  </time-modification>
</norm>
```

(Triplet: 3 actual = 2 normal.)

## 4.7 Tampilan: Accidental, Notehead, Colour

```xml
<note>
  <pitch><step>B</step><alter>-0.5</alter><octave>4</octave></pitch>
  <duration>2</duration>
  <type>quarter</type>
  <accidental>quarter-flat</accidental>
  <notehead>diamond</notehead>
</note>
```

- `<accidental>`: `natural`, `sharp`, `flat`, `quarter-flat`, `double-sharp`,
  `cautionary`, `forced`.
- `<notehead>`: `normal`, `diamond`, `triangle`, `x`, `slash`, `circle`,
  `cluster`, `none`, dan modifier `filled`/`parentheses` (slashes).

## 4.8 Struktur Lengkap Contoh `<note>`

```xml
<note>
  <chord/>
  <grace/>
  <pitch>
    <step>A</step>
    <alter>0</alter>
    <octave>5</octave>
  </pitch>
  <duration>2</duration>
  <tie type="start"/>
  <voice>2</voice>
  <type>quarter</type>
  <accidental>natural</accidental>
  <notations>
    <tied type="start"/>
  </notations>
</note>
```

## 4.9 Checklist Note Element

| Periksa | Ya/Tidak |
|---------|----------|
| Pitch bernada pakai `<pitch>`? | |
| Rest/unpitched sesuai tipe? | |
| Durasi konsisten dgn `divisions`? | |
| `<type>`+`<dot/>` mewakili durasi? | |
| `<chord/>` hanya not ke-2 dst.? | |
| Voice/staff diisi utk polyphony? | |
| Tie: `<tie>` & `<tied>` sinkron? | |

## 4.10 Miskonsepsi

- **"`<accidental>` meniup riski"** — Tidak; harus redundan → sound adalah
  `<alter>`; accidental display-only.
- **"Durasi boleh tidak konsisten dgn type"** — Software akan meng-*resync*;
  selalu jaga konsistensi.
- **"Grace tidak perlu durasi"** — Grace *dibiarkan tanpa `<duration>`*
  (`make-time` atribut), sedapat mungkin kotak.

## 4.11 Referensi Buku & Sumber

- W3C MusicXML 4.0 — Note chapter:
  https://www.w3.org/2021/06/musicxml40/
- music21 docs: https://web.mit.edu/music21/doc/
- Gould, *Behind Bars: The Definitive Guide to Music Notation*.

---

**Rangkuman:** `<note>` adalah blok atom: bernada (`<pitch>`), diam (`<rest>`),
perkusi (`<unpitched>`), ditambah `<duration>`+`<type>` untuk irama,
`<chord/>` untuk vertikalitas, `<tie>`/`<tied>` untuk ligasi, dan `<grace>`
untuk ornamen. Lanjut ke [Attributes & Directions
(`Ch3-Attributes-Directions.md`)].