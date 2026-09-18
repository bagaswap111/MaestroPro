---
title: "Funk, Soul & R&B — Adaptasi Lintas Instrumentasi"
tier: "Master S2"
subject: "Genre Funk Soul R&B"
xml_tags: ["<score-part>", "<midi-instrument>", "<transpose>", "<glissando>", "<notehead>", "<directon>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Funk, Soul & R&B: Adaptasi Lintas Instrumentasi

## 2.1 Peta Fungsi Funk → Ansambel Akustik/Orkestra

Escort funk terbesar adalah **groove-switch**, bukan harmoni:

| Fungsi funk | Instrumen asli | Target akustik |
|-------------|----------------|----------------|
| Bass 16th (slap) | E-bass | Cello pizz., bassoon, tuba double-tongue |
| Clav riff | Clavinet | Vibraphone, marimba, piano |
| Wah-guitar | Wah-wah | Trumpet (harmon-wah), sax in gutter |
| Horn stabs | Brass section | Strings pluck (pizz staccato) section |
| Backbeat drum | Drum kit | Cajón, snare, maracas |
| Trap-hat 16th | Hi-hat | Tamborin (swing 8ths), flexitone |

## 2.2 Adaptasi 1: Funk Band → String Quartet / Chamber

Prinsip: **biarkan bassline 16th pindah** — cello pizz. 16th (double stops
tidak perlu, ada 4 not); horns → violin 2 pluck / viola on 2&4.

```xml
<measure number="1">
  <attributes>
    <time><beats>4</beats><beat-type>4</beat-type></time>
  </attributes>
  <!-- Cello: 16th bass groove, pizzicato -->
  <note>
    <pitch><step>G</step><octave>2</octave></pitch>
    <duration>1</duration>
    <type>16th</type>
    <voice>4</voice>
    <staff>2</staff>
  </note>
  <note>
    <pitch><step>G</step><octave>2</octave></pitch>
    <duration>1</duration>
    <type>16th</type>
    <voice>4</voice>
    <staff>2</staff>
  </note>
  <!-- Vln2 pizz on 2&4 (backbeat) -->
  <note>
    <rest/>
    <duration>2</duration>
    <type>8th</type>
    <voice>2</voice>
  </note>
  <note>
    <pitch><step>D</step><octave>5</octave></pitch>
    <duration>1</duration>
    <type>16th</type>
    <voice>2</voice>
    <articulations><staccato/></articulations>
  </note>
</measure>
```

## 2.3 Adaptasi 2: R&B Ballad → Full Orchestra (String+Full)

- **Vocal lead → trumpet/flute** dengan *falloffs* (`falloff` articulation) —
  adaptasi gaya.
- **Pad synth → string + woodwind** *longue* (arco), divisi.
- **Sub-bass → timpani/cello octave + bass trombone.**
- **Trap hi-hat 16th → tambourine 16th + **marcato** strings on the rim.**

```xml
<score-instrument id="P1-I1">
  <instrument-name>Bass Trombone</instrument-name>
</score-instrument>
<midi-instrument id="P1-I1">
  <midi-channel>1</midi-channel>
  <midi-program>58</midi-program>
</midi-instrument>
<attributes>
  <transpose><diatonic>0</diatonic><chromatic>0</chromatic></transpose>
</attributes>
```

## 2.4 Adaptasi 3: Funk → Brass Band / Wind Band

Horn section funk langsung naik level ke band:
- Sax stabs → cornet section stabs (same rhythm).
- Guitar wah → trombone *gliss* (smear) pada target.
- E-bass → tuba 16th double-tongue (pada C61 — C3 region).
- Tak perlu *straight* — **feels tetap syncopated** pada grid 16th.

```xml
<note>
  <pitch><step>G</step><octave>2</octave></pitch>
  <duration>1</duration>
  <type>16th</type>
  <voice>4</voice>
  <notations>
    <technical><double-tongue/></technical>
  </notations>
</note>
```

## 2.5 Checklist Adaptasi Funk/Soul/R&B

| Cek | Hasil |
|-----|-------|
| *Feel* 16th & ghost tidak hilang? | |
| Backbeat 2&4 dalam target? | |
| Bass 16th dipindah (pizz/tuba/…)? | |
| Stabs horns → dijawab pad/pluck | |
| R&B harmony (dominant+9, slash) konsisten? | |
| Vokal melisma → gliss/run pada lead instrumen? | |
| `tempo` + `<sound groove>` dipertahankan? | |

## 2.6 Latihan

1. **Dasar:** Pindahkan bassline funk 4-bar → cello pizz. (16th).
2. **Menengah:** Tulis horn section funky (ptt+asx+tsx) 2 staves untuk stab.
3. **Lanjut:** Susun R&B ballad untuk string orchestra + vocal lead flute:
   intro pad, chorus stabs, bridge *pluck build*.

## 2.7 Repertoar Adaptasi

- **Vitamin String Quartet (VSQ)** — cover R&B.
- **LILYS / Frank Ocean style covers for orchestra**.
- **Metropole Orkest** — pop orchestras funk charts.

## 2.8 Referensi Buku & Sumber Web

**Buku:**
- Garibaldi, *Future Sounds*; Hunt, *Funk Bass Bible*.
- Steve Vai / Bert, *The Art of Funk*.

**Web:**
- Funk bass: https://www.oktav.com/
- Metropole Orkest: https://www.metropoleorkest.nl/

---

**Rangkuman:** Adaptasi funk/R&B = pindah fungsi grove (bass 16th, backbeat,
stab, pad) ke instrumen akustik dengan teknik idiomatik (pizz, tuba double
tongue, gliss wah) sambil mempertahankan *feel* — bukan straight. Kembali ke
[Funk Karakteristik (`Ch1-Karakteristik-Notasi.md`)] atau lanjut ke
[Latin (`../2.6-Genre-Latin/`)].