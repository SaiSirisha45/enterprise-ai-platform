class CapacityForecast:

    def forecast(
        self,
        current_requests_per_day,
        monthly_growth_percent,
        months
    ):
        forecasts = []

        requests = current_requests_per_day

        for month in range(1, months + 1):
            requests = requests * (1 + monthly_growth_percent / 100)

            forecasts.append({
                "month": month,
                "estimated_requests_per_day": int(requests)
            })

        return forecasts


capacity_forecast = CapacityForecast()