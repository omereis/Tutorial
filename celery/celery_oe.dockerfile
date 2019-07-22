FROM ubuntu:18.04
# MAINTAINER Omer Eisenebrg <one4@nist.gov>
# docker build --rm -t oe_celery -f Dockerfile.oe .
# docker run -h oe_celery --name oe_celery --link redis-server -p 5672:5672 -it -d oe_celery
# docker run -h oe_celery --name oe_celery --link redis-server --link rabbit-server -it -d oe_celery
# the default image doesn't have python, so this is going to be a big install
# celery -A tasks worker --loglevel=info
RUN apt-get update && apt-get install -y man vim

# RUN apt install -y python3.7
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y python3.7
RUN ln -s /usr/bin/python3.7 /usr/bin/python
COPY get-pip.py /tmp
RUN apt install -y python3-distutils
RUN python /tmp/get-pip.py

#RUN pip install flask
RUN pip install redis
#RUN pip install flask_redis
#RUN pip install flask_jwt_extended
#RUN pip install flask_restful
#RUN pip install subprocess32

RUN apt install -y iputils-ping git tree
RUN pip install celery
RUN pip install redis
#RUN pip install flask_wtf

#RUN pip install git+https://github.com/omereis/bumps.git
RUN pip install bumps numpy scipy matplotlib nest_asyncio
#RUN pip install numpy
#RUN pip install scipy
#RUN pip install matplotlib
#RUN pip install mpld3

ENV CELERY_RESULT_BACKEND='amqp'
ENV BROKER_URL='amqp://guest@rabbit.local//'


WORKDIR /home/bumps/celery/
COPY . /home/bumps/celery/
COPY vimrc /usr/share/vim/vimrc
