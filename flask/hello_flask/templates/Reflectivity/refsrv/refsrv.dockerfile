# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y python3.6
RUN apt -y install python3-pip
RUN apt install -y vim man
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN apt install -y tree
RUN apt install -y sqlite3
RUN apt install -y libjsoncpp-dev

# Copy app files to the container
# COPY ./ /home/refsrv
WORKDIR /home/refsrv
ENV HOME=/home/refsrv

ENV FLASK_APP=/home/oe/microblog/microblog.py

RUN apt install -y python3-venv
RUN pip install flask

RUN mkdir /home/oe
WORKDIR /home/oe
ENV HOME=/home/oe
COPY ./ /home/oe

# Make the 5000 port available from outside the container
EXPOSE 5000


