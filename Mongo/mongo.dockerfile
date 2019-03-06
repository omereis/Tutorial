# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y vim man
RUN apt install -y tree curl
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN curl -sS https://bootstrap.pypa.io/get-pip.py >>setup.py
RUN python setup.py

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
RUN touch /etc/apt/sources.list.d/mongodb-org-4.0.list
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list
RUN apt-get install -y mongodb
# RUN service mongodb start


WORKDIR /home/oe/
ENV HOME=/home/oe/
COPY ./ /home/oe

# Make the 5000 port available from outside the container
EXPOSE 5000
