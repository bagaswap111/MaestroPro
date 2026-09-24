---
title: "Jazz Style — Characteristics & Notation"
tier: "Master S2"
subject: "Jazz Style Genre"
xml_tags: ["<harmony>", "<kind>", "<degree>", "<slur>", "<glissando>", "<tie>", "<swing>", "<sound>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Chapter 1 — Jazz Style: Characteristics & Notation

## 1.1 Jazz as a Language (Eras & Subgenres)

Jazz is a language with different historical accents. For the arranger,
parameters (tempo/groove/harmony/form) change from one era to the next:

| Era/Style | Tempo/Feel | Harmony | Typical instruments |
|----------|-----------|---------|----------------|
| New Orleans (Dixie) | 2/2, *two-beat* | Tonic–dominant | Cornet, clarinet, trombone, banjo, tuba |
| Swing (Big Band) | 4/4, *four-to-the-bar swing* | ii–V–I, blues | Full big band (5 sax, 4–5 tpt, 4 tbn, rhythm) |
| Bebop | 4/4 uptempo, *rubato intro* | Chord extensions + alterations | Small group (sax/trp + rhythm) |
| Cool | Gentle, *West Coast* | Same, more relaxed | French horn, flute added |
| Hard Bop / Soul | Mid-tempo, groovy | Blues + gospel | Tenor, organ |
| Modal | *One-chord vamp* | Scales (Dorian, etc.) | Post-bop group |
| Free / Avant | Free tempo | Pan-tonal | Extended woodwind techniques |
| Fusion | Electric, 16ths | *Vamp*, riff | E-piano, synth, wah-guitar, fretless bass |

**Levine, *The Jazz Theory Book*, chapters 1–4:** ii–V–I basics, 7th chords, jazz
scales; chapters 9–11 blues; chapter 19 (alternate), chapters 21–22 (modal & slash chords).

## 1.2 Swing: Notation & Playback

Swing = **asymmetric 8ths** (long-short). Rule of thumb:

- *Swing 8ths* are written as equal (straight) 8ths but *played* 2:1 —
  don't write actual triplets in the score (it confuses real-world reading).
- Software: MuseScore `Swing playback` (54–66%), Dorico `Swing` directive,
  Sibelius `Playback → Swing`.

In MusicXML 3.1+, swing is written with `<sound swing>`:

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
          <words>Swing</words>
        </direction-type>
        <sound tempo="144" swing="eighth" first="third" second="third"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

If **exact notation** is needed (for exams/engraving), write triplet 8ths
(3+3 per beat).

## 1.3 Jazz Harmony: Essential Vocabulary

Vocabulary (Levine's table): **7th chords** on every degree; extensions
9/11/13; alterations (b9, #9, #11, b13); *lead-sheet symbols*.

### 1.3.1 Class, Kind, and Degree in MusicXML

| Symbol | `<kind>` | Degree |
|--------|----------|--------|
| Cmaj7 | major-seventh | — |
| C7 | dominant | — |
| Cm7 | minor-seventh | — |
| C7alt | dominant + degree b9/#9/b13 | `<degree>` |
| Cmaj7#11 | major-seventh + add #11 | `<degree><alter>1</alter>` |

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
      <harmony>
        <root><root-step>C</root-step></root>
        <kind text="7b9#9">dominant</kind>
        <degree>
          <degree-value>9</degree-value><degree-alter>-1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
        <degree>
          <degree-value>9</degree-value><degree-alter>1</degree-alter>
          <degree-type>alter</degree-type>
        </degree>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

See details: `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch4-Harmony-Chord-Symbols.md`.

### 1.3.2 ii–V–I and *Turnaround*

The soul progression of jazz: **ii–V–I** (Dm7–G7–Cmaj7) and *turnaround*
(I–vi–ii–V: Cmaj7–Am7–Dm7–G7). Essential substitutions:

- **Tritone sub:** G7 → D♭7 (bass down a semitone, same 3rd/7th).
- **Backdoor:** ♭VII7 (F#7 resolving to C — a jazz character).
- **Diminished passing:** between chords moving up/down.

## 1.4 Voicing: Drop 2, Rootless (Three-Note), and Upper Structures

- **Drop-2:** 4-note voicing — the 2nd voice from the top is dropped 1 octave;
  extremely common for key comping.
- **Rootless (Bud Powell voicing):** 3rd+7th (9th) without the root — for solo
  piano comping: C7 → E–B♭–D–G (3rd, 7th, 9th, 5th).
- **Upper structures:** 2 or 3 notes from the upper triad (see chapter
  `Ch2-Upper-Structures-Alterations.md`).

### 1.4.1 Basic: Rootless Piano Voicing in MusicXML

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
        <pitch><step>E</step><octave>4</octave></pitch>
        <duration>4</duration>
        <voice>3</voice>
        <staff>2</staff>
        <type>quarter</type>
      </note>
      <note>
        <pitch><step>Bb</step><octave>4</octave></pitch>
        <duration>4</duration>
        <voice>3</voice>
        <staff>2</staff>
        <type>quarter</type>
        <chord/>
      </note>
      <note>
        <pitch><step>D</step><octave>5</octave></pitch>
        <duration>4</duration>
        <voice>3</voice>
        <staff>2</staff>
        <type>quarter</type>
        <chord/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.5 Jazz Melody: Bebop Scale, Approach, and Enclosure

- **Bebop scale:** adds a *color* note (b7→7 in major bebop, b3→3 in minor bebop)
  so the 8-note scale aligns with the beat.
- **Approach tones:** chromatic 1/2 step before a chord tone (walking).
- **Enclosure:** approach from above+below the target (C → B–B♭/A–C).

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
        <pitch><step>B</step><octave>4</octave></pitch>
        <duration>1</duration>
        <type>16th</type>
        <notations><slur type="stop"/></notations>
      </note>
      <note>
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>3</duration>
        <type>8th</type>
        <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.6 Big Band Scoring: Layout & Parts

Standard 5-sax / 4-trumpet / 4-trombone / rhythm layout:

| Part | Range (written) | Transposition |
|------|-----------------|----------|
| Alto Sax 1/2 | G3–E6 | E♭ |
| Tenor Sax 1/2 | G2–E5 | B♭ |
| Bari Sax | A1–G4 | E♭ |
| Trumpet 1–3 | F3–C6 | B♭ |
| Lead Trumpet | (around C6 lead) | B♭ |
| Trombone 1–3 | E2–B♭4 | C (BC) |
| Bass Trombone | G1–F4 | C (BC) |
| Rhythm | — | concert |

**Sax doubling:** 1st requires flute/clarinet — write it in the same part with a
clef switch (flute treble 8, B♭ clarinet).

## 1.7 Common Misconceptions

- **"Swing = triplets"** — Writing actual triplet notes is valid if you want *exact*;
  scores usually write straight + "Swing" + `<sound swing>`.
- **"All chords use extensions"** — Add extensions only when useful;
  rootless for comping, symbols for lead sheets.
- **"Only ii–V–I"** — Modal & free jazz have different languages; blues uses
  static dominant harmony.
- **"Ascending voicing = power slide"** — Large drop-2, clusters, etc. are
  *colors*, not always *chord tones*.

## 1.8 Exercises

1. **Basic:** Write ii–V–I (Dm7–G7–Cmaj7) as a lead sheet in MusicXML.
2. **Intermediate:** Rootless C7 piano voicing (3rd 7th 9th 5th) across 2 octaves.
3. **Advanced:** Arrange an 8-bar *head* of a B-flat blues for sax section, swing text,
   + turnaround ii–V–I with a *tritone sub*.

## 1.9 Listening Repertoire

- Swing: Duke Ellington, *It Don't Mean a Thing*; Count Basie, *April in Paris*.
- Bebop: Charlie Parker, *Ornithology*; Bud Powell.
- Cool: Miles Davis, *Birth of the Cool*.
- Modal: Miles, *So What*; John Coltrane, *Impressions*.
- Fusion: Weather Report, *Birdland*.

## 1.10 Book References & Web Sources

**Books:**
- Mark Levine, *The Jazz Theory Book* (Sher Music).
- Mark Levine, *The Jazz Piano Book*.
- Jerry Coker, *Elements of the Jazz Language*.
- Russ Garcia, *The Arranger's Guide* (Big Band).

**Web:**
- Jazzadvice: https://www.jazzadvice.com/
- ii-V7-I practice (Jazz Studies):
  https://www.learnjazzstandards.com/
- IMSLP — public-domain jazz transcriptions:
  https://imslp.org/

---

**Summary:** Jazz = swing feel + ii–V–I + extensions/alterations + bebop
melodic steps. MusicXML: `<kind>`/`<degree>` for chords, `<sound swing>` for
feel, `<slur>`/`<glissando>` for phrasing. Continue to [Cross-Instrumentation
Jazz Adaptation (`Ch2-Adaptasi-Instrumentasi.md`)].
