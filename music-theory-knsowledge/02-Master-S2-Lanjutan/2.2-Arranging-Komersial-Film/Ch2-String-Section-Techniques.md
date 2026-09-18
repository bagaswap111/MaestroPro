---
title: "String Section Techniques"
tier: "Master S2"
subject: "Arranging Komersial & Film"
xml_tags: ["<note>", "<notations>", "<divisi>", "<tremolo>", "<articulations>", "<direction>", "<words>", "<bowing>", "<glissando>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — String Section Techniques

> **Buku panduan bab ini:** Samuel Adler, *The Study of Orchestration*
> (Bab strings); Walter Piston, *Orchestration* (Bab 5–6); penyusunan
> divisi dalam dorico. Fokus: divisi/unison, bowing, tremolo, harmonics,
> pizzicato — bagaimana menuli string section yang hidup.

## 2.1 Pembagian String Section

| Kelompok | Range (konser) | Peran |
|----------|----------------|-------|
| Violin I | G3 – C7 | melodi/atas |
| Violin II | G3 – C7 | harmoni, counter |
| Viola | C3 – E6 | warna tengah |
| Cello | C2 – A5 | melodi bawah/bass expressif |
| Double Bass | E1 – G4 | bass (notasi 1 oktaf di atas bunyi) |

### 2.1.1 Register per staff

- Vln/Vla: treble.
- Vlc: bass (kadang tenor clef untuk register atas).
- Db: bass (octave-transposing, lihat Tier 1 Ch2 transposisi).

## 2.2 Divisi (div.) dan Unison

**Divisi** = membagi kelompok menjadi dua+ baris; **a2/unison** = semua sama.

- Tandai `div.` di atas staff (kadang `a2`).
- Contoh: Divisi 2 garis: not di voice 1 & voice 2.

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">div.</words>
  </direction-type>
</direction>
```

```xml
<note>
  <pitch><step>E</step><octave>5</octave></pitch>
  <duration>2</duration><voice>1</voice><type>half</type>
</note>
<note>
  <pitch><step>G</step><octave>4</octave></pitch>
  <duration>2</duration><voice>2</voice><type>half</type>
</note>
```

> Kembali `unison`: `<direction><words>unison</words>`. Dorico punya
> *divisi-manajemen* native; kita simpan `<voice>` konsisten.

## 2.3 Tremolo & Vamp

- **Tremolo** — pergantian cepat; `tremolo type="start"` + jumlah slash.
- **Vamp** — repetisi.

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>2</duration><type>half</type>
  <notations>
    <ornaments>
      <tremolo type="start">3</tremolo>
    </ornaments>
  </notations>
</note>
```

> 3 slice → 32nd-tremolo (sangat cepat). Tremolo seharusnya berakhir di
> `<tremolo type="stop">`.

## 2.4 Harmonics

- **Natural**: sentuh titik (oktaf, fifth...); diamond notehead.
- **Artificial**: tekanan + fingerboard; notasi biasa di bawah + diamond.

```xml
<note>
  <pitch><step>G</step><octave>4</octave></pitch>
  <duration>4</duration>
  <type>whole</type>
  <notehead>diamond</notehead>
</note>
```

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">harm.</words>
  </direction-type>
</direction>
```

## 2.5 Bowing Techniques

| Teknik | Simbol | MusicXML |
|--------|--------|----------|
| Up-bow | ⌄ | `<up-bow/>` |
| Down-bow | ⌃ | `<down-bow/>` |
| Col legno | — | `<words>col legno</words>` |
| Sul ponticello | — | `<words>sul pont.</words>` |
| Sul tasto | — | `<words>sul tasto</words>` |
| Sulla punta (bow-where) | — | `<words>sulla punta</words>` |

```xml
<notations>
  <technical>
    <down-bow/>
  </technical>
</notations>
```

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">sul pont.</words>
  </direction-type>
</direction>
```

> **Trik notasi:** ulangi teknik tiap perubahan — jangan asumsi berlanjut.

## 2.6 Pizzicato & Bartók Pizz

- Pizz = pluck; kembali dengan `arco`.
- Bartók pizz = pluck keras (senar pantul ke fingerboard).

```xml
<note>
  <pitch><step>A</step><octave>3</octave></pitch>
  <duration>1</duration>
  <type>quarter</type>
  <notations>
    <articulations>
      <pizzicato/>
    </articulations>
  </notations>
</note>
```

> Pizzicato via `<articulations><pizzicato/>`. Kembali arco:
> `<direction><words>arco</words>`.

## 2.7 String Writing dalam Film

1. **Homophonic stroke** — semua bersama → hangat.
2. **Melodic doubling** — oktaf (vln+cello) → proyeksi.
3. **Contrapuntal** — beberapa garis counter (viola/cello) → puncak.
4. **Tremolo/glissando** — suspense.

### 2.7.1 Glissando

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>2</duration><type>half</type>
  <notations>
    <glissando type="start"/>
  </notations>
</note>
<note>
  <pitch><step>D</step><octave>5</octave></pitch>
  <duration>2</duration><type>half</type>
  <notations>
    <glissando type="stop"/>
  </notations>
</note>
```

## 2.8 Template String Orchestra

1. Part: Vln I, Vln II, Vla, Vlc, Cb.
2. Clef: G/G/G/F/F.
3. Aktifkan divisi.
4. Bowing mapped untuk playback.

## 2.9 Checklist

| Periksa | Ya/Tidak |
|---------|----------|
| Divisi ditandai div./a2? | |
| Range string dalam batas? | |
| Teknik pizz/arco/sul pont/harm unknown? | |
| Tremolo ukuran nilai? | |
| Bowing unik frase? | |

## 2.10 Miskonsepsi

- **"Divisi selalu 2 bagian"** — Bisa 2–3 (divisi a3).
- **"`harmonic` menggunakan notehead diamond saja"** — Diamond menandakan
  natural harmonic; artificial butuh dua pitch.
- **"Glissando harus jarak besar"** — Bisa pula ✳ halftime (portamento).

## 2.11 Latihan

1. Tulis 4 bar homophonic divisi (vln I a3) di MusicXML voice 1–3.
2. Buat glissando violin dari G4 ke B5 + sul pont.
3. Susun kontrata string (vla+vcl counter) 8 bar.

## 2.12 Referensi

- Adler, *The Study of Orchestration* — strings.
- Piston, *Orchestration*.
- Dorico divisi docs.

---

**Rangkuman:** String section = divisi + bowing + tremolo + harmonics +
pizzicato; MusicXML via `<voice>`/`<divisi words>`, `<articulations>`,
`<technical>` (bow), `<tremolo>`, dan `<glissando>`. Lanjut ke [Film
Scoring Notation (`Ch3-Film-Scoring-Notation.md`)].