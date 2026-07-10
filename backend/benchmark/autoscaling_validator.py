class AutoScalingValidator:

    def validate(self, cpu_usage_percent, requests_per_second):

        if cpu_usage_percent > 80 or requests_per_second > 1000:
            return {
                "action": "Scale Up",
                "recommended_replicas": 5
            }

        elif cpu_usage_percent < 30 and requests_per_second < 200:
            return {
                "action": "Scale Down",
                "recommended_replicas": 2
            }

        return {
            "action": "No Scaling Required",
            "recommended_replicas": 3
        }


autoscaling_validator = AutoScalingValidator() 