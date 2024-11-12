import logging
import os

import django
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

User = get_user_model()

username = os.getenv("SUPERUSER_USERNAME", "user_" + get_random_string(8))
email = os.getenv("SUPERUSER_EMAIL", "default@example.com")
password = os.getenv("SUPERUSER_PASSWORD", get_random_string(12))

if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    logger.info(f"Superuser created with username: {username} and password: {password}")
else:
    logger.info("Superuser already exists.")
