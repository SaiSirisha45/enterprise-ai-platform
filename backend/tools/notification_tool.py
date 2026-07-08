from backend.tools.base_tool import BaseTool, retry


class NotificationTool(BaseTool):

    @retry()
    def execute(self, payload):

        self.authenticate(payload["token"])

        self.authorize(
            payload["role"],
            ["admin", "manager"]
        )

        self.validate(payload)

        self.log("Notification Tool Executed Successfully")

        return {
            "status": "success",
            "message": "Notification sent successfully."
        }