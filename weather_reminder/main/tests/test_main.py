from django.test.client import Client
from django.shortcuts import reverse


def test_main(client: Client):
    response = client.get(reverse("main:index"))
    assert response.status_code == 200
