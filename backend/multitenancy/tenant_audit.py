from datetime import datetime


class AuditLog:


    def __init__(
        self,
        tenant_id,
        user_id,
        action,
        resource,
        status
    ):

        self.tenant_id = tenant_id
        self.user_id = user_id
        self.action = action
        self.resource = resource
        self.status = status
        self.timestamp = datetime.utcnow()



    def to_dict(self):

        return {

            "tenant_id": self.tenant_id,

            "user_id": self.user_id,

            "action": self.action,

            "resource": self.resource,

            "status": self.status,

            "timestamp":
                str(self.timestamp)

        }





class TenantAuditManager:


    def __init__(self):

        self.logs = []



    def record(
        self,
        tenant_id,
        user_id,
        action,
        resource,
        status="SUCCESS"
    ):


        log = AuditLog(

            tenant_id,

            user_id,

            action,

            resource,

            status

        )


        self.logs.append(log)


        return log



    def get_logs(
        self,
        tenant_id
    ):

        return [

            log.to_dict()

            for log in self.logs

            if log.tenant_id == tenant_id

        ]




audit_manager = TenantAuditManager() 