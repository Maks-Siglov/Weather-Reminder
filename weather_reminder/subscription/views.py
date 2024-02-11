from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def subscription_list(request: HttpRequest) -> HttpResponse:
    return render(request, "subscription/subscriptions.html")


def create_subscription(request: HttpRequest) -> HttpResponse:
    return render(request, "subscription/create_subscription.html")
