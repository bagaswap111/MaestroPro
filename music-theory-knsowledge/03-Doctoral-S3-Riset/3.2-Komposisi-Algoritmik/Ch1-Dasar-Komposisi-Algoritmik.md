---
title: "Komposisi Algoritmik"
tier: "Doctoral S3"
subject: "Komposisi Algoritmik"
xml_tags: ["<note>", "<pitch>", "<duration>", "<rest>"]
software: ["Python", "Max/MSP", "OpenMusic", "SuperCollider", "music21"]
---

# Bab 1 — Komposisi Algoritmik

> **Buku panduan bab ini:** Curtis Roads & John Strawn, *Foundations of
> Computer Music*; Gerhard Nierhaus, *Algorithmic Composition* (Springer);
> Iannis Xenakis, *Formalized Music*; praktik IRCAM (OpenMusic).
> Fokus: paradigma algoritme — Markov, stochastic, GA, cellular automata,
> L-systems — dan jembatan ke MusicXML.

## 1.1 Definisi

Komposisi algoritmik = penggunaan aturan/prosedur (tidak harus digital)
untuk menghasilkan struktur musikal — dari *Ars combinatoria* Mozart hingga
*Markov chains* modern.

## 1.2 Prinsip Dasar

| Paradigma | Deskripsi | Contoh |
|-----------|-----------|--------|
| **Markov chains** | Transisi state berdasar probabilitas | Melodi kontinu |
| **Stochastic processes** | Random sintetis (Gaussian, Poisson) | onset/durasi aleatorik |
| **Rule-based** | Aturan gramatikal (contrapunctus) | Counterpoint generator |
| **Evolutionary/GA** | Seleksi berbasis fitness | Kantorovich |
| **Cellular automata** | Aturan lokal update sel | Xenakis, *Polytopes* |
| **Fractal / L-systems** | Self-similar | Organizing processes |
| **Grammars** | Sintaks musikal (T-music, generative) | Chorale harmonization |

## 1.3 Arsitektur Umum

```
Input (data, rules, seed)
    │
    ▼
┌────────────────────┐
│ Algoritme generator│   (Markov, GA, stochastic...)
└────────┬───────────┘
         │
         ▼
  Struktur musikal (Stream / OM voice)
         │
         ▼
  MusicXML / sound
```

> Prinsip reproducibility: sebar acak dipatok (`seed`), parameter dicatat —
> penting untuk riset.

## 1.4 Algoritme Kunci

### 1.4.1 Markov Chains

- Bangun *transition matrix* dari korpus (pitch → durasi).
- Contoh prob: `(C→D)=0.3`, `(D→E)=0.2`, dst.
- Mulai dari seed, ikuti probabilitas hingga panjang tercapai.

```python
import random
trans = {
    "C": ["D", "C", "G", "E"],
    "D": ["B", "D", "E", "C"],
    "E": ["F", "E", "D", "G"],
    "G": ["C", "G", "A", "B"],
}
def walk(start="C", length=8):
    seq = [start]
    for _ in range(length - 1):
        seq.append(random.choice(trans[seq[-1]]))
    return seq
print(walk("C"))
```

### 1.4.2 Ars Combinatoria / Dice Game (Mozart)

- Permutasi bar yang sudah ada (dice).
- Basis notorial: Musikalisches Würfelspiel KV 616f.

### 1.4.3 Cellular Automata (Wolfram)

- Sel = pitch/keyer; nilai 0/1.
- Aturan lokal (rule 30, 110, 90) → baris = melodi.

### 1.4.4 Grammars (T-music)

- Rule-based: `Σ → produksi` — dari likid harmony hingga kontrapung.

### 1.4.5 Evolutionary (GA)

- *Population* = solusi (fragmen/fitur).
- Fitness = kemiripan korpus/aturan → crossover/mutasi.

## 1.5 Tool Utama

| Tool | Kekuatan | Bahasa |
|------|----------|--------|
| **Max/MSP** | real-time audio & control | visual |
| **OpenMusic** (IRCAM) | komposisi & analisis | Lisp visual |
| **Python + music21** | transform, XML I/O | Python |
| **SuperCollider** | sound synthesis | sclang |
| **Csound** | sound design | CSD |

> Untuk pendidikan: mulai Python + music21 → OpenMusic untuk spektral &
> algorithmic composition (IRCAM).

## 1.6 musik Algoritmik → Stream

`music21` menerima output sebagai `stream.Part` dan output MusicXML:

```python
from music21 import stream, note

melody = ["C4","E4","G4","B4","C5"]
part = stream.Part()
for p in melody:
    part.append(note.Note(p, quarterLength=0.5))
part.write('musicxml', fp='algo.musicxml')
```

> Detail Stream→MusicXML: `Ch2-MusicXML-Scripting-Python.md`.

## 1.7 Konteks Research

1. **Korpus besar:** J.S. Bach chorale → model probabilitas (DSM).
2. **Fitness:** kemiripan/kompleksitas — evaluasi framework.
3. **Human + machine:** prosedural — manusia memilih varian terbaik.

## 1.8 Checklist Komposisi Algoritmik

| Periksa | Ya/Tidak |
|---------|----------|
| Parameter algoritme (seed) terdokumentasi? | |
| Keluaran bisa → MusicXML? | |
| Model dievaluasi secara musikal? | |
| Reproducibility (seed) dijaga? | |
| Bahan riset (korpus) dicatat? | |

## 1.9 Miskonsepsi

- **"Algoritmik = musik acak"** — Ada kontrol parameter; mengevaluasi
  musikalitas justru kunci.
- **"Muncul secara instan"** — Membutuhkan tuning parameter & evaluasi.
- **"Semua output jadi bagus"** — Seleksi manusia tetap penting (Xenakis,
  Roads menekankan hal ini).

## 1.10 Latihan

1. Implementasi Markov pitch 8-note → Stream → MusicXML.
2. Cellular automata rule 30 → 8 bar melody.
3. GA fitness: chorus harmonik vs kontrapung.

## 1.11 Referensi

- Nierhaus, *Algorithmic Composition*.
- Roads & Strawn, *Foundations of Computer Music*.
- Xenakis, *Formalized Music*.
- IRCAM OpenMusic: https://opengroup.ircam.fr/

---

**Rangkuman:** Komposisi algoritmik memadukan matematika, probabilitas, dan
musik. Output sering Stream/MIDI/MusicXML — jembatan ke notasi (lihat
`Ch2-MusicXML-Scripting-Python.md`).