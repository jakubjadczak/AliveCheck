import pika
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from db_conn import fetch
from dotenv import load_dotenv
import os

load_dotenv()

logger = get_task_logger(__name__)

app = Celery("tasks", broker="pyamqp://admin:admin@rabbitmq//")


@app.task
def send_msg():
    credentials = pika.PlainCredentials("admin", "admin")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("rabbitmq", 5672, "/", credentials)
    )
    channel = connection.channel()

    array = fetch()
    for a in array:
        channel.queue_declare(queue="ip_addresses")
        channel.basic_publish(exchange="", routing_key="ip_addresses", body=f"{a[1]}")

    connection.close()


app.conf.beat_schedule = {
    "print-every-minute": {
        "task": "tasks.send_msg",  # module.func
        "schedule": 60.0,
    },
}
