docker container rm -f bumps_worker1
rem docker build --rm -t bumps_celery -f celery_oe.dockerfile .
docker run -h bumps_worker1 --name bumps_worker1 --link redis-server -p 5672 --link rabbit-server -it -d bumps_celery
docker exec -it bumps_worker1 bash