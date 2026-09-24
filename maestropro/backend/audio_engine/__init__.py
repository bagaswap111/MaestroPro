"""
MaestroPro - Audio Engine Module
Maya Instruments Technology

Handles audio downloading, source separation, and MIDI transcription.
"""

from backend.audio_engine.downloader import (
    AUDIO_EXTENSIONS,
    DownloadError,
    download_audio,
    is_url,
    resolve_source,
)

__all__ = [
    "AUDIO_EXTENSIONS",
    "DownloadError",
    "download_audio",
    "is_url",
    "resolve_source",
]
