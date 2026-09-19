---
title: "Big Band Arranging"
tier: "Master S2"
subject: "Arranging Komersial & Film"
xml_tags: ["<part-list>", "<score-part>", "<harmony>", "<transpose>", "<direction>", "<words>", "<articulations>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 1 — Big Band Arranging

> **Buku panduan bab ini:** Russell Garcia, *The Professional Arranger
> Composer* (kitab klasik big-band voicing); Dave Wolpe, *Instrumental
> Jazz Arranging*; Berklee, *Modern Jazz Voicings*. Fokus: organisasi
> section sax/brass/rhythm, cluster voicing, soli, kicks.

## 1.1 Instrumentasi Big Band Standar

| Kelompok | Instrumen | Jumlah umum |
|----------|-----------|-------------|
| Saxophone | Alto 1–2, Tenor 1–2, Baritone | 5 |
| Trumpet | Trumpet 1–3 (+ flugelhorn) | 3–4 |
| Trombone | Trombone 1–3, Bass Trombone | 4 |
| Rhythm | Piano, Bass, Drums (guitar ad lib.) | 3–4 |

> **Notasi:** Alto/Baritone sax transpos E♭; Tenor sax B♭; Trumpet B♭;
> Trombone konser (BC). (Lihat
> `../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`.)

## 1.2 Saxophone Voicing — Sistem 5-Part

### 1.2.1 Teknik Close & Drop 2

| Formasi | Susunan |
|---------|---------|
| *Close position* | semua chord tones dalam oktaf |
| *Drop 2* | urutan-2 dari atas diturunkan oktaf |
| *Semi-close* | campuran jarak |
| *Spread / open* | rentang lebar (untuk bagi register) |

Contoh **Drop 2 pada C7**: chord tones C E G Bb → rapat E G Bb C → turunkan
**G** (urutan-2 dari atas) oktaf → **G3, E4, Bb4, C5**.

Pemilihan tiap sax sesuai *tessitura*:

| Sax | Range nyaman |
|-----|---------------|
| Alto | Bb3–F5 |
| Tenor | Ab2–E5 |
| Baritone | C2–F4 |

### 1.2.2 Penggunaan "Slots" & Cluster

- **Cluster voicing** (Hughes, NEST): setiap alat memainkan nada terdekat
  — puncak menyatu.
- **Soli internal**: 5 sax + bloc; beri masing-masing arah kecil agar
  tidak *skit* satu oktaf.

### 1.2.3 MusicXML: Drop 2 dalam Part Sax (konser pitch)

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
    </measure>
    <measure number="2">
      <note><pitch><step>G</step><octave>3</octave></pitch><duration>4</duration><type>whole</type><voice>1</voice></note>
    </measure>
    <measure number="3">
      <note><pitch><step>E</step><octave>4</octave></pitch><duration>4</duration><type>whole</type><voice>2</voice></note>
    </measure>
    <measure number="4">
      <note><pitch><step>B</step><accidental>flat</accidental><octave>4</octave></pitch><duration>4</duration><type>whole</type><voice>3</voice></note>
    </measure>
    <measure number="5">
      <note><pitch><step>C</step><octave>5</octave></pitch><duration>4</duration><type>whole</type><voice>4</voice></note>
    </measure>
  </part>
</score-partwise>
```

> Tulis *konser pitch* dalam drafting voicing, lalu bagian tiap sax diberikan
> `<transpose>` (E♭/B♭) secara otomatis di software.

## 1.3 Brass Writing

### 1.3.1 Trumpet Section

- Trumpet 1 (lead): melodi, register tinggi.
- Trumpet 2–3: harmonisasi & fill.
- Register: sampai C6 nyaman; **jangan lama** di register atas (fatigue).

### 1.3.2 Trombone Section

- Trombone 1–2: harmoni.
- Bass Trombone: bass.
- **Shout chorus** — seluruh brass (tpt+tbn) serentak → semangat puncak.

### 1.3.3 MusicXML: Shout Chorus Direction

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
          <words xml:space="preserve">Shout Chorus</words>
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```

## 1.4 Rhythm Section

### 1.4.1 Piano Voicings

- **4-way close** (rootless): 3rd–7th–9th–13th.
- Notasi ringkas: harmony symbol + slash rhythm.

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
      <harmony print-frame="no">
        <root><root-step>D</root-step></root>
        <kind text="m9">minor-ninth</kind>
      </harmony>
    </measure>
  </part>
</score-partwise>
```

### 1.4.2 Walking Bass

- Gerak per ketuk 120-ish, *approach tones* (diatonic/chromatic) menuju
  root/target nada berikutnya.
- Ditulis konser (double bass oktaf lebih rendah dari notasi — lihat
  `../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch2-Transposisi-Instrumen.md`).

### 1.4.3 Drums / Kit

- Notasi perkusi (lihat
  `../../01-Bachelor-S1-Fondasi/1.3-Orkestrasi-Dasar/Ch4-Notasi-Percussion.md`).
- Style template (swing, shuffle, latin) di bagan memudahkan pemain.

## 1.5 Soli, Fill, Kicks — Hirarki Puncak

| Teknik | Deskripsi | MusicXML |
|--------|-----------|----------|
| *Soli* | seluruh section satu ritme | letakkan `<accent/>` |
| *Fill* | figur pengisi | normal notes |
| *Kicks* | aksen unison + rhythm | `<articulations><accent/>` |
| *Head arrangement* | melodi awal improvisasi | plain |

### 1.5.1 Notasi Aksen Kicks

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
        <pitch><step>C</step><octave>5</octave></pitch>
        <duration>1</duration>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent/>
          </articulations>
        </notations>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 1.6 Background vs Foreground

- **Background figures** (tutti strings? No—big band background): sax pads
  di bawah soloist.
- **Foreground** (lead sax /trumpet), `a2` divisi.
- Balance dynamic: background `mf` saat soloist `ff` — seimbang.

## 1.7 Template Software

1. Kit: 5 sax + 4 tpt + 4 tbn + rhythm = 13+ part.
2. Set clef & transpose (`transposing instrument` per part).
3. Concert pitch off saat cetak parts.
4. Layout tanpa rest panjang tak perlu (`cue`/`cutaway`).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="sx1"><part-abbreviation>S.1</part-abbreviation></score-part>
    <score-part id="sx2"><part-abbreviation>S.2</part-abbreviation></score-part>
    <score-part id="trp1"><part-abbreviation>Tpt.1</part-abbreviation></score-part>
    <score-part id="tbn1"><part-abbreviation>Tbn.1</part-abbreviation></score-part>
    <score-part id="bs"><part-abbreviation>Bass</part-abbreviation></score-part>
    <score-part id="dr"><part-abbreviation>Drs.</part-abbreviation></score-part>
  </part-list>
  <part id="sx1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
    </measure>
  </part>
</score-partwise>
```

## 1.8 Checklist Arranging

| Periksa | Ya/Tidak |
|---------|----------|
| Voicing sax rapat, dalam range tiap sax? | |
| Trumpet 1 tidak lelah (register)? | |
| Brass tidak bergeser berlebih? | |
| Rhythm section jelas (symbols + rhythm)? | |
| Perubahan feel ditandai di part? | |

## 1.9 Miskonsepsi

- **"Semua sax di register sama"** — Bukan; baritone bass, alto lead.
- **"Soli = semua main melodi sama"** — Soli blok harmoni, hanya lead terbawa
  melodi; lainnya harmonisasi.
- **"Bass ditulis seperti guitar written"** — Walking bass = notasi konser;
  guitar (di chart) written oktaf di atas.

## 1.10 Latihan

1. Tulis **Drop 2** untuk C7 di 4 sax (alto1, alto2, tenor1, tenor2).
2. Buat **shout chorus** 4 bar: melodi trumpet 1 + block harmonis.
3. Susun **walking bass** 8 bar di ii–V–I di F.
4. Bikin **template** big band 13 part MusicXML dengan transpose benar.

## 1.11 Repertoar Dengar

- Duke Ellington, *Take the A Train*.
- Count Basie, *April in Paris* (shout chorus).
- Sammy Nestico, big band charts.

## 1.12 Referensi

- Garcia, *The Professional Arranger Composer*.
- Wolpe, *Instrumental Jazz Arranging*.
- DiNovi/Levine sampling: arrangement resources online:
  https://www.arrangerstab.com/

---

**Rangkuman:** Big band = bahasa section: sax cluster, brass lead/punch,
rhythm fill. MusicXML: multiple `<score-part>` dengan transpose,
`<harmony>` symbols, articulations kick. Lanjut ke [String Section
Techniques (`Ch2-String-Section-Techniques.md`)].