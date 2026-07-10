from backend.benchmark.metrics import metrics_collector

metrics_collector.add_metrics(
    requests_per_second=320,
    average_latency_ms=145,
    ai_cost_per_request=0.0021,
    rag_accuracy=0.94,
    agent_success_rate=0.98,
    cache_hit_ratio=0.91,
)

print(metrics_collector.latest()) 