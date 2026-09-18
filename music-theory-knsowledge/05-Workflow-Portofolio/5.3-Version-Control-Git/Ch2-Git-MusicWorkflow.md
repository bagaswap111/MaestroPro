---
title: "Git Music Workflow"
tier: "Workflow & Portfolio"
subject: "Version Control Git"
xml_tags: ["musicxml", "score", "template"]
software: ["Git", "GitHub", "MuseScore", "Dorico"]
---

# Bab 2 — Git Music Workflow

> **Buku panduan bab ini:** Chacon & Straub, *Pro Git* (branching &
> workflow bagian 3); workflow profesiona l (GitHub flow). Fokus: menerapkan
> branching/merging untuk produksi partitur kolaboratif.

## 2.1 Branching Strategy untuk Project Arrangement

| Branch | Fungsi |
|--------|--------|
| `main` | Versi release (siap kirim) |
| `develop` | Integrasi terus-menerus |
| `feature/<nama>` | Fitur tunggal (mis. string-arr) |
| `hotfix/<deskripsi>` | Perbaikan darurat |

```
main        ──●──────────────●──────→
                 \          /
feature/strings  ●────────● (digabung)
```

> Model adaptasi Git Flow untuk musik: `develop` sebagai sandang integrasi,
> `main` sebagai versi final yang dikirim ke klien.

## 2.2 Workflow Release untuk Proyek Lagu

1. Mulai dari template di `main`.
2. Buat branch `feature/brass-solo`.
3. Setelah lulus, buka PR → merge ke `develop`.
4. Test di MuseScore/Dorico (render + playback).
5. Release dari `develop` → `main` + tag `v1.2.0`.

## 2.3 Commit Message Style (Konvensional)

```bash
feat: tambahkan bagian brass untuk birama 40-60
fix: perbaiki glissando klarinet pada bar 12
docs: dokumentasikan range instrumen
refactor: bersihkan duplicate voice 2
test: validasi export musicxml
```

Format: `type(scope): deskripsi`. Scope opsional (mis. `fix(strings):`).

## 2.4 Diff MusicXML praktis

```bash
git diff                     # line-by-line
git diff --word-diff=color   # untuk nesting XML
```

> Saat membandingkan cabang:
> `git diff --word-diff=color main develop`.

## 2.5 Kapan Commit?

Commit ketika:

- Selesai seluruh bagian/gerakan.
- Mengubah instrumentasi.
- Mengubah intro/coda.
- Mengganti parameter (tempo/keys).
- Menambahkan ekspor musik baru (MIDI/mxl tak perlu).

**Prinsip:** satu commit = satu perubahan logis.

## 2.6 Merge vs Rebase

| Strategi | Kelebihan | Kelemahan |
|----------|-----------|-----------|
| Merge | History lengkap | Graph bercabang |
| Rebase | Linear, bersih | Rewrite history |

Gunakan **merge** untuk kolaborasi aman; **rebase** untuk membersihkan lokal
sebelum push.

## 2.7 Git LFS untuk Sample Audio

```bash
git lfs install
git lfs track "*.wav" "*.sample"
git add .gitattributes
git commit -m "setup git lfs for samples"
```

> Audio/sample besar jangan di-commit biasa (repo bengkak); LFS memindahkan
> blok ke server.

## 2.8 Release & Tagging

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

## 2.9 Workflow Kolaborasi (Pull Request)

```
1. git checkout -b feature/x
2. ...kerjakan, commit
3. git push origin feature/x
4. buka Pull Request di GitHub
5. reviewer meninjau diff (MusicXML teks!)
6. merge ke develop → test → release
```

## 2.10 Miskonsepsi

- **"PR hanya untuk dev"** — PR + review sangat berguna untuk partitur:
  perbedaan register, perdebatan teknik → terdokumentasi.
- **"Tag bisa diedit mudah"** — Tag = pointer immutable; buat tag baru bukan
  edit tag lama.
- **"Rebase aman untuk berbagi"** — Rebase pada cabang publik bisa konflik;
  hanya untuk cabang pribadi.

## 2.11 Latihan

1. Buat branch `feature/cello-line`, edit, commit, merge → bandingkan diff.
2. Susun release + tag pada 3 ekspor (`v0.1`, `v0.2`, `v1.0`).
3. Buat PR sederhana (push branch alternatif) dan review sendiri.
4. Terapkan Git LFS pada 1 folder audio → cek `.gitattributes`.

## 2.12 Checklist Workflow

| Periksa | Ya/Tidak |
|---------|----------|
| Branch strategy dipilih & didokumentasikan? | |
| Pesan commit konvensional? | |
| MusicXML di-diff sistematis? | |
| Release/test di software notasi sebelum merge? | |
| Git LFS untuk file audio besar (bila ada)? | |

## 2.13 Referensi

- Chacon & Straub, *Pro Git*: https://git-scm.com/book
- GitHub flow docs.

---

**Rangkuman:** Git Music Workflow = branch strategy + commit konvensional +
diff-based review + release/tagging. Jadikan `.musicxml` teks sebagai sumber,
commit untuk perubahan logis, dan PR-pass. Ini menutup Tier 5 — Workflow &
Portfolio.