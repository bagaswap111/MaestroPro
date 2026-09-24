"""
MaestroPro - Orchestration Module
Maya Instruments Technology
Version: 1.1.0

Full Orchestration Workflow: SheetSage2 transcription → human editing in
MuseScore → YuE2 audio-mockup preview → iterate → export.
"""

from backend.orchestration.models import (
    ArrangementConfig,
    CreateSessionRequest,
    EditRegisteredRequest,
    LeadSheetInfo,
    OrchestrateHealthResponse,
    OrchestratePreviewRequest,
    OrchestrateTranscribeRequest,
    OrchestrationSession,
    OrchestrationStage,
    PreviewInfo,
    SessionListResponse,
)
from backend.orchestration.orchestrator import OrchestrationService
from backend.orchestration.session import (
    ALLOWED_TRANSITIONS,
    SessionError,
    SessionStore,
    StageTransitionError,
)
from backend.orchestration.sheetsage2 import SheetSage2Adapter, SheetSage2Error
from backend.orchestration.yue2 import YuE2Adapter, YuE2Error

__all__ = [
    "ALLOWED_TRANSITIONS",
    "ArrangementConfig",
    "CreateSessionRequest",
    "EditRegisteredRequest",
    "LeadSheetInfo",
    "OrchestrateHealthResponse",
    "OrchestratePreviewRequest",
    "OrchestrateTranscribeRequest",
    "OrchestrationSession",
    "OrchestrationService",
    "OrchestrationStage",
    "PreviewInfo",
    "SessionError",
    "SessionListResponse",
    "SessionStore",
    "SheetSage2Adapter",
    "SheetSage2Error",
    "StageTransitionError",
    "YuE2Adapter",
    "YuE2Error",
]
