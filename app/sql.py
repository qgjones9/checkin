from app import db
from app.models import User, Child, Teacher


class ResourceManager(object):
    def __init__(self):
        self.db = db

    def find_all_users(self, selector):
        return User,

