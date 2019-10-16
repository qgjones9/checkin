from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import logging

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


logging.basicConfig(level=logging.DEBUG)
# Create a custom logger
logger = logging.getLogger(__name__)

from app import user_routes, teacher_routes, children_routes, models

