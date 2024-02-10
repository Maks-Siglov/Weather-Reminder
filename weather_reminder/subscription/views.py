from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from users.utils import check_access_token


@check_access_token
def subscription_list(request: HttpRequest) -> HttpResponse:
    return render(request, "subscription/subscriptions.html")
