from django.urls import path

from api.v1 import views

app_name = "weather_api"

urlpatterns = [
    path("get_data/<str:city>/", views.APIWeatherData.as_view()),
    path("send_email/<int:user_id>", views.SendWeatherEmail.as_view()),
]
