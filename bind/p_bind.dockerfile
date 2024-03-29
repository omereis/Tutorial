# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y libzmq3-dev
RUN apt install -y g++
RUN apt install -y vim man
RUN apt install -y tree curl
RUN apt install -y git wget cmake

RUN apt install -y iputils-ping
RUN apt install -y curl zip unzip tar

RUN apt update && apt install -y software-properties-common && add-apt-repository -y ppa:deadsnakes/ppa
RUN apt update && apt install -y python3.7

ENV HOME=/home/oe/binding

WORKDIR /home/oe/binding

COPY ./ $HOME

RUN python3.7 get-pip.py


RUN ln -s /usr/bin/python3.7 /usr/bin/python && \
	ln -s /usr/bin/pip3.7 /usr/bin/pip

# RUN pip install invoke
RUN pip install pyzmq

RUN mv vimrc .vimrc
