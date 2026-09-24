---
title: "Git Music Workflow"
tier: "Workflow & Portfolio"
subject: "Git Version Control"
xml_tags: ["musicxml", "score", "template"]
software: ["Git", "GitHub", "MuseScore", "Dorico"]
---

# Chapter 2 — Git Music Workflow

> **Guidebook for this chapter:** Chacon & Straub, *Pro Git* (branching &
> workflow part 3); professional workflow (GitHub flow). Focus: applying
> branching/merging to collaborative score production.

## 2.1 Branching Strategy for Arrangement Projects

| Branch | Function |
|--------|----------|
| `main` | Release version (ready to send) |
| `develop` | Continuous integration |
| `feature/<name>` | Single feature (e.g. string-arr) |
| `hotfix/<description>` | Emergency fix |

```
main        ──●──────────────●──────→
                 \          /
feature/strings  ●────────● (merged)
```

> Git Flow model adapted for music: `develop` as the integration staging,
> `main` as the final version sent to the client.

## 2.2 Release Workflow for Song Projects

1. Start from the template on `main`.
2. Create branch `feature/brass-solo`.
3. Once it passes, open a PR → merge to `develop`.
4. Test in MuseScore/Dorico (render + playback).
5. Release from `develop` → `main` + tag `v1.2.0`.

## 2.3 Commit Message Style (Conventional)

```bash
feat: add brass section for bars 40-60
fix: fix clarinet glissando at bar 12
docs: document instrument ranges
refactor: clean up duplicate voice 2
test: validate musicxml export
```

Format: `type(scope): description`. Scope optional (e.g. `fix(strings):`).

## 2.4 Practical MusicXML Diffs

```bash
git diff                     # line-by-line
git diff --word-diff=color   # for XML nesting
```

> When comparing branches:
> `git diff --word-diff=color main develop`.

## 2.5 When to Commit?

Commit when:

- A whole section/movement is finished.
- Instrumentation changes.
- The intro/coda changes.
- Parameters change (tempo/keys).
- New music exports are added (MIDI/mxl not needed).

**Principle:** one commit = one logical change.

## 2.6 Merge vs Rebase

| Strategy | Advantage | Disadvantage |
|----------|-----------|--------------|
| Merge | Complete history | Branching graph |
| Rebase | Linear, clean | Rewrites history |

Use **merge** for safe collaboration; **rebase** to tidy up locally
before pushing.

## 2.7 Git LFS for Sample Audio

```bash
git lfs install
git lfs track "*.wav" "*.sample"
git add .gitattributes
git commit -m "setup git lfs for samples"
```

> Don't commit large audio/samples normally (repo bloat); LFS moves
> the blobs to the server.

## 2.8 Release & Tagging

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

## 2.9 Collaboration Workflow (Pull Request)

```
1. git checkout -b feature/x
2. ...work, commit
3. git push origin feature/x
4. open a Pull Request on GitHub
5. reviewer reviews the diff (text MusicXML!)
6. merge to develop → test → release
```

## 2.10 Misconceptions

- **"PRs are only for devs"** — PR + review is very useful for scores:
  register differences, technique debates → documented.
- **"Tags are easily edited"** — Tag = immutable pointer; create a new tag instead of
  editing an old one.
- **"Rebase is safe to share"** — Rebasing a public branch can conflict;
  only for private branches.

## 2.11 Exercises

1. Create branch `feature/cello-line`, edit, commit, merge → compare the diff.
2. Set up releases + tags on 3 exports (`v0.1`, `v0.2`, `v1.0`).
3. Create a simple PR (push an alternate branch) and review it yourself.
4. Apply Git LFS to 1 audio folder → check `.gitattributes`.

## 2.12 Workflow Checklist

| Check | Yes/No |
|-------|--------|
| Branch strategy chosen & documented? | |
| Conventional commit messages? | |
| MusicXML diffed systematically? | |
| Release/tested in notation software before merge? | |
| Git LFS for large audio files (if any)? | |

## 2.13 References

- Chacon & Straub, *Pro Git*: https://git-scm.com/book
- GitHub flow docs.

---

**Summary:** Git Music Workflow = branch strategy + conventional commits +
diff-based review + release/tagging. Make text `.musicxml` the source,
commit for logical changes, and go through the PR pass. This closes Tier 5 — Workflow &
Portfolio.
