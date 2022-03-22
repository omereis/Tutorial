# Using the latest long-term-support Ubuntu OS
FROM ubuntu:20.04

RUN apt -y update
RUN apt -y upgrade

RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
#RUN apt install -y python3.7
#apt install python3-pipRUN ln -s /usr/bin/python3.7 /usr/bin/python

# Make the 5000 port available from outside the container
EXPOSE 6000



# Get-PSReadlineOption | Select *color
# Set-PSReadlineOption -TokenKind Command -ForegroundColor Blue
# Set-PSReadlineOption -TokenKind Parameter -ForegroundColor DarkBlue

