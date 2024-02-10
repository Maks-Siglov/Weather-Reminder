from django.urls import path

from subscription.api.v1 import views

app_name = "subscription_api"

urlpatterns = [
    path("create", views.Subscribe.as_view(), name="create"),
    path("<int:subscription_id>/edit", views.Subscribe.as_view(), name="edit"),
    path(
        "<int:subscription_id>/delete",
        views.Subscribe.as_view(),
        name="delete",
    ),
    path("list/<str:email>", views.SubscriptionList.as_view(), name="list"),
]
