docker pull rabbitmq:latest
docker pull redis:latest
docker build --rm -t oe_celery -f Dockerfile.oe .
rem rabbitmq            "docker-entrypoint.s…"   18 hours ago        Up 18 hours         4369/tcp, 5671-5672/tcp, 25672/tcp   rabbit-server

docker run --name redis-server -d redis
docker run -d -e RABBITMQ_NODENAME=my-rabbit --name rabbit-server rabbitmq
docker run -h oe_celery --name oe_celery --link redis-server --link rabbit-server -it -d oe_celery
