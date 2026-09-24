---
title: "Upper Structures & Alterations"
tier: "Master S2"
subject: "Jazz & Post-Tonal Harmony"
xml_tags: ["<harmony>", "<degree>", "<degree-value>", "<degree-alter>", "<degree-type>", "<kind>", "<bass>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 2 — Upper Structures & Alterations

> **Guidebook for this chapter:** Mark Levine, *The Jazz Theory Book* (Chapters 7–9 —
> upper structures, tritone substitution, altered dominant); Frank Mantooth,
> *Voicings for Jazz Keyboard*; Berklee masterclass. Focus: writing the
> "*altered*" color on dominants efficiently in symbols & parts.

## 2.1 Definition of Upper Structure (US)

*Upper Structure* = a triad (or stack) above the **basic section** of a
dominant chord. The idea: instead of writing a full G7(b9#9b13), write G7
stacked with a Db triad (b9–3–b13) in the upper register.

> **Common notation:** `G7(US bII)` = G7 + Db triad → altered sound.

## 2.2 Grouping Upper Structures on Dominants

| US | Triad above | Upper numbers | Color |
|----|---------------|------------|-------|
| US I | G–B–D | 9–11–13 | natural / Mixolydian |
| US bII | Db–F–Ab | b9–3–b13 | altered |
| US III | Eb–G–Bb | #9–5–b7 | altered (b7 on top) |
| US IV | F–A–C | 11–b13–1 | sus/11 |
| US V | D–F#–A | 5–13–1 | Lydian dominant |
| US VI | A–C#–E | 13–b7–9 | peak color |

### 2.2.1 Register Rules

- Place the US triad in the **upper register** (octave); bass stays on the root.
- Keep **bass + guide tones** (3rd & 7th) clearly located — don't
  crowd them in the middle register.

## 2.3 Altered Dominant — Three Equivalent Notations

| Concept | Symbol | Sound (above G) |
|--------|--------|----------------|
| Altered chord symbol | G7alt | G B F + D♭ E♭ A♭ |
| Degree-based | G7(b9#9b13) | per degree |
| Upper Structure | G7(US bII) | Db triad |

All three are *sonically equivalent*. The choice depends on context/engraver.

### 2.3.1 MusicXML: C7#9♭13

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
        <kind text="7#9b13">dominant</kind>
        <degree>
          <degree-value>9</degree-value>
          <degree-alter>1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
        <degree>
          <degree-value>13</degree-value>
          <degree-alter>-1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 2.3.2 Fm11♭5 (half-diminished with 11)

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
        <root><root-step>F</root-step></root>
        <kind text="m11b5">other</kind>
        <degree>
          <degree-value>5</degree-value>
          <degree-alter>-1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
        <degree>
          <degree-value>11</degree-value>
          <degree-alter>0</degree-alter>
          <degree-type>add</degree-type>
        </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Tritone Substitution

*Tritone substitution* = replacing V7 with **bII7** (tritone distance), sharing
guide tones:

| Chord | 3rd | 7th |
|------|-----|-----|
| G7 | B | F |
| D♭7 | F | C♭ (=B) |

Its strength: half-step resolution (C♭→B♮, F→E) toward the tonic.

### 2.4.1 Application: ii–V–I with Substitution

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
        <root><root-step>D</root-step></root>
        <kind text="m7">minor-seventh</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>D♭</root-step></root>
        <kind text="7">dominant</kind>
      </harmony>
      <harmony print-frame="no">
        <root><root-step>C</root-step></root>
        <kind text="maj7">major-seventh</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 2.4.2 Backup: bIII7 / bVI7

Secondary substitutions: `bVI7 → I` (mixture), `bIII7` over the relative —
a common device in film scoring & modern jazz harmony.

## 2.5 Extensions & Polychords

Extensions (9, 11, 13) may be written as polychords (two different roots):
`C7` over `Db` (US bII). MusicXML representation:

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
        <kind text="C7/US bII">dominant</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

> For fret diagrams, use `<frame>` inside `<harmony>` (guitar) or
> `words` (analytical fallback).

## 2.6 Additional Color Harmony

| Technique | Symbol | MusicXML |
|--------|--------|----------|
| Sus4 | Csus | `<kind>suspended-fourth</kind>` |
| Sus2 | Csus2 | `<kind>suspended-second</kind>` |
| Add9 | Cadd9 | `<kind>major</kind>` + `<degree> add 9` |
| 6/9 | C6/9 | `major` + add 9 |
| Borrowed (modal mixture) | iv→I | `bVI`, `iv` via `<bass>`/degree |
| Diminished passing | °7 | `diminished` |

### 2.6.1 Distinction: Sus vs Add

- **SusX:** replaces the 3rd (no major/minor).
- **Add9:** chord +9, the 3rd remains present (Cmaj → Cadd9).
- MusicXML: sus → `<kind>`; add → `kind` + `<degree> add`.

## 2.7 Voicing Compression (Piano)

- **Drop 2/4**, **quartal**, **cluster** — all add space to the
  upper structure.
- Jazz piano: **root + guide tones in the left hand**; **US triad in the right**
  an octave above the bass.
- On one *grand staff*: staff 2 (bass/root), staff 1 (chord with `<chord/>`).

## 2.8 Exercises

1. Write G7alt in 3 versions: G7b9, G7#9b13, G7(US bII).
2. Apply tritone substitution to ii–V–I in F major.
3. Analyze a 10-bar jazz lead sheet — mark every extension/altered.
4. Convert all three chords to MusicXML `<harmony>` + `<degree>`; verify in
   MuseScore.

## 2.9 Checklist

| Check | Yes/No |
|---------|----------|
| US triad in the upper register? | |
| Guide tones (3rd/7th) clear? | |
| Symbol + degree consistent? | |
| Sus vs add differentiated correctly? | |
| Tritone sub accompanied by analysis? | |

## 2.10 Listening Repertoire

- Herbie Hancock, *Maiden Voyage* — sus/upper structure.
- Thelonious Monk, *Round Midnight* — altered/bII.
- Bill Evans, *Blue in Green* — voicing.

## 2.11 References

- Levine, *The Jazz Theory Book*.
- Mantooth, *Voicings for Jazz Keyboard*.
- MusicXML chord: https://www.w3.org/2021/06/musicxml40/

---

**Summary:** US & alterations add color to dominants; MusicXML
`<degree>` (value/alter/type) writes alterations, `<bass>` for slash chords,
`<kind>` for sus/add, and `words`/`frame` for polychords. Continue to
[Post-Tonal Harmony (`Ch3-Harmoni-PostTonal.md`)].
