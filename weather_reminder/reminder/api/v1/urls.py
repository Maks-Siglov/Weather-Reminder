from django.urls import path

from reminder.api.v1 import views

app_name = "weather_api"

urlpatterns = [
    path(
        "get_data/<str:city>/", views.APIWeatherData.as_view(), name="get_data"
    ),
    path(
        "get_subscription/",
        views.NotificationSubscription.as_view(),
        name="get_subscription",
    ),
]
