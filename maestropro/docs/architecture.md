# MaestroPro Architecture Documentation

## Overview

**MaestroPro** is a revolutionary music software product by **Maya Instruments Technology** that transforms audio into professional music notation using AI-powered analysis and arrangement.

**Tagline:** "From Audio to Artistry"

---

## System Architecture

### Hybrid Architecture Design

MaestroPro uses a hybrid architecture combining:
- **Frontend:** MuseScore 4 QML Plugin (Qt 6 / QtQuick)
- **Backend:** Python 3.10+ FastAPI server
- **AI Core:** Local Ollama instance with Qwen 2.5 Coder

```
┌─────────────────────────────────────────────────────────────┐
│                     MuseScore 4 Host                        │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Frontend (QML Plugin)                   │    │
│  │  - UI Components                                     │    │
│  │  - WebSocket Client (Port 8765)                      │    │
│  │  - REST API Client (Port 8000)                       │    │
│  └───────────────────┬─────────────────────────────────┘    │
└──────────────────────┼──────────────────────────────────────┘
                       │ HTTP/WebSocket
┌──────────────────────▼──────────────────────────────────────┐
│                  Backend Server (Python)                     │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              FastAPI Application                     │    │
│  │  - REST Endpoints                                    │    │
│  │  - WebSocket Manager                                 │    │
│  └──────┬─────────────────────────────────┬────────────┘    │
│         │                                │                  │
│  ┌──────▼────────┐              ┌────────▼────────┐        │
│  │ Audio Engine  │              │ Notation Engine │        │
│  │ - yt-dlp      │              │ - music21       │        │
│  │ - demucs      │              │ - Analysis      │        │
│  │ - basic-pitch │              │ - MusicXML      │        │
│  └───────────────┘              └─────────────────┘        │
│                                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │            Skill Compiler (AI Core)                  │   │
│  │  - Ollama API Client                                 │   │
│  │  - Qwen 2.5 Coder                                    │   │
│  │  - Dynamic Code Generation                           │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                    External Services                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐     │
│  │   YouTube   │  │   Ollama    │  │   Local File    │     │
│  │   (Audio)   │  │ (LLM Host)  │  │    System       │     │
│  └─────────────┘  └─────────────┘  └─────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Details

### 1. Frontend (QML Plugin)

**Location:** `/frontend/`

**Technologies:**
- Qt Quick 2.15
- Qt Quick Controls 2.15
- MuseScore 4 Plugin API

**Key Files:**
- `maestropro.qml` - Main UI interface
- `manifest.json` - Plugin metadata and configuration

**Features:**
- Dark mode professional UI
- YouTube URL input
- Stem separation toggle
- Output format selection
- Real-time progress updates via WebSocket
- Transcription and analysis controls

**Color Scheme:**
- Primary: Deep Blue (#1a3a52)
- Accent: Gold (#d4af37)
- Background: Dark (#2b2b2b)

---

### 2. Backend (FastAPI Server)

**Location:** `/backend/`

**Technologies:**
- FastAPI 0.109.0
- Uvicorn (ASGI server)
- WebSockets for real-time communication
- Pydantic for data validation

#### 2.1 Main Application (`main.py`)

**REST API Endpoints:**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/transcribe` | POST | Initiate audio transcription |
| `/api/analyze` | POST | Analyze MusicXML score |
| `/api/compile-skill` | POST | Compile Markdown rules to Python |
| `/api/status/{task_id}` | GET | Get task status |
| `/ws/{client_id}` | WebSocket | Real-time progress updates |

**Request/Response Models:**
- `TranscribeRequest` - URL, output format, stem separation flag
- `AnalysisRequest` - Score file path
- `SkillCompileRequest` - Markdown rules, rule name
- `StatusResponse` - Status, message, progress, data

#### 2.2 Configuration (`config.py`)

Environment-based configuration using Pydantic Settings:
- Server ports (REST: 8000, WebSocket: 8765)
- Ollama settings (host, port, model)
- Directory paths (downloads, output, temp)
- Audio engine preferences

---

### 3. Audio Engine

**Location:** `/backend/audio_engine/`

**Pipeline:**

```
YouTube URL/MP3
      │
      ▼
┌─────────────┐
│  yt-dlp     │ Download audio from YouTube
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Demucs    │ Source separation (Vocals, Drums, Bass, Other)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ basic-pitch │ Audio-to-MIDI transcription
│  or         │
│  omnizart   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  music21    │ MIDI to MusicXML conversion
└──────┬──────┘
       │
       ▼
  MusicXML File
```

**Modules (to be implemented):**
- `downloader.py` - yt-dlp wrapper for audio download
- `separator.py` - Demucs integration for stem separation
- `transcriber.py` - Audio-to-MIDI conversion

---

### 4. Notation Engine

**Location:** `/backend/notation_engine/`

**Technologies:**
- music21 9.1.0

**Features:**
- Key signature detection
- Time signature analysis
- Tempo estimation
- Roman numeral chord progression analysis
- Musical form identification
- MusicXML generation and manipulation

**Modules (to be implemented):**
- `analyzer.py` - Musical structure analysis
- `converter.py` - MIDI to MusicXML conversion
- `generator.py` - MusicXML output

