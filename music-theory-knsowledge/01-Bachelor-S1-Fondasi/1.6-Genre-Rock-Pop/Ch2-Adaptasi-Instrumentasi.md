---
title: "Rock & Pop — Adaptasi Lintas Instrumentasi"
tier: "Bachelor S1"
subject: "Genre Rock & Pop"
xml_tags: ["<direction>", "<words>", "<sound>", "<notehead>", "<glissando>", "<harmony>"]
software: ["MuseScore", "Dorico", "Sibelius", "Finale"]
---

# Bab 2 — Rock & Pop: Adaptasi Lintas Instrumentasi

## 2.1 Metode Pemetaan Fungsi Rock → Ansambel Baru

Gelombang suara rock diwakili peran yang bisa dipindahkan apa pun alatnya:

| Fungsi rock | Instrumen asli | Terjemahan ansambel akustik |
|-------------|----------------|-----------------------------|
| Distorted lead | Electric guitar | Violin/fiddle tremolo, sax distorto, flugel |
| Power-chord pad | 2–3 guitar | Contrabass/tenor horns, string divisi |
| Bass (root groove) | E-bass | Tuba/fagot/cello pizzicato |
| Backbeat groove | Drum kit | Cajón, snare band, klap |
| Synth/epic pad | Keys/synth | Satis simak (strings), piano octave |
| Vocal hook | Vokalis | Flute/Obo melody, sax lead |

## 2.2 Adaptasi 1: Lagu Pop → Piano+String Quartet (Acoustic Cover)

Tahun portofolio klasik: mengubah ballad pop jadi arrangement kamar.

- **Piano:** comp block chord di mid; *figured bass* dua-tangan mano kiri.
- **Violin 1:** melodi vokal → registro tinggi, potong istirahat.
- **Violin 2 + viola:** pad drift 3rds/6ths, divisi saat pad.
- **Cello:** bass vokal → walking/two-feel, root+5th.

### 2.2.1 Contoh Notasi Chorus Pop di String

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Violin 1</part-name>
    </score-part>
    <score-part id="P2">
      <part-name>Viola</part-name>
    </score-part>
    <score-part id="P4">
      <part-name>Cello</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <key><fifths>-1</fifths></key> <!-- F mayor -->
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>A</step><octave>5</octave></pitch>
        <duration>4</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest/>
        <duration>12</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
      </note>
    </measure>
  </part>
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>-1</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>C</sign><line>3</line></clef>
      </attributes>
      <note>
        <pitch><step>F</step><octave>4</octave></pitch>
        <duration>8</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <rest/>
        <duration>8</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
  </part>
  <part id="P4">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>-1</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
      <note>
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>8</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <technical><pluck>2</pluck></technical>
        </notations>
      </note>
      <note>
        <rest/>
        <duration>8</duration>
        <voice>4</voice>
        <type>half</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

**Prinsip:** vokal → violin 1 (jangan menutupi dengan string lainnya);
progresi → viola/cello sebagai *pad*; bass → cello pizz. Contoh di atas hanya
fragmen — pada cover penuh, isi komplete per bagian.

## 2.3 Adaptasi 2: Rock Band → Brass Ensemble / Big Band

Sax/trumpet section "menelan" energi rock:

- **Melodi (trumpet section):** frase R&R — 8th, aksen staccatissimo, falls.
- **Power chord:** 3 baris gave (sax section) atau terbuka horn section.
- **Gitar lick:** transkripsi ke sax unison (atau oboe/english horn).
- **Drum set → percussion section:** snare backbeat literal, bass drum pada 1&3.

### 2.3.1 Fall (Leap Down) untuk Trumpet

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Trumpet</part-name>
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
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>8th</type>
        <notations>
          <glissando type="start" number="1" line-type="wavy"/>
        </notations>
      </note>
      <note>
        <rest/>
        <duration>2</duration>
        <voice>1</voice>
        <type>8th</type>
        <notations>
          <glissando type="stop" number="1"/>
        </notations>
      </note>
      <note>
        <rest/>
        <duration>12</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Adaptasi 3: Pop-EDM → Full Orchestral

Teknik *orchestral pop cover* (lagu-lagu aransemen orkes):

1. **Pad → string section divisi**, octave-doubling.
2. **Synth lead → trumpet/sax** dengan 8th drive.
3. **Bass synth → bass trombone/tuba + timpani ganda.**
4. **Drums → percussion battery** (snare, toms, tambirin, crash cymbal).
5. **Chorus drop → tutti + glockenspiel** (octave shimmer).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Glockenspiel</part-name>
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
        <pitch><step>C</step><octave>6</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>8th</type>
        <instrument id="P10-I1"/>
        <notations><articulations><doit/></articulations></notations>
      </note>
      <note>
        <rest/>
        <duration>14</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot/>
        <dot/>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.5 Checklist Adaptasi Pop/Rock

| Cek | Hasil |
|-----|-------|
| Versi melodi (hook) tetap prima — identitas terjaga? | |
| Groove: 2 & 4 backbeat / half-time dinyatakan? | |
| Power-chord (5th) tidak menjadi 3rd yang jelas (kecuali disengaja)? | |
| Register tidak bentrok: bass di bawah, pad mid, lead atas? | |
| *Build/drop* ditulis (crescendo + riser/drum fill)? | |
| Chord symbols benar-benar melengkapi part akustik? | |
| Transisi section jelas (verse/pre-chorus/chorus label)? | |

## 2.6 Latihan

1. **Dasar:** Ubah 4-bar intro gitar rock → brass section (trumpet+sax).
2. **Menengah:** Tulis *acoustic cover* 8-bar: piano/pad + violin lead + cello
   bass, voice-chorus doubling.
3. **Lanjut:** Buat *build* 4-bar (dari verse tipis ke full + riser) untuk
   ensemble kamar dan tandai `<words>BUILD</words>` pada tiap part.

## 2.7 Repertoar Adaptasi (Contoh Cover)

- **Vitamin String Quartet** — cover pop untuk string quartet.
- **2Cellos** — rock themes (Thunderstruck, Smooth Criminal) untuk 2 cellos.
- **London Symphony Orchestra — The Greatest Video Game Music**.
- **Bad Plus** — cover jazz trio.

## 2.8 Referensi Buku & Sumber Web

**Buku:**
- Rikky Rooksby, *How to Write Songs on Guitar*.
- Don Muro, *The Art of Sequencing* (MIDI pop arranging).
- Jörg Widmann (umur), tidak wajib.

**Web:**
- Vitamin String Quartet (referensi cover):
  https://www.vitaminstringquartet.com/
- Hooktheory — progresi pop: https://www.hooktheory.com/
- MuseScore — contoh partitur band:
  https://musescore.org/

---

**Rangkuman:** Adaptasi rock/pop = memindahkan peran (lead/power-chord/bass/
backbeat/pad) ke intrumen target sambil menjaga hook, *build*, dan identitas
groove. MusicXML memperjelas dengan `<notehead>`, `<glissando>`, `<direction>
(words/dynamic)`, dan susunan `part-list`. Kembali ke [Fondasi Genre
(`../1.4-Genre-Fondasi/Ch1-Parameter-Genre.md`)] atau lanjut ke
[Brass Band & March (`../1.7-Genre-Brassband-March/`)].