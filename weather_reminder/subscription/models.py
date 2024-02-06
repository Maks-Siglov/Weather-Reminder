from django.db import models


class Subscription(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    notification_period = models.PositiveIntegerField(default=24)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
