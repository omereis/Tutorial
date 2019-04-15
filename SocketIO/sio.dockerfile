# Using the latest long-term-support Ubuntu OS
FROM ubuntu:18.04

# Update the apt-get index and then install project dependencies
RUN apt-get update
RUN apt-get install -y vim man tree
RUN apt install -y software-properties-common
RUN apt install -y python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install flask
RUN pip install flask-socketio

ENV HOME=/home/oe/socket_io/flask_sockets
ENV export FLASK_APP=/home/oe/socket_io/flask_sockets/app.py

# Set the directory for relative file paths
WORKDIR /home/oe/socket_io/flask_sockets

# Install the app dependencies using pip
#RUN pip install -U pip

# Copy app files to the container
COPY ./ /home/oe/socket_io

# Make the 4000 port available from outside the container
EXPOSE 4000


