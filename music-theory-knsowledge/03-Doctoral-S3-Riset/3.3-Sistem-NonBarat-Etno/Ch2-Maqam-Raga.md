---
title: "Maqam Arab & Raga India"
tier: "Doctoral S3"
subject: "Sistem Non-Barat & Etno"
xml_tags: ["<pitch>", "<alter>", "<accidental>", "<ornament>", "<direction>", "<words>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Maqam Arab & Raga India

> **Buku panduan bab ini:** Maqam literature (45 maqamat); Ravi Shankar,
> *My Music, My Life*; Viswanathan & Cormack (Karnatic theory). Fokus:
> mikrotonalitas, ornamentasi, dan kerangka ritmik dalam notasi Barat.

## 2.1 Maqam: Sistem Modal Arab

*Maqam* (مقام): tetrachord (jins) yang membentuk skala lebih besar dengan
interval mikrotonal — terutama untuk Oud, Kanun, dan vokal.

| Maqam | Ciri Nada | Karakter |
|-------|-----------|----------|
| Rast | C D E♭½ F G A B♭½ C | kokoh, membuka |
| Bayati | D E F½ G A B♭ C D | sentimental |
| Hijaz | D E♭ F# G A B♭ C D | dramatis |
| Saba | D E F G♭ A B♭ C D | melankolis |
| Nahawand | C D E♭ F G A B♭ C | berat, minor |

### 2.1.1 Interval Quarter-Tone

- **E♭½** = E "tengah" antara E dan E♭.
- Ditulis di partitur Barat dengan `quarter-flat`/`quarter-sharp`.

### 2.1.2 MusicXML: Hijaz quarter-note example

```xml
<note>
  <pitch>
    <step>E</step>
    <alter>-0.5</alter>
    <octave>4</octave>
  </pitch>
  <duration>2</duration>
  <type>quarter</type>
  <accidental>quarter-flat</accidental>
</note>
```

## 2.2 Ornamen Maqam

- **Qar' (ornament)** — take, birlim, mordent.
- **Glissando/slide** — mikrotonal menanjak.
- **Trill** — kadang mulai dari nada bawah.

```xml
<note>
  <pitch><step>F</step><octave>4</octave></pitch>
  <duration>1</duration><type>eighth</type>
  <notations>
    <ornaments><trill/></ornaments>
  </notations>
</note>
```

## 2.3 Raga: Kerangka Modal India

*Raga* = skala (swaras), hierarki nada (vadi/samvadi), dan ornamentasi khas
— di dalam *taal* (siklus ritme).

| Raga | Aroha (naik) | Avaroha (turun) | Karakter |
|------|--------------|-----------------|----------|
| Shankarabharanam | S R2 G3 M1 P D2 N3 S' | S'N3 D2 P M1 G3 R2 S | grand |
| Bhairavi | S r2 g2 M P d2 n2 S' | S'n2 d2 P M g2 r2 S | pathos |
| Todi | S r2 g2 M d2 N2 S' | S'N2 d2 M g2 r2 S | heroik-sedih |
| Kalyani | S R2 G3 M2 P D2 N3 S' | S'N3 D2 P M2 G3 R2 S | cemerlang |

> Swara: S, R(R1..R4), G, M(M1/M2), P, D, N. `R2` = besar dengan das;
> `M2` = sharp fourth (tivra Madhyam).

## 2.4 Mikrotonal dalam Raga (Shruti & Gamaka)

- **Shruti** = unit pitch terkecil (klasik: 22 shrutis).
- **Gamaka** = slide/ornamen — lebih penting daripada pitch statis.
- Partitur Barat perlu `glissando` & `portamento`.

```xml
<note>
  <pitch><step>G</step><octave>4</octave></pitch>
  <duration>2</duration><type>half</type>
  <notations><glissando type="start"/></notations>
</note>
<note>
  <pitch><step>A</step><octave>4</octave></pitch>
  <duration>2</duration><type>half</type>
  <notations><glissando type="stop"/></notations>
</note>
```

## 2.5 Taal: Siklus Ritmik

| Taal | Beats | Struktur | Keterangan |
|------|-------|----------|------------|
| Tintal | 16 | 4+4+4+4 | umum |
| Jhoomra | 14 | 3+4+3+4 | slow |
| Ektaal | 12 | 2+2+2+2+2+2 | |

```xml
<time>
  <beats>4</beats>
  <beat-type>4</beat-type>
</time>
```

> Struktur poliritmik sam/dam dapat direpresentasi dengan `metronome` atau
> `time signature`, tapi terbaik via teks instruksi.

## 2.6 Kerangka Karya dalam Partitur Barat

1. Visualisasi skala dengan `key signature` (approksimasi).
2. Microtones via `alter`+`accidental` — atau deskripsi untuk interval non-
   mikrotonal.
3. Tambah instruksi teks (nama maqam/raga, ornament wajib).
4. Custom tuning/instrument bila sample tersedia.

## 2.7 Checklist Maqam/Raga

| Periksa | Ya/Tidak |
|---------|----------|
| Nama maqam/raga dicantumkan? | |
| Microtones ditulis `quarter-flat`/`quarter-sharp`? | |
| Ornament/gamaka diindikasikan jelas? | |
| Struktur taal/time signature sesuai? | |
| Instruksi kinerja lokal didokumentasikan? | |

## 2.8 Miskonsepsi

- **"Maqam = minor/hijaz"** — Tiap maqam punya jins & karakter tersendiri;
  Hijaz hanyalah satu.
- **"Raga = skala"** — Raga termasuk hierarki nada + ornament; skala hanya
  satu aspek.
- **"Quarter-tone cukup untuk maqam"** — Variasi cents halus (1/4, 1/5 tone)
  bervariasi per tradisi.

## 2.9 Latihan

1. Tulis 8-bar maqam Bayati di partitur Barat dengan quarter-flat.
2. Buat gamaka glissandi untuk raga Todi.
3. Map taal 16-beat Tintal dalam MusicXML.

## 2.10 Referensi

- Shankar, *My Music, My Life*.
- Viswanathan & Cormack, *Indian Music in Performance and Practice*.
- Rujukan microtone: `../3.1-Psikoakustik-Spektral/Ch2-Mikrotonal-Tuning.md`.

---

**Rangkuman:** Maqam & Raga memperkenalkan mikrotonalitas dan ornamentasi khas
di luar 12-TET. MusicXML menanganinya dengan `alter` non-integer, `accidental`
quarter, `<ornaments>`/`<glissando>`, dan instruksi teks. Ini menutup Tier 3
([Doctoral S3]). Lanjut ke [Tier 4 — MusicXML Masterclass
(`../../04-MusicXML-Masterclass/`)].