from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject2.settings")

app = Celery("djangoProject2", namespace='CELERY')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "cleardata": {
        "task": "newsapi.tasks.cleardata",
        "schedule": crontab(minute=0, hour=0),
    },
}
