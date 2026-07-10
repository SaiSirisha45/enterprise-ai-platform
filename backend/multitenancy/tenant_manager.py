from backend.multitenancy.tenant_models import Tenant


class TenantManager:

    def __init__(self):
        self.tenants = {}


    def create_tenant(
        self,
        tenant_id,
        name,
        description
    ):

        tenant = Tenant(
            tenant_id,
            name,
            description
        )

        self.tenants[tenant_id] = tenant

        return tenant



    def get_tenant(
        self,
        tenant_id
    ):

        return self.tenants.get(tenant_id)



    def list_tenants(self):

        return list(self.tenants.values())



# Global tenant manager

tenant_manager = TenantManager() 