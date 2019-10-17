from flask import jsonify
from app import db, logger, app
from werkzeug.security import generate_password_hash, check_password_hash

# rm -rf app.db migrations && flask db init && flask db migrate -m "populating table" && flask db upgrade
# from app import db
# from app.models import User, Child, Teacher
# quincy = User(username='quincy', email='quincy@example.com', admin=True)
# addison = Child(first_name='addision', last_name='jones', parent=)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    faculty = db.Column(db.Boolean, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'))

    def __init__(self, username, email, password, faculty=False, admin=False):
        self.username = username
        self.email = email
        self.password_hash = password
        self.faculty = faculty
        self.admin = admin

        # create a secure password upon class instantiation
        self.set_password()

    def describe(self):
        data = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "faculty": self.faculty,
            "admin": self.admin,
            "children": self.children
        }
        return data

    def __repr__(self):
        return f'username: {self.username}'

    def set_password(self):
        self.password_hash = generate_password_hash(self.password_hash)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    parent = db.relationship('User', backref='parent', lazy='select')
    grade_level = db.Column(db.String(2), db.ForeignKey("teacher.grade_level"))

    def __repr__(self):
        return f"Child: '{self.first_name} {self.last_name}'"


class Teacher(db.Model):
    """ The grade level of the school
        from app import db
        from app.models import User, Child, Teacher
        # created a user who is apart of the faculty members
        spencer = User(username='spencer holiday', email='spencer@gmail.com', admin=True, faculty=True)
        professor = Teacher(grade_level='k4', teacher=spencer)

    """
    grade_level = db.Column(db.String(2), primary_key=True)
    teacher_id = db.Column(db.Integer)
    teacher = db.relationship('Child', backref='child', lazy='select')

    def __init__(self, grade_level, id):

        teacher = User.query.get(id)

        self.grade_level = grade_level
        self.teacher_id = teacher.username

    def describe(self):
        data = {
            "grade_level": self.grade_level,
            "teacher_id": self.teacher_id
        }
        return data


@app.cli.command("bootstrap")
def bootstrap_data():
    """
    populates database with data
    """
    db.drop_all()
    db.create_all()

    spencer = User(username="spencer", email="spencer@gmail.com", password="sdfasdfsadf", faculty=True, admin=True)
    henderson = User(username="henderson", email="henderson@gmail.com", password="sdfasdfsadf", faculty=True, admin=True)
    db.session.add(spencer)
    db.session.add(henderson)
    db.session.commit()

    gresyson = Child(first_name="greyson", last_name="jones")
    addison = Child(first_name="addison", last_name="jones")
    k5 = Teacher(grade_level="k4", id=1)
    db.session.add(gresyson)
    db.session.add(k5)
    db.session.commit()

    gresyson.parent.append(spencer)
    gresyson.parent.append(henderson)
    addison.parent.append(henderson)

    db.session.commit()

