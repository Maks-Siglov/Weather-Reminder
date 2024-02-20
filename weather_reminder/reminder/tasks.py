import requests
import typing as t

from datetime import datetime
from threading import Thread

from celery import shared_task
from celery.signals import task_success

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@shared_task
def send_subscription_email():
    subscriptions = requests.get(
        f"http://{settings.DOMAIN}/api/weather-data/v1/get_subscription/"
    ).json()
    threads = []
    for subscription in subscriptions:
        thread = Thread(target=make_notification, args=(subscription,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return subscriptions


@shared_task
def make_notification(subscription: dict[str, t.Any]) -> None:
    weather_data = get_weather_data(subscription["city"])
    send_email(subscription, weather_data)


@shared_task
def get_weather_data(city: str):
    url = (
        f"{settings.API_URL}?"
        f"appid={settings.OPEN_WEATHER_KEY}&"
        f"units={settings.DEFAULT_UNITS}"
        f"&q={city}"
    )
    response = requests.get(url)
    data = response.json()
    weather_data = data["list"][0]
    return weather_data


@shared_task
def send_email(
    subscription: dict[str, t.Any], weather_data: dict[str, t.Any]
) -> None:
    dt = datetime.utcfromtimestamp(int(weather_data["dt"])).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    email_context = {
        "city": subscription["city"],
        "dt_txt": dt,
        "main": weather_data["main"],
        "weather_description": weather_data["weather"][0]["description"],
        "wind_speed": weather_data["wind"]["speed"],
        "humidity": weather_data["main"]["humidity"],
        "cloudiness": weather_data["clouds"]["all"],
    }
    email_body = render_to_string("emails/reminder_email.html", email_context)

    mail = EmailMessage(
        subject="Weather Reminder",
        body=email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=(subscription["user_email"],),
    )
    mail.send()


@task_success.connect(sender="reminder.tasks.send_subscription_email")
def update_last_notification_time(subscriptions, **kwargs) -> None:
    subscription_ids = []
    for subscription in subscriptions:
        subscription_ids.append(subscription["pk"])
    requests.post(
        f"http://{settings.DOMAIN}/api/weather-data/v1/"
        f"update-last-notification-time/",
        json={"subscription_ids": subscription_ids},
    )
