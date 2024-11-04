# server/create_superuser.py
import os
import django
import logging
import argparse

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Create a Django superuser.')
parser.add_argument('--username', type=str, help='Username for the superuser')
parser.add_argument('--email', type=str, help='Email for the superuser')
parser.add_argument('--password', type=str, help='Password for the superuser')
args = parser.parse_args()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

User = get_user_model()

username = args.username if args.username else "user_" + get_random_string(8)
password = args.password if args.password else get_random_string(12)
email = args.email if args.email else f"{username}@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    logger.info(f"Superuser created with username: {username} and password: {password}")
else:
    logger.info("Superuser already exists.")