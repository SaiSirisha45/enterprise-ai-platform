from backend.benchmark.regression_detector import regression_detector

previous = {
    "requests_per_second": 300,
    "average_latency_ms": 150,
    "ai_cost_per_request": 0.0030
}

current = {
    "requests_per_second": 360,
    "average_latency_ms": 120,
    "ai_cost_per_request": 0.0022
}

report = regression_detector.compare(previous, current)

print(report) 