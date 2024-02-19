from django.shortcuts import reverse
from django.test.client import Client


def test_get_weather_data_api(client: Client):
    response = client.get(
        reverse("weather_api:get_data", kwargs={"city": "Lviv"})
    )
    assert response.status_code == 200
