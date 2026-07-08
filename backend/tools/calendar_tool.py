from backend.tools.base_tool import BaseTool, retry


class CalendarTool(BaseTool):

    @retry()
    def execute(self, payload):

        self.authenticate(payload["token"])

        self.authorize(
            payload["role"],
            ["admin", "employee", "manager"]
        )

        self.validate(payload)

        self.log("Calendar Tool Executed Successfully")

        return {
            "status": "success",
            "message": "Calendar event created."
        }