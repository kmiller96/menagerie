from notify_run import Notify

from utils.config import PUSH_NOTIFICATION_NOTIFY_URL


def notify(*, title: str = "Eureka!", message: str):
    notification = Notify(endpoint=PUSH_NOTIFICATION_NOTIFY_URL)
    notification.send(f"[{title}] {message}")
