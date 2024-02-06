import json

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import serializers


class WeatherData(APIView):
    def get(self, request, city: str, date: int) -> Response:
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
        day_data = [day for day in city_data if day['date'] == date]
        if day_data is None:
            return Response(
                {"error": f"Weather data for {city} for {date} not found"},
                status=404
            )
        return Response(data=day_data, status=200)

