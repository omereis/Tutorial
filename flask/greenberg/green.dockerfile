# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt -y update
RUN apt install -y python
RUN apt -y install python-pip
RUN apt install -y vim man
# RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN apt install -y tree

# RUN apt install -y python3-venv
RUN pip install flask
RUN pip install flask-wtf
RUN pip install flask-sqlalchemy
RUN pip install flask-migrate
RUN pip install -U flask-cors

WORKDIR /home/oe/microblog
ENV HOME=/home/oe/microblog
ENV SQLALCHEMY_TRACK_MODIFICATIONS True
COPY ./ /home/oe

RUN flask db init
RUN flask db migrate -m "users table"
RUN flask db upgrade

ENV FLASK_APP=microblog.py
ENV FLASK_DEBUG=1

# Make the 5000 port available from outside the container
EXPOSE 5000



# Get-PSReadlineOption | Select *color
# Set-PSReadlineOption -TokenKind Command -ForegroundColor Blue
# Set-PSReadlineOption -TokenKind Parameter -ForegroundColor DarkBlue

