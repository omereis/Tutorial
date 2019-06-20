FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["app.py"]