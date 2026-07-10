from datetime import datetime


class Tenant:

    def __init__(
        self,
        tenant_id,
        name,
        description
    ):
        self.tenant_id = tenant_id
        self.name = name
        self.description = description
        self.created_at = datetime.utcnow()



class TenantUser:

    def __init__(
        self,
        user_id,
        tenant_id,
        role
    ):
        self.user_id = user_id
        self.tenant_id = tenant_id
        self.role = role



class TenantDocument:

    def __init__(
        self,
        document_id,
        tenant_id,
        title
    ):
        self.document_id = document_id
        self.tenant_id = tenant_id
        self.title = title 