#from __future__ import absolute_import, unicode_literals
import sys

print("Parsing...using Python" + sys.version) 

try:
    from celery import Celery
    print("Celery Imported") 
except Exception as excp:
    print ("Error:\n" + str(excp.args)) 

# app = Celery('proj', broker='amqp://rabbit-server', backend='redis://redis-server')
app = Celery('proj',
             broker='amqp://rabbit-server',
             backend='redis://redis-server')

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

def main():
    print("Getting app queue data")
    s = app.control.inspect().stats().keys()
    print("Stats: " + str(s))
    for key in s:
        print("key: " + str(key))
        s1 = s[key]
    print("That's it for now\n")

if __name__ == '__main__':
#    app.start()
    main()
    a = 5
