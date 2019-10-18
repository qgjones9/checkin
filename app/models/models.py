import json
from flask import jsonify, make_response
from app import db, app
from mongoengine import CASCADE, ValidationError
from app.models.helpers import grade_level_validator


class User(db.Document):
    first_name = db.StringField(max_length=50, unique=True)
    last_name = db.StringField(max_length=50)
    email = db.StringField()
    children = db.ListField(db.ReferenceField("self", reverse_delete_rule=CASCADE))
    admin = db.BooleanField(default=False)
    faculty = db.BooleanField(default=False)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return f'<User: {self.first_name} {self.last_name}'


class Teacher(User):
    grade_level = db.StringField(max_length=3, validation=grade_level_validator)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return f'<Teacher: {self.first_name} {self.last_name}'


class Children(Teacher):

    def __repr__(self):
        return f'<Child: {self.first_name} {self.last_name}'


def convert_children_dbref(oid):
    """ converts children dbrefs into their actual objects """
    try:
        user_info = User.objects(id=oid)
        user_info = json.loads(user_info.to_json())
        children = user_info[0]['children']  # list obj
    except IndexError as err:
        message = {"message": "user not found"}
        return jsonify(message=message)
    except ValidationError:
        msg = {"bad request": "invalid event object id, it must be a 12-byte input or a 24-character hex string"}
        return make_response(jsonify(msg), 400)

    new_children_list = []
    # query and append children objs to original obj
    for el in children:
        e = Children.objects.get(id=el["$oid"])
        convert_to_json = json.loads(e.to_json())
        new_children_list.append(convert_to_json)

    children.clear()
    for el in new_children_list:
        children.append(el)

    return jsonify(user_info=user_info)


@app.cli.command("create_user")
def create_user():
    if User.objects:
        User.objects.delete()
    if Children.objects:
        Children.objects.delete()

    # Creates a user object in the database
    user = User(first_name='sheila', last_name='spencer', email='spencer@gmail.com').save()
    User(first_name="cathy", last_name="robinson", email="robinson@example.com").save()

    # create a teacher object
    t = Teacher(first_name="tracy", last_name="henderson", email="henderson@example.com", grade_level="k4").save()
    # Create a child object in the database
    child_01 = Children(first_name='addison', last_name='jones').save()
    child_02 = Children(first_name='greyson', last_name='jones').save()

    # create reference to child on user object
    User.objects(first_name='sheila').update_one(push__children=child_01)
    User.objects(first_name='tracy').update_one(push__children=child_02)


