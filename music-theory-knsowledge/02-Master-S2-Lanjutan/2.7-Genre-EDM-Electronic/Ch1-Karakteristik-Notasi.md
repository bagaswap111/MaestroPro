---
title: "EDM & Electronic — Karakteristik & Notasi"
tier: "Master S2"
subject: "Genre EDM & Electronic"
xml_tags: ["<sound>", "<midi-instrument>", "<midi-program>", "<direction>", "<words>", "<tempo>", "<tremolo>"]
software: ["Dorico", "Sibelius", "Finale", "Logic Pro", "Ableton Live", "Cubase"]
---

# Bab 1 — EDM & Electronic: Karakteristik & Notasi

## 1.1 Grid-based Music dan Notasinya

EDM lahir dari **DAW grid** — 16th (atau 32nd) sebagai unit rapat. Saat seorang
arranger menulis ke MusicXML, tujuannya bukan *human performance* tapi
**scripting akurat** untuk playback.

Bahasa elemen EDM:

| Istilah | Arti |
|---------|------|
| **Build** | Ramp 4/8/16 bar → intensitas naik (riser, snare roll) |
| **Drop** | Puncak energi: bass groove penuh, kick 4/4 |
| **Break** | Tenang: pad, vokal, riser lagu |
| **Riser** | Noise/sweep crescendo (8→16 bar) |
| **Half-time drop** | Energi → bass 1/2 speed (trap feel) |
| **Anticlimax** | *Drop* tidak penuh — dominan menahan |

### 1.1.1 Template Bentuk 128 Bar ("Festival EDM")

`Intro (16) – Build (8) – Drop (16) – Build (8) – Drop (16) – Break (16) –
Riser (8) – Drop (32) – Outro (8)`

## 1.2 Tempo dan Groove EDM

- **House:** 120–128 BPM, kick 4/4, hi-hat off-beat 8th.
- **Techno:** 125–130, *driving*, minimal.
- **Trance:** 135–140, bass-line sequenced, pad epic.
- **Dubstep:** 70–75 BPM (half-time, wub); **Trap:** 70–80, 808, hats 16th/
  32nd; **Future bass:** 150–160, supersaw; **G-House** etc.

Di MusicXML: metronome `<per-minute>` + optional tempo text.

```xml
<direction placement="above">
  <direction-type><words>Drop — 128 BPM</words></direction-type>
  <sound tempo="128"/>
</direction>
<metronome>
  <beat-unit>quarter</beat-unit>
  <per-minute>128</per-minute>
</metronome>
```

## 1.3 Sintesis = Timbre: Program & Bend Notasi

Electronic music: **timbre adalah komposisi**. Trake MIDI program membantu
playback:

| Bunyi | MIDI program |
|-------|--------------|
| Saw lead / supersaw | 80 (Lead 1 - square) / 81 |
| 808 sub bass | 36/ FL bass program |
| Wax / pluck | 98 (FX/bright) |
| Pad | 89 (Warm pad) / 88 |
| Arp | 81 / 84 (Lead) |
| FX riser | 101–110 |

Synthesizer notation for score: tulis *arpeggio* sebagai **not analitik** cukup
triage (bukan semua 16th — readability), dengan `direction` "AI arp".

## 1.4 Bass 808 dan Sidechain (Notasi)

- **808 bass:** *sustain + pitch drop* setiap kick — tulis not panjang dengan
  `glissando` ke bawah (`falloff`), atau sediakan *steps* pitch di 16th.
- **Sidechain / pumping:** sinkopasi volume — tandai `<sound volume>` naik-
  turun per beat di DAW; di score tulis "*sidechain 16th, volume 70%*" di
  direction.

```xml
<note>
  <pitch><step>E</step><octave>1</octave></pitch>
  <duration>4</duration>
  <type>quarter</type>
  <notations>
    <glissando type="start"/>
  </notations>
</note>
```

## 1.5 Arpeggiator dan Chord Stab

- **Arp (16th/32nd)** — not sidik sebagai *sequence* (jangan <chord>).
- **Chord stabs (house)** — semua not serentak di off-beat: `<chord>`.

```xml
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>16th</type>
  <notations><articulations><staccato/></articulations></notations>
</note>
<note>
  <pitch><step>E</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>16th</type>
  <chord/>
  <notations><articulations><staccato/></articulations></notations>
</note>
<note>
  <pitch><step>G</step><octave>4</octave></pitch>
  <duration>2</duration>
  <type>16th</type>
  <chord/>
</note>
```

## 1.6 Miskonsepsi Umum

- **"EDM = tanpa teori harmoni"** — Harmoni progresi *loop* tetap teori
  (minor/dorian/lydian sangat umum).
- **"MIDI program selalu dipertahankan"** — Dorico/MuseScore export dengan
  `midi-program`; jika ingin suara synth, perlu plugin synth di DAW — bagian
  score playback terbatas.
- **"Arp = harus semua not ditulis"** — Untuk playback ya; untuk *score*
  artifikan — tulis pola panduan + text "arp".

## 1.7 Latihan

1. **Dasar:** Tulis 4-bar house groove: kick 4/4, hat off-beat, bass root.
2. **Menengah:** Tulis *build* 8 bar: riser text, snare roll, chord alignment.
3. **Lanjut:** Buat *future bass drop* 16 bar di MusicXML dengan arp 16th,
   supersaw pads, sub-bass gliss — tambahkan `direction` sections.

## 1.8 Repertoar Dengar

- Daft Punk, *One More Time*, *Harder Better* — house.
- Eric Prydz; Above & Beyond (trance); Skrillex (dubstep); Flume
  (future). Zedd.

## 1.9 Referensi Buku & Sumber Web

**Buku:**
- Curtis Roads, *The Computer Music Tutorial* (bab synthesis).
- Francis & J. "Electronic Music USA" — DAW arranging.
- David Sonnenschein, *Sound Design*.

**Web:**
- MIDI program reference:
  https://www.midi.org/
- MusicXML playback spec — `<sound>` & `<midi-instrument>`:
  https://www.w3.org/2021/06/musicxml40/
- Dorico — MIDI & percussion:
  https://www.steinberg.net/help/dorico/

---

**Rangkuman:** EDM = grid 16th + bentuk build/drop + timbre synth. MusicXML
diwakili `<metronome>`, `<sound>`, `midi-program`, arp sebagai not sequence,
stabs `<chord>`. Lanjut ke [Adaptasi EDM/Electronic (`Ch2-Adaptasi-Instrumentasi.md`)].