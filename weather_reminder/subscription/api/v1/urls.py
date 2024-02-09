from django.urls import path

from subscription.api.v1 import views

urlpatterns = [
    path("create", views.Subscribe.as_view()),
    path("<int:subscription_id>/edit", views.Subscribe.as_view()),
    path("<int:subscription_id>/delete", views.Subscribe.as_view()),
    path("list/", views.SubscriptionList.as_view()),
]
