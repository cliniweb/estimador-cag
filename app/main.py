from fastapi import FastAPI

from app.config import get_settings
from app.routers.estimations import router as estimations_router

settings = get_settings()

app = FastAPI(
    title="Estimador CAG",
    description="API FastAPI para estimaciones usando contexto CAG desde doctora.json y OpenAI.",
    version="0.1.0",
)

app.include_router(estimations_router, prefix="/api")


@app.get("/health", tags=["health"])
def health() -> dict[str, str | bool]:
    return {
        "ok": True,
        "environment": settings.app_env,
        "provider": settings.llm_provider,
        "model": settings.llm_model,
    }
