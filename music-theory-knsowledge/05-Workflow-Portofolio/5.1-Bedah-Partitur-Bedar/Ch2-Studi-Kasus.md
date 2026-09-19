---
title: "Studi Kasus Partitur"
tier: "Workflow & Portfolio"
subject: "Bedah Partitur"
xml_tags: ["<part-list>", "<meter>", "<key>", "<direction>", "<sound>"]
software: ["Dorico", "Sibelius", "MuseScore", "IMSLP"]
---

# Bab 2 — Studi Kasus

> **Buku panduan bab ini:** Adler, *The Study of Orchestration* (musical
> examples); Boris Blacher/Heinz Becker, *The Technique of Orchestration*
> (kasus). Fokus: tiga karya pembeda — Beethoven, Gershwin, Zimmer — dan
> pelajaran langsung yang diekstrak.

## 2.1 Kasus A: Beethoven — Symphony No. 5, I

### 2.1.1 Data

| Aspek | Info |
|-------|------|
| Instrumentasi | 2 fl, 2 ob, 2 cl, 2 bsn; 2 hn, 2 tpt; timpani; strings |
| Kunci | C minor (fifths -3) |
| Meter | 4/4 (Allegro con brio, ♩=108) |
| Form | Sonata (exposition w/ repeat) |

### 2.1.2 Pelajaran Orchestration

1. **Motif homogen** — motif `da-da-da-dum` didouble di **semua** voice
   (strings + woodwinds + brass) untuk kekuatan sinyal.
2. **Register** — motif mula dari register tengah (cello) naik ke register
   tinggi sebagai intensitas.
3. **Retransition** — long *general pause* & pengendapan sebelum
   recapitulation.
4. **Timpani sebagai pedal** — timpani meng-bass motif di tonik, membuat
   pusat tonal tak tergoyahkan.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <part-list>
    <score-part id="P8"><part-name>Timpani</part-name></score-part>
    <score-part id="P9"><part-name>Violin I</part-name></score-part>
  </part-list>
  <part id="P8">
    <measure number="1">
      <attributes>
        <divisions>1</divisions>
        <key><fifths>-3</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>F</sign><line>4</line></clef>
      </attributes>
      <note>
        <rest/>
        <duration>4</duration>
      </note>
    </measure>
  </part>
  <part id="P9">
    <measure number="1">
      <attributes>
        <divisions>1</divisions>
        <key><fifths>-3</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <note>
        <rest/>
        <duration>4</duration>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.2 Kasus B: Gershwin — Rhapsody in Blue

### 2.2.1 Data

| Aspek | Info |
|-------|------|
| Instrumentasi | Klarinet solo, brass, woodwinds, strings, percussion, piano |
| Kunci | F mayor / pentatonik jazz |
| Meter | 4/4 (rubato sering) |
| Form | Fantasia (sectional theme) |

### 2.2.2 Pelajaran Orchestration

1. **Glissando klarinet** — pembuka ikonik memerlukan *glissando* dengan
   sembulan; ditulis di klarinet transpos B♭ (notasi konser turun M2).
2. **Jazz + Orchestra** — padukan melodi jazz solo dengan harmoni yang sama
   di strings (unison doubling) → baur etnis.
3. **Rubato** — sering `rit.` sebelum motif utama masuk.
4. **Piano sebagai instrumen orkestra** — piano bukan sekadar pengiring;
   peran berganti antara solois, pengisi, dan perkusi.

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
        <divisions>1</divisions>
        <key><fifths>0</fifths></key>
        <time><beats>4</beats><beat-type>4</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <words xml:space="preserve">rit. molto</words>
        </direction-type>
        <sound tempo="76"/>
      </direction>
      <note>
        <rest/>
        <duration>4</duration>
      </note>
    </measure>
  </part>
</score-partwise>
```

## 2.3 Kasus C: Hans Zimmer — Film Score (mis. *Gladiator*)

### 2.3.1 Data

| Aspek | Info |
|-------|------|
| Media | Film épique |
| Instrumentasi | Brass besar, choir, strings kaya, synth pad |
| Playback | Mockup epik (sample libraries) |
| Tempo map | Click track + hit points |

### 2.3.2 Pelajaran Orchestration

1. **Dynamics besar** — dimulai lembut, crescendo bertingkat pada brass.
2. **Doubling beds** — strings + choir dalam register tegang untuk emosi.
3. **Klik track** — gunakan `tempo` map untuk sinkronisasi adegan (lihat
   `../../02-Master-S2-Lanjutan/2.2-Arranging-Komersial-Film/Ch3-Film-Scoring-Notation.md`).
4. **Lo-fi → hi-fi layer** — mulai tipis (pad) → tambah brass & choir di
   puncak: formula sinematik Berklee.

## 2.4 Template Ringkasan Analisis

```markdown
# {Karya}
- Komposer/Era
- Instrumentasi & key/time
- Form
- 3 pelajaran orkestrasi:
  1. ...
  2. ...
  3. ...
- Replikasi mini: ...
```

> Simpan tiap template sebagai file `.md` di folder `notes/` per proyek.
> Jadikan portofolio analisis — bukti perkembangan diri.

## 2.5 Miskonsepsi

- **"Pelajari masterpiece = duplikasi"** — Menyalin palet = belajar
  kosakata, bukan plagiarisme musikal.
- **"Analisis cukup sekali"** — Ulangi saat gaya berkembang; interpretasi
  berubah seiring perspektif.
- **"MusicXML tak perlu untuk bedah"** — Untuk analisis besar (100+ bar),
  MusicXML+music21 jauh lebih cepat dan dapat di-repeat.

## 2.6 Latihan

1. **Replikasi** — 8-bar mini orchestration meniru teknik case A (motif
   unison).
2. **Kontras** — ubah doubling map satu karya (misal hilangkan bassoon)
   dengarkan bedanya.
3. **Mapping film** — beri tempo map & hit points pada adegan 60-det.
4. **Dokumentasi** — lengkapi template untuk ketiga kasus.

## 2.7 Repertoar Kasus Lain

- Debussy — *Prélude à l'après-midi d'un faune* — superimposisi warna.
- Prokofiev — *Romeo and Juliet* (Montagues & Capulets) — tema brutal.
- John Williams — *Star Wars* — leitmotif brass + strings.

## 2.8 Referensi

- Adler, *The Study of Orchestration* — musical examples.
- Blacher/Becker, *The Technique of Orchestration*.
- Score files: IMSLP (PDF) + MuseScore (MusicXML).

---

**Rangkuman:** Studi kasus (Beethoven, Gershwin, Zimmer) menunjukkan pola
orkestrasi yang bisa direplikasi: doubling motif, glissando khas instrumen,
dinamika bertingkat, dan tempo map film. Catat masing-masingnya ke portfolio.