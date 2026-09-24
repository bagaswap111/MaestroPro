"""
MaestroPro - SheetSage2 Adapter
Maya Instruments Technology
Version: 1.1.0

Runs SheetSage2 transcription (audio → native ABC lead sheet) by invoking the
yue2-music skill's transcribe.py inside the dedicated SheetSage2 environment.
The two model families must stay in separate virtualenvs (dependency pins differ).
"""

import logging
import subprocess
from pathlib import Path
from typing import Callable, Optional

from backend.config import settings

logger = logging.getLogger(__name__)

ProgressCallback = Callable[[str, int, str], None]


class SheetSage2Error(RuntimeError):
    """Raised when SheetSage2 is unavailable or a transcription fails."""


class SheetSage2Adapter:
    """Subprocess adapter around yue2-music/scripts/transcribe.py."""

    def __init__(self, config=None):
        self.config = config or settings

    # -- availability -------------------------------------------------------

    @property
    def script(self) -> Path:
        return Path(self.config.SHEETSAGE2_SKILL_DIR) / "scripts" / "transcribe.py"

    @property
    def python(self) -> str:
        return (self.config.SHEETSAGE2_PYTHON or "").strip()

    @property
    def configured(self) -> bool:
        """True when a dedicated interpreter has been pointed at."""
        return bool(self.python)

    @property
    def available(self) -> bool:
        return self.script.is_file() and self.configured

    def health(self) -> dict:
        detail = ""
        if not self.script.is_file():
            detail = f"Skill script missing: {self.script}"
        elif not self.configured:
            detail = (
                "Set SHEETSAGE2_PYTHON (env MAESTROPRO_SHEETSAGE2_PYTHON) to the "
                "SheetSage2 virtualenv interpreter"
            )
        return {
            "available": self.available,
            "configured": self.configured,
            "skill_dir": str(self.config.SHEETSAGE2_SKILL_DIR),
            "script": str(self.script),
            "python": self.python,
            "detail": detail,
        }

    def require_available(self) -> None:
        if not self.available:
            health = self.health()
            raise SheetSage2Error(
                f"SheetSage2 runtime not available: {health['detail'] or 'unknown reason'}"
            )

    # -- transcription ------------------------------------------------------

    def transcribe(
        self,
        audio_path: Path,
        output_dir: Path,
        *,
        task: Optional[str] = None,
        progress: Optional[ProgressCallback] = None,
    ) -> dict:
        """
        Run SheetSage2 on `audio_path`, writing artifacts into `output_dir`.

        Returns {"abc_path": Path, "abc_text": str, "warnings": list, "output_dir": Path}.
        """
        self.require_available()
        audio_path = Path(audio_path)
        output_dir = Path(output_dir)
        if not audio_path.is_file():
            raise SheetSage2Error(f"Audio file not found: {audio_path}")

        task = task or self.config.SHEETSAGE2_TASK
        output_dir.mkdir(parents=True, exist_ok=True)

        cmd = [
            self.python,
            str(self.script),
            str(audio_path),
            "--output", str(output_dir),
            "--task", task,
            "--model", self.config.SHEETSAGE2_MODEL,
        ]
        if self.config.SHEETSAGE2_REVISION:
            cmd += ["--revision", self.config.SHEETSAGE2_REVISION]

        if progress:
            progress("transcribing", 35, "SheetSage2 is transcribing the lead sheet...")
        logger.info(f"SheetSage2 transcribe: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.script.parent),
                capture_output=True,
                text=True,
                timeout=self.config.SHEETSAGE2_TIMEOUT,
            )
        except subprocess.TimeoutExpired as exc:
            raise SheetSage2Error(
                f"SheetSage2 transcription timed out after {self.config.SHEETSAGE2_TIMEOUT}s"
            ) from exc
        except OSError as exc:
            raise SheetSage2Error(f"Failed to launch SheetSage2 interpreter: {exc}") from exc

        if result.returncode != 0:
            stderr = (result.stderr or "").strip()
            stdout = (result.stdout or "").strip()
            detail = stderr or stdout or f"exit code {result.returncode}"
            failure = output_dir / "failure.json"
            if failure.is_file():
                detail = f"{detail} | {failure.read_text(encoding='utf-8')[:500]}"
            raise SheetSage2Error(f"SheetSage2 transcription failed: {detail}")

        abc_path = output_dir / "score.abc"
        if not abc_path.is_file():
            raise SheetSage2Error(f"SheetSage2 produced no score.abc in {output_dir}")

        warnings = []
        manifest = output_dir / "transcription_manifest.json"
        if manifest.is_file():
            try:
                import json
                data = json.loads(manifest.read_text(encoding="utf-8"))
                warnings = list(data.get("warnings", []))
            except Exception:
                pass

        if progress:
            progress("transcribing", 55, "SheetSage2 transcription complete")

        return {
            "abc_path": abc_path,
            "abc_text": abc_path.read_text(encoding="utf-8"),
            "warnings": warnings,
            "output_dir": output_dir,
        }
