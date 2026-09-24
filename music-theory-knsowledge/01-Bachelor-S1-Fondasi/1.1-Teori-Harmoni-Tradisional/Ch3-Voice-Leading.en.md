---
title: "Voice Leading"
tier: "Bachelor S1"
subject: "Traditional Harmony Theory"
xml_tags: ["<note>", "<voice>", "<staff>", "<rest>", "<chord>", "<slur>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 3 — Voice Leading

> **Textbook for this chapter:** Aldwell & Schachter, *Harmony and Voice Leading*
> (Chapters 1–5, 15) — the primary treatise on part-writing; Kostka & Payne, *Tonal Harmony*
> (Chapters 5–7). Focus: connecting chords with minimal, smooth,
> and independent voice motion.

## 3.1 Basic Principles of Voice Leading

Four non-negotiable principles (Aldwell & Schachter, Chapter 1):

1. **Minimal motion** — voices move as little as possible; `common tones`
   are preserved.
2. **Voice independence** — no *voice crossing*; each voice must be distinguishable
   to the listener.
3. **Avoid perfect parallels** — *consecutive/parallel fifths* and *octaves*
   destroy independence (the bass becomes too strong).
4. **Resolution of tendency tones** — the leading tone (B) & chordal 7th (F) must
   continue logically (B→C, F→E).

### 3.1.1 Types of Motion Between Voices

| Motion | Two voices | Example (C→G) |
|---------|-----------|--------------|
| *Similar* | same direction, different interval | C4→D4, E4→G4 |
| *Parallel* | same direction & interval | C4→D4, E4→F4 (5→5 = forbidden) |
| *Contrary* | opposite directions | C4→B3, G3→G4 |
| *Oblique* | one stationary, one moving | C4→C4, G3→G4 |

### 3.1.2 Special Rules (Aldwell–Schachter)

- **Fifth→fifth** and **octave→octave** (parallel P5/P8 motion between two
  identical voices) = a violation.
- **Direct fifths/octaves** on the outside (a *similar* voice approaching a
  perfect interval) — special attention in soprano+bass.
- The **chordal 7th** must resolve downward; exception: *retardation* V7→I.
- **Doubling** in inversions may double the 5th/3rd; never double the leading tone.

## 3.2 Spacing and Range

Normal *voice ranges* (SATB):

| Voice | Concert range | Notes |
|-------|--------------|---------|
| Soprano | C4–C6 | Working area C4–A5 |
| Alto | G3–E5 | |
| Tenor | C3–G4 | Falsetto register if it keeps rising |
| Bass | E2–C4 | |

Spacing between adjacent voices:

- Soprano→Alto: ≤ 1 octave (usually tighter).
- Alto→Tenor: ≤ 1 octave.
- Tenor→Bass: free (the foundation of harmony).

> "Avoid a gap in the middle" = do not let the *tenor–bass* span get too wide if the
> soprano–alto span is already wide; the inner voices must be **full**.

### 3.2.1 MusicXML: Spacing via Actual Register

MusicXML has no "spacing" element; spacing is determined by the *actual notes* in
each `<voice>`. Make sure `voice` numbering is consistent across measures so the
software can validate the motion.

## 3.3 Common Errors — Diagnosis Table

| Error | Example | Fix |
|-----------|--------|-----------|
| *Parallel fifths* | C5–G4 → D5–A4 (soprano+alto) | Change direction (contrary) |
| *Parallel octaves* | C4–C3 → D4–D3 (bass doubled) | Remove the doubling |
| *Voice crossing* | Soprano drops below alto | Restore the order |
| *Unresolved leading tone* | B → G (not → C) | Resolve it upward |
| *Unresolved 7th* | F (in V7) → G | The 7th must descend → E |
| *Doubled leading tone* | G: B in soprano & bass | Double G/root instead |
| *Gap in the middle* | Tenor far from alto | Raise the tenor |

### 3.3.1 Warning: "Melodic Leaps"

Large melodic leaps are not necessarily wrong, but leaps > 1 octave should be rare; chromatic leaps
within diatonic harmony are also suspicious (usually modulation).

## 3.4 Four-Voice Part-Writing (SATB)

Method: identify the roles — for each chord, choose the inversion & voicing that
minimizes motion.

### 3.4.1 Aldwell–Schachter Workflow (Mini)

1. Determine the bass line (root/5th, give it direction & cadences).
2. Fill the inner voices following the *soprano* + *bass*.
3. Check: common tone? parallel? tendency tone resolved?
4. Check spacing & register at every change.

### 3.4.2 Example ii–V–I (Dm7–G7–Cmaj7) in SATB C major

- Soprano: F → G → E
- Alto: A → B → C
- Tenor: D → D → G
- Bass: D → G → C

Analysis: common tone D (alto? Tenor D→D); B (leading) → C; F (7th) → E ✓.

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
        <clef number="1"><sign>G</sign><line>2</line></clef>
        <clef number="2"><sign>F</sign><line>4</line></clef>
        <staves>2</staves>
      </attributes>
      <note>
        <pitch><step>F</step><octave>5</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>half</type>
        <staff>1</staff>
      </note>
      <note>
        <pitch><step>A</step><octave>4</octave></pitch>
        <duration>2</duration>
        <voice>2</voice>
        <type>half</type>
        <staff>1</staff>
      </note>
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>2</duration>
        <voice>3</voice>
        <type>half</type>
        <staff>2</staff>
      </note>
      <note>
        <pitch><step>D</step><octave>3</octave></pitch>
        <duration>2</duration>
        <voice>4</voice>
        <type>half</type>
        <staff>2</staff>
      </note>
    </measure>
  </part>
</score-partwise>
```

> **MusicXML key:** notes with the same duration and start time in different `voice`s
> form a vertical chord. For a single-staff single-part score, use
> `<chord/>` after the first note (see
> `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch2-The-Note-Element.md`).

## 3.5 Voice Leading and Chord Inversion

- **First inversion** (6) softens the bass motion; doubling the 3rd in a major
  chord is acceptable (borrowed from vocal-style practice).
- **Second inversion (6/4)** = *passing*, *pedal*, or *cadential* —
  not a stable resting place; always *resolves* to V.

Example of a *cadential 6/4→V→I* (C: G–C–E → G–B–D–F → C–E–G):

```
Soprano:  E → D → C
Alto:     C → B → G
Tenor:    G → G → E
Bass:     C → G → C
```

## 3.6 Voice Leading in Orchestration

In orchestration, a "voice" = an instrument (Adler, *Study of Orchestration*,
Chapters 5–7):

- **Melodic doubling** across instruments is allowed (oboe+violin) — not a
  *parallel octave error* in the SATB sense; it is *doubling* (see
  `../1.3-Orkestrasi-Dasar/Ch3-Tekstur-Doubling.md`).
- **Voice crossing across families** is avoided in the same register.
- **Register + tessitura** determine that the bass line stays below.

### 3.6.1 Continuity in the Timeline

Make sure the score flows: *overlap* between measures (players' inversion kit)
comes from the `<backward>/<forward>` elements — do not change `voice` IDs mid-phrase.

## 3.7 Common Misconceptions

- **"Parallel octaves sound bad = only snob ears"** — Not a matter of "hearing",
  but a *mixture* that weakens independence; avoid it in *strict* writing.
- **"Voice crossing is always wrong"** — It can appear in *ornamental*
  figures, but not continuously.
- **"The octave gap between bass & tenor is completely free"** — It can all be wide
  as long as the inner voices fill in; do not keep it wide in every register.
- **"MusicXML has a voice-leading check tool"** — Not automatically; use
  music21 (`voiceLeading` module) or plugins as *assistants*, and keep
  musical-ear control.

## 3.8 Exercises

1. **Basic:** Write SATB `I–vi–ii–V–I` (C major) with optimal
   common-tone usage.
2. **Intermediate:** Identify 5 of the 7 *errors* from table 3.3 in the provided
   sample score.
3. **Advanced:** Translate to MusicXML (4 `<voice>`), verify in music21
   `voiceLeading`, attach the output.

## 3.9 Listening Repertoire

- Bach, *Chorale* BWV 319 ("Machs mit mir, Gott") — perfect SATB.
- Haydn, *St. Antoni Chorale* — correct orchestral doublings.
- Brahms, *Chorale Preludes* — extraordinary spacing.

## 3.10 Book & Web References

**Books:**
- Aldwell & Schachter, *Harmony and Voice Leading*.
- Kostka & Payne, *Tonal Harmony*.
- Robert Gauldin, *Harmonic Practice in Tonal Music*.

**Web:**
- Music21 voiceLeading docs:
  https://web.mit.edu/music21/doc/moduleReference/moduleVoiceLeading.html
- MuseScore Part-Writing plugin (concept):
  https://musescore.org/

---

**Summary:** Voice leading preserves voice independence & smoothness through
common tones, resolution of tendency tones, and the restriction of perfect parallels.
MusicXML represents each voice via `<voice>`/`<staff>` (stable IDs) and vertical
chords via `<chord/>`. Further material: [Chord Progressions & Modulation
(`Ch2-Progresi-Akor-Modulasi.md`)] and [Counterpoint (`Ch1-Species-Counterpoint.md`)].
