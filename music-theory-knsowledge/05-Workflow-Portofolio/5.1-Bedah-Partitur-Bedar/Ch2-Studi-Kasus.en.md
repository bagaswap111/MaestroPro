---
title: "Score Case Studies"
tier: "Workflow & Portfolio"
subject: "Score Dissection"
xml_tags: ["<part-list>", "<meter>", "<key>", "<direction>", "<sound>"]
software: ["Dorico", "Sibelius", "MuseScore", "IMSLP"]
---

# Chapter 2 — Case Studies

> **Guidebook for this chapter:** Adler, *The Study of Orchestration* (musical
> examples); Boris Blacher/Heinz Becker, *The Technique of Orchestration*
> (cases). Focus: three contrasting works — Beethoven, Gershwin, Zimmer — and
> the practical lessons extracted from them.

## 2.1 Case A: Beethoven — Symphony No. 5, I

### 2.1.1 Data

| Aspect | Info |
|--------|------|
| Instrumentation | 2 fl, 2 ob, 2 cl, 2 bsn; 2 hn, 2 tpt; timpani; strings |
| Key | C minor (fifths -3) |
| Meter | 4/4 (Allegro con brio, ♩=108) |
| Form | Sonata (exposition w/ repeat) |

### 2.1.2 Orchestration Lessons

1. **Homogeneous motif** — the `da-da-da-dum` motif is doubled in **all**
   voices (strings + woodwinds + brass) for signaling power.
2. **Register** — the motif starts in the middle register (cello) and climbs to the
   high register as intensity rises.
3. **Retransition** — a long *general pause* & settling before the
   recapitulation.
4. **Timpani as pedal** — the timpani basses the motif on the tonic, creating an
   unshakable tonal center.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P8"><part-name>Timpani</part-name></score-part>
    <score-part id="P9"><part-name>Violin I</part-name></score-part>
  </part-list>
  <part id="P8">
    <measure number="1">
      <attributes>
        <divisions>1</divisions>
        <key><fifths>-3</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
      <note>
        <rest/>
        <duration>4</duration>
      </note>
    </measure>
  </part>
  <part id="P9">
    <measure number="1">
      <attributes>
        <divisions>1</divisions>
        <key><fifths>-3</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <rest/>
        <duration>4</duration>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.2 Case B: Gershwin — Rhapsody in Blue

### 2.2.1 Data

| Aspect | Info |
|--------|------|
| Instrumentation | Solo clarinet, brass, woodwinds, strings, percussion, piano |
| Key | F major / jazz pentatonic |
| Meter | 4/4 (frequent rubato) |
| Form | Fantasia (sectional theme) |

### 2.2.2 Orchestration Lessons

1. **Clarinet glissando** — the iconic opening requires a *glissando* with
   a leap; written for the transposing B♭ clarinet (concert notation down a M2).
2. **Jazz + Orchestra** — blend a jazz solo melody with the same harmony
   in the strings (unison doubling) → an ethnic blend.
3. **Rubato** — frequent `rit.` before the main motif enters.
4. **Piano as an orchestral instrument** — the piano is not merely an accompanist;
   its role shifts among soloist, filler, and percussion.

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
        <divisions>1</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">rit. molto</words>
        </direction-type>
        <sound tempo="76"/>
      </direction>
      <note>
        <rest/>
        <duration>4</duration>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.3 Case C: Hans Zimmer — Film Score (e.g. *Gladiator*)

### 2.3.1 Data

| Aspect | Info |
|--------|------|
| Media | Épic film |
| Instrumentation | Large brass, choir, rich strings, synth pad |
| Playback | Epic mockup (sample libraries) |
| Tempo map | Click track + hit points |

### 2.3.2 Orchestration Lessons

1. **Large dynamics** — starts soft, with tiered crescendos in the brass.
2. **Doubling beds** — strings + choir in tense registers for emotion.
3. **Click track** — use the `tempo` map for scene synchronization (see
   `../../02-Master-S2-Lanjutan/2.2-Arranging-Komersial-Film/Ch3-Film-Scoring-Notation.md`).
4. **Lo-fi → hi-fi layer** — start thin (pad) → add brass & choir at the
   climax: the Berklee cinematic formula.

## 2.4 Analysis Summary Template

```markdown
# {Work}
- Composer/Era
- Instrumentation & key/time
- Form
- 3 orchestration lessons:
  1. ...
  2. ...
  3. ...
- Mini replication: ...
```

> Save each template as a `.md` file in the `notes/` folder per project.
> Make it an analysis portfolio — evidence of your growth.

## 2.5 Misconceptions

- **"Studying a masterpiece = duplication"** — Copying a palette = learning
  vocabulary, not musical plagiarism.
- **"Analysis is done once"** — Repeat it as your style develops; interpretation
  changes as perspective shifts.
- **"MusicXML isn't needed for dissection"** — For large analyses (100+ bars),
  MusicXML+music21 is far faster and repeatable.

## 2.6 Exercises

1. **Replication** — an 8-bar mini orchestration imitating case A's technique
   (unison motif).
2. **Contrast** — alter one work's doubling map (e.g. remove the bassoon)
   and listen to the difference.
3. **Film mapping** — add a tempo map & hit points to a 60-second scene.
4. **Documentation** — complete the template for all three cases.

## 2.7 Other Case Repertoire

- Debussy — *Prélude à l'après-midi d'un faune* — color superimposition.
- Prokofiev — *Romeo and Juliet* (Montagues & Capulets) — brutal theme.
- John Williams — *Star Wars* — brass + strings leitmotif.

## 2.8 References

- Adler, *The Study of Orchestration* — musical examples.
- Blacher/Becker, *The Technique of Orchestration*.
- Score files: IMSLP (PDF) + MuseScore (MusicXML).

---

**Summary:** Case studies (Beethoven, Gershwin, Zimmer) show orchestration
patterns that can be replicated: motif doubling, idiomatic instrument
glissandi, tiered dynamics, and film tempo maps. Record each of them in your portfolio.
