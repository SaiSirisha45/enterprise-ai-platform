import logging
import time
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.error(f"Attempt {attempt}: {e}")
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


class BaseTool:

    def authenticate(self, token):
        if token != "valid_token":
            raise PermissionError("Authentication Failed")
        logging.info("Authentication Successful")

    def authorize(self, role, allowed_roles):
        if role not in allowed_roles:
            raise PermissionError("Authorization Failed")
        logging.info("Authorization Successful")

    def validate(self, payload):
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dictionary")
        logging.info("Validation Successful")

    def log(self, message):
        logging.info(message)