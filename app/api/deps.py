"""Shared API dependencies for FastAPI."""

from app.database.session import get_db

# Re-export get_db so routers can import standard dependencies from deps
__all__ = ["get_db"]
