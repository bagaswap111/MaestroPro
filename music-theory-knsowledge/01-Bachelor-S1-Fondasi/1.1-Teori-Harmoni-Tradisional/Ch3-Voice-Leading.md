---
title: "Voice Leading"
tier: "Bachelor S1"
subject: "Teori Harmoni Tradisional"
xml_tags: ["<note>", "<voice>", "<staff>", "<rest>", "<chord>", "<slur>"]
software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
---

# Bab 3 — Voice Leading

> **Buku panduan bab ini:** Aldwell & Schachter, *Harmony and Voice Leading*
> (Bab 1–5, 15) — kitab utama part-writing; Kostka & Payne, *Tonal Harmony*
> (Bab 5–7). Fokus: menghubungkan akor dengan gerakan suara yang minimal,
> halus, dan independen.

## 3.1 Prinsip Dasar Voice Leading

Empat prinsip non-negotiable (Aldwell & Schachter, Bab 1):

1. **Gerak minimal** — suara bergerak sejauh mungkin; `common tones`
   dipertahankan.
2. **Independensi suara** — tanpa *voice crossing*; tiap suara mampu dibedakan
   pendengarnya.
3. **Hindari paralel sempurna** — *consecutive/parallel fifths* dan *octaves*
   merusak independensi (bass terlalu kuat).
4. **Resolusi tendency tones** — leading tone (B) & chordal 7th (F) harus
   berlanjut logis (B→C, F→E).

### 3.1.1 Jenis Gerakan Antar Suara

| Gerakan | Dua suara | Contoh (C→G) |
|---------|-----------|--------------|
| *Similar* | arah sama, interval beda | C4→D4, E4→G4 |
| *Parallel* | arah & interval sama | C4→D4, E4→F4 (5→5 = dilarang) |
| *Contrary* | arah berlawanan | C4→B3, G3→G4 |
| *Oblique* | satu diam, satu bergerak | C4→C4, G3→G4 |

### 3.1.2 Aturan Khusus (Aldwell–Schachter)

- **Fifth→fifth** dan **octave→octave** (pergerakan paralel P5/P8 antar dua
  suara yang sama) = pelanggaran.
- **Direct fifths/octaves** ke luar (satu suara *similar* menuju interval
  sempurna) — perhatian khusus pada sopran+bass.
- **7th chordal** harus *resolved* turun; exceptional: *retardation* V7→I.
- **Doubling** di inversi boleh 5th/3rd; jangan gandakan leading tone.

## 3.2 Spacing dan Range

*Voice ranges* wajar (SATB):

| Suara | Range konser | Catatan |
|-------|--------------|---------|
| Soprano | C4–C6 | Daerah kerja C4–A5 |
| Alto | G3–E5 | |
| Tenor | C3–G4 | Register sungsang bila naik terus |
| Bass | E2–C4 | |

Spacing antar suara berdekatan:

- Soprano→Alto: ≤ 1 oktaf (biasanya lebih rapat).
- Alto→Tenor: ≤ 1 oktaf.
- Tenor→Bass: bebas (fondasi harmoni).

> "Hindari gap tengah" = jangan biarkan *tenor-bass* terlalu lebar jika
> sopran-alto sudah lebar; suara tengah harus **berisi**.

### 3.2.1 MusicXML: Spacing via Register Aktual

MusicXML tidak punya elemen "spacing"; spacing ditentukan *notes actual* di
setiap `<voice>`. Pastikan `voice` numbering konsisten antar birama agar
software memvalidasi gerak.

## 3.3 Common Errors — Tabel Diagnosis

| Kesalahan | Contoh | Perbaikan |
|-----------|--------|-----------|
| *Parallel fifths* | C5–G4 → D5–A4 (soprano+alto) | Ubah arah (contrary) |
| *Parallel octaves* | C4–C3 → D4–D3 (bass double) | Hilangkan doubling |
| *Voice crossing* | Soprano turun di bawah alto | Kembalikan urutan |
| *Unresolved leading tone* | B → G (bukan → C) | Tuntaskan naik |
| *Unresolved 7th* | F (di V7) → G | 7th harus turun → E |
| *Doubled leading tone* | G: B di sopran & bass | Rangkap G/root |
| *Gap di tengah* | Tenor jauh dari alto | Naikkan tenor |

### 3.3.1 Peringatan: "Melodic Leaps"

Melodi besar belum tentu salah, tetapi lompatan > oktaf harus jarang; lompat
kromatis dalam harmoni diatonik juga mencurigakan (biasanya modulasi).

## 3.4 Part-Writing Empat Suara (SATB)

Metode: identifikasi rolas — untuk tiap akor, pilih inversi & voicing yang
meminimalkan gerakan.

### 3.4.1 Alur Kerja Aldwell–Schachter (Mini)

1. Tentukan bass line (root/5th, berikan arah & kadens).
2. Isi suara tengah mengikuti *soprano* + *bass*.
3. Periksa: common tone? paralel? tendency tone teresolusi?
4. Cek spacing & register pada tiap perubahan.

### 3.4.2 Contoh ii–V–I (Dm7–G7–Cmaj7) di SATB C mayor

