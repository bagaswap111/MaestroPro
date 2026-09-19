---
title: "Markov Chains & L-Systems"
pillar: "MusicXML Architecture & Computational Music"
level: "Level 4-5"
xml_tags: ["note", "pitch", "duration", "measure"]
related_files: ["Ch1-Dasar-Komposisi-Algoritmik.md", "Ch2-MusicXML-Scripting-Python.md"]
---

# Markov Chains & L-Systems

## 📖 Konsep Teoritis (Level 1-3)

### Markov Chains

Markov Chains adalah model probabilistik untuk sistem yang berpindah antar state secara acak berdasarkan **transition probability**.

```
Contoh: 1st-Order Markov Chain untuk chord
State: C | G | Am | F

Transition Matrix:
         C     G     Am    F
C        0.1   0.4   0.3   0.2
G        0.3   0.1   0.2   0.4
Am       0.4   0.2   0.1   0.3
F        0.2   0.5   0.2   0.1
```

**Tipe Markov:**
- **1st Order**: Next state hanya bergantung pada current state
- **2nd Order**: Next state bergantung pada 2 state sebelumnya
- **n-th Order**: Next state bergantung pada n state sebelumnya

### L-Systems (Lindenmayer Systems)

L-Systems adalah sistem formal untuk model pertumbuhan seluler dan generasi fractal.

```
Axiom: A
Rules:
  A → AB
  B → A

Iteration 0: A
Iteration 1: AB
Iteration 2: ABA
Iteration 3: ABAAB
Iteration 4: ABAABABA
```

**Aplikasi Musik:**
- Generasi melodi dari rules
- Pola ritmik fractal
- Struktur formal rekursif
- Pengembangan tema

## 🎼 Implementasi Praktis (Level 4)

### Markov untuk Komposisi

1. **Analyze Training Data**: Ekstrak transition probabilities
2. **Generate New Music**: Gunakan probabilities
3. **Control Parameters**: Atur randomness
4. **Post-Processing**: Cleanup hasil generate

### L-Systems untuk Musik

1. **Define Alphabet**: Not, chord, interval
2. **Write Rules**: Aturan pertumbuhan
3. **Iterate**: Generate sequences
4. **Map to Music**: Konversi ke notasi

## ⚙️ Level 5: Implementasi MusicXML

### Python Script untuk Markov Chain

```python
import random
import music21

# Transition matrix
transitions = {
    'C':  {'C': 0.1, 'G': 0.4, 'Am': 0.3, 'F': 0.2},
    'G':  {'C': 0.3, 'G': 0.1, 'Am': 0.2, 'F': 0.4},
    'Am': {'C': 0.4, 'G': 0.2, 'Am': 0.1, 'F': 0.3},
    'F':  {'C': 0.2, 'G': 0.5, 'Am': 0.2, 'F': 0.1}
}

def generate_markov(start, length):
    sequence = [start]
    for _ in range(length - 1):
        current = sequence[-1]
        probs = transitions[current]
        next_chord = random.choices(
            list(probs.keys()),
            weights=list(probs.values())
        )[0]
        sequence.append(next_chord)
    return sequence

# Generate 16 bars
chords = generate_markov('C', 16)

# Create MusicXML
score = music21.stream.Score()
part = music21.stream.Part()
for chord_name in chords:
    c = music21.chord.Chord(chord_name)
    c.quarterLength = 4
    part.append(c)
score.append(part)
score.write('musicxml', 'generated_markov.xml')
```

### MusicXML Output Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Generated Music</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key>
          <fifths>0</fifths>
        </key>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>G</sign>
          <line>2</line>
        </clef>
      </attributes>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>16</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

### L-Systems Implementation

```python
# L-System rules for melody
axiom = "C"
rules = {
    'C': 'CEG',
    'E': 'EGA',
    'G': 'GAC',
    'A': 'ACE'
}

def iterate_lsystem(axiom, rules, n):
    result = axiom
    for _ in range(n):
        new_result = ""
        for char in result:
            new_result += rules.get(char, char)
        result = new_result
    return result

# Generate melody
melody = iterate_lsystem(axiom, rules, 3)
# Result: "CEGEGAGACEGAGA"

# Map to MusicXML notes
note_map = {'C': 60, 'E': 64, 'G': 67, 'A': 69}
```

### Aturan Engraving

- **Measure numbers**: Harus sequential
- **Key/Time signatures**: Set di awal
- **Barlines**: Standard untuk generated music
- **Clefs**: Pilih sesuai range
- **Dynamics**: Tambahkan setelah generate

### Edge Cases & Troubleshooting

| Masalah | Solusi |
|:---|:---|
| MusicXML invalid | Validate dengan music21 |
| Transisi unnatural | Perbaiki transition matrix |
| L-System terlalu kompleks | Kurangi iterasi |
| Output tidak musikal | Tambahkan constraints |

## 📚 Referensi

- **Buku**: *Foundations of Musical Computing*
- **Buku**: *Algorithmic Composition* (Peter Nelson)
- **Python Lib**: music21, mingus
