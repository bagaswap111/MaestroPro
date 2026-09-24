"""
MaestroPro - Orchestration Session Store
Maya Instruments Technology
Version: 1.1.0

Human-in-the-loop session state for the Full Orchestration Workflow.
Sessions persist as JSON under data/orchestration/<session_id>.json so the
edit → preview → re-edit loop survives backend restarts.
"""

import json
import logging
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

from backend.orchestration.models import (
    ArrangementConfig,
    OrchestrationSession,
    OrchestrationStage,
)

logger = logging.getLogger(__name__)


class SessionError(RuntimeError):
    """Session lookup or state-machine violation."""


class StageTransitionError(SessionError):
    """Illegal stage transition."""


# Human-in-the-loop state machine
ALLOWED_TRANSITIONS: Dict[OrchestrationStage, set] = {
    OrchestrationStage.CONFIGURED: {OrchestrationStage.TRANSCRIBING, OrchestrationStage.ERROR},
    OrchestrationStage.TRANSCRIBING: {
        OrchestrationStage.AWAITING_EDIT, OrchestrationStage.ERROR,
    },
    OrchestrationStage.AWAITING_EDIT: {
        OrchestrationStage.TRANSCRIBING,       # re-run transcription (redo)
        OrchestrationStage.PREVIEWING,
        OrchestrationStage.EXPORTED,
        OrchestrationStage.ERROR,
    },
    OrchestrationStage.PREVIEWING: {
        OrchestrationStage.PREVIEW_READY, OrchestrationStage.ERROR,
    },
    OrchestrationStage.PREVIEW_READY: {
        OrchestrationStage.AWAITING_EDIT,      # user edits again (iterate)
        OrchestrationStage.PREVIEWING,         # regenerate without edit
        OrchestrationStage.TRANSCRIBING,       # redo from source audio
        OrchestrationStage.EXPORTED,
        OrchestrationStage.ERROR,
    },
    OrchestrationStage.EXPORTED: {
        OrchestrationStage.AWAITING_EDIT,      # reopen for further work
        OrchestrationStage.PREVIEWING,
        OrchestrationStage.TRANSCRIBING,
    },
    OrchestrationStage.ERROR: {
        OrchestrationStage.CONFIGURED, OrchestrationStage.TRANSCRIBING,
        OrchestrationStage.PREVIEWING,
    },
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def transition(session: OrchestrationSession, new_stage: OrchestrationStage) -> OrchestrationSession:
    """Apply a validated stage transition (mutates and returns the session)."""
    if new_stage == session.stage:
        return session
    allowed = ALLOWED_TRANSITIONS.get(session.stage, set())
    if new_stage not in allowed:
        raise StageTransitionError(
            f"Illegal transition {session.stage.value} → {new_stage.value}"
        )
    session.stage = new_stage
    session.updated_at = _now()
    return session


class SessionStore:
    """In-memory session registry with JSON persistence."""

    def __init__(self, root: Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self._sessions: Dict[str, OrchestrationSession] = {}
        self._load_existing()

    def _load_existing(self) -> None:
        for path in sorted(self.root.glob("*.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                session = OrchestrationSession.model_validate(data)
                self._sessions[session.session_id] = session
            except Exception as exc:
                logger.warning(f"Skipping unreadable session {path}: {exc}")

    def session_dir(self, session_id: str) -> Path:
        directory = self.root / session_id
        directory.mkdir(parents=True, exist_ok=True)
        return directory

    def create(self, source: str, config: ArrangementConfig) -> OrchestrationSession:
        session_id = f"orc_{uuid.uuid4().hex[:10]}"
        now = _now()
        session = OrchestrationSession(
            session_id=session_id,
            stage=OrchestrationStage.CONFIGURED,
            source=source,
            config=config,
            created_at=now,
            updated_at=now,
        )
        self._sessions[session_id] = session
        self.save(session)
        logger.info(f"Created orchestration session {session_id} for {source}")
        return session

    def get(self, session_id: str) -> OrchestrationSession:
        session = self._sessions.get(session_id)
        if session is None:
            raise SessionError(f"Session not found: {session_id}")
        return session

    def list(self) -> List[OrchestrationSession]:
        return sorted(
            self._sessions.values(),
            key=lambda s: s.created_at,
            reverse=True,
        )

    def save(self, session: OrchestrationSession) -> None:
        session.updated_at = _now()
        path = self.root / f"{session.session_id}.json"
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(
            session.model_dump_json(indent=2),
            encoding="utf-8",
        )
        tmp.replace(path)
        self._sessions[session.session_id] = session

    def update_stage(
        self, session_id: str, new_stage: OrchestrationStage, *, error: Optional[str] = None,
    ) -> OrchestrationSession:
        session = self.get(session_id)
        transition(session, new_stage)
        if error is not None:
            session.error = error
        elif new_stage != OrchestrationStage.ERROR:
            session.error = None
        self.save(session)
        return session
