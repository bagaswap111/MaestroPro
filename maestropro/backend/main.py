"""
MaestroPro - FastAPI Backend Entry Point
Maya Instruments Technology
Version: 1.0.0

Main application server with REST API and WebSocket support.
Handles transcription, analysis, arrangement, and skill compilation.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
import asyncio
import json
import uuid
from pathlib import Path
import logging

from backend.config import settings
from backend.skill_compiler.compiler import SkillCompiler
from backend.orchestration import (
    CreateSessionRequest,
    EditRegisteredRequest,
    OrchestratePreviewRequest,
    OrchestrateTranscribeRequest,
    OrchestrationService,
    OrchestrationStage,
    SessionError,
)
from backend.orchestration.models import (
    OrchestrateHealthComponent,
    OrchestrateHealthResponse,
    SessionListResponse,
)

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ==================== Pydantic Models ====================

class TranscribeRequest(BaseModel):
    """Request model for transcription endpoint."""
    url: str = Field(..., description="YouTube URL or file path")
    options: Optional[Dict[str, Any]] = Field(
        default_factory=lambda: {"separate_stems": True, "quantize": "1/16"}
    )


class AnalyzeRequest(BaseModel):
    """Request model for analysis endpoint."""
    file_path: str = Field(..., description="Path to MusicXML file")


class CompileSkillRequest(BaseModel):
    """Request model for skill compilation endpoint."""
    name: str = Field(..., description="Name of the skill/style")
    markdown: str = Field(..., description="Markdown content with music theory rules")


class ArrangeRequest(BaseModel):
    """Request model for arrangement endpoint."""
    file_path: str = Field(..., description="Path to source MusicXML file")
    style: str = Field(..., description="Name of compiled skill/style to use")
    instruments: Optional[List[str]] = Field(default=None)


class TaskResponse(BaseModel):
    """Response model for task initiation endpoints."""
    task_id: str
    status: str = "queued"
    session_id: Optional[str] = None


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""
    status: str
    app: str
    version: str
    ollama: bool = False
    model: Optional[str] = None


class SkillListResponse(BaseModel):
    """Response model for skill list endpoint."""
    skills: List[Dict[str, Any]]


# ==================== Connection Manager ====================

class ConnectionManager:
    """Manages WebSocket connections for real-time progress updates."""
    
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
    
    async def connect(self, websocket: WebSocket, client_id: str):
        """Accept and register a new WebSocket connection."""
        await websocket.accept()
        self.active_connections[client_id] = websocket
        logger.info(f"Client {client_id} connected")
    
    def disconnect(self, client_id: str):
        """Remove a WebSocket connection."""
        if client_id in self.active_connections:
            del self.active_connections[client_id]
            logger.info(f"Client {client_id} disconnected")
    
    async def send_personal_message(self, message: dict, client_id: str):
        """Send a JSON message to a specific client."""
        if client_id in self.active_connections:
            try:
                await self.active_connections[client_id].send_json(message)
            except Exception as e:
                logger.error(f"Error sending message to {client_id}: {e}")
                self.disconnect(client_id)
    
    async def broadcast(self, message: dict):
        """Broadcast a message to all connected clients."""
        for client_id in list(self.active_connections.keys()):
            await self.send_personal_message(message, client_id)


# Global connection manager instance
manager = ConnectionManager()

# Global skill compiler instance
skill_compiler = SkillCompiler()

# Full Orchestration Workflow service (SheetSage2 + YuE2 + Human-in-the-Loop)
orchestration_service = OrchestrationService(settings)

# Task storage (in production, use Redis or database)
active_tasks: Dict[str, dict] = {}


# ==================== Lifespan Context ====================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup/shutdown events."""
    # Startup
    logger.info(f"🎼 {settings.APP_NAME} v{settings.VERSION} Backend Starting...")
    logger.info(f"Company: {settings.COMPANY}")
    logger.info(f"Tagline: {settings.TAGLINE}")
    logger.info(f"REST API: http://{settings.HOST}:{settings.REST_PORT}")
    logger.info(f"WebSocket: ws://{settings.HOST}:{settings.WS_PORT}")
    logger.info(f"Ollama URL: {settings.OLLAMA_URL}")
    logger.info(f"Default Model: {settings.DEFAULT_MODEL}")
    logger.info(f"Orchestration dir: {settings.ORCHESTRATION_DIR}")
    sheet_health = orchestration_service.sheetsage2.health()
    yue_health = orchestration_service.yue2.health()
    logger.info(
        f"SheetSage2: {'available' if sheet_health['available'] else 'unavailable'}"
        f" ({sheet_health['detail'] or sheet_health['script']})"
    )
    logger.info(
        f"YuE2: {'available' if yue_health['available'] else 'unavailable'}"
        f" ({yue_health['detail'] or yue_health['script']})"
    )
    
    # Check Ollama connectivity
    try:
        import httpx
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.OLLAMA_URL}/api/tags", timeout=5.0)
            if response.status_code == 200:
                logger.info("✅ Ollama connection successful")
            else:
                logger.warning("⚠️ Ollama responded with non-200 status")
    except Exception as e:
        logger.warning(f"⚠️ Could not connect to Ollama: {e}")
        logger.warning("AI features will be unavailable until Ollama is running")
    
    yield
    
    # Shutdown
    logger.info(f"🎼 {settings.APP_NAME} Backend Shutting Down...")
    # Cleanup active connections
    for client_id in list(manager.active_connections.keys()):
        manager.disconnect(client_id)


