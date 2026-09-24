"""
MaestroPro - Orchestration Service
Maya Instruments Technology
Version: 1.1.0

Full Orchestration Workflow (SheetSage2 + YuE2 + Human-in-the-Loop):

  [1] Source audio (upload / YouTube URL)
  [2] Arrangement configuration (genre, instruments, key, tempo)
  [3] SheetSage2 → lead sheet → per-instrument split → multi-part MusicXML
  [4] Human edits the score in MuseScore
  [5] YuE2 → audio mockup from the edited MusicXML
  [6] Iterate (edit → preview → …) until export of print-ready MusicXML
"""

import asyncio
import logging
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Awaitable, Callable, Optional

from backend.audio_engine.downloader import is_url, resolve_source
from backend.config import settings
from backend.orchestration.abc_bridge import (
    AbcBridgeError,
    LeadSheet,
    parse_lead_sheet,
    strip_chords,
)
from backend.orchestration.abc_export import AbcExportError, score_to_native_abc
from backend.orchestration.models import (
    ArrangementConfig,
    EditRegisteredRequest,
    LeadSheetInfo,
    OrchestrationSession,
    OrchestrationStage,
    PreviewInfo,
)
from backend.orchestration.score_builder import (
    ScoreBuildError,
    build_orchestration_score,
    export_musicxml,
)
from backend.orchestration.session import SessionError, SessionStore, transition
from backend.orchestration.sheetsage2 import SheetSage2Adapter, SheetSage2Error
from backend.orchestration.yue2 import YuE2Adapter, YuE2Error

logger = logging.getLogger(__name__)

ProgressFn = Callable[[str, int, str], Awaitable[None]]


