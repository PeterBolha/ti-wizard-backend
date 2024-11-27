import os

from celery import Celery

settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")

app = Celery("settings")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_routes = [
    [
        ("django_webhook.tasks.fire_webhook", {"queue": "webhooks"}),
    ],
]
app.autodiscover_tasks()
