import requests

from celery import shared_task

from django.conf import settings


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
    post_url = (
        f"http://{settings.DOMAIN}/api/weather-data/v1/send_email/"
        f"{subscription['user']}"
    )
    data = {"weather_data": weather_data, "city": subscription["city"]}
    requests.post(post_url, json=data)
