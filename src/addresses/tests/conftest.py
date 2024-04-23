import django
from django.conf import settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def pytest_configure():
    if not settings.configured:
        settings.configure(
            # Minimalna konfiguracja wymagana do uruchomienia testów Django
            INSTALLED_APPS=[
                "django.contrib.admin",
                "django.contrib.auth",
                "django.contrib.contenttypes",
                "django.contrib.sessions",
                "django.contrib.messages",
                "django.contrib.staticfiles",
                "main",
                "users",
                "addresses",
                "django_bootstrap_icons",
                "crispy_forms",
                "crispy_bootstrap5",
                "django_extensions",
            ],
            DATABASES={
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": BASE_DIR / "db.sqlite3",
                }
            },
            # Wszystkie inne potrzebne ustawienia
            USE_TZ=True,
        )
        django.setup()
