import time

from celery.app import Celery
from celery.schedules import crontab

from config.config import setting

redis_url = setting.CELERY_BROKER_URL

celery_app = Celery(__name__, broker=redis_url, backend=redis_url)

celery_app.autodiscover_tasks(["app.parsing.tasks"])

celery_app.conf.beat_schedule = {
    "parse": {
        "task": "app.parsing.tasks.parsing",
        "schedule": crontab(),
        "args": (
            ("AAPL", "LTC", "EOS", "LUNA", "PPC", "SOL", "TRX", "BSV", "BCH", "TUSD"),
        ),
    }
}

celery_app.conf.timezone = "UTC"

if __name__ == "__main__":
    time.sleep(10)
    celery_app.start()