# ==================== FastAPI Application ====================

app = FastAPI(
    title=settings.APP_NAME,
    description=f"AI-Powered Music Transcription & Arrangement by {settings.COMPANY}",
    version=settings.VERSION,
    lifespan=lifespan
)

# CORS middleware for QML frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to MuseScore plugin origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================== WebSocket Endpoint ====================

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """
    WebSocket endpoint for real-time progress updates.
    Client ID should be unique per session.
    """
    await manager.connect(websocket, client_id)
    try:
        while True:
            # Receive messages from client (commands, config requests)
            data = await websocket.receive_text()
            message = json.loads(data)
            
            logger.debug(f"Received from {client_id}: {message.get('type')}")
            
            # Route messages based on type
            msg_type = message.get("type", "unknown")
            
            if msg_type == "command":
                action = message.get("action")
                payload = message.get("payload", {})
                
                # Echo acknowledgment (actual processing via REST API)
                await manager.send_personal_message({
                    "type": "acknowledgment",
                    "action": action,
                    "message": f"Command received: {action}"
                }, client_id)
            
            elif msg_type == "ping":
                await manager.send_personal_message({
                    "type": "pong",
                    "timestamp": asyncio.get_event_loop().time()
                }, client_id)
    
    except WebSocketDisconnect:
        manager.disconnect(client_id)
    except Exception as e:
        logger.error(f"WebSocket error for {client_id}: {e}")
        manager.disconnect(client_id)


# ==================== REST API Endpoints ====================

