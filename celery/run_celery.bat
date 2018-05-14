docker pull rabbitmq:latest
docker pull redis:latest
docker build --rm -t oe_celery -f Dockerfile.oe .
docker build --rm -t celery_client -f Dockerfile.client .
rem rabbitmq            "docker-entrypoint.s…"   18 hours ago        Up 18 hours         4369/tcp, 5671-5672/tcp, 25672/tcp   rabbit-server

docker run -d --name redis-server redis
docker run -d --name rabbit-server rabbitmq
docker run -h oe_celery --name oe_celery --link redis-server --link rabbit-server -it -d oe_celery


rem celery with redis as broker
docker run --name -p 5671:5671 -p 5672:5672 -p 6379:6379 redis-server -d redis
docker run -h oe_celery --name oe_celery --link redis-server -it -d oe_celery
