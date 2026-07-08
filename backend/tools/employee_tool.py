from backend.tools.base_tool import BaseTool, retry


class EmployeeTool(BaseTool):

    @retry()
    def execute(self, payload):

        self.authenticate(payload["token"])

        self.authorize(
            payload["role"],
            ["admin", "hr"]
        )

        self.validate(payload)

        self.log("Employee Tool Executed Successfully")

        return {
            "status": "success",
            "message": "Employee details retrieved."
        }