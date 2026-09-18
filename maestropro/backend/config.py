"""
MaestroPro - Global Configuration
Maya Instruments Technology
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Application
    app_name: str = "MaestroPro"
    app_version: str = "1.0.0"
    debug: bool = True
    
    # Server Configuration
    rest_api_host: str = "0.0.0.0"
    rest_api_port: int = 8000
    websocket_port: int = 8765
    
    # Ollama Configuration
    ollama_host: str = "localhost"
    ollama_port: int = 11434
    ollama_model: str = "qwen2.5-coder:7b"
    
    # Audio Engine Configuration
    download_dir: str = "./downloads"
    output_dir: str = "./output"
    temp_dir: str = "./temp"
    
    # Demucs Configuration
    demucs_model: str = "htdemucs"
    separate_stems: bool = True
    
    # Transcription Engine
    transcription_engine: str = "basic-pitch"  # or "omnizart"
    
    class Config:
        env_prefix = "MAESTROPRO_"
        env_file = ".env"


# Global settings instance
settings = Settings()
