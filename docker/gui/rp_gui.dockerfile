# Using the latest long-term-support Ubuntu OS
FROM ubuntu:20.04

RUN apt -y update
RUN apt -y upgrade

ENV HOME=/home/oe

WORKDIR /home/oe/gui

COPY ./ $HOME

EXPOSE 5005
