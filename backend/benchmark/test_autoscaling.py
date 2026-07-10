from backend.benchmark.autoscaling_validator import autoscaling_validator

result = autoscaling_validator.validate(
    cpu_usage_percent=85,
    requests_per_second=1200
)

print(result) 