---

### 5. Skill Compiler (AI Core)

**Location:** `/backend/skill_compiler/`

**Architecture:**

```
Markdown Rules
      │
      ▼
┌─────────────────┐
│  SkillCompiler  │ Prepare prompt with system instructions
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Ollama API    │ POST /api/generate with Qwen 2.5 Coder
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Code Parser    │ Extract Python code from response
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Code Saver     │ Save to ./compiled_rules/
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Dynamic Loader  │ importlib to load module
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ArrangementRule │ Instantiate and apply to score
└─────────────────┘
```

**Process:**
1. User writes music theory rules in Markdown
2. SkillCompiler sends rules to Ollama with system prompt
3. Qwen 2.5 Coder generates Python class using music21
4. Code is extracted, saved, and dynamically loaded
5. Generated `ArrangementRule` class is applied to scores

**Example Markdown Input:**
```markdown
# Jazz Ballad Arrangement Rules

- Convert all quarter notes to swung eighth notes
- Add walking bass line in left hand
- Voicing: 7th chords with 9th extensions
- Tempo: 70-90 BPM
- Style: Ballad with rubato introduction
```

**Generated Python Class:**
```python
from music21 import stream, note, chord, key, tempo

class ArrangementRule:
    """Implements Jazz Ballad arrangement rules."""
    
    def __init__(self):
        self.rule_name = "Jazz Ballad"
    
    def apply(self, score: stream.Stream) -> stream.Stream:
        """Apply jazz ballad transformations to the score."""
        # Implementation generated by Qwen 2.5 Coder
        return score
```

---

## Communication Flow

### Transcription Workflow

```
User (QML)                Backend (FastAPI)              Audio Engine
    │                          │                              │
    │──POST /api/transcribe──▶│                              │
    │   {url, format, stems}  │                              │
    │                          │──Start Task────────────────▶│
    │◀─{task_id, status}──────│                              │
    │                          │                              │
    │◀─WebSocket Progress─────│                              │
    │   {progress: 0.3,       │                              │
    │    message: "Downloading"}                              │
    │                          │                              │
    │◀─WebSocket Progress─────│                              │
    │   {progress: 0.7,       │                              │
    │    message: "Transcribing"}                             │
    │                          │                              │
    │◀─{status: "complete",   │                              │
    │    data: {xml_path}}───│                              │
    │                          │                              │
```

### Skill Compilation Workflow

```
User (QML)                Backend (FastAPI)           Skill Compiler
    │                          │                            │
    │──POST /api/compile─────▶│                            │
    │   {markdown, name}      │                            │
    │                          │──compile_rules()─────────▶│
    │                          │                            │
    │                          │                     ┌──────┴──────┐
    │                          │                     │   Ollama    │
    │                          │◀────────────────────│   Qwen 2.5  │
    │                          │    Python Code      └─────────────┘
    │                          │                            │
    │                          │──save_rule()──────────────▶│
    │                          │──load_rule()──────────────▶│
    │◀─{status, rule_class}───│                            │
    │                          │                            │
```

---

## Directory Structure

```
/maestropro
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── config.py               # Global configurations
│   ├── audio_engine/           # Audio processing modules
│   │   ├── __init__.py
│   │   ├── downloader.py       # yt-dlp wrapper
│   │   ├── separator.py        # Demucs integration
│   │   └── transcriber.py      # Audio-to-MIDI
│   ├── notation_engine/        # Music notation modules
│   │   ├── __init__.py
│   │   ├── analyzer.py         # Music theory analysis
│   │   ├── converter.py        # MIDI to MusicXML
│   │   └── generator.py        # MusicXML output
│   └── skill_compiler/         # AI rule compilation
│       ├── __init__.py
│       └── compiler.py         # Ollama integration
├── frontend/
│   ├── maestropro.qml          # Main UI interface
│   └── manifest.json           # Plugin metadata
├── docs/
│   └── architecture.md         # This file
└── requirements.txt            # Python dependencies
```

---

## Security Considerations

1. **Local Processing:** All AI inference runs locally via Ollama - no data sent to external servers
2. **CORS Configuration:** Configurable CORS policies for production deployment
3. **Input Validation:** Pydantic models validate all API inputs
4. **File Access:** Controlled access to download/output directories

---

## Performance Optimization

1. **Async Operations:** All I/O operations use async/await
2. **WebSocket Efficiency:** Single persistent connection for real-time updates
3. **Model Caching:** Ollama keeps models loaded in memory
4. **Parallel Processing:** Stem separation can process multiple tracks simultaneously

---

## Future Enhancements

1. **Batch Processing:** Queue system for multiple transcription tasks
2. **Plugin Marketplace:** User-contributed arrangement rules
3. **Cloud Sync:** Optional cloud backup for arrangements
4. **Mobile App:** Companion app for on-the-go transcription
5. **Real-time Transcription:** Live audio input support

---

## Version Information

- **Product:** MaestroPro
- **Version:** 1.0.0
- **Company:** Maya Instruments Technology
- **License:** MIT
- **Minimum MuseScore Version:** 4.0.0

---

*Documentation generated for MaestroPro v1.0.0*
*"From Audio to Artistry"*
