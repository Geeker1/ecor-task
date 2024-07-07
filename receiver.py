import os
import sys
import time
import pika 

from logger import logger as log

QUEUE_NAME = os.getenv("QUEUE_NAME")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")


def callback(channel, method, properties, body):
    log.info(body.decode("utf-8"))


def main():
    time.sleep(6) # 6s delay for rabbitmq to start up properly before connecting
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, port=RABBITMQ_PORT))

    channel = connection.channel()

    # For this case, declare queue again to avoid exception.
    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=callback)

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.info("System was interrupted")
        sys.exit(0)
