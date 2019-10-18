import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MONGODB_SETTINGS = {
        "db": "checkin",
        "host": "mongodb://localhost:27017/checkin"
    }


