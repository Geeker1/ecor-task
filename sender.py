import os
import time
import pika 
import uuid
import datetime
import json

from logger import logger as log

QUEUE_NAME = os.getenv("QUEUE_NAME")
ROUTING_KEY = os.getenv("ROUTING_KEY")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")

SLEEP_DURATION = int(os.getenv("SLEEP_DURATION"))

EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "")


def generate_message():
    # Returns a json object with keys `message_id` and `created_on`.
    message_id = uuid.uuid4()
    created_on = str(datetime.datetime.now())

    data = {
        "message_id": str(message_id),
        "created_on": created_on
    }

    return data

def main():
    time.sleep(6) # 6s delay for rabbitmq to start up properly
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, port=RABBITMQ_PORT))

    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    while True:
        time.sleep(SLEEP_DURATION)

        message = generate_message()

        dump_message = json.dumps(message)

        # Log message before return it
        log.info("PUBLISHER: " + dump_message)

        channel.basic_publish(EXCHANGE, routing_key=ROUTING_KEY, body=dump_message)

if __name__ == "__main__":
    main()
