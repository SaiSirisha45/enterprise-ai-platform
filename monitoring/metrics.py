from fastapi import APIRouter, Response
from prometheus_client import (
    Counter,
    Histogram,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST,
)

router = APIRouter()


# ==========================
# APPLICATION METRICS
# ==========================

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP Requests"
)


ERROR_COUNT = Counter(
    "app_errors_total",
    "Total HTTP Errors"
)


REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "HTTP Request Latency"
)


ACTIVE_USERS = Gauge(
    "app_active_users",
    "Current Active Users"
)


# ==========================
# AI METRICS
# ==========================

TOKEN_USAGE = Counter(
    "ai_token_usage_total",
    "Total LLM Token Usage"
)


RAG_RETRIEVAL_TIME = Histogram(
    "rag_retrieval_time_seconds",
    "RAG Retrieval Time"
)


AGENT_EXECUTION_TIME = Histogram(
    "agent_execution_time_seconds",
    "Agent Execution Time"
)


TOOL_CALLS = Counter(
    "agent_tool_calls_total",
    "Agent Tool Calls"
)


# ==========================
# PROMETHEUS ENDPOINT
# ==========================

@router.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    ) 