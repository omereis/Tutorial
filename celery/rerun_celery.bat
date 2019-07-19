docker container rm -f bumps_celery
docker build --rm -t bumps_celery -f celery_oe.dockerfile .
docker run -h bumps_celery --name bumps_celery --link redis-server -p 5672 --link rabbit-server -it -d bumps_celery
docker exec -it bumps_celery bash