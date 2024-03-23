from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# set today
today = datetime.today().date()

# scheduler configuration
app.conf.beat_schedule = {
    "periodic_task": {
        "task": "analytics.tasks.calculate_daily_order_summary",
        "schedule": crontab(hour=0, minute=1),
        # "schedule": 10,
        "args": {today - timedelta(days=1)},
    }
}
