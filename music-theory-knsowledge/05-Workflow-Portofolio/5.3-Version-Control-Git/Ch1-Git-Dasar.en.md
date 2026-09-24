---
title: "Git — Basics for Musicians"
tier: "Workflow & Portfolio"
subject: "Git Version Control"
xml_tags: ["musicxml", "score-file", "file-format"]
software: ["Git", "GitHub", "SourceTree", "VS Code"]
---

# Chapter 1 — Git: Basics for Musicians

> **Guidebook for this chapter:** Scott Chacon & Ben Straub, *Pro Git* (basics
> section); music file versioning practice (Cuthbert & music21).
> Focus: why & how to use Git for score archives.

## 1.1 Why Version Control for Music?

- Unlimited revisions without a string of `final_v2_final_v3`.
- Collaboration between arrangers without overlapping conflicts.
- Tracking who changed what.
- Automatic backup via remote (GitHub/GitLab).

## 1.2 Core Git Concepts

| Concept | Explanation |
|---------|-------------|
| Repository | Project folder + `.git` history |
| Commit | Snapshot of changes (+ descriptive message) |
| Branch | Working branch (e.g.: `feature/jazzy`) |
| Merge/Rebase | Combining branches |
| Remote | Repository on a server (origin) |
| Working tree | Active files on disk |

**Git's three areas:**

```
Working tree → (git add) → Staging → (git commit) → Repository history
```

## 1.3 Basic Commands

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

## 1.4 `.gitignore` for Music Projects

```gitignore
# Build artifacts
*.mxl
*.mid
*.wav
*.mp3
!score.musicxml     # except the canonical file

# Software cache
*.osmid
._metadata

# Editor
.DS_Store
Thumbs.db

# Virtual env
venv/
__pycache__/
```

> The `!` (negation) rule re-includes a file after a pattern has been created.

## 1.5 Binary vs Text Files

| Type | Diff readability | Recommendation |
|------|------------------|----------------|
| `.musicxml` (XML text) | Good — readable diffs | **make it the source** |
| `.mxl` (zip) | Almost unreadable | ignore |
| `.mscz`/`.sib` | Cannot diff | ignore |

> **Recommendation:** commit `.musicxml` as the *source of truth*, not
> `.mscz`/`.mxl`. This aligns with music21/Tier 3 scripting rules: text XML =
> easy to diff.

## 1.6 MusicXML Diffs in Git

```bash
git diff --color-words
```

For better structural diffs use `xmldiff`:

```bash
pip install xmldiff
xmldiff old.musicxml new.musicxml
```

> See the post-parse format to understand the structure (`Ch1-Anatomi`
> Tier 4: `../../04-MusicXML-Masterclass/4.1-Anatomi-MusicXML/Ch1-Struktur-Root-Partwise.md`).

## 1.7 Simple Workflow (Individual)

```
1. git init
2. create score template
3. git add + commit  (every milestone)
4. continue arranging
5. commit every major change
6. push to remote as backup
```

## 1.8 Misconceptions

- **"Git is only for code"** — Any file's versions (including MusicXML)
  can be versioned — as long as it's text.
- **"`git add .` is always safe"** — If large binary files get included, the repo bloats;
  use `.gitignore`.
- **"Deleting a file = gone from history"** — Old commits remain; you
  can `git revert`/`git checkout` an old version.

## 1.9 Exercises

1. `git init` in a score folder → commit the template.
2. Create two branches (`feature/strings`, `main`) — change one, merge.
3. Create a correct `.gitignore` → `git status` doesn't show `.mxl`.
4. Compare the diff of one `musicxml` before/after a small edit.

## 1.10 Basic Git Checklist

| Check | Yes/No |
|-------|--------|
| Repository initialized? | |
| `.gitignore` created for binary files? | |
| Commit messages descriptive (verbs)? | |
| MusicXML versioned as text? | |
| Remote backup available? |

## 1.11 References

- Chacon & Straub, *Pro Git*: https://git-scm.com/book
- Continue to [Git Music Workflow (`Ch2-Git-MusicWorkflow.md`)].

---

**Summary:** Git manages revisions & collaboration. For music: make
`.musicxml` the source, ignore `.mxl`/`.mscz`, and commit often with
clear messages.
