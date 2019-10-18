from app import app
from app.models.models import convert_children_dbref


@app.route("/user", methods=["GET"])
def create_user():
    return ''

# endpoint to get user detail by id
@app.route("/user/<oid>", methods=["GET"])
def read_user(oid):
    return convert_children_dbref(oid)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def update_user(id):

    return ''

# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):

    return ''

