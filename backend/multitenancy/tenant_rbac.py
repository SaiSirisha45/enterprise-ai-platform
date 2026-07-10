from enum import Enum


class Role(Enum):

    ADMIN = "admin"
    USER = "user"
    VIEWER = "viewer"



class TenantRBAC:


    permissions = {


        "admin": [
            "create_document",
            "delete_document",
            "update_document",
            "search",
            "chat"
        ],


        "user": [
            "search",
            "chat"
        ],


        "viewer": [
            "search"
        ]

    }



    def check_permission(
        self,
        role,
        action
    ):

        allowed_actions = self.permissions.get(
            role
        )


        if not allowed_actions:
            return False


        return action in allowed_actions



rbac = TenantRBAC() 