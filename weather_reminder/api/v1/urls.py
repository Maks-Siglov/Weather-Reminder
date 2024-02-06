from django.urls import path

from api.v1 import views

urlpatterns = [
    path("get/<str:city>/<int:date>", views.WeatherData.as_view()),
]
