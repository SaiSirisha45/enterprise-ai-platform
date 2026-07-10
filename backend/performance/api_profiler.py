import time
import psutil
from functools import wraps


class APIProfiler:


    def __init__(self):

        self.metrics = []



    def profile(self, api_name):

        def decorator(func):

            @wraps(func)
            def wrapper(*args, **kwargs):

                process = psutil.Process()

                start_time = time.time()

                start_memory = (
                    process.memory_info().rss
                    /
                    1024
                    /
                    1024
                )


                result = func(
                    *args,
                    **kwargs
                )


                end_time = time.time()

                end_memory = (
                    process.memory_info().rss
                    /
                    1024
                    /
                    1024
                )


                response_time = (
                    end_time - start_time
                )


                cpu_usage = (
                    process.cpu_percent()
                )


                metric = {

                    "api":
                    api_name,

                    "response_time_seconds":
                    round(response_time,4),

                    "cpu_usage_percent":
                    cpu_usage,

                    "memory_usage_mb":
                    round(
                        end_memory-start_memory,
                        2
                    ),

                    "database_queries":
                    0,

                    "token_usage":
                    0
                }


                self.metrics.append(metric)


                return result


            return wrapper

        return decorator



    def get_report(self):

        return self.metrics



profiler = APIProfiler() 