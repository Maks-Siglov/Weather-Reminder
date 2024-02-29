from django.urls import path

from users.api.v1 import views

app_name = "auth_api"

urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
]
