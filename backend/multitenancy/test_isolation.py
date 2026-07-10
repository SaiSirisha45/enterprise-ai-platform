from backend.multitenancy.tenant_knowledge import knowledge_base



# HR documents

knowledge_base.add_document(
    "tenant_hr",
    "employee_leave_policy.pdf"
)


knowledge_base.add_document(
    "tenant_hr",
    "salary_policy.pdf"
)



# Engineering documents

knowledge_base.add_document(
    "tenant_engineering",
    "python_api_design.pdf"
)


knowledge_base.add_document(
    "tenant_engineering",
    "database_architecture.pdf"
)




# HR search

hr_result = knowledge_base.search(
    "tenant_hr",
    "policy"
)



# Engineering search

eng_result = knowledge_base.search(
    "tenant_engineering",
    "policy"
)



print(
    "HR:",
    hr_result
)


print(
    "Engineering:",
    eng_result
) 