import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "weather_reminder.core.settings.base"
)

app = Celery("weather_reminder")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-weather-email-every-hour": {
        "task": "weather_reminder.remider.tasks.send_weather_reminder_email",
        "schedule": crontab(minute=0, hour="*"),
    },
}
