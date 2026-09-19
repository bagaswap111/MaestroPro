---
title: "Psikoakustik & Teori Spektral"
tier: "Doctoral S3"
subject: "Psikoakustik & Spektral"
xml_tags: ["<note>", "<pitch>", "<alter>", "<microtone>", "<sound>", "<direction>", "<words>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore", "OpenMusic"]
---

# Bab 1 — Psikoakustik & Teori Spektral

> **Buku panduan bab ini:** Curtis Roads, *Microsound*; Gérard Grisey,
> *Écrits / Les fondements de la musique spectrale*; Fineberg, *Spectral
> Music*; Roeder, *The Theory of Spectra*. Fokus: fisiologi pendengaran,
> fonem deret harmonik, dan bagaimana spektralisme mengubah cara kita
> menulis.

## 1.1 Dasar Psikoakustik

*Psikoakustik* mempelajari bagaimana sistem pendengaran manusia memproses
frekuensi — dasar rasional untuk konsonansi, disonansi, dan persepsi timbre.

| Konsep | Definisi | Gagasan Kunci |
|--------|----------|----------------|
| Pitch | Persepsi frekuensi fundamental | Bukan hanya f0; virtual pitch |
| Loudness | Persepsi amplitudo | Kurva equal-loudness (Fletcher-Munson) |
| Timbre | Spektra + envelope | ADSR, formant |
| Critical bands | Pita frekuensi selektif koklea | Basis roughness |
| Masking | Satu suara menutupi yang lain | Frequency & temporal masking |
| Auditory scene | Pemisahan sumber | Susunan psikoakustik |

> **Grisey** membaca karya spektral sebagai *analisis persepsi*: dari
> *inner* ke *outer* — tersusun atas "musique du timbre."

## 1.2 Deret Harmonik (Overtone Series)

Satu nada dasar menghasilkan deret:

| Harmonik | Frek (x dasar) | Interval dari f0 | Cents |
|----------|----------------|-------------------|-------|
| 1 | 1 | Unison | 0 |
| 2 | 2 | Octave | 1200 |
| 3 | 3 | Perfect 12th | 1902 |
| 4 | 4 | Double octave | 2400 |
| 5 | 5 | Major 17th | 2786 |
| 8 | 8 | Triple octave | 3600 |

> Rasio sederhana **2:1, 3:2, 5:4** = partial coincident → konsonan;
> dasar harmoni spektral. **Inharmonicity** (terompet/ timpani) → deret tak
> tepat — menarik bagi komponis.

## 1.3 Musique Spectrale (Grisey, Murail)

Membangun nada/bentuk dari **analisis spektra sumber suara** — bukan progresi
tonal fungsional melainkan "warna."

### 1.3.1 Prinsip Grisey (7 pilar)

1. Ambil satu *sumber* (mis. trombone) sebagai seed.
2. FFT analyse → peta partial (harmonic + formant).
3. Interpolasi antar harmoni: *chorus* (fused) → *diffuse* (splayed).
4. Gunakan microtones — spacing tak sama dengan 12-ET.
5. Skala waktu: zaman *temps* (slow, smooth process).
6. *Processus* tak linear — consisting of *seed* → *annihilation*.
7. Mist pada batas: contoh dari *Partiels*, *Vortex Temporum*.

### 1.3.2 Komposer Kunci

- **Gérard Grisey — Partiels** (1975), *Vortex Temporum*.
- **Tristan Murail — Gondwana**, *Désintégrations*.
- **Kaija Saariaho — L'amour de loin** (terapan), *Verblendungen*.

## 1.4 Roughness dan Konsonansi/Disonansi

### 1.4.1 Model Plomp-Levelt

- Disonansi puncak di sekitar *critical band* (≈ 4–7% bandwidth).
- Diatonic consonance = partial coincident → smooth; complexity = dissonance.
- **Konsonansi bukan mutlak** — konteks kultural; tapi dasar fisiologis kuat.

### 1.4.2 Aplikasi: Mengatur Jarak Partial

