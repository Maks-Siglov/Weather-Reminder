# Generated by Django 5.0.1 on 2024-02-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscription", "0002_subscription_last_notification_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="is_enabled",
            field=models.BooleanField(default=True),
        ),
    ]
