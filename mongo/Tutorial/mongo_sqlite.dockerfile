# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04
#FROM ubuntu:18.04

RUN apt -y update
RUN apt -y upgrade
#RUN apt install -y software-properties-common
#RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y vim man
RUN apt install -y tree curl
#RUN ln -s /usr/bin/python3 /usr/bin/python

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
RUN touch /etc/apt/sources.list.d/mongodb-org-4.0.list
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list
#RUN apt -y update
RUN apt-get install -y mongodb

# RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
# RUN touch /etc/apt/sources.list.d/mongodb-org-3.4.list
# RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list
#RUN apt -y update
#RUN apt install -y mongodb-org

RUN touch /var/lib/mongodb/arad
RUN rm /var/lib/mongodb/*

WORKDIR /home/oe/
ENV HOME=/home/oe/
COPY ./ /home/oe

# RUN service mongodb start

EXPOSE 27017
