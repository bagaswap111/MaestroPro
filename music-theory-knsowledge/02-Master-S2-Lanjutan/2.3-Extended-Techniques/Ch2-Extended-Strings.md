---
title: "Extended Techniques — Strings"
tier: "Master S2"
subject: "Extended Techniques"
xml_tags: ["<note>", "<notations>", "<technical>", "<articulations>", "<notehead>", "<words>", "<direction>", "<glissando>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Extended Techniques: Strings

> **Buku panduan bab ini:** Gardner Read, *Contemporary Instrumental
> Techniques*; Penderecki/Xenakis scores; Patricia & Allen Strange,
> *The Modern Violin*. Fokus: col legno, sul pont/tasto, snap pizz, harmonics
> lanjut, teknik ekstrem — notasi MusicXML.

## 2.1 Col Legno

**Col legno battuto** (pukul dengan kayu) vs **tratto** (gesek dengan kayu) —
keduanya instruksi + kembali `arco`.

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">col legno battuto</words>
  </direction-type>
</direction>
```

Kembali:

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">arco</words>
  </direction-type>
</direction>
```

## 2.2 Sul Ponticello & Sul Tasto

| Teknik | Instruksi | Bunyi |
|--------|-----------|-------|
| *Sul ponticello* | `sul pont.` | metalik, dekat bridge |
| *Sul tasto* | `sul tasto` / `flautando` | lembut, atas fingerboard |
| *Molto sul pont.* | `p.p.s.p.` | histeris |

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">sul pont.</words>
  </direction-type>
</direction>
```

> Gabungan teknik: `sul ponticello + tremolo` — tumpuk instruksi,
> jangan double rest.

## 2.3 Bartók / Snap Pizzicato

Pizz senar ditekan & dilepas — "snap" ke fingerboard.

```xml
<note>
  <pitch><step>G</step><octave>3</octave></pitch>
  <duration>1</duration>
  <type>quarter</type>
  <notations>
    <articulations>
      <snap-pizzicato/>
    </articulations>
  </notations>
</note>
```

## 2.4 Behind-the-Bridge & Teknik Ekstrim

- **b.t.b. (behind the bridge)** — petik antara bridge & tailpiece.
- **Scordatura** — penyeteman nonstandar; notasi: tertulis vs bunyi; MusicXML
  via `<transpose>` atau string-tuning.
- **Bow knock** — ketuk badan instrumen (≋ pertusif).

Scordatura MusicXML pattern:

```xml
<attributes>
  <staff-tuning number="1">
    <tuning-step>G</tuning-step>
    <tuning-octave>3</tuning-octave>
  </staff-tuning>
</attributes>
```

## 2.5 Harmonics Lanjutan

### 2.5.1 Artificial (Buatan)

- Fondasi (bawah) + diamond (atas) dihubungkan.

```xml
<note>
  <pitch><step>C</step><octave>3</octave></pitch>
  <duration>2</duration><type>half</type>
</note>
<note>
  <pitch><step>G</step><octave>4</octave></pitch>
  <duration>2</duration><type>half</type>
  <notehead>diamond</notehead>
</note>
```

> Natural harm. = diamond single; artificial = dua not + note position.

### 2.5.2 Glissando Harmonics

Sering di spektralisme — rangkaian harmonik naik/turun.

## 2.6 Glissando pada Satu Senar

```xml
<note>
  <pitch><step>D</step><octave>4</octave></pitch>
  <duration>3</duration><type>dotted-quarter</type>
  <notations><glissando type="start"/></notations>
</note>
<note>
  <pitch><step>A</step><octave>4</octave></pitch>
  <duration>1</duration><type>quarter</type>
  <notations><glissando type="stop"/></notations>
</note>
```

> Tambah `<technical><string>3</string></technical>` untuk penegasan senar.

## 2.7 Tremolo Unmeasured & Divisimass

- **Unmeasured tremolo** — slash tanpa hitung (Septimitus).
- Gabung divisi + tremolo → tekstur dense.

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>4</duration><type>whole</type>
  <notations><ornaments><tremolo type="start">0</tremolo></ornaments></notations>
</note>
```

> `tremolo type="start">0` = unmeasured (tanpa slash). Nilai 1–8 menambah
> garis.

## 2.8 Repertoar Kontemporer

- **Penderecki — Threnody**: cluster, sul pont, col legno.
- **Xenakis — Metastasis**: glissandi besar (tutti turun).
- **Lachenmann — Intérieur I**: perkusi string (knock, guard).

## 2.9 Checklist

| Periksa | Ya/Tidak |
|---------|----------|
| Instruksi ditulis (sul pont, col legno)? | |
| Snap pizz/bow knock diberi articulation? | |
| Harmonics (natural/artificial) benar? | |
| Glissando start/stop `<glissando>`? | |
| Scordatura/staff-tuning didokumentasikan? | |

## 2.10 Miskonsepsi

- **"Col legno harus selalu battuto"** — Ada tratto (gesek); tentukan.
- **"Art harmony pakai satu diamond saja"** — Butuh dua not (fondasi +
  diamond).
- **"Glissando = slide langsung"** — Di string bisa *portamento* halus; tulis
  sesuai keinginan.

## 2.11 Latihan

1. 2 bar: sul pont. tremolo pada vln.
2. Snap pizz cello (G3) + glissando 1 senar.
3. Scordatura cello (G→F) + not successive.

## 2.12 Referensi

- Read, *Contemporary Instrumental Techniques*.
- Strange, *The Contemporary Violin*.
- Penderecki, *Threnody* (score).

---

**Rangkuman:** Ext. strings = col legno, sul pont/tasto, snap pizz, harmonics,
scordatura, unmeasured tremolo; MusicXML ≤ `<technical>`, `<articulations>`,
`<notehead>`, `<glissando>`, `staff-tuning`. Lanjut ke [Extended Percussion
(`Ch3-Extended-Percussion.md`)].