from django.urls import path

from subscription import views

app_name = "subscription"

urlpatterns = [
    path("", views.subscriptions, name="subscriptions"),
]
