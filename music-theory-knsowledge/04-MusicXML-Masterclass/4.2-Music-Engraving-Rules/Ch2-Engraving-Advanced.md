---
title: "Music Engraving — Advanced"
tier: "MusicXML Masterclass"
subject: "Music Engraving Rules"
xml_tags: ["<print>", "<grace>", "<accidental>", "<cautionary>", "<stem>", "<beam>", "<offset>", "<time-modification>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 2 — Engraving: Advanced

> **Buku panduan bab ini:** Gould, *Behind Bars* (Bab: layout, notation
> collisions, grace, tuplets); MusicXML W3C 4.0 — `print`, `grace`,
> `time-modification`. Fokus: membimbing mesin layout untuk hasil akhir yang
> *publishable*.

## 2.1 Collision Avoidance (Menghindari Tabrakan)

Software menghitung otomatis; kita pandu lewat `<print>` & `<offset>`.

### 2.1.1 `<offset>` pada Direction

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
          <dynamics><mf/></dynamics>
        </direction-type>
        <offset>-2</offset>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> `<offset>` dalam divisions; negatif = mundur. Batasi `-1…+2` biasa.

### 2.1.2 `<print>` — Paksa System/Page Break

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
      <print new-system="yes" new-page="yes">
        <system-layout>
          <system-distance>200</system-distance>
          <top-system-distance>250</top-system-distance>
        </system-layout>
      </print>
    </measure>
  </part>
</score-partwise>
```

- `new-system="yes"` — paksakan baris baru.
- `new-page="yes"` — paksakan halaman baru.
- `system-distance` (tenths) — jarak antar system.

## 2.2 Grace Notes (Not Kecil)

Grace: `<grace/>` sebelum pitch; `<slash="yes">` untuk appoggiatura.

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
        <grace/>
        <pitch><step>D</step><octave>4</octave></pitch>
        <voice>1</voice>
        <type>eighth</type>
        <stem>up</stem>
      </note>
      <note>
        <grace slash="yes"/>
        <pitch><step>E</step><octave>4</octave></pitch>
        <voice>1</voice>
        <type>16th</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

- Multiple grace → seri `<note><grace/>...</note>` berturut-turut.
- `make-time` / `steal-time-previous/next` (3.1+) untuk playback.

## 2.3 Courtesy Accidentals

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
        <pitch><step>G</step><alter>1</alter><octave>4</octave></pitch>
        <duration>2</duration>
        <type>quarter</type>
        <accidental cautionary="yes">sharp</accidental>
      </note>
    </measure>
  </part>
</score-partwise>
```

- `cautionary="yes"` — kurung.
- `edited="yes"` — tidak dirender (untuk analisis).

## 2.4 Pengurutan `<notations>` Lengkap

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
        <pitch><step>E</step><octave>5</octave></pitch>
        <duration>1</duration>
        <type>eighth</type>
        <notations>
          <tied type="stop"/>
          <slur type="stop"/>
          <technical>
            <fingering>3</fingering>
          </technical>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Urutan schema: tied, slur, ... articulation/technical.

## 2.5 Tuplets (Time Modification)

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
        <duration>2</duration>
        <type>quarter</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
      </note>
    </measure>
  </part>
</score-partwise>
```

- Rasio `actual/normal`: triplet 3:2; quintuplet 5:4; 7-tuple 7:4.
- `normal-type`/`normal-dot` opsional untuk teks ornament display.

## 2.6 Manajemen Multi-Staff & Voice

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
        <pitch><step>C</step><octave>3</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
        <staff>2</staff>
      </note>
    </measure>
  </part>
</score-partwise>
```

- `<staves>` di attributes mengaktifkan multi-staves part (piano=2).
- `staff` 1=atas 2=bawah; `voice` per garis.

### 2.6.1 Exemplar: Piano Cross-Staff

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
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
        <staff>1</staff>
        <stem>down</stem>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.7 Numbering via `<print>`

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
      <print>
        <measure-layout>
          <measure-numbering>system</measure-numbering>
        </measure-layout>
      </print>
    </measure>
  </part>
</score-partwise>
```

- `measure-numbering`: `system` (dentut per baris), `measure` (tiap measure),
  `none` (sembunyikan).
- `measure number` attribute — `implicit="yes"` untuk pickup.

## 2.8 Checklist Advanced

| Periksa | Ya/Tidak |
|---------|----------|
| Grace `<grace>` benar? | |
| Courtesy accidental `cautionary="yes"`? | |
| Offset/print dipakai utk collision? | |
| Tuplet pakai `time-modification`? | |
| Multi-staff & voice terkelola? | |

## 2.9 Miskonsepsi

- **"`<print new-page>` selalu dibutuhkan"** — Berlebihan mengganggu layout
  responsive; gunakan hanya saat perlu.
- **"Grace membutuhkan duration"** — Dalam XML grace *tanpa* duration; system
  mengelolanya.
- **"Tuplet teks `3:` tak butuh `<time-modification>`"** — Tetap wajib
  `actual/normal` agar parsing durasi benar.

## 2.10 Referensi

- Gould, *Behind Bars*.
- MusicXML W3C 4.0: https://www.w3.org/2021/06/musicxml40/

---

**Rangkuman:** Layout advanced (collision, grace, courtesy accidental, tuplets,
multi-staff, numbering) diarahkan via `<offset>`, `<print>`, `<grace>`,
`time-modification`, `<staff>`/`<voice>`. Lanjut ke [Engraving — Expressions
(`Ch3-Engraving-Expressions.md`)].