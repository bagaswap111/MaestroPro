---
title: "Psychoacoustics & Spectral Theory"
tier: "Doctoral S3"
subject: "Psychoacoustics & Spectral"
xml_tags: ["<note>", "<pitch>", "<alter>", "<microtone>", "<sound>", "<direction>", "<words>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore", "OpenMusic"]
---

# Chapter 1 — Psychoacoustics & Spectral Theory

> **Guide books for this chapter:** Curtis Roads, *Microsound*; Gérard Grisey,
> *Écrits / Les fondements de la musique spectrale*; Fineberg, *Spectral
> Music*; Roeder, *The Theory of Spectra*. Focus: hearing physiology,
> harmonic-series phonemes, and how spectralism changes the way we
> write.

## 1.1 Foundations of Psychoacoustics

*Psychoacoustics* studies how the human auditory system processes
frequency — the rational basis for consonance, dissonance, and timbre
perception.

| Concept | Definition | Key Idea |
|--------|----------|----------------|
| Pitch | Perception of fundamental frequency | Not just f0; virtual pitch |
| Loudness | Perception of amplitude | Equal-loudness contours (Fletcher-Munson) |
| Timbre | Spectra + envelope | ADSR, formant |
| Critical bands | Selective cochlear frequency bands | Basis of roughness |
| Masking | One sound covers another | Frequency & temporal masking |
| Auditory scene | Separation of sources | Psychoacoustic arrangement |

> **Grisey** reads spectral works as *perception analysis*: from
> *inner* to *outer* — arranged above "musique du timbre."

## 1.2 Harmonic Series (Overtone Series)

One fundamental tone produces a series:

| Harmonic | Freq (× fundamental) | Interval from f0 | Cents |
|----------|-----------------------------------|-------------------|-------|
| 1 | 1 | Unison | 0 |
| 2 | 2 | Octave | 1200 |
| 3 | 3 | Perfect 12th | 1902 |
| 4 | 4 | Double octave | 2400 |
| 5 | 5 | Major 17th | 2786 |
| 8 | 8 | Triple octave | 3600 |

> Simple ratios **2:1, 3:2, 5:4** = coincident partials → consonant;
> basis of spectral harmony. **Inharmonicity** (trumpet/timpani) → series not
> exact — appealing to composers.

## 1.3 Musique Spectrale (Grisey, Murail)

Building tones/shapes from **spectral analysis of sound sources** — not functional tonal
progressions but "color."

### 1.3.1 Grisey's Principles (7 pillars)

1. Take one *source* (e.g., trombone) as the seed.
2. FFT analysis → partial map (harmonic + formant).
3. Interpolation between harmonies: *chorus* (fused) → *diffuse* (splayed).
4. Use microtones — spacing not equal to 12-TET.
5. Time scale: era of *temps* (slow, smooth process).
6. *Processus* non-linear — consisting of *seed* → *annihilation*.
7. Mist at the limits: examples from *Partiels*, *Vortex Temporum*.

### 1.3.2 Key Composers

- **Gérard Grisey — Partiels** (1975), *Vortex Temporum*.
- **Tristan Murail — Gondwana**, *Désintégrations*.
- **Kaija Saariaho — L'amour de loin** (applied), *Verblendungen*.

## 1.4 Roughness and Consonance/Dissonance

### 1.4.1 Plomp-Levelt Model

- Dissonance peaks around the *critical band* (≈ 4–7% bandwidth).
- Diatonic consonance = coincident partials → smooth; complexity = dissonance.
- **Consonance is not absolute** — cultural context; but a strong physiological basis.

### 1.4.2 Application: Regulating Partial Spacing

For each pair (f1,f2): if |f2−f1| < critical bandwidth → *roughness*.
Spectral composers regulate partial spacing to be smooth (providing *smoothness*).

```python
# sketch of critical band calculation (Zwicker)
import math
def critical_band(f):
    return 25 + 75 * (1 + 1.4*(f/1000)**2) ** 0.69  # Hz approx

f1, f2 = 200.0, 250.0
print("rough" if abs(f2-f1) < critical_band((f1+f2)/2) else "smooth")
```

### 1.4.3 Musical Analysis

Terraced dynamics & micro-timing in the partial interpolation process:
from piccolo↔tuba — instrumentation transitions as "spectral morph."

## 1.5 Writing Spectral Scores in MusicXML

### 1.5.1 Notating Partials

Write actual pitches; non-12-TET intervals → microtones.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Piano</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>2</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
      <note>
        <pitch><step>C</step><alter>1</alter><octave>3</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
      <note>
        <pitch><step>G</step><octave>3</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> For non-harmonic partials (incomplete spectrum), use micro-intervals
> on each partial (see `Ch2-Mikrotonal-Tuning.md`).

### 1.5.2 Interpolation & Processes

Write time as a process — best via *computed glissandi* and
crescendo/diminuendo with scale marks:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Piano</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <dynamics><pp/></dynamics>
        </direction-type>
        <sound dynamics="20"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> For precise spectral interpolation use OpenMusic/Canvas — MusicXML
> is the final outlet & playback.

## 1.6 Inharmonicity & Formant

- **Timpani / gong** = inharmonic partials.
- **Vocal / instruments** = formants produce consistent "color."
- Experiments behind: classic spectral superimposition + inharmonic.

## 1.7 Contemporary Studies

| Work | Spectral Aspect |
|-------|----------------|
| Grisey, *Partiels* | Interpolation of string harmonies from trombone |
| Murail, *Gondwana* | Spectralization of brass overtones |
| Nuño, *Mitre* | Fine-grid microtonal textures |

## 1.8 Spectral Checklist

| Check | Yes/No |
|---------|----------|
| Is every partial mapped to an actual pitch? | |
| Are microtones notated with the right accidental? | |
| Is interpolation expressed (glissando/dynamics)? | |
| Are instrument ranges considered? | |
| Is roughness deliberately regulated (smooth/frac)? | |

## 1.9 Misconceptions

- **"Spectralism = new impressionism"** — Difference: based on analysis; it builds
  structure from spectra, not just color.
- **"`alter` integers are enough"** — Micro-intervals require non-integers.
- **"MusicXML playback is already spectral"** — Playback is limited; precision demands a
  special environment.

## 1.10 Exercises

1. Analyze 1 source via FFT → map 16 partials → write as a chord in
   MusicXML.
2. Create an 8-bar interpolation of C harmony (fundamental) → B (upper partial).
3. Calculate the roughness of each interval pair in 2 textures.

## 1.11 References

- Roads, *Microsound*.
- Fineberg, *Spectral Music: History and Techniques*.
- Grisey, *Les Fondements de la musique spectrale*.

---

**Summary:** Psychoacoustics explains *why* intervals are consonant/dissonant;
spectralism uses spectral analysis as compositional material. Notation needs
actual pitches + microtones + the `<sound>` parameter. Continue to [Microtonal &
Tuning (`Ch2-Mikrotonal-Tuning.md`)].
