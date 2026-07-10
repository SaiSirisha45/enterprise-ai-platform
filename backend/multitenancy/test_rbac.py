from backend.multitenancy.tenant_rbac import rbac



print(
    rbac.check_permission(
        "admin",
        "delete_document"
    )
)


print(
    rbac.check_permission(
        "viewer",
        "delete_document"
    )
)


print(
    rbac.check_permission(
        "user",
        "chat"
    )
) 