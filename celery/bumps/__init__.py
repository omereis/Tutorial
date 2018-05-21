from flask import Flask
from flask_redis import FlaskRedis
from flask_jwt_extended import JWTManager
from flask_restful import Api
from .database import Database

"""
Celery fails to find the file when you pass "celeryconfig" as a string.
To get around this we manually import it because python doesn't have a
a problem with the relative path. Then pass it in as an object.
"""
import celeryconfig

"""
Leaving tasks unconfigured is a pattern that allow it to be extended
later. In this example we assume that the package with be used as the
app for Celery and only apply the coniguration in the __init__.
"""
appCelery.config_from_object(celeryconfig)

# Set app
app = Flask(__name__, instance_relative_config=True)

# Set app configs
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)

# Set JWT Manager
jwt = JWTManager(app)

# Set RESTful API
api = Api(app)

# Set redis
redis = FlaskRedis(app)

# Set Redis db
rdb = Database(redis)
print("rdb created: " + str(rdb))

# Import the Flask views after instancing the app
import bumps_flask.views
from tasks import app

