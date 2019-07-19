FROM ubuntu:16.04
MAINTAINER Omer Eisenebrg <one4@nist.gov>
# docker build --rm -t oe_celery -f Dockerfile.oe .
# docker run -h oe_celery --name oe_celery --link redis-server -p 5672:5672 -it -d oe_celery
# docker run -h oe_celery --name oe_celery --link redis-server --link rabbit-server -it -d oe_celery
# the default image doesn't have python, so this is going to be a big install
# celery -A tasks worker --loglevel=info
RUN apt-get update && apt-get install -y man vim

RUN apt install -y python3.7
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3.7 /usr/bin/python
COPY get-pip.py /tmp
RUN apt install -y python3-distutils
RUN python /tmp/get-pip.py

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install redis
RUN pip install flask_redis
RUN pip install flask_jwt_extended
RUN pip install flask_restful
RUN pip install subprocess32
#RUN apt-get install -y man vim
RUN apt -y dist-upgrade
RUN apt install -y python2.7 python-pip
#RUN apt-get install -y rabbitmq-server
RUN apt-get install -y iputils-ping
RUN pip install celery
RUN pip install redis
RUN pip install flask_wtf
RUN apt-get install -y git
RUN pip install git+https://github.com/omereis/bumps.git
RUN pip install numpy
RUN pip install scipy
RUN pip install matplotlib
RUN pip install mpld3

#RUN ln -s /run/shm /dev/shm

RUN mkdir /home/root
RUN mkdir /home/root/celery
COPY Source\* /home/root/celery

RUN mkdir /home/root/celery/proj
COPY . /home/root/celery/
#COPY proj\* /home/root/celery/proj

RUN chmod a+x /home/root/celery/celery_test/run_tasks.sh
RUN chmod a+x /home/root/celery/proj/start_proj.sh
RUN chmod a+x /home/root/celery/proj/stop_proj.sh

ENV CELERY_RESULT_BACKEND='amqp'
ENV BROKER_URL='amqp://guest@rabbit.local//'

ENV LINES=45
ENV COLUMNS=100
 
#CMD rabbitmq-server start

WORKDIR /home/root/celery/