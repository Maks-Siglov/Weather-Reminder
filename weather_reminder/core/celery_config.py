import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "core.settings.dev"
)

app = Celery("reminder")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = settings.CELERY_BROKER_URL

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-weather-email-every-hour": {
        "task": "reminder.tasks.send_subscription_email",
        "schedule": crontab(minute='*'),
    },
}
