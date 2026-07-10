from backend.multitenancy.tenant_audit import audit_manager



audit_manager.record(

    "tenant_hr",

    "user_101",

    "VIEW_DOCUMENT",

    "employee_policy.pdf"

)



audit_manager.record(

    "tenant_engineering",

    "user_202",

    "SEARCH",

    "api_design.pdf"

)



logs = audit_manager.get_logs(
    "tenant_hr"
)



print(logs) 