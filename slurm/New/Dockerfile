FROM ubuntu:16.04


RUN apt-get update && apt-get install -y \
    build-essential \
#    libmunge-dev    \
    vim             \
    libmunge-dev    \
    python          \
    iputils-ping    \
    net-tools       \
    man             \
    munge

	ENV PATH=$PATH:"/bin"
# Install slurm from git.
#ADD https://github.com/SchedMD/slurm/archive/slurm-15-08-5-1.tar.gz /tmp/slurm.tgz
ADD https://download.schedmd.com/slurm/slurm-17.11.5.tar.bz2 /tmp/slurm.tgz

RUN cd /tmp && tar x -f slurm.tgz && rm /tmp/slurm.tgz
#RUN cd /tmp && tar x -f slurm.tgz && rm /tmp/slurm.tgz
RUN cd /tmp/slurm-17.11.5 && ./configure && make && make install
COPY slurm.conf /usr/local/etc/slurm.conf
RUN cd /home & mkdir slurm
# Add slurm user
RUN useradd -ms /bin/bash slurm
#RUN adduser slurm && \
#    echo "slurm:slurm" | chpasswd
USER slurm
RUN mkdir /home/slurm/.ssh
ADD ssh/id_rsa.pub /home/slurm/.ssh/authorized_keys
USER root
#RUN rm -Rf /tmp/slurm-slurm-15-08-5-1

