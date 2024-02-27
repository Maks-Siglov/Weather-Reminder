import pytest

from reminder.tasks import send_subscription_email


@pytest.mark.celery()
def test_send_subscription_email(celery_app, test_user_with_subscription):

    result = send_subscription_email.delay()

    assert result
