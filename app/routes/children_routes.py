from app import app
from flask import jsonify
from flask import request, make_response
from app.models.models import Teacher, convert_children_dbref, Children


@app.route("/child", methods=["POST"])
def create_child():
    data = request.get_json()
    t = Children()
    try:
        t.first_name = data["first_name"]
        t.last_name = data["last_name"]
        t.grade_level = data["grade_level"]
        t.save()
    except KeyError:
        return {'error': 'check you post parameters'}

    msg = {"success": "child created"}
    return make_response(jsonify(msg), 200)


@app.route("/child/<oid>", methods=["GET"])
def read_child(oid):
    return convert_children_dbref(oid)


@app.route("/child/<id>", methods=["PUT"])
def update_child(id):

    return ''


@app.route("/child/<id>", methods=["DELETE"])
def delete_child(id):

    return ''



