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
        redisStr = str(redis)
        visits = "<i>cannot connect to Redis, counter disabled</i><br>"  + "Err: {}".format(e)

    html =  "<title>Docker App</title>" \
            "<h2>Hello {name} and welcome!</h2>" \
            "<br>version Jan 31, 12:20 pm" \
            "<table border=\"1\" width=\"100%\"><tr>" \
            "<td align=\"center\" style=\"background-color:powderblue;\"><b>Host Name</b></td><td> {hostname}</td>" \
            "</tr><tr>" \
            "<td align=\"center\" style=\"background-color:rgb(156, 198, 204);\"><b>IP</b><td> {ip}</td></td>" \
            "</tr><tr>" \
            "<td align=\"center\"  style=\"background-color:rgb(0, 255, 255);\"><b>Visits</b></td><td style=\"background-color:yellow;\"> {visits}</td>" \
            "</tr>" \
            "<td align=\"center\"><b>Time</b></td><td> {current_time}</td>" \
            "</tr><tr>" \
            "<td align=\"center\"><b>Version</b></td><td> {python_version}</td>" \
            "</tr><tr>" \
            "<td align=\"center\"><b>str(Redis)</b></td><td> {redisStr}</td>" \
            "</tr></table>" \
            "<h2>Thanks you. Come again<br><center>and again</center></h2>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), ip=socket.gethostbyname(socket.gethostname()), visits=visits, current_time=strTime, python_version=python_version, redisStr=redisStr)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
