from core.settings.base import *

DEBUG = True

ALLOWED_HOSTS += ["localhost", "127.0.0.1"]

DOMAIN = "localhost:8000"


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
