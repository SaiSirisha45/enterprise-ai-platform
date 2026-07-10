import pytest
from httpx import AsyncClient, ASGITransport

from backend.main import app


@pytest.mark.asyncio
async def test_root_api():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.get("/")

        assert response.status_code in [
            200,
            404
        ]


@pytest.mark.asyncio
async def test_auth_endpoint_exists():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/auth/login",
            json={
                "email": "wrong@gmail.com",
                "password": "wrongpassword"
            }
        )

        assert response.status_code in [
            200,
            401,
            400
        ] 
        