@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.
    Returns app status and Ollama connectivity.
    """
    ollama_available = False
    current_model = None
    
    try:
        import httpx
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.OLLAMA_URL}/api/tags", timeout=5.0)
            if response.status_code == 200:
                ollama_available = True
                data = response.json()
                models = data.get("models", [])
                for model in models:
                    if settings.DEFAULT_MODEL in model.get("name", ""):
                        current_model = model.get("name")
                        break
                if not current_model and models:
                    current_model = models[0].get("name")
    except Exception:
        pass
    
    return HealthResponse(
        status="ok",
        app=settings.APP_NAME,
        version=settings.VERSION,
        ollama=ollama_available,
        model=current_model
    )


@app.post("/api/transcribe", response_model=TaskResponse)
async def transcribe_audio(request: TranscribeRequest, background_tasks: BackgroundTasks):
    """
    Initiate audio transcription from YouTube URL or local file.
    Returns task_id for tracking progress via WebSocket.
    """
    task_id = f"txn_{uuid.uuid4().hex[:8]}"
    
    # Store task info
    active_tasks[task_id] = {
        "type": "transcribe",
        "status": "queued",
        "url": request.url,
        "options": request.options,
        "progress": 0
    }
    
    # Queue background task (placeholder - implement full pipeline in Phase 2)
    background_tasks.add_task(process_transcription, task_id, request)
    
    logger.info(f"Transcription task {task_id} queued for URL: {request.url}")
    
    return TaskResponse(task_id=task_id, status="queued")


@app.post("/api/analyze", response_model=dict)
async def analyze_score(request: AnalyzeRequest):
    """
    Analyze a MusicXML score for musical structure.
    Returns key, tempo, time signature, chord progression, and form.
    """
    file_path = Path(request.file_path)
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {file_path}")
    
    # Placeholder - implement full analysis in Phase 4
    # from backend.notation_engine.analyzer import analyze_score
    # result = analyze_score(str(file_path))
    
    result = {
        "key": "G major",
        "tempo": 120,
        "time_signature": "4/4",
        "chord_progression": ["I", "V", "vi", "IV"],
        "form": ["Verse", "Chorus", "Verse", "Chorus"],
        "duration_quarter_length": 64.0,
        "file_path": str(file_path)
    }
    
    logger.info(f"Analysis complete for {file_path.name}")
    
    return result


@app.post("/api/skills/compile", response_model=dict)
async def compile_skill(request: CompileSkillRequest):
    """
    Compile Markdown music theory rules into executable Python code.
    Uses Ollama with Qwen 2.5 Coder model.
    """
    try:
        logger.info(f"Compiling skill: {request.name}")
        
        # Use skill compiler to process markdown
        result = await skill_compiler.compile_and_load(
            name=request.name,
            markdown_content=request.markdown
        )
        
        if result["success"]:
            logger.info(f"Skill compilation successful: {request.name}")
            return {
                "status": "success",
                "file": result["file_path"],
                "class_name": result["class_name"],
                "message": "Compilation successful ✓"
            }
        else:
            logger.error(f"Skill compilation failed: {result.get('error')}")
            raise HTTPException(
                status_code=400,
                detail={
                    "status": "error",
                    "message": result.get("error", "Unknown compilation error")
                }
            )
    
    except Exception as e:
        logger.error(f"Compilation error: {e}")
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "message": str(e)
            }
        )


@app.get("/api/skills/list", response_model=SkillListResponse)
async def list_skills():
    """
    List all available compiled skills/styles.
    Returns metadata including instruments and compilation status.
    """
    skills = []
    
    try:
        metadata_file = settings.metadata_file
        if metadata_file.exists():
            import json
            with open(metadata_file, 'r') as f:
                data = json.load(f)
                skills = data.get("skills", [])
    except Exception as e:
        logger.error(f"Error loading skills metadata: {e}")
    
    return SkillListResponse(skills=skills)


@app.delete("/api/skills/{skill_name}", response_model=dict)
async def delete_skill(skill_name: str):
    """
    Delete a compiled skill by name.
    Removes both .py file and metadata entry.
    """
    try:
        skill_file = settings.SKILLS_PY_DIR / f"{skill_name}.py"
        
        if skill_file.exists():
            skill_file.unlink()
            logger.info(f"Deleted skill file: {skill_file}")
        
        # Remove from metadata
        # (Implement metadata update logic)
        
        return {"status": "deleted", "skill_name": skill_name}
    
    except Exception as e:
        logger.error(f"Error deleting skill: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/arrange", response_model=TaskResponse)
async def arrange_score(request: ArrangeRequest, background_tasks: BackgroundTasks):
    """
    Apply a compiled skill/style to arrange a score.
    Adds new instrument parts based on music theory rules.
    """
    task_id = f"arr_{uuid.uuid4().hex[:8]}"
    
    # Store task info
    active_tasks[task_id] = {
        "type": "arrange",
        "status": "queued",
        "file_path": request.file_path,
        "style": request.style,
        "instruments": request.instruments,
        "progress": 0
    }
    
    # Queue background task (placeholder - implement in Phase 4)
    background_tasks.add_task(process_arrangement, task_id, request)
    
    logger.info(f"Arrangement task {task_id} queued: {request.style}")
    
    return TaskResponse(task_id=task_id, status="queued")


# ==================== Full Orchestration Workflow ====================
# SheetSage2 + YuE2 + Human-in-the-Loop (see docs/architecture.md §16)

def orchestration_progress(task_id: str):
    """Build an async progress callback that mirrors the WebSocket protocol."""

    async def _progress(stage: str, percent: int, message: str) -> None:
        if task_id in active_tasks:
            active_tasks[task_id]["status"] = stage
            active_tasks[task_id]["progress"] = percent
        await manager.send_personal_message({
            "type": "progress",
            "task_id": task_id,
            "stage": stage,
            "percent": percent,
            "message": message,
        }, task_id)

    return _progress


@app.post("/api/orchestrate/session")
async def create_orchestrate_session(request: CreateSessionRequest):
    """
    Step [1]+[2]: create a human-in-the-loop orchestration session.
    Registers the audio source and arrangement configuration.
    """
    session = orchestration_service.create_session(request.source, request.config)
    logger.info(
        f"Orchestration session {session.session_id} created: "
        f"{session.config.genre} [{', '.join(session.config.instruments)}]"
    )
    return session


@app.post("/api/orchestrate/transcribe", response_model=TaskResponse)
async def orchestrate_transcribe(
    request: OrchestrateTranscribeRequest,
    background_tasks: BackgroundTasks,
):
    """
    Step [3]: SheetSage2 transcribes the source → lead sheet is split into
    per-instrument parts → multi-part MusicXML for editing in MuseScore.

    Provide either `session_id`, or `source` + `config` to auto-create one.
    Progress streams over WebSocket as task_id events.
    """
    # Resolve or create the session
    if request.session_id:
        try:
            session = orchestration_service.get_session(request.session_id)
        except SessionError as exc:
            raise HTTPException(status_code=404, detail=str(exc))
        if request.source:
            session.source = request.source
        if request.config:
            session.config = request.config
            session.stage = OrchestrationStage.CONFIGURED
        orchestration_service.sessions.save(session)
    else:
        if not request.source or not request.config:
            raise HTTPException(
                status_code=422,
                detail="Provide session_id, or both source and config",
            )
        session = orchestration_service.create_session(request.source, request.config)

    # Preflight: SheetSage2 runtime must be configured
    health = orchestration_service.sheetsage2.health()
    if not health["available"]:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unavailable",
                "component": "sheetsage2",
                "message": health["detail"],
                "session_id": session.session_id,
            },
        )

    task_id = f"orc_{uuid.uuid4().hex[:8]}"
    active_tasks[task_id] = {
        "type": "orchestrate_transcribe",
        "status": "queued",
        "session_id": session.session_id,
        "progress": 0,
    }
    background_tasks.add_task(
        _run_transcribe_task, task_id, session.session_id,
    )
    logger.info(
        f"Orchestration transcribe task {task_id} queued "
        f"(session {session.session_id})"
    )
    return TaskResponse(task_id=task_id, status="queued", session_id=session.session_id)


@app.post("/api/orchestrate/preview", response_model=TaskResponse)
async def orchestrate_preview(
    request: OrchestratePreviewRequest,
    background_tasks: BackgroundTasks,
):
    """
    Step [5]: YuE2 generates an audio mockup from the (edited) MusicXML.
    The score is exported to native ABC first and used as symbolic conditioning.
    """
    if not request.session_id:
        raise HTTPException(status_code=422, detail="session_id is required")
    try:
        session = orchestration_service.get_session(request.session_id)
    except SessionError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    score_path = Path(request.musicxml_path or session.musicxml_path or "")
    if not score_path.is_file():
        raise HTTPException(
            status_code=409,
            detail=(
                f"Score not found ({score_path or 'no score yet'}); "
                "run /api/orchestrate/transcribe first"
            ),
        )

    health = orchestration_service.yue2.health()
    if not health["available"]:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unavailable",
                "component": "yue2",
                "message": health["detail"],
                "session_id": session.session_id,
            },
        )

    task_id = f"prev_{uuid.uuid4().hex[:8]}"
    active_tasks[task_id] = {
        "type": "orchestrate_preview",
        "status": "queued",
        "session_id": session.session_id,
        "progress": 0,
    }
    background_tasks.add_task(
        _run_preview_task, task_id, session.session_id, request,
    )
    logger.info(f"Orchestration preview task {task_id} queued (session {session.session_id})")
    return TaskResponse(task_id=task_id, status="queued", session_id=session.session_id)


@app.get("/api/orchestrate/session/{session_id}")
async def get_orchestrate_session(session_id: str):
    """Poll human-in-the-loop session state: stage, artifacts, previews."""
    try:
        return orchestration_service.get_session(session_id)
    except SessionError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@app.get("/api/orchestrate/sessions", response_model=SessionListResponse)
async def list_orchestrate_sessions():
    """List all orchestration sessions (most recent first)."""
    return SessionListResponse(sessions=orchestration_service.list_sessions())


@app.post("/api/orchestrate/session/{session_id}/edit")
async def register_orchestrate_edit(session_id: str, request: EditRegisteredRequest):
    """
    Step [4]: register a human edit performed in MuseScore.
    Bumps the edit revision so the next preview reflects the edited score.
    """
    try:
        return orchestration_service.register_edit(session_id, request)
    except SessionError as exc:
        status = 404 if "not found" in str(exc).lower() else 409
        raise HTTPException(status_code=status, detail=str(exc))


@app.post("/api/orchestrate/session/{session_id}/export")
async def export_orchestrate_session(session_id: str):
    """Step [6]: export the final score as print-ready MusicXML."""
    try:
        return orchestration_service.export_session(session_id)
    except SessionError as exc:
        status = 404 if "not found" in str(exc).lower() else 409
        raise HTTPException(status_code=status, detail=str(exc))


@app.get("/api/orchestrate/health", response_model=OrchestrateHealthResponse)
async def orchestrate_health():
    """Report SheetSage2 & YuE2 runtime availability for the orchestration workflow."""
    data = orchestration_service.health()
    return OrchestrateHealthResponse(
        status=data["status"],
        sheetsage2=OrchestrateHealthComponent(**data["sheetsage2"]),
        yue2=OrchestrateHealthComponent(**data["yue2"]),
    )


async def _run_transcribe_task(task_id: str, session_id: str):
    """Background wrapper: run transcribe and publish completion/error events."""
    progress = orchestration_progress(task_id)
    try:
        session = await orchestration_service.run_transcribe(
            task_id, session_id, progress=progress,
        )
        await manager.send_personal_message({
            "type": "complete",
            "task_id": task_id,
            "session_id": session_id,
            "file_path": session.musicxml_path,
            "stage": session.stage.value,
        }, task_id)
    except Exception as exc:
        logger.error(f"Orchestration transcribe task {task_id} failed: {exc}")
        if task_id in active_tasks:
            active_tasks[task_id]["status"] = "error"
        await manager.send_personal_message({
            "type": "error",
            "task_id": task_id,
            "session_id": session_id,
            "stage": "transcription",
            "message": str(exc),
        }, task_id)


async def _run_preview_task(task_id: str, session_id: str, request: OrchestratePreviewRequest):
    """Background wrapper: run YuE2 preview and publish completion/error events."""
    progress = orchestration_progress(task_id)
    try:
        session = await orchestration_service.run_preview(
            task_id,
            session_id,
            musicxml_path=request.musicxml_path,
            style_prompt=request.style_prompt,
            lyrics=request.lyrics,
            progress=progress,
        )
        latest = session.previews[-1] if session.previews else None
        await manager.send_personal_message({
            "type": "complete",
            "task_id": task_id,
            "session_id": session_id,
            "audio_path": latest.audio_path if latest else None,
            "stage": session.stage.value,
        }, task_id)
    except Exception as exc:
        logger.error(f"Orchestration preview task {task_id} failed: {exc}")
        if task_id in active_tasks:
            active_tasks[task_id]["status"] = "error"
        await manager.send_personal_message({
            "type": "error",
            "task_id": task_id,
            "session_id": session_id,
            "stage": "preview",
            "message": str(exc),
        }, task_id)


# ==================== Background Task Handlers ====================

async def process_transcription(task_id: str, request: TranscribeRequest):
    """
    Background task handler for audio transcription.
    Implements full pipeline: download → separate → transcribe → quantize → MusicXML
    """
    # Placeholder implementation (Phase 2)
    # Update task status via WebSocket
    try:
        # Simulate progress updates
        stages = [
            ("downloading", "Downloading audio from source..."),
            ("separating", "Isolating instruments using Demucs..."),
            ("transcribing", "Converting audio to MIDI with Basic Pitch..."),
            ("quantizing", "Cleaning and quantizing rhythm..."),
            ("generating", "Generating MusicXML notation..."),
        ]
        
        for i, (stage, message) in enumerate(stages):
            active_tasks[task_id]["status"] = stage
            active_tasks[task_id]["progress"] = int((i + 1) / len(stages) * 100)
            
            await manager.send_personal_message({
                "type": "progress",
                "task_id": task_id,
                "stage": stage,
                "percent": active_tasks[task_id]["progress"],
                "message": message
            }, task_id)  # Use task_id as client_id for simplicity
            
            await asyncio.sleep(1)  # Simulate work
        
        # Mark complete
        active_tasks[task_id]["status"] = "complete"
        output_file = settings.PROJECTS_DIR / f"{task_id}_score.musicxml"
        output_file.touch()  # Placeholder
        
        await manager.send_personal_message({
            "type": "complete",
            "task_id": task_id,
            "file_path": str(output_file)
        }, task_id)
    
    except Exception as e:
        logger.error(f"Transcription error for {task_id}: {e}")
        await manager.send_personal_message({
            "type": "error",
            "task_id": task_id,
            "stage": "processing",
            "message": str(e)
        }, task_id)


async def process_arrangement(task_id: str, request: ArrangeRequest):
    """
    Background task handler for score arrangement.
    Loads compiled skill and applies arrangement rules.
    """
    # Placeholder implementation (Phase 4)
    try:
        active_tasks[task_id]["status"] = "analyzing"
        
        await manager.send_personal_message({
            "type": "progress",
            "task_id": task_id,
            "stage": "analyzing",
            "percent": 25,
            "message": "Analyzing source score..."
        }, task_id)
        
        await asyncio.sleep(1)
        
        active_tasks[task_id]["status"] = "arranging"
        
        await manager.send_personal_message({
            "type": "progress",
            "task_id": task_id,
            "stage": "arranging",
            "percent": 75,
            "message": f"Applying {request.style} arrangement rules..."
        }, task_id)
        
        await asyncio.sleep(1)
        
        # Mark complete
        active_tasks[task_id]["status"] = "complete"
        output_file = settings.PROJECTS_DIR / f"{task_id}_arranged.musicxml"
        output_file.touch()  # Placeholder
        
        await manager.send_personal_message({
            "type": "complete",
            "task_id": task_id,
            "file_path": str(output_file)
        }, task_id)
    
    except Exception as e:
        logger.error(f"Arrangement error for {task_id}: {e}")
        await manager.send_personal_message({
            "type": "error",
            "task_id": task_id,
            "stage": "arranging",
            "message": str(e)
        }, task_id)


# ==================== Main Entry Point ====================

if __name__ == "__main__":
    import uvicorn
    
    logger.info("=" * 60)
    logger.info(f"Starting {settings.APP_NAME} Backend Server")
    logger.info("=" * 60)
    
    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.REST_PORT,
        log_level=settings.LOG_LEVEL.lower()
    )
