from __future__ import absolute_import, unicode_literals
from celery import Celery

appCelery = Celery('proj',
             broker='amqp://rabbit-server',
             backend='redis://redis-server',
             include=['bumps.run_job'])

# Optional configuration, see the application user guide.
appCelery.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    appCelery.start()
