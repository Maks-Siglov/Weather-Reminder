from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from users.utils import check_access_token


@check_access_token
def subscriptions(request: HttpRequest) -> HttpResponse:
    print(request.user)
    return render(request, "subscription/subscriptions.html")
