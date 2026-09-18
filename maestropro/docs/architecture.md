# MaestroPro Architecture Documentation

**Product:** MaestroPro  
**Company:** Maya Instruments Technology  
**Tagline:** "From Audio to Artistry"  
**Version:** 2.0.0  
**Status:** Ready for Implementation  

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [System Architecture](#2-system-architecture)
3. [Technology Stack](#3-technology-stack)
4. [Project Structure](#4-project-structure)
5. [Core Workflows](#5-core-workflows)
6. [API Specifications](#6-api-specifications)
7. [AI Core: Skill Compiler](#7-ai-core-skill-compiler)
8. [Audio Engine](#8-audio-engine)
9. [Notation Engine](#9-notation-engine)
10. [Frontend UI](#10-frontend-ui)
11. [Deployment Strategy](#11-deployment-strategy)

---

## 1. Executive Summary

### 1.1 Product Vision
MaestroPro is an end-to-end desktop application and MuseScore 4 plugin that bridges raw audio and professional music notation using local AI.

**Key Capabilities:**
- **Transcribe:** YouTube/MP3 → MusicXML notation
- **Analyze:** Auto-detect Key, Tempo, Chords, Form
- **Arrange:** AI-powered instrumentation from Markdown rules
- **Compile:** Convert music theory rules to executable Python

### 1.2 Brand Identity

| Element | Value |
|---------|-------|
| **Product** | MaestroPro |
| **Company** | Maya Instruments Technology |
| **Tagline** | "From Audio to Artistry" |
| **Primary Color** | Deep Blue `#1a3a52` |
| **Accent Color** | Gold `#d4af37` |

---

## 2. System Architecture

### 2.1 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND: MuseScore 4 Plugin              │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐    │
│  │  QML UI     │  │  WebSocket   │  │  REST API       │    │
│  │  (maestropro.qml) │  Client (JS) │  │  Client (JS)    │    │
│  └─────────────┘  └──────────────┘  └─────────────────┘    │
└─────────────────────────────────────────────────────────────┘
         │                        │
         │ WebSocket :8765        │ REST HTTP :8000
         ▼                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND: FastAPI Server                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Connection Manager │ Task Queue │ Event Bus         │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│  │  Audio      │  │  Notation    │  │  Skill          │   │
│  │  Engine     │  │  Engine      │  │  Compiler       │   │
│  └─────────────┘  └──────────────┘  └─────────────────┘   │
└─────────────────────────────────────────────────────────────┘
         │                        │
         ▼                        ▼
┌─────────────────┐      ┌───────────────────────────────────┐
│  Ollama Runtime │      │  Local Storage                    │
│  (Port 11434)   │      │  - Audio/MIDI Cache               │
│  qwen2.5-coder  │      │  - Compiled Skills (.py)          │
└─────────────────┘      │  - User Projects                  │
                         └───────────────────────────────────┘
```

### 2.2 Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| **QML UI** | User interface, progress visualization, user input |
| **WebSocket Client** | Real-time progress updates from backend |
| **REST API Client** | Task initiation, configuration requests |
| **FastAPI Server** | Request routing, task management, WebSocket broadcasting |
| **Audio Engine** | Download, separate stems, transcribe to MIDI, quantize |
| **Notation Engine** | Score analysis, arrangement execution, MusicXML generation |
| **Skill Compiler** | Parse Markdown, generate Python via Ollama, validate, load |
| **Ollama** | Local LLM runtime for code generation |

---

## 3. Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | QML (Qt 6) | Native MuseScore 4 plugin UI |
| **Frontend Logic** | JavaScript ES6 | WebSocket, API calls, state management |
| **Backend** | Python 3.10+ | Core runtime |
| **API Framework** | FastAPI + Uvicorn | REST + async support |
| **WebSocket** | `websockets` | Real-time progress streaming |
| **Audio Download** | `yt-dlp` | YouTube/audio extraction |
| **Source Separation** | `demucs` v4 | Isolate vocals, drums, bass, other |
| **Audio-to-MIDI** | `basic-pitch` | Polyphonic MIDI transcription |
| **Music Theory** | `music21` | Analysis, manipulation, MusicXML I/O |
| **AI Runtime** | `Ollama` | Local LLM execution |
| **AI Model** | `qwen2.5-coder:7b` | Markdown → Python code generation |
| **Validation** | Python `ast` | Syntax checking |
| **Packaging** | `PyInstaller` | Standalone executable |

---

## 4. Project Structure

```
maestropro/
├── README.md
├── MASTER_ARCHITECTURE.md
├── requirements.txt
├── .gitignore
│
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── config.py               # Global settings
│   ├── audio_engine/
│   │   ├── __init__.py
│   │   ├── downloader.py       # yt-dlp wrapper
│   │   ├── separator.py        # Demucs integration
│   │   └── transcriber.py      # Basic Pitch + quantization
│   ├── notation_engine/
│   │   ├── __init__.py
│   │   ├── analyzer.py         # Key, tempo, chord detection
│   │   ├── arranger.py         # Apply compiled skills
│   │   └── xml_generator.py    # MusicXML assembly
│   └── skill_compiler/
│       ├── __init__.py
│       ├── compiler.py         # Main compilation pipeline
│       ├── parser.py           # Markdown parsing
│       ├── validator.py        # AST validation
│       └── loader.py           # Dynamic module loading
│
├── frontend/
│   └── maestropro/
│       ├── main.qml            # Main dashboard
│       ├── manifest.json       # Plugin metadata
│       ├── js/
│       │   ├── websocket_client.js
│       │   ├── api_client.js
│       │   └── score_controller.js
│       └── assets/
│           ├── logo.png
│           └── theme.qml
│
├── data/                       # Runtime data (gitignored)
│   ├── cache/
│   ├── projects/
│   └── skills/
│       ├── markdown/
│       ├── compiled/
│       └── metadata.json
│
├── docs/
│   ├── USER_GUIDE.md
│   ├── DEVELOPER_GUIDE.md
│   └── MARKDOWN_SYNTAX.md
│
├── tests/
│   ├── test_downloader.py
│   ├── test_transcriber.py
│   ├── test_analyzer.py
│   └── test_compiler.py
│
└── installer/
    ├── build_windows.spec
    └── setup_ollama.ps1
```

---

## 5. Core Workflows

### 5.1 Transcription Workflow (Audio → MusicXML)

```
User Input (YouTube URL / MP3)
    ↓
[1] yt-dlp downloads → 16-bit 44.1kHz WAV
    ↓
[2] Demucs separates into 4 stems:
    - vocals.wav (ignored)
    - drums.wav (optional)
    - bass.wav → transcribe
    - other.wav → transcribe
    ↓
[3] Basic Pitch transcribes → MIDI files
    ↓
[4] Quantizer snaps to 1/16 grid, removes ghost notes
    ↓
[5] music21 generates .musicxml
    ↓
[6] WebSocket event → QML → MuseScore opens score
```

### 5.2 Skill Compilation Workflow (Markdown → Python)

```
User writes jazz_ballad.md
    ↓
Click "Compile" in SkillManager UI
    ↓
POST /api/skills/compile with markdown
    ↓
Backend parses markdown → structured rules
    ↓
Build system prompt + rules → Ollama API
    ↓
Qwen 2.5 Coder generates Python class
    ↓
AST syntax validation
    ↓
Import allowlist validation
    ↓
Save to data/skills/compiled/jazz_ballad.py
    ↓
Update metadata.json
    ↓
UI shows "✓ Compilation Successful"
```

### 5.3 Arrangement Workflow

```
User opens transcribed score
    ↓
Click "Add Arrangement"
    ↓
Select style + instruments → POST /api/arrange
    ↓
Backend analyzes score (key, chords, form)
    ↓
Dynamically load compiled skill class
    ↓
Execute arrangement rules (harmonize, voice_lead)
    ↓
Create new music21.Part objects
    ↓
Merge with original score → export .musicxml
    ↓
WebSocket event → MuseScore opens arranged score
```

---

## 6. API Specifications

### 6.1 WebSocket Protocol (Port 8765)

**Endpoint:** `ws://localhost:8765/ws/{client_id}`

**Client → Backend (Commands):**
```json
{
  "type": "command",
  "action": "transcribe",
  "payload": {
    "url": "https://youtube.com/watch?v=...",
    "options": {"separate_stems": true, "quantize": "1/16"}
  }
}
```

**Backend → Client (Progress):**
```json
{
  "type": "progress",
  "task_id": "txn_abc123",
  "stage": "source_separation",
  "percent": 45,
  "message": "Isolating instruments using Demucs..."
}
```

**Backend → Client (Complete):**
```json
{
  "type": "complete",
  "task_id": "txn_abc123",
  "file_path": "C:/MaestroPro/data/projects/song1/score.musicxml"
}
```

### 6.2 REST API Endpoints (Port 8000)

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `GET` | `/api/health` | - | `{status, app, version, ollama, model}` |
| `POST` | `/api/transcribe` | `{url, options}` | `{task_id, status}` |
| `POST` | `/api/analyze` | `{file_path}` | `{key, tempo, chords, form}` |
| `POST` | `/api/skills/compile` | `{name, markdown}` | `{status, file, class_name}` |
| `GET` | `/api/skills/list` | - | `{skills: [...]}` |
| `DELETE` | `/api/skills/{name}` | - | `{status, skill_name}` |
| `POST` | `/api/arrange` | `{file_path, style, instruments}` | `{task_id, status}` |

---

## 7. AI Core: Skill Compiler

### 7.1 Model Configuration

```yaml
Runtime: Ollama
Model: qwen2.5-coder:7b
Quantization: Q4_K_M (~4.5 GB)
RAM Required: 8 GB minimum, 16 GB recommended
Endpoint: http://localhost:11434/api/generate
Temperature: 0.2
Top P: 0.9
Context: 4096 tokens
```

### 7.2 System Prompt

The compiler sends this system prompt with every request:

```
You are the core AI engine of MaestroPro by Maya Instruments Technology.
Your task is to convert Markdown music theory rules into a valid, executable
Python class using the 'music21' library.

STRICT RULES:
1. Output ONLY valid Python code. No markdown formatting, no explanations.
2. Class name must be PascalCase matching the style name.
3. Always include: from music21 import stream, note, chord, interval, key, meter, pitch
4. Class must include: __init__, harmonize, voice_lead, validate_range methods.
5. Use try-except blocks around ALL music21 operations.
6. Implement ALL rules from the Markdown. No placeholders.
7. Respect physical instrument ranges (Violin: G3-E7, Viola: C3-A6, etc.)
8. Return only the class definition. No test code, no example usage.
```

### 7.3 Validation Pipeline

1. **Syntax Check:** `ast.parse()` validates Python syntax
2. **Import Check:** Ensure only allowed modules (`music21`, `typing`, `math`, `random`)
3. **Sandbox Test:** Execute on 2-bar sample (Phase 3)
4. **Save & Load:** Dynamic import via `importlib.util`

---

## 8. Audio Engine

### 8.1 Components

| Module | Function |
|--------|----------|
| `downloader.py` | yt-dlp wrapper, downloads as 16-bit 44.1kHz WAV |
| `separator.py` | Demucs v4 source separation (vocals, drums, bass, other) |
| `transcriber.py` | Basic Pitch MIDI transcription + quantization |

### 8.2 Processing Pipeline

```python
# Pseudocode
wav_path = download_audio(youtube_url)
stems = separate_stems(wav_path, model="htdemucs_ft")
midi_bass = transcribe_to_midi(stems["bass.wav"])
midi_other = transcribe_to_midi(stems["other.wav"])
quantized = quantize_midi(midi_bass, grid="1/16")
musicxml = midi_to_musicxml(quantized)
```

---

## 9. Notation Engine

### 9.1 Components

| Module | Function |
|--------|----------|
| `analyzer.py` | Detect key, tempo, time signature, Roman numeral chords |
| `arranger.py` | Execute compiled skill rules on score |
| `xml_generator.py` | Merge parts, export final MusicXML |

### 9.2 Analysis Output Example

```json
{
  "key": "G major",
  "tempo": 120,
  "time_signature": "4/4",
  "chord_progression": ["I", "V", "vi", "IV"],
  "form": ["Verse", "Chorus", "Verse", "Chorus"],
  "duration_quarter_length": 64.0
}
```

---

## 10. Frontend UI

### 10.1 Theme Constants

```qml
// theme.qml
readonly property color primary: "#1a3a52"      // Deep Blue
readonly property color accent: "#d4af37"       // Gold
readonly property color bgDark: "#0d1b2a"
readonly property color bgCard: "#1b2838"
readonly property color textPrimary: "#ffffff"
readonly property color textSecondary: "#a0aec0"
readonly property color success: "#48bb78"
readonly property color error: "#fc8181"
```

### 10.2 Main Sections

1. **Header:** Logo, product name, company, connection status
2. **Transcribe:** YouTube URL input, stem separation options, progress bar
3. **Analyze:** Key/tempo/form display, analyze button
4. **Arrange:** Style selector, instrument checkboxes, arrange button
5. **Skill Manager:** New/Edit/Compile/Delete buttons, skills list

---

## 11. Deployment Strategy

### 11.1 Installer Contents

```
MaestroPro-Setup-v1.0.0.exe
├── Bundled Ollama Runtime (~100MB)
├── Pre-downloaded Qwen 2.5 Coder 7B model (~4.5GB)
├── maestropro-backend.exe (PyInstaller bundle)
├── MuseScore Plugin folder (QML files)
└── Auto-setup scripts
```

### 11.2 Installation Flow

1. Run MaestroPro-Setup.exe
2. Detect MuseScore 4 installation
3. Copy QML plugin to `Documents/MuseScore4/Plugins/maestropro/`
4. Install Ollama silently
5. Start Ollama service
6. Copy pre-bundled model to Ollama models directory
7. Create Start Menu shortcut for MaestroPro Backend
8. Backend starts in system tray (ports 8000, 8765)
9. User opens MuseScore → MaestroPro appears in Plugins menu

### 11.3 Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 8 GB | 16 GB |
| **Storage** | 10 GB free | 20 GB free |
| **CPU** | 4 cores | 8 cores |
| **OS** | Windows 10, macOS 12+, Linux | Windows 11, macOS 14+, Linux |

---

## Appendix A: Development Roadmap

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| **Phase 1: Foundation** | Week 1-2 | Repo setup, WebSocket bridge, QML skeleton, FastAPI server |
| **Phase 2: Transcription MVP** | Week 3-5 | Full audio pipeline: YouTube → Demucs → Basic Pitch → MusicXML |
| **Phase 3: AI Skill Compiler** | Week 6-8 | Markdown parser, Ollama client, validator, loader, SkillManager UI |
| **Phase 4: Arrangement Engine** | Week 9-11 | Score analyzer, arranger, 3-5 built-in styles, ArrangementDialog |
| **Phase 5: Polish & Package** | Week 12-14 | UI theming, error handling, PyInstaller, Ollama auto-setup, docs |

---

## Appendix B: Constraints & Edge Cases

| # | Issue | Mitigation |
|---|-------|------------|
| 1 | AI hallucinates invalid Python | Mandatory `ast.parse()` + sandbox test |
| 2 | RAM < 8GB | Auto-detect, downgrade to `qwen2.5-coder:1.5b` |
| 3 | Complex polyphony errors | Provide "Quantize & Clean" tool, document expectations |
| 4 | MuseScore API slow | Bypass: Python generates final `.musicxml`, MuseScore just opens |
| 5 | Ollama not running | `/api/health` checks status, UI shows warning |
| 6 | YouTube download fails | Error handling, support local MP3 fallback |
| 7 | Dangerous imports | Validator checks against allowlist |
| 8 | Large audio files (>30 min) | Chunk processing, progress per chunk |
| 9 | Port conflicts | Config allows custom ports, auto-detect available |
| 10 | Ambiguous Markdown | System prompt instructs closest `music21` equivalent + comment |

---

*© 2026 Maya Instruments Technology. All rights reserved.*  
*MaestroPro — From Audio to Artistry* 🎼✨
