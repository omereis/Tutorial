# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y vim man
RUN apt install -y tree curl
RUN apt install -y git wget cmake

RUN apt install -y g++ sdb

ENV HOME=/home/oe

WORKDIR /home/oe

COPY ./ $HOME

EXPOSE 5500
