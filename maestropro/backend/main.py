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
