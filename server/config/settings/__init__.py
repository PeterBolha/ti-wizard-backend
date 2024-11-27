from .celery import app as celery_app
from .installed_apps import *
from .settings import *

__all__ = ("celery_app",)
