"""
MaestroPro - YuE2 Adapter
Maya Instruments Technology
Version: 1.1.0

Runs YuE2 audio-mockup generation (style + lyrics + native ABC → song audio)
by invoking the yue2-music skill's run_yue2.py inside the dedicated YuE2
environment. YuE2 does not render MusicXML directly: the edited score is
exported to native ABC first and supplied as the symbolic condition.

The preview is a generative, score-conditioned mockup — not a sample-accurate
instrumental render of the notation.
"""

import json
import logging
import subprocess
from pathlib import Path
from typing import Callable, Optional

from backend.config import settings

logger = logging.getLogger(__name__)

ProgressCallback = Callable[[str, int, str], None]

DEFAULT_LYRICS = (
    "[Verse]\n"
    "La la la la la la la\n"
    "La la la la la la la\n"
    "Hold the line and let it show\n"
    "Notes across the evening glow\n"
    "\n"
    "[Chorus]\n"
    "Sing it once and let it ring\n"
    "Every chord an echoed wing"
)


class YuE2Error(RuntimeError):
    """Raised when YuE2 is unavailable or a generation run fails."""


class YuE2Adapter:
    """Subprocess adapter around yue2-music/scripts/run_yue2.py."""

    def __init__(self, config=None):
        self.config = config or settings

    # -- availability -------------------------------------------------------

    @property
    def script(self) -> Path:
        return Path(self.config.YUE2_SKILL_DIR) / "scripts" / "run_yue2.py"

    @property
    def python(self) -> str:
        return (self.config.YUE2_PYTHON or "").strip()

    @property
    def configured(self) -> bool:
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
                "Set YUE2_PYTHON (env MAESTROPRO_YUE2_PYTHON) to the YuE2 "
                "virtualenv interpreter (yue2-infer wheel)"
            )
        return {
            "available": self.available,
            "configured": self.configured,
            "skill_dir": str(self.config.YUE2_SKILL_DIR),
            "script": str(self.script),
            "python": self.python,
            "detail": detail,
        }

    def require_available(self) -> None:
        if not self.available:
            health = self.health()
            raise YuE2Error(
                f"YuE2 runtime not available: {health['detail'] or 'unknown reason'}"
            )

    # -- preview generation -------------------------------------------------

    def build_request(
        self,
        *,
        session_id: str,
        genre: str,
        instruments: list,
        tempo: Optional[int],
        style_prompt: Optional[str],
        lyrics: Optional[str],
        seed: Optional[int] = None,
    ) -> dict:
        """Compose a YuE2 song request (ABC is passed via --abc-file, not inline)."""
        tempo_text = f"{tempo} BPM" if tempo else "moderate tempo"
        default_style = (
            f"{genre}, orchestral arrangement, {', '.join(instruments)}, "
            f"{tempo_text}, faithful melodic contour, clean studio mix"
        )
        return {
            "id": f"orchestrate_{session_id}",
            "style": (style_prompt or default_style).strip(),
            "lyrics": (lyrics or DEFAULT_LYRICS).strip(),
            "seed": int(seed if seed is not None else self.config.YUE2_SEED),
        }

    def generate_preview(
        self,
        *,
        abc_text: str,
        request: dict,
        output_dir: Path,
        cot: str = "full",
        progress: Optional[ProgressCallback] = None,
    ) -> dict:
        """
        Run YuE2 generation conditioned on native ABC.

        Returns {"audio_path": Path, "output_dir": Path, "cot": str, "run": dict}.
        """
        self.require_available()
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        request_path = output_dir / "request.json"
        abc_path = output_dir / "condition.abc"
        request_path.write_text(
            json.dumps(request, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        abc_path.write_text(abc_text, encoding="utf-8")

        cmd = [
            self.python,
            str(self.script),
            "generate",
            "--request", str(request_path),
            "--abc-file", str(abc_path),
            "--output", str(output_dir / "run"),
            "--cot", cot,
            "--model", self.config.YUE2_MODEL,
            "--vae", self.config.YUE2_VAE,
        ]

        if progress:
            progress("generating_audio", 40, f"YuE2 is generating the {cot} preview...")
        logger.info(f"YuE2 generate: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.script.parent),
                capture_output=True,
                text=True,
                timeout=self.config.YUE2_TIMEOUT,
            )
        except subprocess.TimeoutExpired as exc:
            raise YuE2Error(
                f"YuE2 generation timed out after {self.config.YUE2_TIMEOUT}s"
            ) from exc
        except OSError as exc:
            raise YuE2Error(f"Failed to launch YuE2 interpreter: {exc}") from exc

        run_dir = output_dir / "run"
        run_json = run_dir / "run.json"
        run_data = {}
        if run_json.is_file():
            try:
                run_data = json.loads(run_json.read_text(encoding="utf-8"))
            except Exception:
                run_data = {}

        audio_path = run_dir / "audio.flac"
        if not audio_path.is_file():
            # Some flows may emit wav; accept either
            candidates = sorted(run_dir.glob("audio.*"))
            if candidates:
                audio_path = candidates[0]

        if result.returncode != 0 or not audio_path.is_file():
            stderr = (result.stderr or "").strip()
            stdout = (result.stdout or "").strip()
            failure = run_dir / "failure.json"
            detail = stderr or stdout or f"exit code {result.returncode}"
            if failure.is_file():
                detail = f"{detail} | {failure.read_text(encoding='utf-8')[:500]}"
            raise YuE2Error(f"YuE2 preview generation failed: {detail}")

        if progress:
            progress("generating_audio", 85, "YuE2 preview audio ready")

        return {
            "audio_path": audio_path,
            "output_dir": run_dir,
            "cot": cot,
            "run": run_data,
        }
