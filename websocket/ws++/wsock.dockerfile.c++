# Using the latest long-term-support Ubuntu OS
FROM ubuntu:16.04

RUN apt -y update
RUN apt -y upgrade
# RUN apt install -y software-properties-common
#  RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y vim man
RUN apt install -y tree curl
RUN apt install -y git wget

RUN apt install -y cmake

RUN apt update
RUN apt install -y libboost-dev
RUN apt install -y libboost-all-dev
RUN apt install -y libasio-dev
RUN apt install -y build-essential

ENV HOME=/home/oe

RUN mkdir -p $HOME/ws &&\
	cd $HOME/ws &&\
	git clone https://github.com/zaphoyd/websocketpp . &&\
	mkdir $HOME/ws/build &&\
	cd $HOME/ws/build

ENV CPLUS_INCLUDE_PATH=/home/oe/ws

# &&\
#cmake -D BUILD_EXAMPLES=ON -D BUILD_TESTS=ON -D OPENSSL_CRYPTO_LIBRARY=~/Dev/build-x64/openssl/lib/libcrypto.so -D OPENSSL_SSL_LIBRARY=~/Dev/build-x64/openssl/lib/libssl.so -D OPENSSL_INCLUDE_DIR=~/Dev/build-x64/openssl/include/ -DCMAKE_INSTALL_PREFIX=./installdir ..

#RUN mkdir -p $HOME/git &&\
#	cd $HOME/git &&\
#	git clone --recurse-submodules https://github.com/socketio/socket.io-client-cpp.git &&\
#	git clone https://github.com/jmossberg/websocketpp-examples.git &&\
#	cd websocketpp-examples\
#	chmod +x *.sh

#RUN cd $HOME/git/websocketpp-examples &&\
#	./install_tools.sh &&\
#	./install_boost.sh 1.67.0 &&\
#	./download_websocketpp.sh 0.8.1 &&\
#	./create_certificate.sh &&\
#	make websocketpp_examples

# RUN apt-get install -y python3-pip
# RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN ln -s /usr/bin/pip3 /usr/bin/pip

# ENV CPLUS_INCLUDE_PATH=/home/oe/websocketpp/
WORKDIR /home/oe

EXPOSE 5000