from core.settings.base import *

DEBUG = True

ALLOWED_HOSTS += ["*"]

DOMAIN = "localhost:8000" #for docker 172.19.0.1:8000


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}
