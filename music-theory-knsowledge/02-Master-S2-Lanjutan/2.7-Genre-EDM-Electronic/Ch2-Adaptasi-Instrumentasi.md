---
title: "EDM & Electronic — Adaptasi Lintas Instrumentasi"
tier: "Master S2"
subject: "Genre EDM & Electronic"
xml_tags: ["<score-part>", "<midi-instrument>", "<midi-program>", "<glissando>", "<tremolo>", "<direction>", "<beat-repeat>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — EDM & Electronic: Adaptasi Lintas Instrumentasi

## 2.1 Dari Synth ke Akustik: Peta Timbre → Instrumen

EDM → ansambel akustik/orchestra adalah **translasi timbre + groove**, bukan
bassline literal:

| Bunyi synth | Warna akustik |
|-------------|---------------|
| Supersaw lead | Violin section *unisono* + tremolo |
| 808 sub-bass | Bass trombone/tuba + timpani (C1 region) |
| Pluck/piano | Harp/marimba + pianoforte arpeggio |
| Stab chord | Horn/trumpet stabs (straight, no swing) |
| Arp 16th | Xylophone/marimba / mandolin tremolo |
| Risers/TRUE | Timpani roll + string gliss up + cymbal |
| Drops half-time | Kecil — punch, strings détaché |

## 2.2 Adaptasi 1: Festival House → Full Orchestra (Live Score)

Strategi *orchestral house cover*:

1. `kick 4/4` → timpani (quarter notes) + contrabass.
2. `chord stab` → brass stabs (trumpet 1–3 + horns) di off-beat.
3. `pad` → string section divisi pad (arco, dynamic swells).
4. `lead saw` → violin 1 + piccolo *unison/octave* (register tinggi).
5. `build` → snare roll + riser text (`cresc. molto`) + timpani roll.
6. `drop` → full tutti + timpani + cymbals + chimes.

```xml
<note>
  <pitch><step>E</step><octave>1</octave></pitch>
  <duration>4</duration>
  <voice>4</voice>
  <staff>2</staff>
  <type>quarter</type>
  <notations><technical><timpani-tap/></technical></notations>
</note>
```

## 2.3 Adaptasi 2: Trap (808) → Modern Acoustic Ensemble

- **808 gliss** → contrabass gliss (mi) at octave 1 (extreme), atau tuba
  *scoop*.
- **Hi-hat 16th/32nd** → tambourine/jingle (mara) 16th (straight).
- **Vocal chops** → saxophone *sob* atau violin *pizzicato* (staccato echo).
- **Half-time drop** → strings *détaché* pada bass line, timpani + crash.

```xml
<direction placement="above">
  <direction-type><words>half-time drop</words></direction-type>
</direction>
<note>
  <pitch><step>F</step><octave>1</octave></pitch>
  <duration>8</duration>
  <type>half</type>
  <notations><glissando type="start" line-type="chromatic"/></notations>
</note>
```

## 2.4 Adaptasi 3: Trance → Lounge/Piano Chamber

- **Arp 16th** → piano right-hand arpeggio (not write 96ths — originale break)
  + *mandolin* tremolo.
- **Pad epic** → vibes/marimba + string con sordino.
- **Lead melody** → flute/x flute (register 2nd oktaf).
- **Bass line** → cello/bass pizz, arpeggiated.

## 2.5 Checklist Adaptasi EDM → Akustik

| Cek | Hasil |
|-----|-------|
| Feel/bpm EDM dipertahankan (tempo text)? | |
| Kick/drop → timpani/percussion mapping? | |
| Sub-bass → tuba/bass register diterapkan? | |
| Arp → instrumen idiomatik (xylo/piano)? | |
| Riser build → roll + ws? | |
| Chord stabs → brass section off-beat? | |
| `score-part`+`midi-program` untuk ekspor DAW benar? | |

## 2.6 Latihan

1. **Dasar:** Tulis 4-bar house → timpani+strings combo (kick 4/4, stabs).
2. **Menengah:** Trap 808 gliss → contrabass (8 bar half-time).
3. **Lanjut:** Orkestrasi *future-bass drop* 16 bar: supersaw→strings, arp→
   xylo, sub→tuba, riser→snare roll, pad→string divisi — cek di MuseScore.

## 2.7 Referensi Repertoar (Live EDM→Orchestra)

- **Metropole Orkest + DJs** (live house set).
- **KOP Balls symphonic EDM concerts**.
- 8-bit/chiptune → orchestra arrangements (video game music).

## 2.8 Referensi Buku & Sumber Web

**Buku:**
- Curtis Roads, *Computer Music Tutorial*.
- Blend of *"Electronic vs acoustic palette"* — orchestration-diff studies.

**Web:**
- Dorico — playback MIDI program:
  https://www.steinberg.net/help/dorico/
- MusicXML `<playback>` example:
  https://www.w3.org/2021/06/musicxml40/tutorial/

---

**Rangkuman:** EDM → akustik = peta timbre synth ke warna orkestra/kamer,
peta groove ke perkusi, dan pertahankan bentuk build/drop. MusicXML
`score-part`+`midi-program` mendukung ekspor DAW. Kembali ke [EDM Karakteristik
(`Ch1-Karakteristik-Notasi.md`)]. Genre Tier 2 selesai — lanjut ke **Deepening
Tier 01**. Kembali ke akar: [Fondasi Genre
(`../../01-Bachelor-S1-Fondasi/1.4-Genre-Fondasi/Ch1-Parameter-Genre.md`)].