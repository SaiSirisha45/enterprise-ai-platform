from backend.tools.base_tool import BaseTool, retry


class LeaveTool(BaseTool):

    @retry()
    def execute(self, payload):

        self.authenticate(payload["token"])

        self.authorize(
            payload["role"],
            ["employee", "manager", "admin"]
        )

        self.validate(payload)

        self.log("Leave Tool Executed Successfully")

        return {
            "status": "success",
            "message": "Leave request processed."
        }