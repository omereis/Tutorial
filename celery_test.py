from celery import Celery
############################################################################### 
def list_queues():
    try:
        app = Celery('bumps', broker='amqp://rabbit-server', backend='redis://redis-server')
#        s = app.control.inspect().stats().keys()
        queues = app.amqp.queues
        ctrl = app.control
        qq = ctrl.Mailbox.get_queue()
        print("Stats: " + str(s))
        for key in s:
            print("key: " + str(key))
        s1 = s[key]
        print("That's it for now\n")
    except Exception as e:
        print("Error:\n" + str(e))
############################################################################### 
if __name__ == '__main__':
    list_queues()
