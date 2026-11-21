"""Tests for health check and root endpoints."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root_endpoint(async_client: AsyncClient):
    """Test GET / returns 200 and welcome payload."""
    response = await async_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "docs" in data
    assert data["docs"] == "/docs"


@pytest.mark.asyncio
async def test_health_check_endpoint(async_client: AsyncClient):
    """Test GET /api/v1/health returns 200, healthy status, and project metadata."""
    response = await async_client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "project_name" in data
    assert "version" in data
    assert "environment" in data
    assert "timestamp" in data
