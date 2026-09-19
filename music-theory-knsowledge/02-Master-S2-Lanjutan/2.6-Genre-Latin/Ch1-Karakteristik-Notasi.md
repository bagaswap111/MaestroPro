---
title: "Latin Music — Karakteristik & Notasi (Bossa, Salsa, Samba, Tango)"
tier: "Master S2"
subject: "Genre Latin"
xml_tags: ["<harmony>", "<kind>", "<direction>", "<words>", "<unpitched>", "<tremolo>", "<dot>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Latin Music: Karakteristik & Notasi

## 1.1 Klave dan Pola Ritme: Pusat Semua Groove Latin

**Clave** adalah *siklus 2-bar* (3–2 atau 2–3) yang menjadi semacam *nacek*.
Tiga gaya inti:

| Gaya | Clave | Getaran |
|------|-------|---------|
| **Bossa nova** | Clave (bossa) 3–2, swing subtle | Syncopation lembut di bass & gitar |
| **Salsa/mambo** | Son clave 3–2/2–3 | Campana/montuno, *son montuno* |
| **Samba** | *Partido alto / Brazilian* | 2 semiquaver "amadan", surdo |
| **Tango** | — (marcato, *habanera*) | Bass on off-beat, *staccato* violin |

### 1.1.1 Son Clave 3-2 dalam notasi perkusi

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Claves</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>percussion</sign><line>2</line></clef>
      </attributes>
      <!-- 3 side: 1, &a of 2, 4 -->
      <note>
        <unpitched display-step="C" display-octave="5"/>
        <duration>3</duration>
        <type>eighth</type><dot/>
      </note>
      <note>
        <unpitched display-step="C" display-octave="5"/>
        <duration>1</duration>
        <type>16th</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Notasi clave: cowbell / claves, satu staf, `>n` accent. Siklus TIDAK pindah —
> 3–2 vs 2–3 (mulai di bar 1 ketukan).

## 1.2 Bossa Nova: Harmoni Berwarna, Groove Tenang

Karakter: **bass root+5th 8th swing, chord off-beat** (2&4), syncopation
*breathing*, harmoni **jazz** (ii–V), tempo 120–132.

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
        <time><beats>2</beats><beat-type>2</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <pitch><step>A</step><octave>2</octave></pitch>
        <duration>2</duration>
        <type>eighth</type>
      </note>
      <note>
        <pitch><step>D</step><octave>4</octave></pitch>
        <duration>2</duration>
        <type>eighth</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.3 Salsa: Montuno dan Coro

- **Montuno** — pola piano/gitar syncopated 2-bar (*guajeo*): 2 chords
  compression.
- **Coro:** riff vokal pendek menjawab *soneo* (improvisasi vokal).
- **Bass tumbao**: root pada ketukan 1 & *3&* off-beat; dan "2–3 tumbao".
- **Percussion:** congas (tumbao), bongos (martillo), timbales (cowbell),
  shaker.

### 1.3.1 Guajeo Piano (Contoh 2 Bar)

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
        <pitch><step>G</step><octave>3</octave></pitch>
        <duration>1</duration>
        <type>16th</type>
        <voice>1</voice>
        <staff>1</staff>
      </note>
      <note>
        <pitch><step>B</step><octave>3</octave></pitch>
        <duration>1</duration>
        <type>16th</type>
        <voice>1</voice>
        <staff>1</staff>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Samba: Energi Karnaval, Semiquaver Grid

- Base: 2 semiquaver pada setiap off-beat (3rd semiquaver pada ketukan kuat);
  surdo menghenstruksi pattern (tumbado vs teleco).
- Cymbals: *tarol* / repique fills.
- Harmoni: II–V berulang, minor-jazz.

## 1.5 Tango: Dramaturgi dan *Habanera*

- **Habanera** (bass pattern 8th off-beat) — denyut karakteristik.
- **Bandoneón** (substitusi: accordion, samso); string *staccato*; bass
  *walking dramatic*; *arrastre* (glissando) di violins.
- Forma: ABAC / ABA-C; *rubato* intro, *tango* kesan.

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
        <direction-type><words>Tango</words></direction-type>
      </direction>
      <note>
        <pitch><step>E</step><octave>3</octave></pitch>
        <duration>2</duration>
        <type>eighth</type>
        <notations><articulations><staccato/></articulations></notations>
      </note>
      <note>
        <pitch><step>A</step><octave>3</octave></pitch>
        <duration>2</duration>
        <type>eighth</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.6 Miskonsepsi Umum

- **"Latin = 16th saja"** — Bossa sok *swing*, salsa *straight* kuat fall;
  bukan selalu 16th grid.
- **"Clave 3–2 ↔ 2–3 tidak penting"** — Salah! Menentukan *donde* rasa;
  Jangan pindah dari 3-side ke 2-side begitu saja (neu).
- **"Semua Latin = samba"** — Brazil/tango/afro-Cuban beda ritme/harmoni/roll.
- **"Bossa = jazz santai"** — Though jazz-ish, groove *companion* syncopation
  sangat berbeda dari swing.

## 1.7 Latihan

1. **Dasar:** Tulis clave 3–2 (2 bar) dan pola bass tumbao (3–2).
2. **Menengah:** Guajeo piano 8 bar atas harmoni Dm7–G7 (Salsa).
3. **Lanjut:** Susun *tango* 16 bar: habanera bass, bandoneón-emulation,
  staccato strings, *arrastre* glissando di intro.

## 1.8 Repertoar Dengar

- Bossa: Jobim *Wave*, *Corcovado*; João Gilberto.
- Salsa: Tito Puente *Oye Como Va*; El Gran Combo.
- Samba: Antônio Carlos "Aquarela do Brasil";
- Tango: Ástor Piazzolla *Libertango*, *Oblivión*.

## 1.9 Referensi Buku & Sumber Web

**Buku:**
- Roberta L. "Afro-Cuban Music" (Volume 1–2), John Santos.
- *Latin Jazz: The First of the Fusions, 1880s to Today* (John Storm Roberts).
- Aldo Biscardi, *The Art of Latin Arranging*.

**Web:**
- Latin percussion notation (Paiste):
  https://www.clasclave.org/
- IMSLP — Latin jazz scores:
  https://imslp.org/

---

**Rangkuman:** Latin = clave + harmoni jazz (bossa) / straight (salsa) /
Brazilian energy / bandoneón-drama (tango). MusicXML: notasi perkusi
`<unpitched>`, `<direction> (words)`, `<tremolo>` untuk rolls, habanera via
ritme. Lanjut ke [Adaptasi Latin (`Ch2-Adaptasi-Instrumentasi.md`)].