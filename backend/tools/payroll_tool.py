from backend.tools.base_tool import BaseTool, retry


class PayrollTool(BaseTool):

    @retry()
    def execute(self, payload):

        self.authenticate(payload["token"])

        self.authorize(
            payload["role"],
            ["admin", "finance"]
        )

        self.validate(payload)

        self.log("Payroll Tool Executed Successfully")

        return {
            "status": "success",
            "message": "Payroll information retrieved."
        }