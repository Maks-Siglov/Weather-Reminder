import requests

from celery import shared_task
from datetime import timedelta

from django.conf import settings
from django.utils import timezone


@shared_task
def send_weather_reminder_email():
    from subscription.models import Subscription

    subscription = Subscription.objects.all()
    current_time = timezone.now()

    for subscription in subscription:
        if current_time - subscription.last_notification_time >= timedelta(
            hours=subscription.notification_period
        ):
            weather_data = get_weather_data(subscription.city)
            post_url = (
                f"http://{settings.DOMAIN}/api/weather-data/v1/send_email/"
                f"{subscription.user.id}"
            )

            payload = {"weather_data": weather_data, "city": subscription.city}

            requests.post(post_url, json=payload)


def get_weather_data(city):
    url = f"http://{settings.DOMAIN}/api/weather-data/v1/get_data/{city}"
    return requests.get(url).json()
