from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from users.forms import UserForm
from users.utils import check_access_token


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "users/login.html")
