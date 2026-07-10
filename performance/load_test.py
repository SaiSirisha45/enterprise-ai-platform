from locust import HttpUser, task, between


class EnterpriseAIUser(HttpUser):

    wait_time = between(1, 2)

    # ------------------------
    # Login API
    # ------------------------
    @task(2)
    def login(self):
        self.client.post(
            "/auth/login",
            json={
                "email": "charan@gmail.com",
                "password": "charan123"
            }
        )

    # ------------------------
    # Chat API
    # ------------------------
    @task(3)
    def chat(self):
        self.client.post(
            "/chat/",
            json={
                "message": "Hello Enterprise AI"
            }
        )

    # ------------------------
    # Chat History
    # ------------------------
    @task(2)
    def chat_history(self):
        self.client.get("/chat/history")

    # ------------------------
    # Knowledge API
    # ------------------------
    @task(2)
    def knowledge(self):
        self.client.get("/knowledge/") 