# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt -y update
RUN apt install -y python
RUN apt -y install python-pip
RUN apt install -y vim man
# RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN apt install -y tree

# RUN apt install -y python3-venv
RUN pip install flask

WORKDIR /home/oe/microblog
ENV HOME=/home/oe/microblog
COPY ./ /home/oe

ENV FLASK_APP=microblog.py

# Make the 5000 port available from outside the container
EXPOSE 5000


