---
title: "Git — Dasar untuk Musisi"
tier: "Workflow & Portfolio"
subject: "Version Control Git"
xml_tags: ["musicxml", "score-file", "file-format"]
software: ["Git", "GitHub", "SourceTree", "VS Code"]
---

# Bab 1 — Git: Dasar untuk Musisi

> **Buku panduan bab ini:** Scott Chacon & Ben Straub, *Pro Git* (bagian
> dasar); praktik versioning file musik (Cuthbert & music21).
> Fokus: mengapa & bagaimana Git untuk arsip partitur.

## 1.1 Mengapa Version Control untuk Musik?

- Revisi tak terbatas tanpa barisan `final_v2_final_v3`.
- Kolaborasi antar arranger tanpa konflik tumpang tindih.
- Tracking siapa mengubah apa.
- Backup otomatis via remote (GitHub/GitLab).

## 1.2 Konsep Inti Git

| Konsep | Penjelasan |
|--------|------------|
| Repository | Folder proyek + history `.git` |
| Commit | Snapshot perubahan (+pesan deskriptif) |
| Branch | Cabang kerja (misal: `feature/jazzy`) |
| Merge/Rebase | Menggabungkan cabang |
| Remote | Repositori di server (origin) |
| Working tree | File aktif di disk |

**Tiga area Git:**

```
Working tree → (git add) → Staging → (git commit) → Repository history
```

## 1.3 Perintah Dasar

```bash
git init
git add .
git commit -m "Initial score layout"

# Remote
git remote add origin https://github.com/you/your-score.git
git push -u origin main

# Branch
git checkout -b feature/mix
git branch
git switch main
```

## 1.4 `.gitignore` untuk Proyek Music

```gitignore
# Build artifacts
*.mxl
*.mid
*.wav
*.mp3
!score.musicxml     # kecuali file kanonik

# Cache software
.*.osmid
._metadata

# Editor
.DS_Store
Thumbs.db

# Virtual env
venv/
__pycache__/
```

> Aturan `!` (negation) mengembalikan file setelah pola dibuat.

## 1.5 File Biner vs Teks

| Tipe | Diff readability | Rekomendasi |
|------|------------------|-------------|
| `.musicxml` (XML teks) | Bagus — diff terbaca | **jadikan sumber** |
| `.mxl` (zip) | Hampir tak terbaca | ignore |
| `.mscz`/`.sib` | Tidak bisa diff | ignore |

> **Rekomendasi:** commit `.musicxml` sebagai *source of truth*, bukan
> `.mscz`/`.mxl`. Ini selaras kaidah music21/Tier 3 scripting: XML teks =
> mudah di-diff.

## 1.6 Diff MusicXML di Git

```bash
git diff --color-words
```

Untuk diff struktural lebih baik pakai `xmldiff`:

```bash
pip install xmldiff
xmldiff old.musicxml new.musicxml
```

> lihat format pasca-parse untul memahami struktur (`Ch1-Anatomi` Tier 4:
> `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch1-Struktur-Root-Partwise.md`).

## 1.7 Workflow Simpel (Individu)

```
1. git init
2. buat template score
3. git add + commit  (setiap milestone)
4. lanjut arrangement
5. commit tiap perubahan besar
6. push ke remote sebagai backup
```

## 1.8 Miskonsepsi

- **"Git hanya untuk code"** — Versi file apa saja (termasuk MusicXML)
  bisa di-version — dengan syarat teks.
- **"`git add .` selalu aman"** — Bila file biner besar ikut, repo membesar;
  gunakan `.gitignore`.
- **"Delete file = hilang dari history"** — Commit lama tetap ada; Anda
  bisa `git revert`/`git checkout` versi lama.

## 1.9 Latihan

1. `git init` pada folder score → commit template.
2. Buat dua cabang (`feature/strings`, `main`) — ubah di satu, merge.
3. Buat `.gitignore` benar → `git status` tak menampilkan `.mxl`.
4. Bandingkan diff satu `musicxml` sebelum/sesudah edit kecil.

## 1.10 Checklist Git Dasar

| Periksa | Ya/Tidak |
|---------|----------|
| Repositori diinisialisasi? | |
| `.gitignore` untuk file biner dibikin? | |
| Commit pesan deskriptif (kata kerja)? | |
| MusicXML di-versi sebagai teks? | |
| Remote backup tersedia? | |

## 1.11 Referensi

- Chacon & Straub, *Pro Git*: https://git-scm.com/book
- Lanjut ke [Git Music Workflow (`Ch2-Git-MusicWorkflow.md`)].

---

**Rangkuman:** Git mengelola revisi & kolaborasi. Untuk musik: jadikan
`.musicxml` sebagai sumber, ignore `.mxl`/`.mscz`, dan commit sering dengan
pesan jelas.