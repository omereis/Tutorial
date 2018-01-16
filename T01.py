#!/usr/bin/python

import ast
import inspect
import math
import click
print ("Hello, Python!")

def get_g (L, T, th):
    theta = th * math.pi / 180.0
    par = (1 + 1.0 / 4.0 * math.sin(theta/2)**2)
    return ((4.0 * (math.pi ** 2) * L / T ** 2) * par)

@click.command()
@click.option('--count', default=1, help='Number of greetings,')
@click.option('--name', prompt='Your Name', help='The person to greet.')

def hello (count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo("Howdi %s :-)" % name)
if __name__ == "__main__":
    try :
        hello()
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
