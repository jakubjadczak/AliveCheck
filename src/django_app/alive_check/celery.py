import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alive_check.settings")

app = Celery("alive_check", broker="pyamqp://guest@localhost//")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# @app.task
# def process_database():
#     # Tutaj dodaj logikę przetwarzania wszystkich obiektów z bazy danych
#     print("Processing database...")

# # Dodanie harmonogramu do przetwarzania zadania co 10 minut
# app.conf.beat_schedule = {
#     'process-every-10-minutes': {
#         'task': 'celery_app.process_database',
#         'schedule': 600.0  # 10 minut
#     },
# }
# app.conf.timezone = 'UTC'


@app.task
def add(x, y):
    return x + y
