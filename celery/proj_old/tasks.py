from celery import Celery

app = Celery('bumps',
             broker='amqp://rabbit-server',
             backend='redis://redis-server')

@app.task
def add(x,y):
    return x + y