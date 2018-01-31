from flask import Flask
from redis import Redis, RedisError
import os
import sys
import socket
import datetime

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        tUTC = datetime.datetime.now()
        strTime = str(datetime.datetime.now())
        python_version = sys.version
    except:
        strTime = "can't get local time"
    try:
        visits = redis.incr("counter")
        print("test")
    except RedisError as e:
        visits = "<i>cannot connect to Redis, counter disabled</i><br>"  + "Err: {}".format(e)

    html =  "<title>Docker App</title>" \
            "<h2>Hello {name} and welcome!</h2>" \
            "<br>version Jan 31, 12:20 pm" \
            "<table border=\"1\" width=\"100%\"><tr>" \
            "<td align=\"right\"><b>Host Name</b></td><td> {hostname}</td>" \
            "</tr><tr>" \
            "<td align=\"right\"><b>IP</b><td> {ip}</td></td>" \
            "</tr><tr>" \
            "<td align=\"right\"><b>Visits</b></td><td> {visits}</td>" \
            "</tr>" \
            "<td align=\"right\"><b>Time</b></td><td> {current_time}</td>" \
            "</tr><tr>" \
            "<td align=\"right\"><b>Version</b></td><td> {python_version}</td>" \
            "</table>" \
            "<h2>Thanks you. Come again<br><center>and again</center></h2>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), ip=socket.gethostbyname(socket.gethostname()), visits=visits, current_time=strTime, python_version=python_version)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)