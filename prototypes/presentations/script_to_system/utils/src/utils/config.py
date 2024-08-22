import os

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
URL = f"http://localhost:8000?debug={str(DEBUG).lower()}"

DB_PATH = os.environ.get("DB_PATH")

ENABLE_PUSH_NOTIFICATIONS = os.environ.get("ENABLE_PUSH_NOTIFICATIONS", "True").lower() == "true"
PUSH_NOTIFICATION_CHANNEL = "m3XLomjaooQVYq9S3dkf"
PUSH_NOTIFICATION_NOTIFY_URL = f"https://notify.run/{PUSH_NOTIFICATION_CHANNEL}"
PUSH_NOTIFICATION_CHANNEL_URL = f"https://notify.run/c/{PUSH_NOTIFICATION_CHANNEL}"
