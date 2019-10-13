from app import app, db
from flask import Flask, request, jsonify
from .models import User, Teacher, Child
from app import logger


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400

    username = json_data['username']
    email = json_data['email']
    faculty = json_data['faculty']
    admin = json_data['admin']
    new_user = User(username, email, faculty, admin)

    if new_user:
        logger.debug('creating new user')
        db.session.add(new_user)

        logger.debug('new user created, committing to database')
        db.session.commit()

        logger.debug('new user committed to database')

    return {'message': 'new user created and committed to database'}


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()

    logger.debug("print out each user's information is painful")
    data = []
    for user in all_users:
        data.append(user.__repr__())

    print(data)
    user_info = all_users[0].__repr__()
    return user_info


# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return ''


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    # user = User.query.get(id)
    # username = request.json['username']
    # email = request.json['email']
    # faculty = request.json['faculty']
    # admin = request.json['admin']
    #
    # user.email = email
    # user.username = username
    # user.faculty = faculty
    # user.admin = admin
    #
    # db.session.commit()
    return ''


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    # user = User.query.get(id)
    # db.session.delete(user)
    # db.session.commit()
    return ''
