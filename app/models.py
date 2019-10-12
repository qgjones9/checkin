from app import db

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
    children = db.relationship('Child', backref='parent', lazy=True)
    teacher = db.relationship('Teacher', backref='teacher', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'))

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
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))

