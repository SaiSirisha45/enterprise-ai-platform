import pytest
from httpx import AsyncClient, ASGITransport

from backend.main import app


@pytest.mark.asyncio
async def test_get_knowledge():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.get("/knowledge")

        assert response.status_code == 200

        data = response.json()

        assert isinstance(data, list)


@pytest.mark.asyncio
async def test_knowledge_response_not_empty():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.get("/knowledge")

        assert response.status_code == 200

        data = response.json()

        assert len(data) >= 1 