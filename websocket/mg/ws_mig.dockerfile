# Using the latest long-term-support Ubuntu OS
FROM ubuntu:18.04

# Update the apt-get index and then install project dependencies
RUN apt-get update
RUN apt-get install -y vim man tree
RUN apt install -y software-properties-common
RUN apt install -y python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install flask-socketio

ENV HOME=/home/oe/ws_mig/

# Set the directory for relative file paths
WORKDIR /home/oe/ws_mig

# Copy app files to the container
COPY ./ /home/oe/ws_mig

RUN pip install -r requirements.txt

COPY ./vimrc /etc/vim/vimrc

# EXPOSE 6000


