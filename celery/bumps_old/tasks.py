from __future__ import absolute_import, unicode_literals
from .celery import appCelery


@appCelery.task
def add(x, y):
    return x + y


@appCelery.task
def mult(x, y):
    return x * y


@appCelery.task
def xsum(numbers):
    return sum(numbers)
