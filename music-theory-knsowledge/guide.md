Membangun website berbasis file Markdown (`.md`) untuk perpustakaan teori musik yang terintegrasi dengan **MusicXML** adalah proyek yang sangat ambisius dan brilian. Ini pada dasarnya adalah membangun "Wiki Pribadi" atau "Digital Garden" untuk komposer/arranger modern.

Untuk website berbasis Markdown (sangat disarankan menggunakan *Static Site Generator* seperti **MkDocs, Hugo, Docusaurus, atau Obsidian Publish**), struktur hierarki folder dan file harus sangat rapi.

Berikut adalah **Jabaran Struktur Website hingga 5 Level (Level 1 s.d. Level 5)**. Setiap level mewakili kedalaman dari Kategori Besar hingga implementasi kode/tag MusicXML spesifik.

---

### 🟢 LEVEL 1: ROOT / TIER (Kategori Utama / Derajat Akademik)
*Ini adalah folder utama di root website Anda.*
1. `01-Bachelor-S1-Fondasi/`
2. `02-Master-S2-Lanjutan/`
3. `03-Doctoral-S3-Riset/`
4. `04-MusicXML-Masterclass/` (Khusus teknis XML)
5. `05-Workflow-Portofolio/` (Studi kasus & otomasi)

---

### 🟡 LEVEL 2: SUBJECT / BOOK (Mata Kuliah / Buku Inti)
*Ini adalah sub-folder di dalam masing-masing Tier.*

#### Dari `01-Bachelor-S1-Fondasi/`
*   `1.1-Teori-Harmoni-Tradisional/`
*   `1.2-Kontrapung-Bentuk-Musik/`
*   `1.3-Orkestrasi-Dasar/`

#### Dari `02-Master-S2-Lanjutan/`
*   `2.1-Harmoni-Jazz-PostTonal/`
*   `2.2-Arranging-Komersial-Film/`
*   `2.3-Extended-Techniques/`

#### Dari `03-Doctoral-S3-Riset/`
*   `3.1-Psikoakustik-Spektral/`
*   `3.2-Komposisi-Algoritmik/`
*   `3.3-Sistem-NonBarat-Etno/`

#### Dari `04-MusicXML-Masterclass/`
*   `4.1-Anatomi-MusicXML/`
*   `4.2-Music-Engraving-Rules/`
*   `4.3-Playback-MIDI-Integration/`

#### Dari `05-Workflow-Portofolio/`
*   `5.1-Bedah-Partitur-Bedar/`
*   `5.2-Otomasi-Python-Scripting/`
*   `5.3-Version-Control-Git/`

---

### 🟠 LEVEL 3: CHAPTER (Bab Buku)
*Ini adalah file `.md` utama atau folder di dalam Subject.*

*(Contoh penjabaran untuk **1.3-Orkestrasi-Dasar** dan **4.1-Anatomi-MusicXML**)*

**Contoh di `1.3-Orkestrasi-Dasar/`:**
*   `Ch1-Keluarga-Instrumen-Ranges.md`
*   `Ch2-Transposisi-Instrumen.md`
*   `Ch3-Tekstur-Doubling.md`
*   `Ch4-Notasi-Percussion.md`

**Contoh di `4.1-Anatomi-MusicXML/`:**
*   `Ch1-Struktur-Root-Partwise.md`
*   `Ch2-The-Note-Element.md`
*   `Ch3-Attributes-Directions.md`
*   `Ch4-Harmony-Chord-Symbols.md`

---

### 🔴 LEVEL 4: SECTION (Sub-Bab / Konsep Spesifik)
*Ini adalah Heading (H2 `##`) di dalam file `.md` Level 3.*

*(Contoh penjabaran di dalam file **Ch2-Transposisi-Instrumen.md**)*

**File: `Ch2-Transposisi-Instrumen.md`**
*   `## 4.1 Konsep Transposisi Konser vs Instrumen Transpos`
*   `## 4.2 Keluarga Woodwind (Flute, Clarinet in Bb, Alto Sax)`
*   `## 4.3 Keluarga Brass (French Horn in F, Trumpet in Bb)`
*   `## 4.4 Aturan Oktavasi (Contrabass, Piccolo, Guitar)`

*(Contoh penjabaran di dalam file **Ch2-The-Note-Element.md**)*

