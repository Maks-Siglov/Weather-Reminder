"""
URL configuration for Weather Reminder project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/v1/", include("users.api.v1.urls", namespace="auth_api")),
    path(
        "api/weather-data/v1/",
        include("reminder.api.v1.urls", namespace="weather_api"),
    ),
    path(
        "api/subscription/v1/",
        include("subscription.api.v1.urls", namespace="subscription_api"),
    ),
    path("", include("main.urls", namespace="main")),
    path(
        "subscriptions/",
        include("subscription.urls", namespace="subscription"),
    ),
    path("users/", include("users.urls", namespace="users")),
]
