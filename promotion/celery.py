from __future__ import absolute_import
import os

from celery import Celery
from promotion.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "promotion.settings.development")

app = Celery("promotion")

app.config_from_object("promotion.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)