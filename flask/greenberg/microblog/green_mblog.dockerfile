# Using the latest long-term-support Ubuntu OS
FROM ubuntu:18.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt -y update
RUN apt install -y python
RUN apt -y install python-pip
RUN apt install -y vim man
RUN apt install -y tree
RUN rm /usr/bin/python
RUN apt install -y python3-pip
RUN ln -s /usr/bin/python3.6 /usr/bin/python

RUN pip3 install flask
RUN apt install -y python3-venv
RUN pip install python-dotenv
RUN pip install flask_wtf

WORKDIR /home/oe/microblog
ENV HOME=/home/oe/microblog
ENV SQLALCHEMY_TRACK_MODIFICATIONS True
COPY ./ /home/oe

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=microblog.py
ENV FLASK_DEBUG=1

# Make the 5000 port available from outside the container
EXPOSE 5000



# Get-PSReadlineOption | Select *color
# Set-PSReadlineOption -TokenKind Command -ForegroundColor Blue
# Set-PSReadlineOption -TokenKind Parameter -ForegroundColor DarkBlue

