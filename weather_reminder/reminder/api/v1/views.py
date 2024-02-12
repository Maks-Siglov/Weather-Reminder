import requests

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView

from reminder.services.send_reminder_email import send_reminder_email
from subscription.models import Subscription

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
            weather_data = request.data["weather_data"]
            city = request.data["city"]
        except KeyError:
            return Response(
                {"error": "Missing required parameters)"}, status=422
            )
        try:
            user = User.objects.get(id=user_id)
            subscription = Subscription.objects.get(user=user, city=city)
        except ObjectDoesNotExist:
            return Response(
                {"error": "User or Subscription not found"}, status=404
            )

        send_reminder_email(weather_data, city, user)
        subscription.last_notification_time = timezone.now()
        subscription.save()

        return Response({"message": "Email has been send"}, status=200)
