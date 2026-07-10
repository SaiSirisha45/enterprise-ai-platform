from backend.benchmark.capacity_forecast import capacity_forecast

forecast = capacity_forecast.forecast(
    current_requests_per_day=100000,
    monthly_growth_percent=15,
    months=6
)

for month in forecast:
    print(month) 