import pytest

from django.shortcuts import reverse
from django.test.client import Client

from subscription.models import Subscription
from users.models import User


@pytest.mark.django_db
def test_get_subscription_for_notification(
        client: Client, test_user_with_subscription: tuple[User, Subscription]
):
    response = client.get(reverse("weather_api:get_subscription"))
    assert response.status_code == 200
    assert len(response.json()) == 1
