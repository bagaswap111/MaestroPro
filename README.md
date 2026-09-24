# MaestroPro

> **From Audio to Artistry** — AI-powered music transcription, notation & orchestration by **Maya Instruments Technology**.

A monorepo containing the **MaestroPro** desktop app (MuseScore 4 plugin + Python backend), the **yue2-music** AI skill (SheetSage2 + YuE2), a **MusicXML music-theory knowledge library**, and its **web viewer**.

**License:** MIT (see [`LICENSE`](LICENSE)) · **Author:** Bagaskoro Saputro / Maya Instruments Technology

---

## Table of Contents

1. [What's in this repo](#whats-in-this-repo)
2. [MaestroPro App (`maestropro/`)](#maestropro-app-maestropro)
   - [Architecture overview](#architecture-overview)
   - [Backend modules](#backend-modules)
   - [Orchestration engine (v1.1)](#orchestration-engine-v11)
   - [API reference](#api-reference)
   - [WebSocket protocol](#websocket-protocol)
   - [Setup & run](#setup--run)
   - [Configuration](#configuration)
   - [Tests](#tests)
3. [yue2-music Skill (`yue2-music/`)](#yue2-music-skill-yue2-music)
4. [Music Theory Library (`music-theory-knsowledge/`)](#music-theory-library-music-theory-knsowledge)
5. [Theory Webview (`music-theory-knsowledge-webview/`)](#theory-webview-music-theory-knsowledge-webview)
6. [Documentation](#documentation)
7. [Tech stack](#tech-stack)

---

## What's in this repo

| Directory | What it is |
| :--- | :--- |
| [`maestropro/`](maestropro/) | The MaestroPro application: FastAPI + WebSocket backend, MuseScore 4 QML plugin frontend, tests, and docs. |
| [`yue2-music/`](yue2-music/) | Agent skill wrapping **SheetSage2** (audio → lead-sheet ABC) and **YuE2** (score-conditioned song generation) with strict native-ABC tooling. |
| [`music-theory-knsowledge/`](music-theory-knsowledge/) | Markdown knowledge base: academic music theory (S1–S3) bound to MusicXML tags & engraving rules. |
| [`music-theory-knsowledge-webview/`](music-theory-knsowledge-webview/) | Small Node.js server that renders the knowledge base (Markdown + MusicXML scores) in the browser. |
| [`docs/`](docs) | *(in `maestropro/docs`)* Master architecture document and the v1.1 SheetSage2/YuE2 integration spec. |

```text
MaestroPro/                          ← this repo
├── maestropro/                      ← the app
│   ├── backend/                     ← FastAPI + WebSocket Python backend
│   │   ├── main.py                  ← REST + WS entry point
│   │   ├── config.py                ← settings (ports, paths, model IDs)
│   │   ├── audio_engine/            ← source resolution & download (downloader.py)
│   │   ├── notation_engine/         ← placeholder (planned: analyze/arrange/MusicXML)
│   │   ├── skill_compiler/          ← Markdown → Python skill compiler (compiler.py)
│   │   └── orchestration/           ← SheetSage2 + YuE2 HITL workflow (v1.1) ✅
│   ├── frontend/                    ← MuseScore 4 plugin (QML + manifest.json)
│   ├── tests/                       ← pytest suite (orchestration)
│   ├── docs/                        ← architecture.md, version-1.1.md
│   └── requirements.txt
├── yue2-music/                      ← SheetSage2/YuE2 skill (SKILL.md + scripts/)
├── music-theory-knsowledge/         ← theory curriculum (Markdown)
├── music-theory-knsowledge-webview/ ← browser viewer (Node)
├── LICENSE                          ← MIT
└── .gitignore
```

---

## MaestroPro App (`maestropro/`)

**Version:** backend `1.1.0` · architecture doc `2.1.0`

MaestroPro bridges raw audio and professional notation. It runs as a **MuseScore 4 plugin (QML UI)** talking to a **local Python backend** over REST (`:8000`) and WebSocket (`:8765`). Heavy AI work (audio ML, music theory, LLM codegen, neural transcription/generation) stays in Python; MuseScore just opens the final `.musicxml`.

The **orchestration engine (v1.1)** — SheetSage2 lead-sheet transcription + YuE2 audio previews with human-in-the-loop editing — is the fully built and tested pipeline today; the classic Demucs/Basic-Pitch transcription path and notation engine are scaffolded for later phases (see [Architecture overview](#architecture-overview)).

### Architecture overview

```text
┌──────────────────────────────┐
│  MuseScore 4 Plugin (QML)    │  UI, progress, score open
│  REST client + WS client     │
└──────────┬───────────────────┘
           │ HTTP :8000  ·  WS :8765
┌──────────▼───────────────────┐
│  FastAPI backend (Python)    │
│  ├─ audio_engine  🟡         │  resolve/download sources (yt-dlp)
│  ├─ notation_engine 🟡       │  placeholder (planned analyze/arrange)
│  ├─ skill_compiler ✅         │  Markdown → Python via local Ollama (Qwen)
│  └─ orchestration ✅          │  SheetSage2 transcribe → edit → YuE2 preview
└──────────┬───────────────────┘
           │ subprocess (separate venvs)
┌──────────▼───────────────────┐      ┌────────────────────┐
│  yue2-music skill scripts    │◄────►│ Ollama :11434      │
│  (SheetSage2 / YuE2)         │      │ qwen2.5-coder:7b   │
└──────────────────────────────┘      └────────────────────┘

✅ fully implemented · 🟡 scaffold / planned (see Backend modules)
```

### Backend modules

| Module | Files | Status | Purpose |
| :--- | :--- | :--- | :--- |
| **Entry** | `main.py` | ✅ | FastAPI app, lifespan, WebSocket `/ws/{client_id}`, all REST endpoints, background tasks with progress pushed over WS. |
| **Config** | `config.py` | ✅ | `Settings` (pydantic-settings): ports, data dirs, Ollama, SheetSage2/YuE2 skill dirs & venvs, model IDs, timeouts. |
| **Audio engine** | `downloader.py` | 🟡 | Source resolution (`is_url`, `resolve_source`) + **yt-dlp** download. Stem separation (Demucs) & Basic Pitch transcription are planned (Phase 2). |
| **Notation engine** | `__init__.py` | 🟡 | Placeholder package for score analysis, arrangement execution, and MusicXML generation (planned). |
| **Skill compiler** | `compiler.py` | ✅ | Single-module pipeline: parse Markdown → prompt → local **Ollama/Qwen 2.5 Coder** → AST validation → sandbox test → save `.py` → dynamic class load. |
| **Orchestration** | *11 modules* | ✅ | Full SheetSage2 + YuE2 human-in-the-loop arrangement workflow (see below), covered by the test suite. |

> 🟡 = scaffold / partial. The classic `/api/transcribe`, `/api/analyze` and `/api/arrange`
> handlers currently emit **simulated progress** (placeholder MusicXML); the
> **orchestration** pipeline (`/api/orchestrate/*`) is the fully implemented path.

### Orchestration engine (v1.1)

`backend/orchestration/` implements the **Full Orchestration Workflow** (spec: [`maestropro/docs/version-1.1.md`](maestropro/docs/version-1.1.md)):

```text
[1] Insert song (upload audio / paste YouTube URL)
[2] Configure arrangement (genre, instruments, part count, key, tempo, style, lyrics)
[3] SheetSage2 transcribes → native 2-voice ABC lead sheet → multi-part MusicXML
[4] Human edits the score in MuseScore (HITL)
[5] YuE2 generates an audio mockup from the edited score (via native ABC export)
[6] Iterate (edit → preview → listen) until satisfied → export print-ready MusicXML
```

**Session state machine:**
`configured → transcribing → awaiting_edit → previewing → preview_ready → exported`, with `error` recovery and redo loops (re-transcribe / re-preview).

| Module | Responsibility |
| :--- | :--- |
| `models.py` | `OrchestrationStage`, `ArrangementConfig`, session & request/response models. |
| `instruments.py` | Instrument presets; role resolution (first part = melody, bass-name hints → bass). |
| `abc_bridge.py` | Dynamically loads `yue2-music/scripts/abc_tools.py`; parses native ABC → lead sheet (notes + chords); `strip_chords()`. |
| `chords.py` | music21 figures ↔ native ABC chord symbols and chord pitch sets. |
| `score_builder.py` | Lead sheet + config → multi-part music21 score (melody, chord symbols, realized harmony) → MusicXML. |
| `abc_export.py` | MusicXML → strict native 2-voice ABC for YuE2: unit quantization, chord-onset splits with ties, per-bar accidental replay validation. |
| `sheetsage2.py` | Subprocess adapter for `transcribe.py` (`score.abc` + manifest). |
| `yue2.py` | Subprocess adapter for `run_yue2.py` (request JSON + `--abc-file` → `run/audio.flac`). |
| `session.py` | Allowed-transitions state machine + atomic JSON session store. |
| `orchestrator.py` | `OrchestrationService`: create/get/list sessions, `run_transcribe`, `run_preview`, register edits, export, health. |

**Important notes:**
- SheetSage2 and YuE2 each run in their **own virtualenv** (`SHEETSAGE2_PYTHON`, `YUE2_PYTHON`). Unconfigured → endpoints return **HTTP 503** with setup guidance.
- The YuE2 preview is a **generative, score-conditioned mockup** — musically useful but *not* sample-accurate. Use MuseScore playback for exact rendering.

### API reference

Base URL: `http://localhost:8000`

| Method | Endpoint | Purpose |
| :--- | :--- | :--- |
| `POST` | `/api/transcribe` | Start audio → MusicXML transcription task *(simulated progress scaffold)*. |
| `POST` | `/api/analyze` | Analyze a score (key, tempo, chords, form) *(stub)*. |
| `POST` | `/api/skills/compile` | Compile a Markdown skill via Ollama. |
| `GET` | `/api/skills/list` | List available skills. |
| `DELETE` | `/api/skills/{name}` | Delete a skill. |
| `POST` | `/api/arrange` | Run arrangement on a score with a compiled skill *(simulated progress scaffold)*. |
| `GET` | `/api/health` | Backend + Ollama health. |
| `POST` | `/api/orchestrate/session` | Create an orchestration session (source + `ArrangementConfig`). |
| `POST` | `/api/orchestrate/transcribe` | Run SheetSage2 → MusicXML (background task + WS progress). |
| `POST` | `/api/orchestrate/preview` | Run ABC export → YuE2 audio mockup (background task + WS progress). |
| `GET` | `/api/orchestrate/session/{id}` | Get full session state. |
| `GET` | `/api/orchestrate/sessions` | List sessions. |
| `POST` | `/api/orchestrate/session/{id}/edit` | Register the user's edited MusicXML. |
| `POST` | `/api/orchestrate/session/{id}/export` | Export final print-ready MusicXML. |
| `GET` | `/api/orchestrate/health` | SheetSage2/YuE2 availability, skill dirs, venvs. |

### WebSocket protocol

URL: `ws://localhost:8765/ws/{client_id}` — JSON messages:

```jsonc
// backend → frontend
{ "type": "progress",  "task_id": "txn_...", "stage": "...", "percent": 45, "message": "..." }
{ "type": "complete",  "task_id": "txn_...", "file_path": ".../score.musicxml", "session_id": "..." }
{ "type": "error",     "task_id": "txn_...", "stage": "...", "message": "..." }
```

### Setup & run

**Requirements:** Python 3.10+ (tested on 3.13), FFmpeg on PATH, optional NVIDIA GPU (Demucs / YuE2), [Ollama](https://ollama.com) for the skill compiler, MuseScore 4 for the plugin UI.

```powershell
# 1. Backend
cd maestropro
python -m venv .venv
.\.venv\Scripts\activate          # Windows
pip install -r requirements.txt

# 2. Run API + WebSocket servers
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000

# 3. Tests
python -m pytest tests -q
```

**MuseScore plugin:** copy / point MuseScore at `maestropro/frontend/` (`manifest.json` + `maestropro.qml`).

**Orchestration (optional, v1.1):** provide two separate virtualenvs for the AI skills and point config at them:

```powershell
$env:MAESTROPRO_SHEETSAGE2_PYTHON = "C:\path\to\sheetsage2\.venv\Scripts\python.exe"
$env:MAESTROPRO_YUE2_PYTHON       = "C:\path\to\yue2\.venv\Scripts\python.exe"
```

Then check `GET /api/orchestrate/health`.

### Configuration

Key settings in `backend/config.py` (env prefix `MAESTROPRO_`):

| Setting | Default | Meaning |
| :--- | :--- | :--- |
| `WS_PORT` / `REST_PORT` | `8765` / `8000` | WebSocket / REST ports. |
| `OLLAMA_URL` | `http://localhost:11434` | Local LLM endpoint. |
| `SHEETSAGE2_SKILL_DIR` / `YUE2_SKILL_DIR` | `<repo>/yue2-music` | Skill checkout location. |
| `SHEETSAGE2_PYTHON` / `YUE2_PYTHON` | *(empty)* | Per-skill venv interpreters. |
| `SHEETSAGE2_MODEL` | `m-a-p/SheetSage2` | Transcription model. |
| `YUE2_MODEL` / `YUE2_VAE` | `m-a-p/YuE2-3B` / `m-a-p/YuE2-Vae` | Generation model + VAE. |
| `YUE2_SEED` | `831001` | Reproducible generation seed. |
| `SHEETSAGE2_TIMEOUT` / `YUE2_TIMEOUT` | `1800` / `3600` s | Subprocess timeouts. |
| `ORCHESTRATION_DIR` | `data/orchestration` | Session files (ABC, MusicXML, runs). |

### Tests

```powershell
cd maestropro
python -m pytest tests -q        # currently 37 tests
```

`tests/test_orchestration.py` covers: native ABC parsing & chord stripping, chord-symbol mapping, multi-part score construction, MusicXML round-trips, strict ABC export validation, session state-machine transitions, and adapter health/request building.

---

## yue2-music Skill (`yue2-music/`)

An agent skill (see [`SKILL.md`](yue2-music/SKILL.md)) for generating, covering, transcribing and editing songs with two models:

| Model | Role |
| :--- | :--- |
| **SheetSage2** (`m-a-p/SheetSage2`, MIT/UC Berkeley) | Audio → native 2-voice **ABC lead sheet** (melody + chords). |
| **YuE2** (`m-a-p/YuE2-3B` + `YuE2-Vae`, NetEase) | Style/lyrics (+ optional ABC plan) → song audio. `cot`: `full` (melody+chord ABC), `melody` (chord-free ABC), `off` (no ABC). |
| **MERT2** | Continuous feature analysis only (loaded by SheetSage2 itself; never fed to YuE2 as codec tokens). |

```text
yue2-music/
├── SKILL.md                 # Workflow selection table & rules
├── scripts/
│   ├── transcribe.py        # SheetSage2 CLI → score.abc + transcription_manifest.json
│   ├── run_yue2.py          # YuE2 CLI → run/audio.flac + run.json (generate/plan/decode/all-modes)
│   ├── abc_tools.py         # Strict native ABC parser/validator/stripper (shared contract)
│   ├── listen.py            # Listening comparison helper
│   └── common.py
├── references/              # models-and-setup.md, generation-and-covers.md, ...
├── assets/                  # prompt.json example
└── LICENSE                  # skill instructions CC BY-NC 4.0; weights keep their own licenses
```

**Native ABC contract** (enforced by `abc_tools.py`): `X:1`, blank `T:`, `M:`, `L:1/32`, `Q:1/4=int`, exactly two `V:` lines, `K:`; 1–4 measures per group with matching bar grids in both voices; durations from `{1,2,3,4,6,8,12,16,24,32,48}` units (1 quarter = 8); chords only on the Vocal voice.

**Runtime baseline:** one request at a time, BF16 NVIDIA GPU with ~24 GB VRAM, separate environments for SheetSage2 vs YuE2 (dependency pins differ).

---

## Music Theory Library (`music-theory-knsowledge/`)

Markdown knowledge base (**Perpustakaan Teori Musik MaestroPro**) combining academic music theory with concrete **MusicXML** implementation for arrangers, composers, and digital engravers (Dorico, Sibelius, Finale, MuseScore).

Five-level structure: **Tier** (S1/S2/S3 degree folder) → **Subject** → **Chapter** (`.md`) → **Section** (`##`) → **Sub-section / XML node** (`###` + `<tag>`).

```text
music-theory-knsowledge/
├── 01-Bachelor-S1-Fondasi/       # harmony, counterpoint, orchestration, genres
├── 02-Master-S2-Lanjutan/        # advanced topics
├── 03-Doctoral-S3-Riset/         # research-level
├── 04-MusicXML-Masterclass/      # deep MusicXML tagging
├── 05-Workflow-Portofolio/       # portfolio workflows
├── README.md · guide.md · sillaby.md · toc.md
```

Details: [`music-theory-knsowledge/README.md`](music-theory-knsowledge/README.md).

---

## Theory Webview (`music-theory-knsowledge-webview/`)

Minimal Node.js server that renders the knowledge base in the browser using **marked** (Markdown) and **OpenSheetMusicDisplay** (MusicXML score preview).

```powershell
cd music-theory-knsowledge-webview
npm install
npm start          # node server.mjs
```

---

## Documentation

| Document | Contents |
| :--- | :--- |
| [`maestropro/docs/architecture.md`](maestropro/docs/architecture.md) | **Master Architecture** (v2.1.0): 16 sections — branding, 3 architecture diagrams, tech stack, directory layout, core workflows (incl. orchestration workflow D), API contracts, Ollama specs, skill compiler, audio/notation engines, QML UI, deployment, roadmap, constraints, file-by-file Phase 1 spec, **§16 SheetSage2 & YuE2 integration**. *Note: its file-by-file spec describes the target layout; some listed files are still placeholders in code.* |
| [`maestropro/docs/version-1.1.md`](maestropro/docs/version-1.1.md) | v1.1 integration spec: where SheetSage2/YuE2 upgrade transcription, arrangement, style-learning, and the full HITL orchestration workflow + endpoints. |
| [`yue2-music/SKILL.md`](yue2-music/SKILL.md) | Skill workflows (generate / cover / edit / reharmonize) and model setup rules. |
| [`yue2-music/references/`](yue2-music/references) | Model downloads, revisions, generation & cover recipes. |

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| Frontend | QML (Qt 6) — MuseScore 4 plugin, JavaScript clients |
| Backend API | Python 3.10+ · FastAPI · `websockets` · pydantic-settings |
| Audio | yt-dlp (wired) · Demucs / Basic Pitch / librosa / pretty-midi *(planned)* |
| Notation / theory | music21 (analysis, arrangement, MusicXML I/O) |
| LLM (skills) | Ollama · `qwen2.5-coder:7b` (local, AST-validated codegen) |
| AI music models | SheetSage2 (transcription) · YuE2-3B + YuE2-Vae (generation) — via `yue2-music` skill, separate venvs |
| Knowledge viewer | Node.js · marked · OpenSheetMusicDisplay |
| Testing / QA | pytest · pytest-asyncio · black · flake8 |

---

*© 2026 Maya Instruments Technology. MIT License. MaestroPro — From Audio to Artistry* 🎼
