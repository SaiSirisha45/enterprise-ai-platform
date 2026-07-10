from fastapi import FastAPI, Request
from fastapi.testclient import TestClient

from backend.multitenancy.tenant_middleware import TenantMiddleware
from backend.multitenancy.tenant_manager import tenant_manager


app = FastAPI()


app.add_middleware(
    TenantMiddleware
)


tenant_manager.create_tenant(
    "tenant_hr",
    "HR Department",
    "HR Documents"
)



@app.get("/test")
def test(request: Request):

    if request.state.tenant:

        return {
            "tenant":
            request.state.tenant.name
        }

    return {
        "tenant": "None"
    }



client = TestClient(app)



response = client.get(
    "/test",
    headers={
        "tenant-id":"tenant_hr"
    }
)


print(response.json())