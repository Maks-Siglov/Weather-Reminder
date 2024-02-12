import requests

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.http import HttpRequest

from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.services.send_reminder_email import send_reminder_email

from users.models import User


class APIWeatherData(APIView):
    def get(self, request: HttpRequest, city: str) -> Response:
        url = (
            f"{settings.API_URL}?"
            f"appid={settings.OPEN_WEATHER_KEY}&"
            f"units={settings.DEFAULT_UNITS}"
            f"&q={city}"
        )
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = data["list"][0]
            return Response(data=weather_data, status=200)

        return Response(status=404)


class SendWeatherEmail(APIView):
    def post(self, request: HttpRequest, user_id: int) -> Response:
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=404)

        send_reminder_email(request.data, user)

        return Response({"message": "Email has been send"}, status=200)
