import os
basedir = os.path.abspath(os.path.dirname(__file__))

#from oe_debug import print_debug

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'mblog_app.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'all-my-secrets'
    #print_debug ('init, Config, SQLALCHEMY_DATABASE_URI: "' + SQLALCHEMY_DATABASE_URI + '"')
