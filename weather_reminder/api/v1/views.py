import json
import requests

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.http import HttpRequest

from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


class WeatherData(APIView):
    def get(self, request: HttpRequest, city: str, date: int) -> Response:
        try:
            with open("api/v1/mock_data/data.json") as f:
                weather_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return Response({"error": "Error during taking data"}, status=500)

        city_data = weather_data.get(city)
        if city_data is None:
            return Response(
                {"error": f"Weather data for {city} not found"}, status=404
            )
        day_data = [day for day in city_data if day["date"] == date]
        if day_data is None:
            return Response(
                {"error": f"Weather data for {city} for {date} not found"},
                status=404,
            )
        return Response(data=day_data, status=200)


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

        # weather_data=request.data
        print(request.data)

        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=404)

        mail = EmailMessage(
            subject="Weather Reminder",
            body=str(request.data),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=(user.email,),
        )
        mail.send()
        return Response({"message": "Email has been send"}, status=200)
