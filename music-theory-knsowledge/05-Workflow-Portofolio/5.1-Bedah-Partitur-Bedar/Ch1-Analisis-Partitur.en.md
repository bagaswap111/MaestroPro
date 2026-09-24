---
title: "Score Analysis"
tier: "Workflow & Portfolio"
subject: "Score Dissection"
xml_tags: ["<part-list>", "<key>", "<time>", "<measure>", "<direction>"]
software: ["Dorico", "Sibelius", "MuseScore", "IMSLP", "music21"]
---

# Chapter 1 — Score Analysis

> **Guidebook for this chapter:** Samuel Adler, *The Study of Orchestration*
> (the "Analyzing Scores" chapter); Nikolai Rimsky-Korsakov, *Principles of
> Orchestration* (Chapters 1–5); Bach Society-style *score reading* practice.
> Focus: a systematic score dissection framework that can be repeated on any work.

## 1.1 Why Dissect Scores?

Analyzing masterworks is one of the fastest ways to build an
orchestration vocabulary: every decision the composer makes — instrumentation,
register, doubling, balance, and fugue — becomes a lesson that can be
replicated. This is the core of the arranger's skill.

**Practical benefits:**
- Seeing *how* effectiveness is achieved (the process), not just the result.
- Building an internal reference for the orchestra's sense of breadth.
- Providing an objective basis for your own arrangement decisions.

## 1.2 Seven-Stage Analysis Framework

| Stage | Focus | Key Questions | Tools |
|-------|-------|---------------|-------|
| 1. Identity | Work, composer, era, editor | Who & when? Which edition? | IMSLP/score |
| 2. Instrumentation | Complete `part-list` | How many parts? Which instruments? | MusicXML part-list |
| 3. Key & Meter | `key`, `time`, tempo | Tonal & rhythmic setting | music21 analyze |
| 4. Formal Structure | section, rehearsal | Exposition? Development? | Rehearsal marks |
| 5. Texture | melody, harmony, bass | Homophonic/polyphonic? | Score inspection |
| 6. Orchestration palette | doubling, register | Who has the melody? Who fills in? | Instrument pairs |
| 7. Expression details | articulations, dynamics | Expressive nuance | Part inspection |

> **Adler** recommends staged analysis: first *skim* (identity +
> structure) → second *zoom in* (palette + details) → third *roll* it into
> your personal portfolio.

## 1.3 Score Sources

| Source | Type | Notes |
|--------|------|-------|
| **IMSLP.org** | Public domain (PDF & MusicXML) | Primary source |
| **MuseScore.com** | Community (handy MusicXML) | Check quality |
| **Digital scores** | Commercial editions (scanned) | Subject to copyright |
| **Library of Congress** | Manuscripts/historical | For research |

> Download both the PDF **and** MusicXML versions when possible: PDF for the
> visual (register, bowing), XML for isolated analysis in music21.

## 1.4 Analysis Workflow in music21

```python
from music21 import converter, corpus

score = converter.parse('beethoven.musicxml')

# 1) Key & progression (relative/absolute key)
print(score.analyze('key'))

# 2) Size of each part
for part in score.parts:
    print(part.partName, 'len:', len(part.notes))

# 3) Tempo & metronome
for tm in score.metronomeMarkBoundaries():
    print('bar', tm[0].number, '→', tm[1])

# 4) Cut a section (extract exposition: bar 1–8)
subset = score.measures(1, 8)
subset.show('text')
```

> `converter.parse` accepts `format='musicxml'`, `format='midi'`, or
> `corpus.parse('fugue')` for the built-in corpus.

## 1.5 Register & Doubling Analysis Techniques

- **Comfortable register test:** check whether the melody sits in the
  comfortable register of the lead instruments.
- **Doubling map:** create a table of who plays the same pitch at each
  key moment (identify simultaneous octaves/unisons).

Example doubling table for a climax moment:

| Bar | Instruments | Register | Role |
|-----|-------------|----------|------|
| 45–52 | Violin I + Flute | A5–E6 | Unison melody |
| 45–52 | Trombone 1 + Bassoon | G3–C4 | Harmony filler |
| 45–52 | Cello + Bass | C2–C3 | Bass |

## 1.6 Analysis Checklist

| Check | Notes |
|-------|-------|
| 1. Complete identity (composer, era)? | |
| 2. Instrumentation identified? | |
| 3. Key/meter/tempo noted? | |
| 4. Form mapped (section labels)? | |
| 5. Texture & palette analyzed? | |
| 6. Details (dynamics/articulation) studied? | |
| 7. Conclusions documented in portfolio? | |

## 1.7 Misconceptions

- **"Score analysis = memorizing notes"** — Its main purpose is to understand
  orchestration decisions (the why), not just the notes.
- **"One part is enough"** — The full score is required to
  see the balance.
- **"Every work can be dissected in 7 stages"** — Short sketches/pop songs need only
  three stages: instrumentation → structure → texture.

## 1.8 Exercises

1. **Skim** — take the score of 1 Mozart symphony, note instrumentation &
   form (15 minutes).
2. **Zoom in** — pick a 16-bar climax, draw a doubling map.
3. **Roll** — write 3 lessons → your own 8-bar orchestration miniature.
4. **Digital** — parse MusicXML via music21, extract tempo/key.

## 1.9 Recommended Repertoire for Dissection

- **Mozart — Symphony No. 40:** clear form & structure.
- **Beethoven — Symphony No. 5, I:** motif + doubling.
- **Ravel — Boléro:** gradual orchestration crescendo.
- **Stravinsky — The Rite of Spring:** modern textural color.

## 1.10 References

- Adler, *The Study of Orchestration*.
- Rimsky-Korsakov, *Principles of Orchestration*.
- IMSLP: https://imslp.org/

---

**Summary:** Score dissection uses a systematic framework (identity →
instrumentation → structure → detail). Use IMSLP + music21 to
speed things up; document every analysis in your portfolio. Continue to [Case
Studies (`Ch2-Studi-Kasus.md`)].
