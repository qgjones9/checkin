from app import app, db
from flask import Flask, request, jsonify, make_response, json
from .models import User, Teacher, Child
from app import logger


@app.route("/user", methods=["POST"])
def add_user():
    json_data = request.get_json()
    username = json_data['username']
    email = json_data['email']
    faculty = json_data['faculty']
    admin = json_data['admin']
    password = json_data['password']
    logger.info(password)
    new_user = User(username, email, password, faculty, admin)
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
    logger.debug("retrieved all users from database")
    users = []
    for user in all_users:
        users.append(user.describe())

    return jsonify(users=users)


# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    logger.info(f'attempting to retrieve user from database with id of {id}')
    user = User.query.get(id)
    json_data = user.describe()
    return jsonify(user=json_data)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    if user is None:
        return {"message": f"Unable to find user with id {id}"}
    logger.info('found user in database')
    for key in request.get_json():
        if key == "email":
            user.email = request.json['email']
        if key == "username":
            user.username = request.json['username']
        if key == "admin":
            user.admin = request.json["admin"]
        if key == "faculty":
            user.faculty = request.json["faculty"]

    logger.info('connecting to database and updating user record')
    db.session.commit()
    logger.info('database updated. returning updated user data to UI')

    return user_detail(id)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    logger.info(f'Searching for user with user id {id}')
    user = User.query.get(id)
    logger.info('Found user in database and deleting the fucker')
    db.session.delete(user)
    db.session.commit()
    logger.info('user deleted from database')
    return {"message": "deleted user from database"}

