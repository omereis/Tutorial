FROM ubuntu:14.04
# docker build -t richardbronosky/celery -f Dockerfile.rb .
#MAINTAINER Richard Bronosky <bruno@bronosky.com>
# the default image doesn't have python, so this is going to be a big install
RUN apt-get update && apt-get install -y python-pip man vim
RUN pip install --upgrade pip
# remove this next line when development is done
RUN apt-get update && apt-get install -y tmux vim git iputils-ping
RUN pip install -U https://github.com/RichardBronosky/celery_test/archive/master.zip
RUN mkdir /home/root
RUN mkdir /home/root/celery
COPY Source\* /home/root/celery

RUN pip install redis
#USER nobody
#ENTRYPOINT bash
#ENTRYPOINT celery -A celery_test.tasks worker --loglevel=info
# celery -A tasks worker --loglevel=info

# docker build -t richardbronosky/celery:v4 -f Dockerfile.rb .
# docker run -t -i --link rabbit-server:rabbit richardbronosky/celery:v4