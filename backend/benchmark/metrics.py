from dataclasses import dataclass, asdict


@dataclass
class BenchmarkMetrics:
    requests_per_second: float
    average_latency_ms: float
    ai_cost_per_request: float
    rag_accuracy: float
    agent_success_rate: float
    cache_hit_ratio: float


class MetricsCollector:

    def __init__(self):
        self.metrics = []

    def add_metrics(
        self,
        requests_per_second,
        average_latency_ms,
        ai_cost_per_request,
        rag_accuracy,
        agent_success_rate,
        cache_hit_ratio,
    ):

        metric = BenchmarkMetrics(
            requests_per_second=requests_per_second,
            average_latency_ms=average_latency_ms,
            ai_cost_per_request=ai_cost_per_request,
            rag_accuracy=rag_accuracy,
            agent_success_rate=agent_success_rate,
            cache_hit_ratio=cache_hit_ratio,
        )

        self.metrics.append(metric)

    def latest(self):

        if not self.metrics:
            return None

        return asdict(self.metrics[-1])

    def all_metrics(self):

        return [asdict(m) for m in self.metrics]


metrics_collector = MetricsCollector() 