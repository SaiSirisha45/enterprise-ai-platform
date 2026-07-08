from backend.tools.project_tool import ProjectTool
if __name__ == "__main__":

    tool = ProjectTool()

    payload = {
        "token": "valid_token",
        "role": "admin"
    }

    result = tool.execute(payload)

    print(result)