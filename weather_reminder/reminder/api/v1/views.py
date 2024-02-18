import requests

from django.conf import settings
from django.db.models import ExpressionWrapper, F, DurationField, IntegerField
from django.db.models.functions import ExtractHour, ExtractMinute, ExtractDay
from django.http import HttpRequest
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView

from reminder.api.v1.serializers import UserSubscriptionSerializer

from subscription.models import Subscription


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


class NotificationSubscription(APIView):
    def get(self, request: HttpRequest):
        notification_time = timezone.now()

        time_difference_expression = ExpressionWrapper(
            notification_time - F("last_notification_time"),
            output_field=DurationField(),
        )
        subscriptions_with_time_dif = Subscription.objects.annotate(
            time_difference_hours=ExpressionWrapper(
                ExtractDay(time_difference_expression) * 24
                + ExtractHour(time_difference_expression)
                + ExtractMinute(time_difference_expression) / 60,
                output_field=IntegerField(),
            )
        )
        subscriptions = subscriptions_with_time_dif.filter(
            is_enabled=True,
            time_difference_hours__gte=F("notification_period"),
        )
        serializer = UserSubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)
