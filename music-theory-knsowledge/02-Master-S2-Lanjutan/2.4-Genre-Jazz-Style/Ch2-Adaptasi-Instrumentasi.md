---
title: "Jazz Style — Adaptasi Lintas Instrumentasi"
tier: "Master S2"
subject: "Genre Jazz Style"
xml_tags: ["<score-part>", "<midi-instrument>", "<transpose>", "<swing>", "<glissando>", "<harmony>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Jazz Style: Adaptasi Lintas Instrumentasi

## 2.1 Metode: Idiom Jazz ke Ansambel Non-Jazz

Berganti *idiom* tidak berarti *identitas* hilang — hilang apabila
*swing/feel/harmony* di-drop. Pemetaan fungsi:

| Fungsi jazz | Instrumen asli | Target non-jazz |
|-------------|----------------|-----------------|
| Melodi *head* (swing) | Trumpet/Alto | Violin (fiddle-jazz), flute, oboe |
| Comp (voicing) | Piano/guitar | Harp, horn pad, string divisi |
| *Walking bass* | Acoustic bass | Cello pizz., bassoon (register rendah) |
| Drums (ride/swing) | Kit | Cajón ringan, brushes kit |
| Horn section stabs | Sax/Brass | Trumpet classical, woodwind choir |

## 2.2 Adaptasi 1: Lead Sheet Jazz → String Quartet "Jazz Quartet"

Gaya *"string jazz"* (contoh: Turtle Island String Quartet, Kronos (Jazz
program)).

- **Violin 1:** *head* melodi — gunakan *glissando* (bend string), *grace
  note approach*, *vibrato*.
- **Violin 2:** pad/driving 8th (swing) dengan *pizz* accento.
- **Viola:** comp rootless — pluck chord (muted), 3rd+7th.
- **Cello:** walking bass — pizzicato barrel, chromatic approach.

### 2.2.1 Contoh Comp Rootless di String (mm 1, ii–V–I)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>String Quartet</part-name>
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
      <!-- Vln1: pickup downbeat D sung as swing eighth -->
      <note>
        <pitch><step>D</step><octave>6</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>8th</type>
        <notations><glissando type="start"/></notations>
      </note>
      <!-- Cello: walking D -->
      <note>
        <pitch><step>D</step><octave>3</octave></pitch>
        <duration>2</duration>
        <voice>4</voice>
        <type>8th</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.3 Adaptasi 2: Big Band → Symphonic Wind Band

Transkripsi Ellington/Basie untuk wind band (format umum competitive):

- **Sax section** → clarinet choir/baritone sax portabel.
- **Trumpet section** → cornet section + flugel (melodi lunak).
- **Trombones** → tetap 3–4, substitusi dengan euphonium pada melodi.
- **Rhythm** → piano/harp digantikan piano saja; drums kit ke percussion kit.

Aturan: lagu swing → **tetap swing** (jangan *straight*), karena *feel* adalah
identitas.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Piano</part-name>
    </score-part>
    <score-part id="P2">
      <part-name>Flugelhorn</part-name>
    </score-part>
  </part-list>
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose><diatonic>-1</diatonic><chromatic>-2</chromatic></transpose>
      </attributes>
      <score-instrument id="P2-I1">
        <instrument-name>Flugelhorn</instrument-name>
      </score-instrument>
      <midi-instrument id="P2-I1">
        <midi-channel>2</midi-channel>
        <midi-program>57</midi-program>
      </midi-instrument>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Adaptasi 3: Jazz-Funk → Brass Band / Percussion Ensemble

- Bass synt/fretless → **tuba slaptongue** atau bassoon staccato.
- E-piano comp → **horn section** (voicing rootless, divisi).
- *Ride cymbal* words → **tamburin/cowbell** pada ketukan swing.
- Guitar wah → **trumpet wa-wa mute** (`Harmon`).

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
      <direction placement="below">
        <direction-type>
          <words>with Harmon mute — wah</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 2.5 Jazz Vocal → Solo Sax (Instrumental Lead)

Teknik *vocal scat → sax*:
- Tulis kontur melodi, jangan lirik.
- *Bends* → lip gliss; *fall* → falloff.
- Scat 8th → swing vál.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Saxophone</part-name>
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
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>2</duration>
        <type>8th</type>
        <notations>
          <articulations><falloff/></articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.6 Checklist Adaptasi Jazz

| Cek | Hasil |
|-----|-------|
| Swing <sound> tetap (jangan di-straight-kan)? | |
| ii–V–I & substitution tetap (identity)? | |
| Voicing dipindah — rootless/tight? | |
| Walking bass tersambung (approach)? | |
| Head/melodi dalam frase *jazz articulation* (tongue/slur)? | |
| Horn section knife-edge stabs konsisten | |
| `score-part`+`transpose` benar untuk ansambel target | |

## 2.7 Latihan

1. **Dasar:** Tulis 8-bar ii–V–I *lead* untuk flute + string quartet.
2. **Menengah:** Ubah komp piano rootless → horn section (3 horn) 4 bar.
3. **Lanjut:** Susun *So What* (modal) untuk string quartet: vamps modal,
   vln1 head angka; cello bass = dorian line.

## 2.8 Repertoar Adaptasi

- **Turtle Island String Quartet** — standard jazz untuk strings.
- **Gordon Goodwin / Big Phat Band** — big band populer.
- **Brass Brazil** — bossa/funk for brass.

## 2.9 Referensi Buku & Sumber Web

**Buku:**
- Mark Levine (theory + piano book).
- Jerry Bergonzi, *Inside Improvisation* series.
- Ted Pease, *Jazz Composition: Theory and Practice*.

**Web:**
- Jazzadvice — approach/enclosure: https://www.jazzadvice.com/
- Learnjazzstandards: https://www.learnjazzstandards.com/
- Universal Edition — string jazz repertoire.

---

**Rangkuman:** Adaptasi jazz = menjaga swing & harmoni ii–V (identitas) sambil
memindahkan fungsi (lead/head, comp, walking bass, rhythm) ke instrumen target
dengan teknik idiom setara (gliss/wah/mute). Kembali ke [Jazz Karakteristik
(`Ch1-Karakteristik-Notasi.md`)] atau lanjut ke [Funk/Soul/R&B
(`../2.5-Genre-Funk-Soul-RnB/`)].