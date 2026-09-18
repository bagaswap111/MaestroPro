---
title: "Scripting Praktis untuk Arranger"
tier: "Workflow & Portfolio"
subject: "Otomasi Python Scripting"
xml_tags: ["score-partwise", "note", "pitch", "transpose", "duration"]
software: ["Python", "music21", "MuseScore", "Dorico"]
---

# Bab 2 — Scripting Praktis untuk Arranger

> **Buku panduan bab ini:** music21 documentation; praktik otomasi dari
> workflow MIDI (kuantisasi — kait ke
> `../../04-MusicXML-Masterclass/4.3-Playback-MIDI-Integration/Ch2-MIDI-Quantization.md`).
> Fokus: 5 skrip yang menyelesaikan pekerjaan harian arranger.

## 2.1 Skenario Kasus Sering

| # | Skenario | Manfaat |
|---|----------|---------|
| 1 | Batch transposisi | Pindahkan seluruh part sekaligus |
| 2 | Pemisahan part | 1 file per instrumen utk part cetak |
| 3 | Template generator | Kerangka orkestra 100+ part instan |
| 4 | Validasi range | Tandai not di luar rentang |
| 5 | Normalisasi MIDI | Bersihkan file MIDI-import |

## 2.2 Skrip A: Batch Transposisi

```python
from pathlib import Path
from music21 import converter

for xml_path in Path('scores').glob('*.musicxml'):
    score = converter.parse(str(xml_path))
    score.transpose('M2', inPlace=True)
    out = xml_path.with_name(xml_path.stem + '_transposed.musicxml')
    score.write('musicxml', fp=str(out))
    print('Done:', out.name)
```

**Catatan:** untuk part transpos per-instrumen cek
`../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`.

## 2.3 Skrip B: Pemisahan Part

```python
from music21 import converter, stream

score = converter.parse('full_score.musicxml')

for i, part in enumerate(score.parts):
    single = stream.Score()
    single.insert(0, part)
    safe_name = part.partName or f"part_{i}"
    safe_name = "".join(c for c in safe_name if c.isalnum() or c in " _-")
    single.write('musicxml', fp=f"parts/{safe_name}.musicxml")
```

## 2.4 Skrip C: Template Orkestra

```python
from music21 import stream, instrument, meter, key

TEMPLATE = [
    ("Flute 1", "Fl.1", 73, 1),       # (name, abbr, mgm, channel)
    ("Oboe 1", "Ob.1", 68, 2),
    ("Clarinet Bb 1", "Cl.1", 71, 3),
    ("Bassoon 1", "Bsn.1", 70, 4),
    ("Horn in F 1", "Hn.1", 60, 5),
    ("Trumpet Bb 1", "Tpt.1", 56, 6),
    ("Trombone 1", "Tbn.1", 57, 7),
    ("Percussion", "Perc.", 0, 10),
    ("Violin I", "Vl.I", 40, 9),
    ("Viola", "Vla.", 41, 10),
    ("Cello", "Vc.", 42, 11),
    ("Double Bass", "Db.", 43, 12),
]

def build_template():
    score = stream.Score()
    for name, abbr, prog, ch in TEMPLATE:
        part = stream.Part()
        part.partName = name
        part.partAbbreviation = abbr
        inst = instrument.Instrument(midiProgram=prog, midiChannel=ch)
        part.append(inst)
        part.append(key.Key('C'))
        part.append(meter.TimeSignature('4/4'))
        score.append(part)
    return score

tpl = build_template()
tpl.write('musicxml', fp='orchestra_template.musicxml')
```

> **Percussion channel 10** khusus GM; gunakan `midiProgram=0` (perc). Untuk
> hi-hat/snare merujuk `Ch4-Notasi-Percussion`.

## 2.5 Skrip D: Validasi Range

```python
RANGES = {
    "Flute": ("C4", "D7"),
    "Oboe": ("Bb3", "A6"),
    "Clarinet Bb 1": ("D3", "A6"),
    "Horn in F 1": ("F2", "F5"),
}

for part in score.parts:
    lo, hi = RANGES.get(part.partName, (None, None))
    if lo is None:
        continue
    lo_p = note.Note(lo).pitch
    hi_p = note.Note(hi).pitch
    for n in part.recurse().notes:
        if not lo_p <= n.pitch <= hi_p:
            print(f"[{part.partName}] out:", n.pitch, 'bar', n.measureNumber)
```

> Rentang mengikuti Adler/Rimsky di Tier 1 (`Ch1-Keluarga-Instrumen-Ranges`).

## 2.6 Skrip E: Normalisasi MIDI-Import

```python
midi = converter.parse('draft.mid')
midi.quantize(quantizationUnit=0.5)

from music21 import stream
cleaned = stream.Stream()
for n in midi.flatten().notes:
    if n.quarterLength >= 0.125:      # buang ghost < 1/32
        cleaned.append(n)
cleaned.write('musicxml', fp='cleaned.musicxml')
```

> Rujukan kuantisasi: `../../04-MusicXML-Masterclass/4.3-Playback-MIDI-Integration/Ch2-MIDI-Quantization.md`.

## 2.7 Rekomendasi Workflow

1. Simpan skrip di `scripts/` + `requirements.txt`.
2. Gunakan `argparse` untuk CLI-friendly.
3. Eksekusi massal dengan `concurrent.futures` bila file banyak.
4. Selalu validasi output dengan parse ulang (MuseScore round-trip).

## 2.8 Miskonsepsi

- **"Scripting menggantikan telinga"** — Otomasi mempercepat tugas
  mekanis; keputusan musical tetap manusia.
- **"`quantize` memperbaiki semua"** — Tak dapat memperbaiki timing yang
  sangat off; kombinasi loop + manual edit.
- **"Template sekali buat selamanya"** — Update tiap ada perubahan range/
  instrument baru.

## 2.9 Latihan

1. Jalankan Skrip A pada 3 file → cek hasil di editor.
2. Buat Skrip D dengan rentang 10 instrumen → jalankan pada karya Anda.
3. Integrasi Skrip C + pemisahan part → workflow lengkap orkestra.
4. Ekstrak chordify + roman numeral untuk analisis cepat (dari Ch1).

## 2.10 Checklist Praktis

| Periksa | Ya/Tidak |
|---------|----------|
| Skrip test pada file kecil dulu? | |
| Path/folder output jelas? | |
| Hasil tervalidasi (parse ulang)? | |
| Logging error + exception handling? | |
| Dependencies didokumentasikan? | |

## 2.11 Referensi

- *music21 docs*: https://web.mit.edu/music21/userGuide/
- Cutbirth/Ariza.
- Rujukan kuantisasi Tier 4.

---

**Rangkuman:** 5 skrip praktis — batch transposisi, pemisahan part, template,
validasi range, normalisasi MIDI — mengotomasi pekerjaan berulang arranger.
Test kecil → scaling → validasi output.