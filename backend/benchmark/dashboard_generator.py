from backend.benchmark.metrics import metrics_collector


class DashboardGenerator:

    def generate(self):

        latest = metrics_collector.latest()

        if latest is None:
            return "No benchmark data available."

        dashboard = f"""
===============================
Enterprise Benchmark Dashboard
===============================

Requests/Second     : {latest['requests_per_second']}
Average Latency(ms) : {latest['average_latency_ms']}
AI Cost/Request($)  : {latest['ai_cost_per_request']}
RAG Accuracy        : {latest['rag_accuracy']}
Agent Success Rate  : {latest['agent_success_rate']}
Cache Hit Ratio     : {latest['cache_hit_ratio']}
"""

        return dashboard


dashboard_generator = DashboardGenerator() 