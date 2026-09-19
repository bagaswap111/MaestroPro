---
title: "Playback dalam MusicXML"
tier: "MusicXML Masterclass"
subject: "Playback & MIDI Integration"
xml_tags: ["<playback>", "<midi-instrument>", "<midi-channel>", "<midi-program>", "<sound>", "<direction>", "<miscellaneous>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Playback dalam MusicXML

> **Buku panduan bab ini:** MusicXML W3C 4.0 — *midi-instrument*, *sound*,
> *playback*; Michael Good "music XML is not MIDI"; Fififf, *Sound Production*
> (Tier 03) untuk approach mockup. Fokus: jembatan notasi → suara.

## 1.1 Dari Notasi ke Suara

MusicXML bukan sengaja *playback engine*; ia menyimpan *hint*:

| Elemen | Peran |
|--------|-------|
| `<sound>` | tempo, dynamics, pan pada momen tertentu |
| `<midi-instrument>` | channel, program, volume, pan per part |
| `<midi-unpitched>` | pitch percussive (GM) |
| `<playback>` | mute/solo generik |
| `<instrument-change>` | ganti patch di tengah |

## 1.2 `<midi-instrument>` & `<midi-channel>`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <score-instrument id="P1-I1">
        <instrument-name>Violin</instrument-name>
      </score-instrument>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>40</midi-program>
        <volume>78.7402</volume>
        <pan>0</pan>
        <name>Violins</name>
      </midi-instrument>
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
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

- `<midi-channel>` 1–16 (API lihat 0-15).
- `<midi-program>` GM program (1–128; umum lihat 0-based di beberapa alat).
- `<volume>` 0–100; `<pan>` -90..+90.

### 1.2.1 GM Quick List

| Program | Instrumen |
|---------|-----------|
| 0 | Grand Piano |
| 40 | Violin |
| 41 | Viola |
| 42 | Cello |
| 43 | Contrabass |
| 48 | Strings ens. |
| 56 | Trumpet |
| 60 | French Horn |
| 71 | Clarinet |
| 73 | Flute |
| 8 | Celesta |

## 1.3 `<sound>` — Atribut

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
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
      <direction placement="above">
        <direction-type>
          <dynamics><mp/></dynamics>
        </direction-type>
        <sound tempo="108" dynamics="70" pan="0"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

Atribut umum: `tempo` (BPM), `dynamics` (0-127), `pan`, `elevation`,
`damper-pedal`, `soft-pedal`, `sostenuto-pedal`, `dacapo`, `segno`, `coda`,
`fine`, `pizzicato`, `divisions`.

## 1.4 Per-Part: mute/solo

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
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
      <playback>
        <mute on="yes"/>
      </playback>
    </measure>
  </part>
</score-partwise>
```

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
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
      <playback>
        <solo/>
      </playback>
    </measure>
  </part>
</score-partwise>
```

> Gunakan saat ekspor campuran per bagis (stem) — bukan saat mengedit.

## 1.5 Instrument Change & Key Switches

**<instrument-change>** mengganti patch di tengah part:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Flute</part-name>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>74</midi-program>
      </midi-instrument>
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
        <duration>4</duration>
        <type>whole</type>
      </note>
      <direction placement="above">
        <direction-type>
          <instrument-change>
            <instrument-name>Flute Legato</instrument-name>
          </instrument-change>
        </direction-type>
        <sound midi-program="74"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> **Key switch** (VST) TIDAK distandarkan di MusicXML murni. Banyak library
> (Dorico expression maps, MuseScore custom) menyimpan key switch di luar XML.

## 1.6 Automation CC

| CC | Fungsi |
|----|--------|
| CC1 | mod-wheel → vibrato |
| CC11 | expression → gain |
| CC64 | sustain pedal |

Nilai distandarkan di `miscellaneous-field` bila software menyimpannya:

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
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">mod-wheel CC11 expression</words>
        </direction-type>
        <miscellaneous>
          <miscellaneous-field name="cc11">64</miscellaneous-field>
        </miscellaneous>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> Ini nonstandar; runtime-availability tergantung app.

## 1.7 Timing: `offset` & `duration`

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
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">subito p</words>
        </direction-type>
        <offset>2</offset>
      </direction>
    </measure>
  </part>
</score-partwise>
```

- `offset` dalam divisions — geser momen (untuk subito/con sord. timing).
- `duration` pada `<direction>` panjang (wedge, trill).

## 1.8 Workflow Mockup

1. Parse MusicXML di MuseScore/Dorico (engine built-in).
2. Set expression maps (legato, marcato) per part.
3. Ekspor stem (per part) & mix.
4. Bawa ke DAW untuk ambient/pan/reverb.

## 1.9 Checklist Playback

| Periksa | Ya/Tidak |
|---------|----------|
| Tiap part punya channel+program? | |
| Dynamics `sound dynamics`? | |
| Tempo map lengkap? | |
| Pan/volume balance? | |
| Mute/solo via playback? | |

## 1.10 Miskonsepsi

- **"MusicXML = MIDI"** — Bukan: XML *semantic*, MIDI *performative*;
  keduanya saling melengkapi.
- **"`midi-program` dianggap sebagai patch VST final"** — Hanya referensi GM;
  sound actual dari sampler.
- **"Key switch ada di MusicXML oficial"** — Non-standar; gunakan
  instrument-change + expression maps.

## 1.11 Referensi

- MusicXML W3C 4.0: https://www.w3.org/2021/06/musicxml40/
- MuseScore playback: https://musescore.org/en/handbook/playback

---

**Rangkuman:** Playback dari MusicXML = `<midi-instrument>` (channel/program/
volume/pan) + `<direction><sound>` (tempo/dynamics/pan) + `playback` mute/
solo; CC & key switch lewat ekstensi. Lanjut ke [MIDI Quantization
(`Ch2-MIDI-Quantization.md`)].