**File: `Ch2-The-Note-Element.md`**
*   `## 4.1 Elemen <pitch> (Step, Octave, Alter)`
*   `## 4.2 Elemen <rest> dan <unpitched>`
*   `## 4.3 Elemen <duration> dan <type>`
*   `## 4.4 Elemen <chord> (Notasi Akor Vertikal)`

---

### 🟣 LEVEL 5: SUB-SECTION / XML NODE (Detail Mikro & Implementasi Kode)
*Ini adalah Heading (H3 `###` atau H4 `####`) di dalam file `.md`, berisi penjelasan teori yang langsung diikat dengan **Tag/Node MusicXML** atau aturan engraving spesifik.*

*(Contoh penjabaran Level 5 dari file **Ch2-Transposisi-Instrumen.md**)*

**File: `Ch2-Transposisi-Instrumen.md`**
*   `### 4.2.1 Clarinet in Bb: Cara kerja transposisi di otak arranger`
*   `### 4.2.2 Implementasi Clarinet Bb di MusicXML`
    *   `#### Tag <score-instrument> dan ID unik`
    *   `#### Tag <midi-instrument> dan <midi-channel>`
    *   `#### **KUNCI:** Tag `<transpose><diatonic>-1</diatonic><chromatic>-2</chromatic></transpose>` di dalam `<attributes>`
*   `### 4.3.1 French Horn in F: Menangani register ekstrem`
*   `### 4.3.2 Implementasi Horn F di MusicXML`
    *   `#### Tag `<transpose>` untuk Horn F`
    *   `#### Mengatasi tabrakan *ledger line* di software notasi via XML`

*(Contoh penjabaran Level 5 dari file **Ch4-Harmony-Chord-Symbols.md**)*

**File: `Ch4-Harmony-Chord-Symbols.md`**
*   `### 4.1 Menulis Chord Symbol Dasar (Cmaj7, Dm7)`
*   `### 4.2 Menulis Extended & Altered Chords (C7#9, Fm11b5)`
    *   `#### Struktur Tag `<harmony>` dan `<frame>` (Chord Diagram)`
    *   `#### Tag `<degree><degree-value>9</degree-value><degree-alter>1</degree-alter><degree-type>alter</degree-type></degree>`
*   `### 4.3 Slash Chords & Polychords (C/E, D/F#)`
    *   `#### Menggunakan `<bass><bass-step>E</bass-step></bass>``
    *   `#### Trik menuliskan Polychord kompleks menggunakan `<words>` jika `<harmony>` tidak support`

---

### 💡 Rekomendasi Teknis untuk Membangun Website Ini

1.  **Platform / Tools:**
    *   Gunakan **Obsidian** untuk menulis dan mengelola file `.md` secara lokal. Obsidian sangat bagus untuk membuat *link* antar konsep (misal: saat menulis tentang "Clarinet Bb", Anda bisa langsung klik link ke halaman "Tag Transpose MusicXML").
    *   Untuk mempublikasikannya ke web, gunakan **MkDocs (dengan tema Material)** atau **Docusaurus**. Keduanya sangat sempurna untuk dokumentasi teknis yang menggabungkan teks dan *code-block* (untuk menampilkan contoh kode XML).

2.  **Format Penulisan Markdown:**
    Selalu gunakan format *Code Block* untuk setiap contoh MusicXML agar mudah dibaca dan di-*copy* oleh pengguna (atau oleh Anda sendiri saat butuh referensi).
    ```xml
    <!-- Contoh format penulisan di Level 5 -->
    <attributes>
      <transpose>
        <diatonic>-1</diatonic>
        <chromatic>-2</chromatic>
      </transpose>
    </attributes>
    ```

3.  **Sistem Tagging / Frontmatter:**
    Di bagian paling atas setiap file `.md` (Level 3), tambahkan *Frontmatter* YAML untuk metadata. Ini akan membantu mesin pencari di website Anda.
    ```yaml
    ---
    title: "Transposisi Instrumen"
    tier: "Bachelor S1"
    subject: "Orkestrasi Dasar"
    xml_tags: ["<transpose>", "<score-instrument>", "<attributes>"]
    software: ["Dorico", "Sibelius", "Finale", "MuseScore"]
    ---
    ```

Dengan struktur 5 level ini, website Anda tidak hanya akan menjadi tumpukan teks teori musik, tetapi akan menjadi **Database Teknis yang Hidup**, di mana setiap konsep harmoni/orkestrasi langsung terhubung dengan cara mengeksekusinya di dalam kode MusicXML.