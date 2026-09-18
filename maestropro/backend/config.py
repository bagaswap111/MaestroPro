"""
MaestroPro - Global Configuration Module
Maya Instruments Technology
Version: 1.0.0

Centralized configuration management using Pydantic Settings.
Supports environment variables for flexible deployment.
"""

import os
from pathlib import Path
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Application Info
    APP_NAME: str = "MaestroPro"
    COMPANY: str = "Maya Instruments Technology"
    VERSION: str = "1.0.0"
    TAGLINE: str = "From Audio to Artistry"
    
    # Server Configuration
    WS_PORT: int = 8765
    REST_PORT: int = 8000
    OLLAMA_PORT: int = 11434
    HOST: str = "0.0.0.0"
    
    # AI Configuration
    OLLAMA_URL: str = "http://localhost:11434"
    DEFAULT_MODEL: str = "qwen2.5-coder:7b"
    TEMPERATURE: float = 0.2
    TOP_P: float = 0.9
    NUM_PREDICT: int = 4096
    NUM_CTX: int = 4096
    KEEP_ALIVE: str = "10m"
    
    # Hardware Detection (auto-adjusted)
    RAM_GB_MIN: float = 8.0
    RAM_GB_RECOMMENDED: float = 16.0
    
    # Directory Paths
    BASE_DIR: Path = Path.home() / "MaestroPro"
    DATA_DIR: Path = BASE_DIR / "data"
    CACHE_DIR: Path = DATA_DIR / "cache"
    PROJECTS_DIR: Path = DATA_DIR / "projects"
    SKILLS_DIR: Path = DATA_DIR / "skills"
    SKILLS_MD_DIR: Path = SKILLS_DIR / "markdown"
    SKILLS_PY_DIR: Path = SKILLS_DIR / "compiled"
    
    # Audio Engine Settings
    AUDIO_SAMPLE_RATE: int = 44100
    AUDIO_BIT_DEPTH: int = 16
    DEMUCS_MODEL: str = "htdemucs_ft"
    QUANTIZE_GRID: str = "1/16"
    GHOST_NOTE_VELOCITY_THRESHOLD: int = 20
    
    # Allowed imports for AI-generated code
    ALLOWED_IMPORTS: set = {"music21", "typing", "math", "random"}
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_prefix = "MAESTROPRO_"
        case_sensitive = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create necessary directories on initialization
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Create all required directories if they don't exist."""
        directories = [
            self.CACHE_DIR,
            self.PROJECTS_DIR,
            self.SKILLS_MD_DIR,
            self.SKILLS_PY_DIR,
        ]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def get_model_for_hardware(self) -> dict:
        """
        Detect available RAM and recommend appropriate model.
        Returns dict with model name and demucs model.
        """
        try:
            import psutil
            ram_gb = psutil.virtual_memory().total / (1024 ** 3)
            
            if ram_gb >= self.RAM_GB_RECOMMENDED:
                return {
                    "model": "qwen2.5-coder:14b",
                    "demucs_model": "htdemucs_ft"
                }
            elif ram_gb >= self.RAM_GB_MIN:
                return {
                    "model": "qwen2.5-coder:7b",
                    "demucs_model": "htdemucs_ft"
                }
            else:
                return {
                    "model": "qwen2.5-coder:1.5b",
                    "demucs_model": "htdemucs"
                }
        except Exception:
            # Fallback to default
            return {
                "model": self.DEFAULT_MODEL,
                "demucs_model": self.DEMUCS_MODEL
            }
    
    @property
    def ollama_generate_url(self) -> str:
        """Full URL for Ollama generate endpoint."""
        return f"{self.OLLAMA_URL}/api/generate"
    
    @property
    def metadata_file(self) -> Path:
        """Path to skills metadata JSON file."""
        return self.SKILLS_DIR / "metadata.json"


# Singleton instance
settings = Settings()
