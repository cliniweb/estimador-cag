from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env."""

    openai_api_key: str | None = Field(default=None)
    llm_provider: Literal["openai"] = "openai"
    llm_model: str = "gpt-4o-mini"
    app_env: str = "development"
    log_level: str = "DEBUG"
    cag_context_json: Path = Path("app/context/doctora.json")

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def context_path(self) -> Path:
        """Return the absolute path to the CAG JSON context file."""
        if self.cag_context_json.is_absolute():
            return self.cag_context_json
        return PROJECT_ROOT / self.cag_context_json


@lru_cache
def get_settings() -> Settings:
    return Settings()
