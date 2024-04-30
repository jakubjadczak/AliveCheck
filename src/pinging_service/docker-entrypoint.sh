#!/bin/bash
set -e

wait_for_rabbitmq() {
    echo "Waiting for RabbitMQ..."
    while ! nc -z rabbitmq 5672; do
        sleep 1
    done
    echo "RabbitMQ is available!"
}

wait_for_rabbitmq

exec python mq_receiver.py
