from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from backend.multitenancy.tenant_manager import tenant_manager


class TenantMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next
    ):

        tenant_id = request.headers.get(
            "tenant-id"
        )


        if tenant_id:

            tenant = tenant_manager.get_tenant(
                tenant_id
            )

            if tenant:

                request.state.tenant = tenant

            else:

                request.state.tenant = None

        else:

            request.state.tenant = None


        response = await call_next(
            request
        )

        return response 