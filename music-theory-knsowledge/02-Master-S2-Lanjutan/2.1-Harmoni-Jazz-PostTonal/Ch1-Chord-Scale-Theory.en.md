---
title: "Chord-Scale Theory"
tier: "Master S2"
subject: "Jazz & Post-Tonal Harmony"
xml_tags: ["<harmony>", "<root>", "<kind>", "<degree>", "<root-alter>", "<degree-alter>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Chord-Scale Theory

> **Guidebook for this chapter:** Mark Levine, *The Jazz Theory Book* (Chapters 1–7);
> George Russell, *The Lydian Chromatic Concept of Tonal Organization*
> (LCC); reference aid *The Berklee Book of Jazz Harmony*. Focus: connecting
> each chord with its scale/mode as material for improvisation and harmony.

## 1.1 The Chord-Scale Concept

*Chord-scale theory* connects every chord with the scale/mode above it —
for phrase improvisation and vertical composition. A chord is not merely a
collection of notes; it "activates" a scale that contains a safe sonority
for it.

| Chord | Scale | Intervals |
|------|-------|----------|
| Cmaj7 | Ionian (C major) | 1 2 3 4 5 6 7 |
| Dm7 | Dorian | 1 2 b3 4 5 6 b7 |
| G7 | Mixolydian | 1 2 3 4 5 6 b7 |
| Fmaj7 | Lydian | 1 2 3 #4 5 6 7 |
| Am7 | Aeolian | 1 2 b3 4 5 b6 b7 |
| Bø7 | Locrian | 1 b2 b3 4 b5 b6 b7 |
| C7alt | Super Locrian | 1 b2 #2 3 b5 b6 b7 |

### 1.1.1 The Seven Modes as Colors

| Mode | Character | Triad/7th and above |
|------|----------|--------------------|
| Ionian | neutral, basic | maj7 |
| Dorian | minor + natural 6 (flexible) | m7 |
| Phrygian | minor + b2 | m7 |
| Lydian | maj7 + #4 (dreamy) | maj7 |
| Mixolydian | dom7 + b7 (blues) | 7 |
| Aeolian | natural minor | m7 |
| Locrian | m7b5 / half-dim | ø7 |

## 1.2 Applying It in Improvisation

1. min7 → Dorian (or Aeolian when a darker color is wanted).
2. dom7 → Mixolydian; *alterations* (b9/#9/b13) fit when approaching an
   altered chord.
3. maj7 → Ionian or Lydian (Lydian ♮4 commonly used to avoid #4).
4. ø7 → Locrian (or Locrian #2 when using the melodic minor scale).
5. Change the scale **when the chord changes** (usually at the barline).

### 1.2.1 Guide Tones — 3rd & 7th

- The 3rd determines major/minor.
- The 7th determines function (dom vs maj).
- All jazz solos build **voice leading through guide tones**.

## 1.3 Application: ii–V–I in F

| Chord | Scale | Notes |
|------|-------|------|
| Gm7 | G Dorian | G A Bb C D E F |
| C7 | C Mixolydian | C D E F G A Bb |
| Fmaj7 | F Lydian | F G A B C D E |

Example of a 2-bar solo line:

```
Gm7:  G – A – Bb – C      (stepwise, dorian)
C7:   D – F – E            (guide 7-3 + passing)
Fmaj7: C – E – F           (approach to F)
```

## 1.4 Avoid Notes & Chord-Scale

- **Avoid note** = a note that *collides* with the foundation (e.g. the 4th on
  Ionian/maj7 when not given a pattern).
- On *Maj7*: the 4th is often "avoid" (off-kilter), replaced by the 3rd or #4 (Lydian).
- On *dom7*: the avoid limit depends on context (Mixolydian#11 is OK when
  outlined).
- LCC concept (Russell): **Lydian** above a major chord is the "brightest"
  scale; "Chord = scale of radiating color" — the scale is determined by the *chord*.

## 1.5 Upper Structures as a Consequence of Chord-Scale

| US | Triad above | Upper numbers | Effect |
|----|---------------|------------|------|
| US bII | Db–F–Ab | b9–3–b13 | altered |
| US III | Eb–G–Bb | #9–5–b7 | altered |
| US V | D–F#–A | 9–5–13 | Lydian dominant |
| US VI | A–C#–E | 13–b7–9 | peak color |

### 1.5.1 MusicXML: Altered Dominant with `<degree>`

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
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="7b9#9">dominant</kind>
        <degree>
          <degree-value>9</degree-value>
          <degree-alter>-1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
        <degree>
          <degree-value>9</degree-value>
          <degree-alter>1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

> `degree-value`=9, `degree-alter` -1 = flat, 1 = sharp, `degree-type` `alter`.

## 1.6 Lydian Chromatic Concept (Russell)

- Four "generating scales" from root C (brightest to darkest):
  Lydian > Ionian > Mixolydian > ... > Locrian.
- Lydian as the "super-palace"; the true major chord = sub-Lydian chord.
- Practical: for maj7 use **Lydian** (#4 avoids b9 clash); on
  dom7 use **Lydian dominant** (maj3, #4, b7).

## 1.7 Unifying It in Composition

1. Write a progression (ii–V–I, turnarounds, modal).
2. Determine the scale & guide tones for each chord.
3. Create a melody from diatonic steps + guide-tone approach.
4. Enrich the harmony with upper structures so altered colors are implied
   without calculating every note in the accompaniment.

## 1.8 Case Studies

- **Levine** — chapters 1–7 (chord-scale, ii–V–I, rhythm changes).
- **Russell LCC** — "recharges" the modal approach.
- **Herbie Hancock "Maiden Voyage"** — modal: D dorian, C dorian, F mix.
- **John Coltrane "Giant Steps"** — distant key changes (CDM
  application).

## 1.9 Chord-Scale Writing Checklist

| Check | Yes/No |
|---------|----------|
| Does every chord have an implied scale? | |
| Are guide tones clear in the main register? | |
| Upper structure/alteration via `<degree>`? | |
| Do the modes match the requested color? | |
| Are avoid notes avoided / handled? | |

## 1.10 Exercises

1. **Basic:** Write the Dorian, Mixolydian, Lydian scales from root G.
2. **Intermediate:** Improvise an 8-bar ii–V–I in Bb; settle in the guide-tone
   approach.
3. **Advanced:** Analyze "Giant Steps" — chord-scale for each bar; create a
   MusicXML lead sheet with `<harmony>`.

## 1.11 Listening Repertoire

- Miles Davis, *So What* — modal dorian.
- John Coltrane, *Giant Steps / Naima* — chord progressions.
- Herbie Hancock, *Maiden Voyage*.
- Bill Evans trio — chord-scale voicings.

## 1.12 Book References & Web Sources

**Books:**
- Levine, *The Jazz Theory Book*.
- Russell, *Lydian Chromatic Concept of Tonal Organization*.
- *The Berklee Book of Jazz Harmony*.

**Web:**
- iReal Pro chord list: https://irealpro.com/
- *Jazz Theory* resource: https://tobiasone.gr/ jazz library
- MusicXML chord docs: https://www.w3.org/2021/06/musicxml40/

---

**Summary:** Chord-scale theory connects chords & scale-modes as the
basis of color/improvisation; Levine + Russell offer two lenses: function and
modal-color. MusicXML stores chord classes in `<harmony>`, alterations/upper
structures in `<degree>`. Continue to [Upper Structures & Alterations
(`Ch2-Upper-Structures-Alterations.md`)].
