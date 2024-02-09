from django.urls import path

from api.v1 import views

app_name = 'weather_api'

urlpatterns = [
    path("get/<str:city>/<int:date>", views.WeatherData.as_view()),
    path("get_data/<str:city>/", views.APIWeatherData.as_view()),
]
