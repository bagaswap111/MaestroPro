---
title: "Blues — Adaptasi Lintas Instrumentasi"
tier: "Bachelor S1"
subject: "Genre Blues"
xml_tags: ["<glissando>", "<slur>", "<pitch>", "<harmony>", "<notehead>", "<stem>"]
software: ["MuseScore", "Dorico", "Sibelius", "Finale"]
---

# Bab 2 — Blues: Adaptasi Lintas Instrumentasi

## 2.1 Prinsip Metode "Fungsi Suara" untuk Blues

Sebelum memindahkan blues ke ansambel baru, petakan empat fungsi inti:

| Fungsi | Peran di blues | Opsi instrumen target |
|--------|----------------|-----------------------|
| **Lead/Melodi** | Kalimat blues + bends | Vokal, sax, trumpet, violin, obo |
| **Comp / Pad** | Harmonisa chord, isolasi 3rd-7th | Piano, guitar strum, string pad |
| **Bass** | Walking/two-feel, prinsip approach | Double bass, e-bass, cello pizz., fagot |
| **Rhythm/Fill** | Shuffle + stabs + fills | Drums, tamburin, djembe, hang |

Aturan emas: **idiom dapat dipindah, register tidak boleh bentrok** — tandai
`lead` paling atas, `comp` tengah, `bass` bawah; rhythm pada peran kepadatan.

## 2.2 Adaptasi 1: Blues Batu 12-Bar → String Quartet

- **Violin 1 (lead):** frase blues di D dorian blues (D–F–G–A–♭B–C–D);
  bends → roll glissando (dari bawah, umum pada fiddling).
- **Violin 2 (rhythm/stabs):** off-beat accent pada 8th (`staccatissimo`),
  *col legno* pada reprise.
- **Viola (comp):** guide tones 3rd/7th, divisi saat pad.
- **Cello (bass):** walking pizzicato; aksen 1 & 3 pada bass line.

```xml
<measure number="1">
  <attributes>
    <time><beats>4</beats><beat-type>4</beat-type></time>
    <key><fifths>0</fifths></key>
  </attributes>
  <!-- Violin 1: kick-off 2 8ths -->
  <note>
    <pitch><step>F</step><octave>5</octave></pitch>
    <duration>2</duration>
    <voice>1</voice>
    <type>eighth</type>
    <notations>
      <slur type="start"/>
    </notations>
  </note>
  <note>
    <pitch><step>D</step><octave>5</octave></pitch>
    <duration>2</duration>
    <voice>1</voice>
    <type>eighth</type>
    <notations>
      <slur type="stop"/>
      <glissando type="start" line-type="wavy"/>
    </notations>
  </note>
  <!-- Cello walking: D - F - A - C -->
  <note>
    <pitch><step>D</step><octave>3</octave></pitch>
    <duration>4</duration>
    <voice>4</voice>
    <type>quarter</type>
  </note>
</measure>
```

**Catatan voicing string:** jazz/string penulis menulis *chord* di bawah
melodi — arpeggio (broken chord) agar tidak tenggelam, bukan <chord> penuh.

## 2.3 Adaptasi 2: Blues → Big Band (Era Jump/Swing)

Big-band blues pakai **form baku dan bagian horn section**:

- Sax section: melodi unison (register 1 oktaf) pada *head*.
- Brass hits: stabs bar 1–4, stop-time di bar 4 (`rest`, semua berhenti).
- *Shout chorus*: seluruh section unison ritme setahun, naik register tiap chorus.

### 2.3.1 Layout MusicXML Big-Band Blues

`part-list` + score-order **trumpets (B♭), trombones, saxes, rhythm.**

```xml
<part-list>
  <score-part id="P1">
    <part-name>Trumpet 1</part-name>
    <score-instrument id="P1-I1">
      <instrument-name>B Trumpet</instrument-name>
    </score-instrument>
    <midi-instrument id="P1-I1">
      <midi-channel>1</midi-channel>
      <midi-program>56</midi-program>
    </midi-instrument>
  </score-part>
  <score-part id="P6">
    <part-name>Rhythm (Piano/Bass/Drums)</part-name>
  </score-part>
</part-list>
```

