# Using the latest long-term-support Ubuntu OS
FROM ubuntu:18.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y python3-pip
RUN apt install -y python3.7
RUN apt install -y vim man
RUN apt install -y tree curl
RUN ln -s /usr/bin/python3.7 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
#RUN curl -sS https://bootstrap.pypa.io/get-pip.py >>setup.py
#RUN python setup.py

#RUN pip install websockets
#RUN pip install sqlalchemy
#RUN pip install pymysql
RUN pip install aiohttp aiofiles aiodns

WORKDIR /home/oe/
ENV HOME=/home/oe/
COPY ./ /home/oe

# Make the 5678 port available from outside the container
