import pytest
from httpx import AsyncClient, ASGITransport

from backend.main import app


@pytest.mark.asyncio
async def test_chat_endpoint():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/chat",
            json={
                "message": "Hello AI"
            }
        )

        assert response.status_code == 200


@pytest.mark.asyncio
async def test_empty_chat_request():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/chat",
            json={}
        )

        # Current implementation accepts empty requests.
        assert response.status_code == 200 