async def _noop_progress(stage: str, percent: int, message: str) -> None:
    return None


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class OrchestrationService:
    """Coordinates SheetSage2 transcription, human edits, and YuE2 previews."""

    def __init__(self, config=None):
        self.config = config or settings
        self.sessions = SessionStore(self.config.ORCHESTRATION_DIR)
        self.sheetsage2 = SheetSage2Adapter(self.config)
        self.yue2 = YuE2Adapter(self.config)

    # ------------------------------------------------------------------
    # Health
    # ------------------------------------------------------------------

    def health(self) -> dict:
        return {
            "status": "ok",
            "sheetsage2": self.sheetsage2.health(),
            "yue2": self.yue2.health(),
        }

    # ------------------------------------------------------------------
    # Session helpers
    # ------------------------------------------------------------------

    def create_session(self, source: str, config: ArrangementConfig) -> OrchestrationSession:
        return self.sessions.create(source, config)

    def get_session(self, session_id: str) -> OrchestrationSession:
        return self.sessions.get(session_id)

    def list_sessions(self):
        return self.sessions.list()

    def register_edit(
        self, session_id: str, request: EditRegisteredRequest
    ) -> OrchestrationSession:
        """
        Step [4]: the user finished editing in MuseScore.

        Bumps the edit revision, adopts the edited path when supplied, and
        returns the session to 'awaiting_edit' (existing previews become stale).
        """
        session = self.sessions.get(session_id)
        if session.stage not in (
            OrchestrationStage.AWAITING_EDIT,
            OrchestrationStage.PREVIEW_READY,
            OrchestrationStage.EXPORTED,
        ):
            raise SessionError(
                f"Session is {session.stage.value}; edits are accepted while "
                "awaiting_edit, preview_ready, or exported"
            )

        if request.musicxml_path:
            edited = Path(request.musicxml_path)
            if not edited.is_file():
                raise SessionError(f"Edited MusicXML not found: {edited}")
            session.musicxml_path = str(edited)

        session.edit_revision += 1
        session.stage = OrchestrationStage.AWAITING_EDIT
        session.updated_at = _now()
        self.sessions.save(session)
        logger.info(
            f"Session {session_id}: edit revision {session.edit_revision} registered"
            + (f" ({request.note})" if request.note else "")
        )
        return session

    def export_session(self, session_id: str) -> OrchestrationSession:
        """Step [6]: copy the final score to a print-ready export location."""
        session = self.sessions.get(session_id)
        if not session.musicxml_path or not Path(session.musicxml_path).is_file():
            raise SessionError("No score available to export; run transcribe first")

        transition(session, OrchestrationStage.EXPORTED)
        exports_dir = self.config.PROJECTS_DIR / "exports"
        exports_dir.mkdir(parents=True, exist_ok=True)
        target = exports_dir / f"{session.session_id}_r{session.edit_revision}.musicxml"
        shutil.copy2(session.musicxml_path, target)
        session.export_path = str(target)
        self.sessions.save(session)
        logger.info(f"Session {session_id} exported to {target}")
        return session

    # ------------------------------------------------------------------
    # Step [3]: SheetSage2 → multi-part MusicXML
    # ------------------------------------------------------------------

    async def run_transcribe(
        self,
        task_id: str,
        session_id: str,
        progress: Optional[ProgressFn] = None,
    ) -> OrchestrationSession:
        progress = progress or _noop_progress
        session = self.sessions.get(session_id)
        loop = asyncio.get_running_loop()

        try:
            self.sessions.update_stage(session_id, OrchestrationStage.TRANSCRIBING)
            session = self.sessions.get(session_id)

            session_dir = self.sessions.session_dir(session_id)

            # [1] Resolve source (URL download or local file)
            await progress("resolving_source", 10, "Resolving audio source...")
            source_dir = session_dir / "source"
            audio_path = await asyncio.to_thread(
                resolve_source, session.source, source_dir
            )
            session.source_audio_path = str(audio_path)
            self.sessions.save(session)

            # [3a] SheetSage2 transcription → native ABC
            await progress("transcribing", 25, "Transcribing with SheetSage2...")

            def _sheet_progress(stage: str, percent: int, message: str) -> None:
                # Bridge sync adapter progress from the worker thread onto the loop
                asyncio.run_coroutine_threadsafe(progress(stage, percent, message), loop)

            transcription_dir = session_dir / "transcription"
            if transcription_dir.exists():
                shutil.rmtree(transcription_dir)
            result = await asyncio.to_thread(
                self.sheetsage2.transcribe,
                audio_path,
                transcription_dir,
                task=self.config.SHEETSAGE2_TASK,
                progress=_sheet_progress,
            )

            # [3b] Parse lead sheet
            await progress("splitting_parts", 60, "Building lead sheet model...")
            lead: LeadSheet = await asyncio.to_thread(
                parse_lead_sheet,
                result["abc_text"],
                melody_voice=session.config.melody_voice,
                warnings=result.get("warnings"),
            )
            if not lead.melody:
                raise SheetSage2Error(
                    "Transcription produced no melody notes; try another source audio"
                )

            # Retain a pristine copy of the transcription in the session
            lead_path = session_dir / "lead_sheet.abc"
            lead_path.write_text(result["abc_text"], encoding="utf-8")

            session.lead_sheet = LeadSheetInfo(
                abc_path=str(lead_path),
                bpm=lead.bpm,
                meter=lead.meter,
                key=lead.key,
                chords=[{"onset_quarters": c.onset, "symbol": c.symbol} for c in lead.chords],
                warnings=lead.warnings,
                melody_notes=len(lead.melody),
                secondary_notes=len(lead.secondary),
            )

            # [3c] Split into instrument parts → multi-part MusicXML
            await progress("generating", 75, "Splitting into instrument parts...")
            score = await asyncio.to_thread(
                build_orchestration_score, lead, session.config
            )
            musicxml_path = session_dir / "score.musicxml"
            await asyncio.to_thread(export_musicxml, score, musicxml_path)
            session.musicxml_path = str(musicxml_path)

            self.sessions.update_stage(session_id, OrchestrationStage.AWAITING_EDIT)
            session = self.sessions.get(session_id)

            await progress(
                "complete", 100,
                "Multi-part score ready — edit it in MuseScore, then request a preview",
            )
            logger.info(
                f"Session {session_id}: transcribed → {musicxml_path} "
                f"({len(session.config.instruments)} parts, {len(lead.chords)} chords)"
            )
            return session

        except (
            SheetSage2Error, AbcBridgeError, ScoreBuildError, SessionError,
            FileNotFoundError, ValueError, OSError,
        ) as exc:
            logger.error(f"Transcribe failed for {session_id}: {exc}")
            await self._fail(session_id, task_id, "transcription", str(exc), progress)
            raise

    # ------------------------------------------------------------------
    # Step [5]: YuE2 audio mockup
    # ------------------------------------------------------------------

    async def run_preview(
        self,
        task_id: str,
        session_id: str,
        *,
        musicxml_path: Optional[str] = None,
        style_prompt: Optional[str] = None,
        lyrics: Optional[str] = None,
        progress: Optional[ProgressFn] = None,
    ) -> OrchestrationSession:
        progress = progress or _noop_progress
        session = self.sessions.get(session_id)
        loop = asyncio.get_running_loop()

        score_path = Path(musicxml_path or session.musicxml_path or "")
        if not score_path.is_file():
            raise SessionError(
                f"MusicXML score not found: {score_path or '(none)'}; "
                "run /api/orchestrate/transcribe first"
            )

        try:
            self.sessions.update_stage(session_id, OrchestrationStage.PREVIEWING)
            session = self.sessions.get(session_id)
            session_dir = self.sessions.session_dir(session_id)
            revision = session.edit_revision

            # Load the (possibly human-edited) score
            await progress("exporting_abc", 20, "Exporting score to native ABC...")

            def _load_score():
                from music21 import converter
                return converter.parse(str(score_path))

            score = await asyncio.to_thread(_load_score)

            # MusicXML → native two-voice ABC (melody + chords)
            abc_text = await asyncio.to_thread(
                score_to_native_abc, score, bpm=session.config.tempo
            )

            has_chords = '"' in abc_text
            cot = "full" if has_chords else "melody"
            if cot == "melody":
                abc_text = await asyncio.to_thread(strip_chords, abc_text)

            abc_dir = session_dir / "abc"
            abc_dir.mkdir(parents=True, exist_ok=True)
            abc_path = abc_dir / f"score_r{revision}.abc"
            abc_path.write_text(abc_text, encoding="utf-8")

            # Snapshot the exact score used for this preview
            snapshot_dir = session_dir / "previews"
            snapshot_dir.mkdir(parents=True, exist_ok=True)
            snapshot_path = snapshot_dir / f"score_r{revision}.musicxml"
            if score_path.resolve() != snapshot_path.resolve():
                shutil.copy2(score_path, snapshot_path)

            # YuE2 request from session config (per-call overrides win)
            request = self.yue2.build_request(
                session_id=session_id,
                genre=session.config.genre,
                instruments=session.config.instruments,
                tempo=session.config.tempo,
                style_prompt=style_prompt or session.config.style_prompt,
                lyrics=lyrics or session.config.lyrics,
            )

            await progress(
                "generating_audio", 35,
                f"YuE2 generating {cot}-conditioned audio mockup...",
            )
            run_dir = session_dir / "preview_run"
            if run_dir.exists():
                shutil.rmtree(run_dir)

            def _yue_progress(stage: str, percent: int, message: str) -> None:
                asyncio.run_coroutine_threadsafe(progress(stage, percent, message), loop)

            result = await asyncio.to_thread(
                self.yue2.generate_preview,
                abc_text=abc_text,
                request=request,
                output_dir=run_dir,
                cot=cot,
                progress=_yue_progress,
            )

            preview = PreviewInfo(
                audio_path=str(result["audio_path"]),
                musicxml_snapshot=str(snapshot_path),
                abc_path=str(abc_path),
                cot=cot,
                created_at=_now(),
                edit_revision=revision,
            )
            session.previews.append(preview)
            self.sessions.update_stage(session_id, OrchestrationStage.PREVIEW_READY)
            session = self.sessions.get(session_id)

            await progress(
                "complete", 100,
                "Preview ready — listen, then edit in MuseScore and iterate, or export",
            )
            logger.info(f"Session {session_id}: preview {cot} → {preview.audio_path}")
            return session

        except (
            YuE2Error, AbcExportError, AbcBridgeError, SessionError,
            FileNotFoundError, ValueError, OSError,
        ) as exc:
            logger.error(f"Preview failed for {session_id}: {exc}")
            await self._fail(session_id, task_id, "preview", str(exc), progress)
            raise

    # ------------------------------------------------------------------

    async def _fail(
        self,
        session_id: str,
        task_id: str,
        stage: str,
        message: str,
        progress: ProgressFn,
    ) -> None:
        try:
            session = self.sessions.get(session_id)
            if session.stage != OrchestrationStage.EXPORTED:
                session.stage = OrchestrationStage.ERROR
                session.error = message
                session.updated_at = _now()
                self.sessions.save(session)
        except SessionError:
            pass
        try:
            await progress(stage, 0, f"Error: {message}")
        except Exception:
            pass
