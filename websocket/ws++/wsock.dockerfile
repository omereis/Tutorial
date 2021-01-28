# Using the latest long-term-support Ubuntu OS
FROM ubuntu:18.04

RUN apt -y update
RUN apt -y upgrade
# RUN apt install -y software-properties-common
#  RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y vim man tree curl git wget cmake
#RUN apt install -y build-essential

RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update -y &&\
	apt install -y python3.7
RUN apt install -y python3.7-distutils
RUN mkdir -p /tmp/pip && cd /tmp/pip && wget https://bootstrap.pypa.io/get-pip.py
RUN ln -s /usr/bin/python3.7 /usr/bin/python
RUN python3.7 /tmp/pip/get-pip.py

RUN pip install asyncio websockets websocket-client 
# RUN pip install websockets websocket 

ENV HOME=/home/oe/
#ENV CPLUS_INCLUDE_PATH=/home/oe/websocketpp/
COPY ./ /home/oe
WORKDIR /home/oe

EXPOSE 5000
