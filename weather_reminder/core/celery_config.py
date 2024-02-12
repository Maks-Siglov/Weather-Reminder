import os

from celery import Celery
from celery.schedules import crontab

from reminder.tasks import send_weather_reminder_email

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "core.settings.base"
)

app = Celery("reminder", broker="amqp://guest:guest@localhost:5672/")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
CELERY_IMPORTS = ("reminder.tasks",)

app.conf.beat_schedule = {
    "send-weather-email-every-hour": {
        "task": "reminder.tasks.send_weather_reminder_email",
        "schedule": crontab(minute=0, hour="*"),
    },
}
