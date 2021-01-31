# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
# RUN apt install -y software-properties-common
#  RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y vim man tree curl git wget cmake

# Install Python 3.5.2, to simulate Red Pitaya environment
RUN cd /usr/src &&\
	wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz &&\
	tar xzf Python-3.5.2.tgz
RUN cd /usr/src/Python-3.5.2 &&\
	./configure --enable-optimizations &&\
	make altinstall
RUN ln -s /usr/local/bin/python3.5 /usr/bin/python3
RUN apt install -y python3-pip

ENV HOME=/home/oe/

# install Miniconda
RUN mkdir -p ~/miniconda3 && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
RUN bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
RUN ~/miniconda3/bin/conda init bash
RUN ~/miniconda3/bin/conda create -n py37 -y python=3.7

#RUN ~/miniconda3/bin/conda run -n py37
#RUN ~/miniconda3/bin/conda activate py37

#ENV CPLUS_INCLUDE_PATH=/home/oe/websocketpp/
COPY ./ /home/oe
WORKDIR /home/oe

EXPOSE 5000

