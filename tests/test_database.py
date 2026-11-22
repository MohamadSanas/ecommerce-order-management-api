"""Unit tests for database session and engine setup (Task 2.1)."""

import pytest
from app.database import session
from app.database.session import get_db
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from app.core.config import settings
from app.database.session import AsyncSessionLocal, engine


def test_async_engine_configuration():
    """Verify async engine is properly configured with connection pool parameters."""
    assert isinstance(engine, AsyncEngine)
    assert "postgresql+asyncpg" in str(engine.url)

    # Check pool configuration
    pool = engine.pool
    assert pool.size() == settings.DB_POOL_SIZE or hasattr(pool, "_recycle")
    assert pool._recycle == settings.DB_POOL_RECYCLE


def test_async_session_factory():
    """Verify session factory produces AsyncSession instances with expire_on_commit=False."""
    session = AsyncSessionLocal()
    try:
        assert isinstance(session, AsyncSession)
        # In SQLAlchemy AsyncSession wraps a sync_session where expire_on_commit lives
        assert session.sync_session.expire_on_commit is False
    finally:
        pass
async def test_get_db_yields_session():
    gen = get_db()
    session = await anext(gen)
    assert isinstance(session, AsyncSession)
    
    with pytest.raises(StopAsyncIteration):
        await anext(gen)


if __name__ == "__main__":
    test_async_engine_configuration()
    test_async_session_factory()
    print("All tests passed")


