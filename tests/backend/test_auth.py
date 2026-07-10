import pytest
from httpx import AsyncClient, ASGITransport

from backend.main import app


@pytest.mark.asyncio
async def test_register():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/auth/register",
            json={
                "name": "Test User",
                "email": "testuser123@gmail.com",
                "password": "password123"
            }
        )

        print(response.json())

        assert response.status_code in [
            200,
            201,
            400
        ]



@pytest.mark.asyncio
async def test_login():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/auth/login",
            json={
                "email": "testuser123@gmail.com",
                "password": "password123"
            }
        )

        print(response.json())

        assert response.status_code in [
            200,
            401
        ] 