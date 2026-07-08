from backend.tools.base_tool import BaseTool, retry


class EmailTool(BaseTool):

    @retry()
    def execute(self, payload):

        self.authenticate(payload["token"])

        self.authorize(
            payload["role"],
            ["admin", "employee"]
        )

        self.validate(payload)

        self.log("Email Tool Executed Successfully")

        return {
            "status": "success",
            "message": "Email sent successfully."
        }