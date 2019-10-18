from flask import Flask
from config import Config
import logging
from flask_mongoengine import MongoEngine

# create app and add config
app = Flask(__name__)
app.config.from_object(Config)

# setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# instantiate db
db = MongoEngine(app)

# tell flask about my routes and models
from app import models
from app.routes import children_routes, teacher_routes, user_routes
