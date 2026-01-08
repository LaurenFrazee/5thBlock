from werkzeug.security import generate_password_hash, check_password_hash
from flaskr.db import db

# --------------------
# Association Tables
# --------------------

student_parent = db.Table(
    "student_parent",
    db.Column("student_id", db.Integer, db.ForeignKey("student.id")),
    db.Column("parent_id", db.Integer, db.ForeignKey("parent.id")),
)

student_courses = db.Table(
    "student_courses",
    db.Column("student_id", db.Integer, db.ForeignKey("student.id")),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id")),
)

# --------------------
# User Models
# --------------------

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    avatar = db.Column(db.String(255), default="teacher-avatar.png")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    teacher = db.relationship("Teacher", backref="students")

    parents = db.relationship(
        "Parent",
        secondary=student_parent,
        back_populates="students",
    )

    courses = db.relationship(
        "Course",
        secondary=student_courses,
        back_populates="students",
    )

    avatar_image = db.Column(db.String(255), default="default.png")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    students = db.relationship(
        "Student",
        secondary=student_parent,
        back_populates="parents",
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# --------------------
# Phase 3 Models
# Course → Module → Quiz
# --------------------

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), nullable=False)

    published = db.Column(db.Boolean, nullable=False, default=False)

    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)

    teacher = db.relationship("Teacher", backref="courses")

    modules = db.relationship(
        "Module",
        back_populates="course",
        cascade="all, delete-orphan",
    )

    students = db.relationship(
        "Student",
        secondary=student_courses,
        back_populates="courses",
    )

    def __repr__(self):
        return f"<Course {self.id} {self.title!r}>"


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    published = db.Column(db.Boolean, nullable=False, default=False)

    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)

    course = db.relationship("Course", back_populates="modules")

    quizzes = db.relationship(
        "Quiz",
        back_populates="module",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Module {self.id} {self.title!r}>"


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    module_id = db.Column(db.Integer, db.ForeignKey("module.id"), nullable=False)

    published = db.Column(db.Boolean, nullable=False, default=False)

    due_date = db.Column(db.Date, nullable=True)

    module = db.relationship("Module", back_populates="quizzes")

    def __repr__(self):
        return f"<Quiz {self.id} {self.title!r}>"
