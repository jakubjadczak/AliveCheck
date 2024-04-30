import pika, sys, os
from dotenv import load_dotenv
from ip_ping import ping_ip
from utils import byte_string_to_dict
from db_conn import insert_stat

load_dotenv()


def main():
    credentials = pika.PlainCredentials(
        os.getenv("RABBITMQ_DEFAULT_USER"), os.getenv("RABBITMQ_DEFAULT_PASS")
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            os.getenv("RABBITMQ_HOST"), os.getenv("RABBITMQ_PORT"), "/", credentials
        )
    )
    channel = connection.channel()

    channel.queue_declare(queue=os.getenv("IP_QUEUE"))

    def callback(ch, method, properties, body):
        data = byte_string_to_dict(body)
        response = ping_ip(data["ip_address"], data["id"])
        print(response)
        insert_stat(response)

    channel.basic_consume(
        queue=os.getenv("IP_QUEUE"), on_message_callback=callback, auto_ack=True
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
