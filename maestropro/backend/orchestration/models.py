"""
MaestroPro - Orchestration Models
Maya Instruments Technology
Version: 1.1.0

Pydantic models for the Full Orchestration Workflow
(SheetSage2 + YuE2 + Human-in-the-Loop).
"""

from enum import Enum
from typing import List, Optional, Dict, Any

from pydantic import BaseModel, Field, field_validator


class OrchestrationStage(str, Enum):
    """Human-in-the-loop state machine stages."""

    CONFIGURED = "configured"
    TRANSCRIBING = "transcribing"
    AWAITING_EDIT = "awaiting_edit"
    PREVIEWING = "previewing"
    PREVIEW_READY = "preview_ready"
    EXPORTED = "exported"
    ERROR = "error"


class ArrangementConfig(BaseModel):
    """Step [2] of the workflow: orchestration configuration."""

    genre: str = Field(
        ..., min_length=1,
        description="Target genre/orchestration, e.g. 'String Orchestra'"
    )
    instruments: List[str] = Field(
        ..., min_length=1,
        description="Target instrument parts in score order; first carries the melody"
    )
    part_count: Optional[int] = Field(
        default=None, ge=1, le=32,
        description="Number of parts; defaults to len(instruments)"
    )
    key: Optional[str] = Field(
        default=None,
        description="Optional target key (music21 spelling, e.g. 'Eb major'); "
                    "overrides the transcribed key by transposition"
    )
    tempo: Optional[int] = Field(
        default=None, ge=20, le=300,
        description="Optional tempo override (BPM)"
    )
    style_prompt: Optional[str] = Field(
        default=None,
        description="Free-text style for YuE2 preview; built from genre/instruments if omitted"
    )
    lyrics: Optional[str] = Field(
        default=None,
        description="Lyrics for the YuE2 preview vocal; placeholder vocalise if omitted"
    )
    quantize_grid: str = Field(default="1/16", description="Rhythm quantize grid")
    melody_voice: str = Field(
        default="Vocal",
        description="Native ABC voice treated as the lead melody ('Vocal' or 'Ins')"
    )

    @field_validator("instruments")
    @classmethod
    def _non_empty_names(cls, value: List[str]) -> List[str]:
        cleaned = [name.strip() for name in value if name and name.strip()]
        if not cleaned:
            raise ValueError("instruments must contain at least one non-empty name")
        return cleaned

    @field_validator("melody_voice")
    @classmethod
    def _valid_voice(cls, value: str) -> str:
        if value not in ("Vocal", "Ins"):
            raise ValueError("melody_voice must be 'Vocal' or 'Ins'")
        return value


class LeadSheetInfo(BaseModel):
    """Step [3] output: SheetSage2 lead-sheet metadata retained for the session."""

    abc_path: str
    bpm: int
    meter: str
    key: str
    chords: List[Dict[str, Any]] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    melody_notes: int = 0
    secondary_notes: int = 0


class PreviewInfo(BaseModel):
    """One YuE2 audio mockup iteration (step [5])."""

    audio_path: str
    musicxml_snapshot: str
    abc_path: str
    cot: str
    created_at: str
    edit_revision: int = 0


class OrchestrationSession(BaseModel):
    """Full human-in-the-loop orchestration session state."""

    session_id: str
    stage: OrchestrationStage = OrchestrationStage.CONFIGURED
    source: str
    config: ArrangementConfig
    source_audio_path: Optional[str] = None
    lead_sheet: Optional[LeadSheetInfo] = None
    musicxml_path: Optional[str] = None
    edit_revision: int = 0
    previews: List[PreviewInfo] = Field(default_factory=list)
    export_path: Optional[str] = None
    error: Optional[str] = None
    created_at: str
    updated_at: str


class CreateSessionRequest(BaseModel):
    """Create a session: workflow steps [1] + [2]."""

    source: str = Field(..., description="YouTube/HTTP URL or local audio file path")
    config: ArrangementConfig


class OrchestrateTranscribeRequest(BaseModel):
    """Run SheetSage2 → multi-part MusicXML (workflow step [3])."""

    session_id: Optional[str] = Field(
        default=None, description="Existing session; omit to auto-create from source+config"
    )
    source: Optional[str] = None
    config: Optional[ArrangementConfig] = None


class OrchestratePreviewRequest(BaseModel):
    """Run YuE2 audio mockup from (edited) MusicXML (workflow step [5])."""

    session_id: Optional[str] = None
    musicxml_path: Optional[str] = Field(
        default=None,
        description="Edited MusicXML; defaults to the session's current score"
    )
    style_prompt: Optional[str] = None
    lyrics: Optional[str] = None


class EditRegisteredRequest(BaseModel):
    """Human edit performed in MuseScore (workflow step [4])."""

    musicxml_path: Optional[str] = Field(
        default=None,
        description="Path where the edited score was saved; defaults to session score"
    )
    note: Optional[str] = Field(default=None, description="Optional user note about the edit")


class SessionListResponse(BaseModel):
    sessions: List[OrchestrationSession]


class OrchestrateHealthComponent(BaseModel):
    available: bool
    configured: bool
    skill_dir: str
    script: str
    python: str = ""
    detail: str = ""


class OrchestrateHealthResponse(BaseModel):
    status: str
    sheetsage2: OrchestrateHealthComponent
    yue2: OrchestrateHealthComponent


class TaskResponse(BaseModel):
    """Response for async orchestration tasks."""

    task_id: str
    status: str = "queued"
    session_id: Optional[str] = None
