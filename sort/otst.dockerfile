FROM ubuntu:16.04

# Update the apt-get index and then install project dependencies
RUN apt-get update && apt-get install -y man vim git tree

RUN apt update
RUN apt install -y build-essential
RUN apt install -y manpages-dev
RUN apt install -y gdb
#RUN rm -f /etc/vim/vimrc
# Set the home directory to our app user's home.
ENV HOME=/home/omereis/sort
# Set the directory for relative file paths
WORKDIR /home/omereis/sort
COPY ./ /home/omereis/sort
RUN cp vimrc /etc/vim
