import pika
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from db_conn import fetch
from dotenv import load_dotenv
import os
import json

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
        data = {"id": a[0], "ip_address": a[1]}
        json_data = json.dumps(data)
        channel.queue_declare(queue="ip_addresses")
        channel.basic_publish(
            exchange="",
            routing_key="ip_addresses",
            body=json_data,
            properties=pika.BasicProperties(content_type="application/json"),
        )

    connection.close()


app.conf.beat_schedule = {
    "print-every-minute": {
        "task": "tasks.send_msg",  # module.func
        "schedule": 60.0,
    },
}
