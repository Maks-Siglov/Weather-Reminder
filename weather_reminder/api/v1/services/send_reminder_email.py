from datetime import datetime

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from users.models import User


def send_reminder_email(data: dict, user: User) -> None:
    weather_data = data["weather_data"]
    city = data["city"]

    dt = datetime.utcfromtimestamp(int(weather_data["dt"])).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    email_context = {
        "city": city,
        "dt_txt": dt,
        "main": weather_data["main"],
        "weather_description": weather_data["weather"][0]["description"],
        "wind_speed": weather_data["wind"]["speed"],
        "humidity": weather_data["main"]["humidity"],
        "cloudiness": weather_data["clouds"]["all"],
    }

    email_html = render_to_string("emails/reminder_email.html", email_context)

    mail = EmailMessage(
        subject="Weather Reminder",
        body=email_html,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=(user.email,),
    )
    mail.send()
