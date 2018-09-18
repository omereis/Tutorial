#!/usr/bin/env python

import flask


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        print ("argv[1]: {}".format(argv[1]))
        port = int(argv[1])
    else:
        port = 5000
    APP.debug=True
    APP.run(port=port)
