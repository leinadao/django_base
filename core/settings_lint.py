# -*- coding: utf-8 -*-
"""Django settings for pipeline linting."""

from .settings import *  # noqa: F401, F403.

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "lint.sqlite3",
    }
}
