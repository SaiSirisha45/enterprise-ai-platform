from backend.tools.base_tool import BaseTool, retry


class ProjectTool(BaseTool):

    @retry()
    def execute(self, payload):

        self.authenticate(payload["token"])

        self.authorize(
            payload["role"],
            ["admin", "manager", "employee"]
        )

        self.validate(payload)

        self.log("Project Tool Executed Successfully")

        return {
            "status": "success",
            "message": "Project information retrieved."
        }