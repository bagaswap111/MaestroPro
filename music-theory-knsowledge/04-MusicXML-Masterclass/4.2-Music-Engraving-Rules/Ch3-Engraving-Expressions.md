---
title: "Music Engraving — Expressions"
tier: "MusicXML Masterclass"
subject: "Music Engraving Rules"
xml_tags: ["<wedge>", "<direction>", "<direction-type>", "<dynamics>", "<sound>", "<words>", "<metronome>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 3 — Engraving: Expressions

> **Buku panduan bab ini:** Gould, *Behind Bars* (Bab 19 — dynamics; Bab 20 —
> tempo); MusicXML W3C 4.0 — `direction` & `wedge`. Fokus: hairpin, dinamika,
> teks ekspresi, dan integrasi playback agar render & suara serasi.

## 3.1 Hairpins dan Tanda Dinamik Lintas-Bar

*Hairpin* (crescendo/diminuendo) = `<wedge>`; ia membentang antar dua titik
(start → stop).

### 3.1.1 Crescendo

```xml
<direction placement="below">
  <direction-type>
    <wedge type="crescendo" spread="10"/>
  </direction-type>
</direction>
```

### 3.1.2 Diminuendo dan Stop

```xml
<direction placement="below">
  <direction-type>
    <wedge type="diminuendo" spread="8"/>
  </direction-type>
</direction>
...
<direction placement="below">
  <direction-type>
    <wedge type="stop"/>
  </direction-type>
</direction>
```

- `spread` (tenths) — lebar mulut wedge.
- `number` — untuk beberapa hairpin paralel.

## 3.2 Dynamics dan Penempatan

Dinamika titik = `<dynamics>`; posisi default di bawah staff (`below`).

```xml
<direction placement="below">
  <direction-type>
    <dynamics>
      <ff/>
    </dynamics>
  </direction-type>
  <sound dynamics="90"/>
</direction>
```

> `<sound dynamics>` (0–127) menentukan dynamics playback. Nilai umum:
> ppp≈30, p≈40, mp≈55, mf≈70, f≈80, ff≈90, fff≈100.

### 3.2.1 Senarai elemen `<dynamics>`

`pppppp`…`ppp`, `pp`, `p`, `mp`, `mf`, `f`, `ff`, `fff`, `ffff`, plus
`fp`, `pf`, `sf`, `sfz`, `sfp`, `fz`, `rfz`, `rf`.

## 3.3 Teks Instruksi (Expression Words)

### 3.3.1 Teks vs Sound

- `<words>` — teks tampil (rit., accel., con sord., tutti).
- `<sound>` — nilai playback (tempo, dynamics).

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">rit.</words>
  </direction-type>
  <sound tempo="90"/>
</direction>
```

### 3.3.2 Format Teks

```xml
<direction placement="above">
  <direction-type>
    <words font-family="Times New Roman" font-size="14" font-style="italic"
           font-weight="bold" xml:space="preserve">
      cantabile
    </words>
  </direction-type>
</direction>
```

- Styling opsional di `words`; ini *soft hint* — software override.

## 3.4 Hairpin vs Dynamics Point — Peta Keputusan

| Fungsi | Elemen yang tepat |
|--------|-------------------|
| Dinamika instan | `<dynamics>` |
| Perubahan gradual | `<wedge>` (start → stop) |
| Instruksi imperatif "cresc." teks | `<words>` |
| Playback ramp | `<sound>` pada start/stop + `wedge` |

## 3.5 Contoh: Crescendo → Forte Penutup

```xml
<measure number="9">
  <direction placement="below">
    <direction-type>
      <wedge type="crescendo" spread="12"/>
    </direction-type>
  </direction>
  <note>
    <pitch><step>F</step><octave>4</octave></pitch>
    <duration>4</duration>
    <type>whole</type>
  </note>
</measure>

<measure number="10">
  <direction placement="below">
    <direction-type>
      <wedge type="stop"/>
    </direction-type>
  </direction>
  <direction placement="below">
    <direction-type>
      <dynamics><ff/></dynamics>
    </direction-type>
    <sound dynamics="95"/>
  </direction>
  <note>
    <pitch><step>F</step><octave>4</octave></pitch>
    <duration>4</duration>
    <type>whole</type>
  </note>
</measure>
```

## 3.6 Tempo Expressions

```xml
<direction placement="above">
  <direction-type>
    <words xml:space="preserve">Andante</words>
    <metronome parentheses="yes">
      <beat-unit>quarter</beat-unit>
      <per-minute>76</per-minute>
    </metronome>
  </direction-type>
  <sound tempo="76"/>
</direction>
```

- `parentheses="yes"` — metronome dalam kurung.
- Acengan seperti `M.M.` tidak perlu ditulis; `per-minute` memberi angka.

## 3.7 Catatan Placement

| Tampilan | Umumnya |
|----------|---------|
| Di atas staff | Tempo, articulation, tekstik instruksi |
| Di bawah staff | Dynamics, hairpin, bowing |
| Posisi bebas | `default-x`, `default-y` (tenths) |

### 3.7.1 Precision via default

```xml
<direction placement="below">
  <direction-type>
    <dynamics><mp/></dynamics>
  </direction-type>
  <default-x>42</default-x>
  <default-y>18</default-y>
</direction>
```

## 3.8 Checklist Expressions

| Periksa | Ya/Tidak |
|---------|----------|
| Hairpin punya start & stop (`wedge`)? | |
| Dynamics + `sound dynamics` sinkron? | |
| Teks instruksi di `words`? | |
| Placement atas/bawah konsisten? | |
| Spread hairpin sesuai frase? | |

## 3.9 Miskonsepsi

- **"`<wedge>` butuh nilai dynamics"** — Tidak; wedge adalah visual; `sound`
  opsional untuk playback ramp.
- **"Dinamika wajib elemen khusus"** — `words` dgn teks bekerja, tapi elemen
  `<dynamics>` member standardisasi.
- **"Tempo harus `parentheses`"** — Break convention; parentheses hanya untuk
  tempi relatif/rauno.

## 3.10 Referensi

- Gould, *Behind Bars* — ch.19–20.
- MusicXML W3C — direction/wedge:
  https://www.w3.org/2021/06/musicxml40/

---

**Rangkuman:** Expressions = `<direction>` (words, dynamics, wedge, metronome,
sound) untuk menyatukan render & playback. Lanjut ke [Playback & MIDI
Integration (`../4.3-Playback-MIDI-Integration/`)].