**Trick seksi:** pada *stop time*, semua brass menulis `rest` 2 ketuk penuh lalu
`stab` — bisa ditulis via `<note><rest/>` + `<harmony>` di part rhythm.

## 2.4 Adaptasi 3: Blues → Solo Piano (Stride/Boogie)

Piano blues = **stride** (bass on 1&3, chord on 2&4) atau **boogie-woogie**
(pola delapan bass line disinkop).

```xml
<!-- Boogie in C: [C] (root+10th) ... -->
<measure number="1">
  <note>
    <pitch><step>C</step><octave>3</octave></pitch>
    <duration>1</duration>
    <type>16th</type>
    <voice>3</voice>
    <staff>2</staff>
  </note>
  <note>
    <pitch><step>E</step><octave>4</octave></pitch>
    <duration>1</duration>
    <type>16th</type>
    <voice>3</voice>
    <staff>2</staff>
  </note>
  <note>
    <pitch><step>G</step><octave>4</octave></pitch>
    <duration>1</duration>
    <type>16th</type>
    <voice>3</voice>
    <staff>2</staff>
  </note>
  <note>
    <pitch><step>C</step><octave>4</octave></pitch>
    <duration>1</duration>
    <type>16th</type>
    <voice>3</voice>
    <staff>2</staff>
  </note>
</measure>
```

## 2.5 Adaptasi 4: Blues → Brass Band (Tanpa Gitar/Bass)

- **Soprano cornet (lead)** — melodi dengan blue bend (via `lip slur`).
- **Tenor horn / baritone (comp)** — guide tones.
- **Euphonium / tuba (bass)** — walking, register konser.
- **Percussion (tambur/snare)** — shuffle pattern dengan rimshot/press.

Pakai **BBb/Eb** yang ditulis transpos: euphonium (B♭) di staf treble (tradisi
brass band Inggris), tuba konser di staf bass.

## 2.6 Checklist Adaptasi

| Cek | Hasil |
|-----|-------|
| 12/16/24-bar form dipertahankan? | |
| Blue notes dibawa (bend/gliss/slur)? | |
| Guide tones 3rd/7th tidak hilang pada comp? | |
| Bass walking/approach menggerakkan harmoni? | |
| Stabs pada off-beat konsisten? | |
| Register tidak bentrok (lead > comp > bass)? | |
| Swing/shuffle ditulis via text + `<sound>` atau triplet? | |

## 2.7 Latihan

1. **Dasar:** Terjemahkan 12-bar C blues ke trio piano (melodi + comp + bass).
2. **Menengah:** Tulis horn stabs untuk 8 sax pada bar 5–8 (off-beat).
3. **Lanjut:** Susun versi 12-bar untuk *woodwind quintet* (flute, obo, clarinet,
   horn, bassoon) + penanda `<sound tempo>` swing.

## 2.8 Repertoar Adaptasi (Referensi Dengar)

- Big band: Duke Ellington *Cottontail* (sax-section shout chorus).
- Stride: Fats Waller, *Ain't Misbehavin'*; Jelly Roll Morton (piano blues).
- String: Mark O'Connor, *Appalachia Waltz* (fiddle blues).
- Brass: Canadian Brass, blues transcriptions.

## 2.9 Referensi Buku & Sumber Web

**Buku:**
- Mark Levine (jazz blues), Kostka & Payne (basics).
- Sy Oliver / arranger swing literature pada *Modern Hip* anthology.
- Ted Nash, *Chavez Ravine* (frontline narrative).

**Web:**
- IMSLP — partitur Ellington-style:
  https://imslp.org/
- Brass band arrangements (open):
  https://www.brassband.co.uk/
- Free percussion-notated blues charts:
  https://www.musescore.org/

---

**Rangkuman:** Adaptasi blues memindahkan empat fungsi suara (lead/comp/bass/
rhythm) dan idiom *bends/stabs/walking* ke ansambel target dengan kepatuhan
register dan notasi. MusicXML mewujudkannya melalui `<glissando>`, `<slur>`,
`<harmony>`, `<notehead>`, dan arrangement part-list yang benar. Kembali ke
[Fondasi Genre (`../1.4-Genre-Fondasi/Ch1-Parameter-Genre.md`)] atau lanjut ke
[Rock & Pop (`../1.6-Genre-Rock-Pop/`)].