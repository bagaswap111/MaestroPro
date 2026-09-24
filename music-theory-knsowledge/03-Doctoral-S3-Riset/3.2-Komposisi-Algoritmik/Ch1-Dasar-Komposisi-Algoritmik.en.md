---
title: "Algorithmic Composition"
tier: "Doctoral S3"
subject: "Algorithmic Composition"
xml_tags: ["<note>", "<pitch>", "<duration>", "<rest>"]
software: ["Python", "Max/MSP", "OpenMusic", "SuperCollider", "music21"]
---

# Chapter 1 — Algorithmic Composition

> **Guide books for this chapter:** Curtis Roads & John Strawn, *Foundations of
> Computer Music*; Gerhard Nierhaus, *Algorithmic Composition* (Springer);
> Iannis Xenakis, *Formalized Music*; IRCAM practice (OpenMusic).
> Focus: algorithmic paradigms — Markov, stochastic, GA, cellular automata,
> L-systems — and the bridge to MusicXML.

## 1.1 Definition

Algorithmic composition = use of rules/procedures (not necessarily digital)
to generate musical structure — from Mozart's *Ars combinatoria* to modern
*Markov chains*.

## 1.2 Basic Principles

| Paradigm | Description | Example |
|-----------|-----------|--------|
| **Markov chains** | State transitions based on probability | Continuous melody |
| **Stochastic processes** | Random synthesis (Gaussian, Poisson) | Aleatoric onset/duration |
| **Rule-based** | Grammatical rules (contrapunctus) | Counterpoint generator |
| **Evolutionary/GA** | Fitness-based selection | Kantorovich |
| **Cellular automata** | Local cell update rules | Xenakis, *Polytopes* |
| **Fractal / L-systems** | Self-similar | Organizing processes |
| **Grammars** | Musical syntax (T-music, generative) | Chorale harmonization |

## 1.3 General Architecture

```
Input (data, rules, seed)
    │
    ▼
┌────────────────────┐
│ Generator algorithm │   (Markov, GA, stochastic...)
└────────┬───────────┘
         │
         ▼
  Musical structure (Stream / OM voice)
         │
         ▼
  MusicXML / sound
```

> Reproducibility principle: random draws are pinned (`seed`), parameters are recorded —
> important for research.

## 1.4 Key Algorithms

### 1.4.1 Markov Chains

- Build a *transition matrix* from a corpus (pitch → duration).
- Example probabilities: `(C→D)=0.3`, `(D→E)=0.2`, etc.
- Start from a seed, follow probabilities until the desired length is reached.

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

- Permute existing bars (dice).
- Notorial basis: Musikalisches Würfelspiel KV 616f.

### 1.4.3 Cellular Automata (Wolfram)

- Cell = pitch/keyer; value 0/1.
- Local rules (rule 30, 110, 90) → row = melody.

### 1.4.4 Grammars (T-music)

- Rule-based: `Σ → production` — from liquid harmony to counterpoint.

### 1.4.5 Evolutionary (GA)

- *Population* = solutions (fragments/features).
- Fitness = corpus/rules similarity → crossover/mutation.

## 1.5 Main Tools

| Tool | Strength | Language |
|------|----------|--------|
| **Max/MSP** | real-time audio & control | visual |
| **OpenMusic** (IRCAM) | composition & analysis | visual Lisp |
| **Python + music21** | transform, XML I/O | Python |
| **SuperCollider** | sound synthesis | sclang |
| **Csound** | sound design | CSD |

> For education: start with Python + music21 → OpenMusic for spectral &
> algorithmic composition (IRCAM).

## 1.6 Algorithmic Music → Stream

`music21` accepts output as `stream.Part` and outputs MusicXML:

```python
from music21 import stream, note

melody = ["C4","E4","G4","B4","C5"]
part = stream.Part()
for p in melody:
    part.append(note.Note(p, quarterLength=0.5))
part.write('musicxml', fp='algo.musicxml')
```

> Stream→MusicXML details: `Ch2-MusicXML-Scripting-Python.md`.

## 1.7 Research Context

1. **Large corpora:** J.S. Bach chorales → probability models (DSM).
2. **Fitness:** similarity/complexity — evaluation framework.
3. **Human + machine:** procedural — humans choose the best variants.

## 1.8 Algorithmic Composition Checklist

| Check | Yes/No |
|---------|----------|
| Are algorithm parameters (seed) documented? | |
| Can the output go → MusicXML? | |
| Is the model evaluated musically? | |
| Is reproducibility (seed) maintained? | |
| Are research materials (corpus) recorded? | |

## 1.9 Misconceptions

- **"Algorithmic = random music"** — Parameters are controlled; evaluating
  musicality is precisely the key.
- **"It appears instantly"** — Requires parameter tuning & evaluation.
- **"All output turns out good"** — Human selection remains important (Xenakis,
  Roads emphasize this).

## 1.10 Exercises

1. Implement an 8-note Markov pitch → Stream → MusicXML.
2. Cellular automata rule 30 → 8-bar melody.
3. GA fitness: harmonic chorale vs counterpoint.

## 1.11 References

- Nierhaus, *Algorithmic Composition*.
- Roads & Strawn, *Foundations of Computer Music*.
- Xenakis, *Formalized Music*.
- IRCAM OpenMusic: https://opengroup.ircam.fr/

---

**Summary:** Algorithmic composition combines mathematics, probability, and
music. Output is often Stream/MIDI/MusicXML — a bridge to notation (see
`Ch2-MusicXML-Scripting-Python.md`).