- Soprano: F → G → E
- Alto: A → B → C
- Tenor: D → D → G
- Bass: D → G → C

Analisis: common tone D (alto? Tenor D→D); B (leading) → C; F (7th) → E ✓.

```xml
<measure number="1">
  <note>
    <pitch><step>F</step><octave>5</octave></pitch>
    <duration>2</duration>
    <voice>1</voice>
    <type>half</type>
    <staff>1</staff>
  </note>
  <note>
    <pitch><step>A</step><octave>4</octave></pitch>
    <duration>2</duration>
    <voice>2</voice>
    <type>half</type>
    <staff>1</staff>
  </note>
  <note>
    <pitch><step>D</step><octave>4</octave></pitch>
    <duration>2</duration>
    <voice>3</voice>
    <type>half</type>
    <staff>2</staff>
  </note>
  <note>
    <pitch><step>D</step><octave>3</octave></pitch>
    <duration>2</duration>
    <voice>4</voice>
    <type>half</type>
    <staff>2</staff>
  </note>
</measure>
```

> **Kunci MusicXML:** not dengan durasi sama & waktu mulai sama pada `voice`
> berbeda membentuk akor vertikal. Untuk satu partitur satu staf, gunakan
> `<chord/>` setelah not pertama (lihat
> `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch2-The-Note-Element.md`).

## 3.5 Voice Leading dan Chord Inversion

- **First inversion** (6) melunakkan gerak bass; rangkap boleh 3rd di akor
  mayor (daring praktik jiwa vokal).
- **Second inversion (6/4)** = *passing*, *pedal*, atau *cadential* —
  bukan tempat pijak stabil; selalu *resolve* ke V.

Contoh *cadential 6/4→V→I* (C: G–C–E → G–B–D–F → C–E–G):

```
Soprano:  E → D → C
Alto:     C → B → G
Tenor:    G → G → E
Bass:     C → G → C
```

## 3.6 Voice Leading dalam Orkestrasi

Di orkestrasi, "suara" = instrumen (Adler, *Study of Orchestration*,
Bab 5–7):

- **Doubling melodi** antar instrumen diperbolehkan (oboe+violin) — bukan
  *parallel octave error* dalam pengertian SATB; itu *doubling* (lihat
  `../1.3-Orkestrasi-Dasar/Ch3-Tekstur-Doubling.md`).
- **Voice crossing antar keluarga** dihindari di register sama.
- **Register + tesselature** menentukan bass saya tetap di bawah.

### 3.6.1 Kontinuitas dalam Timeline

Pastikan partitur berjalan: *overlap* antar birama (kit inversi pemain)
datang dari `<backward>/<forward>` element — jangan ubah `voice` ID di tengah
kalimat.

## 3.7 Miskonsepsi Umum

- **"Paralel oktaf didengar = saliva telinga"** — Bukan pembahasan "dengar",
  tapi *mixture* yang melemahkan independensi; hindari dalam *strict* writing.
- **"Voice crossing selalu salah"** — dalam *ornamental* figur bisa muncul,
  tapi jangan berkelanjutan.
- **"Jarak oktaf antara bass & tenor bebas-mana saja"** — semuanya boleh lebar
  bila suara tengah mengisi; jangan lebar terus di semua register.
- **"MusicXML punya tool cek voice leading"** — Tidak otomatis; gunakan
  music21 (`voiceLeading` module) atau plugin sebagai *assistant*, tetap
  kontrol telinga-musical.

## 3.8 Latihan

1. **Dasar:** Tulis SATB `I–vi–ii–V–I` (C mayor) dengan common-tone
   optimum.
2. **Menengah:** Identifikasi 5 dari 7 *errors* dari tabel 3.3 pada contoh
   partitur yang disediakan.
3. **Lanjut:** Terjemahkan ke MusicXML (4 `<voice>`), verifikasi di music21
   `voiceLeading`, lampirkan output.

## 3.9 Repertoar Dengar

- Bach, *Chorale* BWV 319 ("Machs mit mir, Gott") — SATB sempurna.
- Haydn, *St. Antoni Chorale* — doublings orkestra benar.
- Brahms, *Chorale Preludees* — spacing luar biasa.

## 3.10 Referensi Buku & Sumber Web

**Buku:**
- Aldwell & Schachter, *Harmony and Voice Leading*.
- Kostka & Payne, *Tonal Harmony*.
- Robert Gauldin, *Harmonic Practice in Tonal Music*.

**Web:**
- Music21 voiceLeading docs:
  https://web.mit.edu/music21/doc/moduleReference/moduleVoiceLeading.html
- MuseScore Part-Writing plugin (concept):
  https://musescore.org/

---

**Rangkuman:** Voice leading menjaga independensi & kehalusan suara melalui
compute tones, resolusi tendency tones, dan pembatasan paralel sempurna.
MusicXML mewakili tiap suara lewat `<voice>`/`<staff>` (ID stabil) dan akor
vertikal `<chord/>`. Materi lanjutan: [Progresi Akor & Modulasi
(`Ch2-Progresi-Akor-Modulasi.md`)] dan [Kontrapung (`Ch1-Species-Counterpoint.md`)].