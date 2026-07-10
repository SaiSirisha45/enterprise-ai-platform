from backend.multitenancy.tenant_manager import tenant_manager


tenant_manager.create_tenant(
    "tenant_hr",
    "HR Department",
    "Human Resource Documents"
)


tenant_manager.create_tenant(
    "tenant_engineering",
    "Engineering",
    "Engineering Documents"
)


tenant = tenant_manager.get_tenant(
    "tenant_hr"
)


print(tenant.name)


print(
    len(
        tenant_manager.list_tenants()
    )
) 
