---
title: "Brass Band & March — Adaptasi Lintas Instrumentasi"
tier: "Bachelor S1"
subject: "Genre Brass Band & March"
xml_tags: ["<score-part>", "<score-instrument>", "<midi-instrument>", "<transpose>", "<direction>", "<dynamics>"]
software: ["MuseScore", "Dorico", "Sibelius", "Finale"]
---

# Bab 2 — Brass Band & March: Adaptasi Lintas Instrumentasi

## 2.1 Peta Peran March → Ansambel Lain

March adalah mesin yang sangat "rol" — perannya bisa dipindah ke ansambel mana
pun selama pola *2-beat* dan *countermelody* dipertahankan:

| Peran march | Peran target |
|-------------|--------------|
| Melodi (cornet lead) | Violin 1, flute, sax soprano |
| Countermelody (euphonium) | Cello melodic line (teru), viola |
| Harmoni (cornet 2/3 + tenor horn) | String divisi/choir vintage |
| Bass (tubas) | Cello/bass pizzicato, bass kuda kayu |
| Percussion (snare/bass) | Cajón, tambur, bass drum orkestra |

## 2.2 Adaptasi 1: March → Winter/Full Orchestra

Berdasarkan konvensi *march orchestral transcribed* (contoh: transcription
Sousa untuk symphonic band).

- **Woodwind:** flute (piccolo doubling di strain), oboe (counter), clarinet
  (woodwind colour), bassoon (comic/legato).
- **Brass:** trumpets (melodi, doubling cornet), horns (mid brass/open melody),
  trombones (harmony+gliss pada *bass-clef*), tuba (bass).
- **Percussion:** snare+bass drum trial; cymbal crash pada climax.

### 2.2.1 Layout Score Simfoni untuk March

Urutan part (stand this order): piccolo, flute 1/2, oboe 1/2, english horn,
clarinet 1–3, bass clarinet, bassoon 1/2, contrabassoon, horns 1–4, trumpets
1–3, trombones 1–3, tuba, timpani, percussion, harp, strings (violin 1/2,
viola, cello, bass).

Di MusicXML `part-list` harus mengikuti urutan ini jika ingin *engraving* benar.

### 2.2.2 Melodi disalin dengan doubling oktaf

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name>Piccolo</part-name>
    </score-part>
    <score-part id="P2">
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
      <!-- Flute + Piccolo octave: piccolo on top -->
      <note>
        <pitch><step>F</step><octave>6</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>8th</type>
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
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <!-- Trumpet unison concert offset? in written -->
      <note>
        <pitch><step>F</step><octave>5</octave></pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>8th</type>
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

## 2.3 Adaptasi 2: Brass Band → *German Brass / Symphonic Pops*

- Ubah cornet/flugel → **trumpets + horn section** (die diatur treble 1 oktaf
  lebih rendah untuk kebebasan register).
- Tenor horn baritone → **horn 3/4, tenor trombone.**
- Euphonium tetaplah core — subtitle *solo voice*.
- Tuba dipertahankan; tambahkan *contrabass* bila orkestra.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P3">
      <part-name>Horn in F</part-name>
      <score-instrument id="P3-I1">
        <instrument-name>Horn in F</instrument-name>
      </score-instrument>
      <midi-instrument id="P3-I1">
        <midi-channel>3</midi-channel>
        <midi-program>60</midi-program>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P3">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose>
          <diatonic>-1</diatonic>
          <chromatic>-5</chromatic>
        </transpose>
      </attributes>
      <note>
        <rest/>
        <duration>16</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.4 Adaptasi 3: March → Brass Quartet / Fanfare (Indoor)

Untuk upacara, march direduksi ke kekuatan **4 suara**:
- Trumpet 1 (melodi) + Trumpet 2 / Horn (counter), Trombone (harmoni), Tuba
  (bass) — dengan snare opsional di score ringkas.

Transposisi: trumpets B♭ treble, horn F, TB BC, tuba BB♭ (BC) — semua ditulis
di MusicXML dengan `transpose` yang sesuai per `score-part`.

## 2.5 Checklist Adaptasi March/Brass Band

| Cek | Hasil |
|-----|-------|
| Form strain–trio (subdominant) dipertahankan? | |
| 2-beat feel + pickup masuk di semua part? | |
| Countermelody tidak hilang (dipindah ke euph/viola)? | |
| Transposisi benar per `score-part` (B♭/E♭/F)? | |
| Perkusi ritme (snare/tambur) dinyatakan `<unpitched>`? | |
| Layout part-list sesuai skor target (wind/orkestra)? | |
| Dinamik `p`/`ff` kontras pada Trio dibawa? | |

## 2.6 Latihan

1. **Dasar:** Terjemahkan cornet part (B♭ treble, written) ke trumpet part C.
2. **Menengah:** Tulis *grandioso* 8 bar untuk orkestra (piccolo+trumpet+string
   doubling) pada kunci subdominant.
3. **Lanjut:** Susun brass quartet dari 2-strain march (L1) + tambah cymbal
   crash pada recession — cek dengan MuseScore part extraction.

## 2.7 Repertoar Adaptasi

- Leopold Stokowski / transcription Sousa untuk orchestra.
- King's Trumpeters / fanfare brass quartet.
- *American Patrol* arrangement banyak ansambel.

## 2.8 Referensi Buku & Sumber Web

**Buku:**
- Samuel Adler, *Study of Orchestration* (brass & triple).
- David Whitwell, *Band Music History*.
- Mogens Ellegaard.

**Web:**
- Brass quartets free: https://www.bandmusicpdf.org/
- Sousa Foundation: https://www.sousafoundation.net/
- MuseScore Brass section templates.

---

**Rangkuman:** March/brass band dipindah ke ansambel lain dengan menjaga 2-beat
feel, pickup, countermelody, dan *grandioso*, sambil mengubah transposisi
`score-part` dan layout `part-list`. Kembali ke [Fondasi Genre
(`../1.4-Genre-Fondasi/Ch1-Parameter-Genre.md`)] atau lanjut ke
[Vokal & Choral (`../1.8-Genre-Vokal-Choral/`)].