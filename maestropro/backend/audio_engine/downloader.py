"""
MaestroPro - Audio Downloader
Maya Instruments Technology

Fetches remote audio (YouTube/URL) for the Full Orchestration Workflow.
Local file paths pass through unchanged.
"""

import logging
import shutil
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

AUDIO_EXTENSIONS = {".wav", ".mp3", ".flac", ".m4a", ".ogg", ".opus", ".aac", ".wma", ".aif", ".aiff"}


class DownloadError(RuntimeError):
    """Raised when a remote audio source cannot be fetched."""


def is_url(source: str) -> bool:
    """Return True when the source looks like a remote URL."""
    try:
        parsed = urlparse(source)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False


def resolve_source(source: str, output_dir: Path) -> Path:
    """
    Resolve an orchestration source to a local audio file.

    - Local existing file: returned as-is (copied into output_dir when possible).
    - URL: downloaded via yt-dlp as 16-bit 44.1 kHz WAV into output_dir.
    """
    if is_url(source):
        return download_audio(source, output_dir)

    path = Path(source).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Audio source not found: {source}")
    if path.suffix.lower() not in AUDIO_EXTENSIONS:
        raise ValueError(
            f"Unsupported audio format '{path.suffix}'. "
            f"Allowed: {', '.join(sorted(AUDIO_EXTENSIONS))}"
        )

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        target = output_dir / f"source{path.suffix.lower()}"
        if path.resolve() != target.resolve():
            shutil.copy2(path, target)
            return target
    except OSError:
        pass
    return path


def download_audio(url: str, output_dir: Path) -> Path:
    """Download audio from a URL as 16-bit 44.1 kHz WAV using yt-dlp."""
    try:
        import yt_dlp
    except ImportError as exc:
        raise DownloadError(
            "yt-dlp is not installed. Install maestropro/requirements.txt "
            "or provide a local audio file path instead of a URL."
        ) from exc

    output_dir.mkdir(parents=True, exist_ok=True)
    outtmpl = str(output_dir / "source.%(ext)s")
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "16",
        }],
        "outtmpl": outtmpl,
        "quiet": True,
        "no_warnings": True,
    }

    logger.info(f"Downloading audio from {url} ...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)
    except Exception as exc:
        raise DownloadError(f"Failed to download audio: {exc}") from exc

    wav_path = output_dir / "source.wav"
    if not wav_path.is_file():
        candidates = sorted(output_dir.glob("source.*"))
        if not candidates:
            raise DownloadError("Download finished but no audio file was produced")
        return candidates[0]
    return wav_path
