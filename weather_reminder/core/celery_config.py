import os

from celery import Celery
from celery.schedules import crontab

from reminder.tasks import send_subscription_email

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "core.settings.dev"
)

app = Celery("reminder", broker="amqp://guest:guest@localhost:5672/")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
CELERY_IMPORTS = ("reminder.tasks",)

send_subscription_email.delay()

# app.conf.beat_schedule = {
#     "send-weather-email-every-hour": {
#         "task": "reminder.tasks.send_subscription_email",
#         "schedule": crontab(minute=0, hour="*"),
#     },
# }
