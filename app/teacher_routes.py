from app import app, db
from flask import Flask, request, jsonify, make_response, json
from .models import User, Teacher, Child
from app import logger


# endpoint to show all users
@app.route("/teacher", methods=["GET"])
def get_teacher():
    teacher_info = request.get_json()
    if not teacher_info:
        return {"message": "No input data provided"}, 400

    all_teachers = Teacher.query.all()
    logger.debug("retrieved all users from database")
    teachers = []
    for teacher in all_teachers:
        teachers.append(teacher.describe())

    return jsonify(teachers=teachers)


# endpoint to create new user
@app.route("/teacher", methods=["POST"])
def add_teacher():
    teacher_info = request.get_json()
    grade_level = teacher_info['grade_level']
    teacher = teacher_info['id']
    new_user = Teacher(grade_level, teacher)

    if new_user:
        logger.debug('creating new user')
        db.session.add(new_user)

        logger.debug('new user created, committing to database')
        db.session.commit()

        logger.debug('new user committed to database')

    return {'message': 'new user created and committed to database'}


# endpoint to get user detail by id
@app.route("/teacher/<grade_level>", methods=["GET"])
def teacher_detail(grade_level):
    logger.info(f'attempting to retrieve teacher from database assigned to grade_level {grade_level}')
    teachers = Teacher.query.get(grade_level)
    teacher_info = teachers.describe()
    return jsonify(teachers=teacher_info)


# endpoint to update user
@app.route("/teacher/<grade_level>", methods=["PUT"])
def teacher_update(grade_level):
    teacher = Teacher.query.get(grade_level)
    if teacher is None:
        return {"message": f"Unable to find user with grade_level {grade_level}"}
    logger.info('found teacher in database')

    logger.info('updating teacher record')
    teacher.grade_level = request.json["grade_level"]
    teacher_name = User.query.get(request.json["id"])
    teacher.teacher_id = teacher_name.username

    logger.info('connecting to database')
    db.session.commit()
    logger.info('database updated. returning updated user data to UI')

    return teacher_detail(grade_level)


# endpoint to delete user
@app.route("/teacher/<id>", methods=["DELETE"])
def teacher_delete(id):
    logger.info(f'Searching for user with user id {id}')
    teacher = Teacher.query.get(id)
    logger.info('Found user in database and deleting the fucker')
    db.session.delete(teacher)
    db.session.commit()
    logger.info('user deleted from database')
    return {"message": "deleted user from database"}
