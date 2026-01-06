from werkzeug.security import generate_password_hash, check_password_hash
from flaskr.db import db

# Association tables
student_parent = db.Table('student_parent',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('parent_id', db.Integer, db.ForeignKey('parent.id'))
)

student_courses = db.Table('student_courses',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

# Models
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # hashed password
    avatar = db.Column(db.String(255), default='teacher-avatar.png')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))  # hashed password
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

    teacher = db.relationship('Teacher', backref='students')
    parents = db.relationship('Parent', secondary='student_parent', back_populates='students')
    courses = db.relationship('Course', secondary=student_courses, backref='students')
    avatar_image = db.Column(db.String(255), default='default.png')

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))  # hashed password

    students = db.relationship('Student', secondary='student_parent', back_populates='parents')
