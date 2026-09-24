---
title: "MaestroPro Music Theory Library"
tier: "0-Root"
subject: "Index"
xml_tags: ["score-partwise", "note", "pitch", "harmony", "transpose"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# MaestroPro — Music Theory & MusicXML Library

> **Tagline:** "From Theory to Digital Notation"
>
> This Markdown-based library combines an academic music theory curriculum
> (Bachelor–Doctoral) with the technical implementation of **MusicXML** for arrangers, composers,
> and *digital engravers* using Dorico, Sibelius, Finale, and MuseScore.

## 5-Level Structure

Every theory concept is tied directly to a MusicXML tag/node or a specific
*engraving* rule:

| Level | Name | Form |
|-------|------|------|
| 1 | Tier (Academic Degree) | Main folder |
| 2 | Subject / Core Book | Sub-folder |
| 3 | Chapter | `.md` file |
| 4 | Section (Sub-Chapter) | `##` heading |
| 5 | Sub-Section / XML Node | `###` / `####` heading + MusicXML `<tag>` |

## Curriculum Map

### 🎓 Tier 1 — Bachelor S1 (Foundation)

**Focus:** Traditional rules, instrument ranges, and translating sound into standard notation.

| Subject | Required Books | Chapters |
|---------|-----------|---------|
| `1.1-Teori-Harmoni-Tradisional` | Kostka & Payne; Aldwell & Schachter | Diatonic Harmony; Progressions & Modulation; Voice Leading |
| `1.2-Kontrapung-Bentuk-Musik` | Mann; Goetschius | Species Counterpoint; Fugue; Sonata & Rondo |
| `1.3-Orkestrasi-Dasar` | Adler; Rimsky-Korsakov | Ranges; Transposition; Texture & Doubling; Percussion Notation |
| `1.4-Genre-Fondasi` | 7-dial Genre Parameters | Genre Parameters |
| `1.5-Genre-Blues` | Blues form & scales | Notation Characteristics; Instrumentation Adaptation |
| `1.6-Genre-Rock-Pop` | Rock/pop grid | Notation Characteristics; Instrumentation Adaptation |
| `1.7-Genre-Brassband-March` | Brass band & march | Notation Characteristics; Instrumentation Adaptation |
| `1.8-Genre-Vokal-Choral` | Vocal & choral | Notation Characteristics; Instrumentation Adaptation |

> **Genre Note:** Genre lessons are **embedded** in each tier
> as an L2 subject, not a separate tier — per the curriculum decision.

### 🎓 Tier 2 — Master S2 (Advanced)

**Focus:** Modern harmony, *extended* techniques, media arranging (film/game).

| Subject | Required Books | Chapters |
|---------|-----------|---------|
| `2.1-Harmoni-Jazz-PostTonal` | Levine; Straus; Russell | Chord-Scale; Upper Structures; Post-Tonal Harmony |
| `2.2-Arranging-Komersial-Film` | Garcia; Snow & Meyer | Big Band; String Section; Film Scoring |
| `2.3-Extended-Techniques` | New Music Perspectives; Berio; Ligeti | Woodwind-Brass; Strings; Percussion |
| `2.4-Genre-Jazz-Style` | Jazz style | Notation Characteristics; Instrumentation Adaptation |
| `2.5-Genre-Funk-Soul-RnB` | Funk/soul/R&B | Notation Characteristics; Instrumentation Adaptation |
| `2.6-Genre-Latin` | Latin (salsa, bossa) | Notation Characteristics; Instrumentation Adaptation |
| `2.7-Genre-EDM-Electronic` | EDM & electronic | Notation Characteristics; Instrumentation Adaptation |

### 🎓 Tier 3 — Doctoral S3 (Research)

**Focus:** Acoustics, algorithmic composition, microtonality, and XML schema manipulation.

| Subject | Chapters |
|---------|---------|
| `3.1-Psikoakustik-Spektral` | Spectral Theory; Microtonal & Tuning |
| `3.2-Komposisi-Algoritmik` | Algorithmic Composition Fundamentals; Python MusicXML Scripting |
| `3.3-Sistem-NonBarat-Etno` | Gamelan; Maqam & Raga |

### 🛠️ Tier 4 — MusicXML Masterclass (XML Technical)

**Focus:** Anatomy, *engraving rules*, and playback integration.

| Subject | Chapters |
|---------|---------|
| `4.1-Anatomi-MusicXML` | Root Structure; Note Element; Attributes & Directions; Harmony |
| `4.2-Music-Engraving-Rules` | Fundamentals; Advanced; Expressions |
| `4.3-Playback-MIDI-Integration` | Playback; MIDI Quantization |

### 🗂️ Tier 5 — Workflow & Portfolio (Case Studies & Automation)

| Subject | Chapters |
|---------|---------|
| `5.1-Bedah-Partitur-Bedar` | Score Analysis; Case Studies |
| `5.2-Otomasi-Python-Scripting` | music21 Basics; Practical Scripting |
| `5.3-Version-Control-Git` | Git Basics; Git Music Workflow |

## How to Use

1. **Navigation:** Open the folder matching the Tier → Subject → choose the chapter file.
2. **Frontmatter:** Every chapter has YAML metadata (`title`, `tier`,
   `subject`, `xml_tags`, `software`) for indexing and search purposes.
3. **Code Examples:** All MusicXML examples are in `xml` *code blocks*
   ready to copy and test in Dorico/Sibelius/Finale/MuseScore.
4. **Cross-References:** Follow the links between chapters to connect theory
   concepts with their MusicXML implementation.

## Writing Conventions

```yaml
---
title: "Example Chapter"
tier: "Bachelor S1"
subject: "Basic Orchestration"
xml_tags: ["<transpose>", "<score-instrument>", "<attributes>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---
```

- Primary language: **Indonesian**, with technical terms in English.
- Every theory concept has a **MusicXML Application** section.
- *Engraving* rules refer to *Behind Bars* (Elaine Gould) and the
  W3C MusicXML 4.0 standard.
