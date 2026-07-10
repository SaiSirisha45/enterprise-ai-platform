from backend.benchmark.benchmark_runner import benchmark_runner
from backend.benchmark.dashboard_generator import dashboard_generator

benchmark_runner.run()

print(dashboard_generator.generate())