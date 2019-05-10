# Using the latest long-term-support Ubuntu OS
FROM ubuntu:18.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y vim man
RUN apt install -y tree
#RUN apt install -y curl
RUN apt install -y python3.6
RUN ln -s /usr/bin/python3.6 /usr/bin/python
RUN apt install -y python3-pip
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install matplotlib
RUN pip install scipy
RUN apt install -y libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
RUN apt install -y freeglut3-dev
RUN apt install -y libwebkitgtk-1.0-0
RUN apt install -y libjpeg-dev zlib1g-dev libpng-dev libtiff-dev libsdl-dev libnotify-dev libsm-dev
RUN pip install -U -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 wxPython
RUN pip install refl1d

WORKDIR /home/oe/
ENV HOME=/home/oe/
COPY ./ /home/oe

