from flask import Blueprint
from App.models import Student
from App.models import db

main = Blueprint('first_blue', __name__)


def init_blue(app):
    app.register_blueprint(blueprint=main)


@main.route('/')
def index():
    return 'hello world'


@main.route('/create')
def create_database():
    db.create_all()
    return '革命成功'


@main.route('/add_student')
def add_student():
    student = Student()
    student.s_name = "逍遥"
    db.session.add(student)
    db.session.commit()
    return 'add success'