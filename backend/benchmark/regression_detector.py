class RegressionDetector:

    def compare(self, previous, current):

        report = {}

        # Latency
        if current["average_latency_ms"] > previous["average_latency_ms"]:
            report["latency"] = "Regression"
        elif current["average_latency_ms"] < previous["average_latency_ms"]:
            report["latency"] = "Improved"
        else:
            report["latency"] = "Stable"

        # Requests per second
        if current["requests_per_second"] > previous["requests_per_second"]:
            report["throughput"] = "Improved"
        elif current["requests_per_second"] < previous["requests_per_second"]:
            report["throughput"] = "Regression"
        else:
            report["throughput"] = "Stable"

        # AI Cost
        if current["ai_cost_per_request"] < previous["ai_cost_per_request"]:
            report["cost"] = "Improved"
        elif current["ai_cost_per_request"] > previous["ai_cost_per_request"]:
            report["cost"] = "Regression"
        else:
            report["cost"] = "Stable"

        return report


regression_detector = RegressionDetector() 