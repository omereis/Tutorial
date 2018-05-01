docker pull ubuntu:16.04
docker run -h celery_ubuntu --name celery_ubuntu -p 5672:5672 -it -d celery_ubuntu
docker run -it ubuntu bash

docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3

rem Unix
apt-get update -y
apt-get install -y man vim
apt -y dist-upgrade
apt install -y python2.7 python-pip
apt-get install -y rabbitmq-server
pip install celery
ln -s /run/shm /dev/shm

docker build -t rb_celery .

docker run --name rb_redis -d redis
docker run -d -e RABBITMQ_NODENAME=my-rabbit --name rabbit-server rabbitmq
	
docker run -d -t -i --link rabbit-server:rabbit --link rb_redis -h celery --name celery celery_redis

curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -

docker build -t richardbronosky/celery:v4 https://gist.githubusercontent.com/RichardBronosky/e81539af0d01fc455da2/raw/Dockerfile