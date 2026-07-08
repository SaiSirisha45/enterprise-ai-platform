from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.routes import router as auth_router
from chat.routes import router as chat_router
from rag.routes import router as knowledge_router
from agents.routes import router as agents_router
from workflows.routes import router as workflow_router
from admin.routes import router as admin_router
from evaluation.routes import router as analytics_router

app = FastAPI(title="Enterprise AI Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5175",
        "http://localhost:5176",
        "http://127.0.0.1:5176",
        "http://localhost:5177",
        "http://127.0.0.1:5177",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(knowledge_router)
app.include_router(agents_router)
app.include_router(workflow_router)
app.include_router(admin_router)
app.include_router(analytics_router)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Platform Backend is Running!"
    } 