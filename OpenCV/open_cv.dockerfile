# Using the latest long-term-support Ubuntu OS
FROM ubuntu:18.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y python3.7
RUN ln -s /usr/bin/python3.7 /usr/bin/python
ENV HOME=/home/oe

WORKDIR /home/oe/open_cv
#WORKDIR /home/oe/cpp/rp_server


COPY ./ $HOME
COPY ./ $WORKDIR

RUN python get-pip.py
RUN pip install opencv-python
