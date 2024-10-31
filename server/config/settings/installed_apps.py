INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    "rest_framework",
    'rest_framework_simplejwt',
    "drf_spectacular",
]


LOCAL_APPS = [
    "apps.federations",
]

INSTALLED_APPS += LOCAL_APPS

LOCAL_MIGRATIONS = [app_path.split(".")[-1] for app_path in LOCAL_APPS]

MIGRATION_PATH = "config.migrations."  # Path to the centralised migration dir

MIGRATION_MODULES = {
    app_name: MIGRATION_PATH + app_name for app_name in LOCAL_MIGRATIONS
}