Untuk tiap pasangan (f1,f2): jika |f2−f1| < critical bandwidth → *roughness*.
Komponis spektral mengatur jarak partial agar halus (memberi *smoothness*).

```python
# sketsa penghitungan critical band (Zwicker)
import math
def critical_band(f):
    return 25 + 75 * (1 + 1.4*(f/1000)**2) ** 0.69  # Hz approx

f1, f2 = 200.0, 250.0
print("rough" if abs(f2-f1) < critical_band((f1+f2)/2) else "smooth")
```

### 1.4.3 Analisis Musical

Terraced dynamic & mikro-timing dalam proses interpolasi partial:
dari piccolo↔tuba — transisi instrumentasi sebagai "spectral morph".

## 1.5 Menulis Partitur Spektral di MusicXML

### 1.5.1 Notasi Partial

Tulis pitch nyata; interval non-12-TET → microtone.

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
        <pitch><step>C</step><octave>2</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
      <note>
        <pitch><step>C</step><alter>1</alter><octave>3</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
      <note>
        <pitch><step>G</step><octave>3</octave></pitch>
        <duration>4</duration><type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
```

> Untuk partial non-harmonik (spektral tak penuh), gunakan mikro interval
> pada tiap partial (lihat `Ch2-Mikrotonal-Tuning.md`).

### 1.5.2 Interpolasi & Proses

Tulis waktu sebagai proses — paling baik via *glissandi terhitung* dan
crescendo/diminuendo dengan tanda skala:

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
          <dynamics><pp/></dynamics>
        </direction-type>
        <sound dynamics="20"/>
      </direction>
    </measure>
  </part>
</score-partwise>
```

> Untuk interpolasi spektral presisi gunakan OpenMusic/Canvas — MusicXML
> adalah outlet final & playback.

## 1.6 Inharmonicity & Formant

- **Timpani / gong** = inharmonic partial.
- **Vokal / instrument** = formants menghasilkan "warna" yang konsisten.
- Eksperimen di belakang: superimposisi spektral klasik + inharmonic.

## 1.7 Studi Kontemporer

| Karya | Aspek Spektral |
|-------|----------------|
| Grisey, *Partiels* | Interpolasi harmoni string dari trombone |
| Murail, *Gondwana* | Spektralisasi dari overtone brass |
| Nuño, *Mitre* | Fine-grid microtonal textures |

## 1.8 Checklist Spektral

| Periksa | Ya/Tidak |
|---------|----------|
| Setiap partial dipetakan ke pitch aktual? | |
| Microtones dicatat dengan accidental tepat? | |
| Interpolasi dinyatakan (glissando/dynamics)? | |
| Rentang instrumen diperhatikan? | |
| Roughness diatur disengaja (smooth/frac) ? | |

## 1.9 Miskonsepsi

- **"Spektralisme = impresionisme baru"** — Lain: berbasis analisis; Gensaka
  struktur dari spektra, bukan sekedar warna.
- **"`alter` integer cukup"** — Untuk mikro interval wajib non-integer.
- **"Playback MusicXML sudah spektral"** — Playback terbatas; presisi menuntut
  environment khusus.

## 1.10 Latihan

1. Analisis 1 sumber via FFT → peta 16 partial → tulis sebagai chord di
   MusicXML.
2. Buat 8-bar interpolasi harmoni C (fundamental) → B (upper partial).
3. Hitung roughness tiap pasangan interval dalam 2 tekstur.

## 1.11 Referensi

- Roads, *Microsound*.
- Fineberg, *Spectral Music: History and Techniques*.
- Grisey, *Les Fondements de la musique spectrale*.

---

**Rangkuman:** Psikoakustik menjelaskan *mengapa* interval konsonan/disonan;
spektralisme memakai analisis spektra sebagai materi komposisi. Notasi perlu
pitch aktual + mikrotonal + parameter `<sound>`. Lanjut ke [Mikrotonal &
Tuning (`Ch2-Mikrotonal-Tuning.md`)].