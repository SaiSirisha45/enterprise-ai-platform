from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

# ==========================================
# Routers
# ==========================================
from backend.auth.routes import router as auth_router
from backend.chat.routes import router as chat_router
from backend.rag.routes import router as knowledge_router
from backend.agents.routes import router as agents_router
from backend.workflows.routes import router as workflow_router
from backend.admin.routes import router as admin_router
from backend.evaluation.routes import router as analytics_router

# ==========================================
# Database
# ==========================================
from backend.database.database import Base, engine

# ==========================================
# Monitoring - Metrics
# ==========================================
from monitoring.metrics import (
    router as metrics_router,
    REQUEST_COUNT,
    ERROR_COUNT,
    REQUEST_LATENCY,
)

# ==========================================
# Monitoring - Logging
# ==========================================
from monitoring.logging import logger

# ==========================================
# Monitoring - Tracing
# ==========================================
from monitoring.tracing import tracer
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.trace.status import Status, StatusCode

# ==========================================
# Security - Rate Limiter
# ==========================================
from security.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

# ==========================================
# Create Database Tables
# ==========================================
Base.metadata.create_all(bind=engine)

# ==========================================
# Create FastAPI App
# ==========================================
app = FastAPI(
    title="Enterprise AI Platform API",
    version="1.0.0",
)

# ==========================================
# Rate Limiter
# ==========================================
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)
app.add_middleware(SlowAPIMiddleware)

# ==========================================
# OpenTelemetry
# ==========================================
FastAPIInstrumentor.instrument_app(app)

# ==========================================
# CORS
# ==========================================
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

# ==========================================
# Metrics + Logging + Tracing Middleware
# ==========================================
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):

    with tracer.start_as_current_span(
        f"{request.method} {request.url.path}"
    ) as span:

        start_time = time.time()

        REQUEST_COUNT.inc()

        logger.info(
            "Incoming Request",
            extra={
                "method": request.method,
                "path": request.url.path,
            },
        )

        try:

            response = await call_next(request)

            duration = time.time() - start_time

            REQUEST_LATENCY.observe(duration)

            if response.status_code >= 400:

                ERROR_COUNT.inc()

                logger.error(
                    "Request Failed",
                    extra={
                        "status": response.status_code,
                        "path": request.url.path,
                    },
                )

            if duration > 2:

                logger.warning(
                    "Slow Request",
                    extra={
                        "duration": round(duration, 2),
                        "path": request.url.path,
                    },
                )

            return response

        except Exception as e:

            ERROR_COUNT.inc()

            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR))

            logger.exception("Unhandled Exception")

            raise

# ==========================================
# Register Routers
# ==========================================

# Monitoring
app.include_router(metrics_router)

# Authentication
app.include_router(auth_router)

# Chat
app.include_router(chat_router)

# Knowledge
app.include_router(knowledge_router)

# Agents
app.include_router(agents_router)

# Workflow
app.include_router(workflow_router)

# Admin
app.include_router(admin_router)

# Analytics
app.include_router(analytics_router)

# ==========================================
# Health Check
# ==========================================
@app.get("/")
@limiter.limit("20/minute")
async def root(request: Request):

    with tracer.start_as_current_span("Health Check"):

        logger.info("Health Check Endpoint Accessed")

        return {
            "message": "Enterprise AI Platform Backend is Running!",
            "status": "healthy",
            "version": "1.0.0",
        } 