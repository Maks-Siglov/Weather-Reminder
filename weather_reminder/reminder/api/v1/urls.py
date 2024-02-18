from django.urls import path

from reminder.api.v1 import views

app_name = "weather_api"

urlpatterns = [
    path(
        "get_data/<str:city>/", views.APIWeatherData.as_view(), name="get_data"
    ),
    path(
        "send_email/<int:user_id>",
        views.SendWeatherEmail.as_view(),
        name="send_email",
    ),
    path(
        "get_subscription/",
        views.NotificationSubscription.as_view(),
        name="get_subscription",
    ),
]
