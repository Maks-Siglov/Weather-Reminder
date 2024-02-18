import requests

from datetime import datetime

from celery import shared_task

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@shared_task
def send_subscription_email():
    subscriptions = requests.get(
        f"http://{settings.DOMAIN}/api/weather-data/v1/get_subscription/"
    ).json()
    for subscription in subscriptions:
        weather_data = get_weather_data(subscription["city"])
        send_email(subscription, weather_data)


@shared_task
def get_weather_data(city):
    return requests.get(
        f"http://{settings.DOMAIN}/api/weather-data/v1/get_data/{city}"
    ).json()


@shared_task
def send_email(subscription, weather_data):
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
