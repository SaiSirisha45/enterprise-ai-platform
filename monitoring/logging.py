import logging
import sys

from pythonjsonlogger import jsonlogger


def setup_logger():

    logger = logging.getLogger("enterprise-ai")

    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)

    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.propagate = False

    return logger


logger = setup_logger() 