# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y python3
RUN apt install -y python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN apt install -y vim
COPY ./vimrc /etc/vim/vimrc

RUN pip install --upgrade pip
RUN pip install flask

WORKDIR /home/oe/
ENV HOME=/home/oe/
COPY ./ /home/oe

ENV FLASK_DEBUG=1

# Make the 5000 port available from outside the container
EXPOSE 6000



# Get-PSReadlineOption | Select *color
# Set-PSReadlineOption -TokenKind Command -ForegroundColor Blue
# Set-PSReadlineOption -TokenKind Parameter -ForegroundColor DarkBlue

