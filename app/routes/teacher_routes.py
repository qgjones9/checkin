from app import app
from flask import jsonify
from flask import request, make_response
from app.models.models import Teacher, convert_children_dbref


@app.route("/teacher", methods=["POST"])
def create_teacher():
    data = request.get_json()
    t = Teacher()
    try:
        t.first_name = data["first_name"]
        t.last_name = data["last_name"]
        t.email = data["email"]
        t.grade_level = data["grade_level"]
        if data["faculty"]:
            t.faculty = data["faculty"]
        if data["admin"]:
            t.admin = data["admin"]
        t.save()
    except KeyError:
        return {'error': 'check you post parameters'}

    msg = {"success": "user created"}
    return make_response(jsonify(msg), 200)


@app.route("/teacher/<oid>", methods=["GET"])
def read_teacher(oid):
    return convert_children_dbref(oid)


# endpoint to update teacher
@app.route("/teacher/<id>", methods=["PUT"])
def update_teacher(id):

    return ''

# endpoint to delete teacher
@app.route("/teacher/<id>", methods=["DELETE"])
def delete_teacher(id):

    return ''



