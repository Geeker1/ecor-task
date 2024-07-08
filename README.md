# ECOR TASK

This is a simple task to test a simple PUB-SUB system with RabbitMQ, Python and Docker.

## INSTRUCTIONS
This system is made up of three components.

- Publisher: Sends Messages to the Queue
- Queue(RabbitMQ): Stores Messages from publisher and sends to consumers
- Consumer: Receives messages from queue

Each component here represent a docker service as defined in docker-compose.yaml file
`rabbitmq`, `publisher` and `consumer`.

### DOCKER
To test application, ensure you have docker and docker compose installed on your system.

https://docs.docker.com/engine/install/
https://docs.docker.com/compose/install/

Docker compose comes with docker so you might not need to install it seperately.

Run `docker compose build` to build images for each service.

Before you start services, there are environment variables to take note of which configure each service
The defaults in `.env` file should be enough to test this project.

- *SLEEP_DURATION*: 10
- *QUEUE_NAME*: "ecor"
- *ROUTING_KEY*: "ecor"
- *RABBITMQ_HOST*: "rabbitmq"
- *RABBITMQ_PORT*: 5672

__NOTE: `QUEUE_NAME`, `RABBITMQ_HOST` and `RABBITMQ_PORT` should be same for publisher & consumer service__

Run `docker compose up publisher consumer` to start the publisher and consumer services.

__NOTE: There is an initial 6s delay on `publisher` and `consumer` services. This is to ensure `rabbitmq` service starts properly before we attempt connection.__


Monitor logs for each service to ensure messages are being sent and received using right queue according to `SLEEP_DURATION`.

If you want to monitor changes in different terminals, you could run 

`docker compose up publisher` - terminal 1
`docker compose up consumer` - terminal 2

Then monitor logs as needed.
