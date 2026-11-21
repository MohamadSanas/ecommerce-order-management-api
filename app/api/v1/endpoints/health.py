"""Health check and service status endpoints."""

from datetime import datetime, timezone
from typing import Any, Dict

from fastapi import APIRouter, status
from pydantic import BaseModel

from app.core.config import settings

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    project_name: str
    version: str
    environment: str
    timestamp: datetime


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Service Health Check",
    description="Returns the current operational status of the API service.",
)
async def check_health() -> Dict[str, Any]:
    """Check service health and environment metadata."""
    return {
        "status": "healthy",
        "project_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp": datetime.now(timezone.utc),
    }
