import os
import psutil
import requests
from monitoring.logging import logger

# Read configuration from environment variables
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")
ALERT_EMAIL = os.getenv("ALERT_EMAIL")


def send_slack_alert(message: str):
    """Send alert to Slack if webhook is configured."""
    if not SLACK_WEBHOOK:
        logger.warning("Slack webhook not configured.")
        return

    payload = {"text": message}

    try:
        requests.post(SLACK_WEBHOOK, json=payload, timeout=5)
        logger.info("Slack alert sent.")
    except Exception as e:
        logger.exception(f"Failed to send Slack alert: {e}")


def send_email_alert(subject: str, body: str):
    """
    Placeholder for email alerts.
    Integrate SMTP or SendGrid later.
    """
    logger.info(
        "Email alert triggered",
        extra={
            "subject": subject,
            "body": body,
        },
    )


def check_system_health():
    """Monitor CPU and memory usage."""

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    if cpu > 80:
        message = f"🚨 High CPU Usage: {cpu}%"
        logger.warning(message)
        send_slack_alert(message)

    if memory > 80:
        message = f"🚨 High Memory Usage: {memory}%"
        logger.warning(message)
        send_slack_alert(message) 
        
def agent_failed(agent_id: str):
    message = f"❌ Agent Failed: {agent_id}"
    logger.error(message)
    send_slack_alert(message)


def workflow_failed(workflow_id: str):
    message = f"❌ Workflow Failed: {workflow_id}"
    logger.error(message)
    send_slack_alert(message)


def high_error_rate():
    message = "🚨 High Error Rate Detected"
    logger.error(message)
    send_slack_alert(message)


def slow_response(endpoint: str):
    message = f"🐢 Slow Response: {endpoint}"
    logger.warning(message)
    send_slack_alert(message)         