---
title: "Latin Music — Adaptasi Lintas Instrumentasi"
tier: "Master S2"
subject: "Genre Latin"
xml_tags: ["<score-part>", "<midi-instrument>", "<transpose>", "<glissando>", "<tremolo>", "<direction>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Latin Music: Adaptasi Lintas Instrumentasi

## 2.1 Peta Peran Latin → Ansambel Baru

| Peran Latin | Instrumen asli | Target |
|-------------|----------------|--------|
| Clave (mie) | Claves/campana | Wood block (kayu), rim tap |
| Guajeo/montuno | Piano | Vibraphone/piano, guitar |
| Tumbao bass | Bass | Tuba pizz? cello arco down |
| Congas | Conga | Djembe, Congo/envuelto drums |
| Timbales | Timbales | Tambourine, bongo |
| Bandoneón | Bandoneón | Accordion, oboe (melodi), sax |
| Brass montuno | Trumpet/trombone | Sax, strings con fuoco |

**Aturan:** *Clave hanya tidak berubah* — walau ansambel berubah, pola clave
menjadi "gigi" yang menghubungkan semua.

## 2.2 Adaptasi 1: Bossa Jazz → String Quartet / Chamber

- **Bass:** cello pizz. svolta syncopated (root+5th, 8th).
- **Guitar syncopation** → viola *pizz* pada klvn 2&4.
- **Melodi vocal** → violin 1 (frasis clear, breathes).
- **Drums (brush)** → *brush cajón* sedikit shake / maracas.

```xml
<measure number="1">
  <attributes>
    <time><beats>2</beats><beat-type>2</beat-type></time>
  </attributes>
  <note>
    <pitch><step>F</step><octave>3</octave></pitch>
    <duration>2</duration>
    <type>eighth</type>
    <voice>4</voice>
    <staff>2</staff>
  </note>
  <note>
    <pitch><step>E</step><octave>5</octave></pitch>
    <duration>2</duration>
    <type>eighth</type>
    <voice>1</voice>
    <staff>1</staff>
  </note>
</measure>
```

## 2.3 Adaptasi 2: Salsa → Big Band / Jazz Combo

- **Montuno (piano)** → comp piano/jazz (same guajeo), atau horn section
  *rhythmic*.
- **Coro** → sax section *unison riff* (tetap syncopated).
- **Tumbao** → bass walking (Latin feel: *walking straight* tanpa swing).
- **Timbales** → *tamburin* atau *cowbell* (percussion) di kit.

```xml
<score-instrument id="P1-I1">
  <instrument-name>Alto Sax</instrument-name>
</score-instrument>
<midi-instrument id="P1-I1">
  <midi-channel>1</midi-channel>
  <midi-program>65</midi-program>
</midi-instrument>
<attributes>
  <transpose>
    <diatonic>2</diatonic>
    <chromatic>-3</chromatic>
  </transpose>
</attributes>
```

> Sax Alto E♭: written ↑ maj 6th = concert. `<transpose>` bertanggung jawab —
> jangan salah menulis part (lihat `Ch2-Transposisi-Instrumen.md`).

## 2.4 Adaptasi 3: Tango → Full Orchestra / String Solo

- **Bandoneón-emulasi** → violin quintet melodi (frasis dramatic, wide
  register), atau oboe/english horn.
- **Habanera bass** → celli pizz. pada off-beat + timpani (deep).
- **Staccato strings** → tutti col legno? (trick),
  *marcato* interjeksi.
- **Arrastre (glissando)** → violins `glissando` line-type wavy.

```xml
<note>
  <pitch><step>D</step><octave>5</octave></pitch>
  <duration>3</duration>
  <type>quarter</type><dot/>
  <notations>
    <glissando type="start" line-type="wavy"/>
  </notations>
</note>
```

## 2.5 Checklist Adaptasi Latin

| Cek | Hasil |
|-----|-------|
| Clave tidak berubah (3–2/2–3 terjaga)? | |
| Syncopation di bawaan instrumen non-perkusi? | |
| Bass tumbao / habanera pattern terjaga? | |
| Harmoni (bossa ii–V / salsa) dipertahankan? | |
| Melodi emosi (bandoneón) di register terbaik? | |
| `unpitched` untuk clave/conga benar? | |
| Tempo khas (bossa ~120, samba ~180) ditulis? | |

## 2.6 Latihan

1. **Dasar:** Pindahkan guajeo piano → vibraphone (8 bar, Dm7–G7).
2. **Menengah:** Clave tetap: tulis salsa untuk combo (piano comp,
   conga tumbao pada bongo, bass tumbao).
3. **Lanjut:** Orkestrasi tango: intro pad, habanera cellos, solo violin
   arrastre, tutti staccato on climax — lengkap part-list.

## 2.7 Repertoar Adaptasi

- Yo-Yo Ma *Songs from the Americas* (tango).
- Kronos Quartet *Tango*; Metropole orkest salsa charts.
- Ryuichi Sakamoto bossa covers.

## 2.8 Referensi Buku & Sumber Web

**Buku:**
- Rebeca Mauleón, *101 Montunos* (salsa piano).
- John Storm Roberts, *Latin Jazz*.
- Zé Buchman, *A Language for Brazilian Percussion*.

**Web:**
- Conga notation guide (Afro-Cuban): https://www.congahead.com/
- Clave pattern resources: https://www.el-clave.de/
- Tango scores: https://www.tango.info/

---

**Rangkuman:** Adaptasi Latin = memindah clave, groove (bossa/salsa/samba),
harmoni, dan emosi instrumentasi (bandoneón/trumpet montuno) ke ansambel target
tanpa mengubah clave/syncopation. Kembali ke [Latin Karakteristik
(`Ch1-Karakteristik-Notasi.md`)] atau lanjut ke [EDM & Electronic
(`../2.7-Genre-EDM-Electronic/`)].