from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    from weather_reminder.reminder.tasks import send_weather_reminder_email
    send_weather_reminder_email()
    return render(request, "main/index.html")
