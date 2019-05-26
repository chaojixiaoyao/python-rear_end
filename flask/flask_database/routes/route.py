from flask import (
    Blueprint,
)
from App.models import Student
from App.models import db
import random

main = Blueprint('first_blue', __name__)


def init_blue(app):
    app.register_blueprint(blueprint=main)


@main.route('/')
def index():
    return 'hello world'


@main.route('/create')
def create_database():
    # 创建表
    db.create_all()
    # 删除表db.drop_all()
    return '革命成功'


@main.route('/add_student')
def add_student():
    student = Student()
    student.s_name = "逍遥"
    db.session.add(student)
    db.session.commit()
    return 'add success'


@main.route('/add_students')
def add_students():
    # st = Student()
    # st.s_name = 'peter'
    #
    # st1 = Student()
    # st1.s_name = 'jack'
    #
    # st2 = Student()
    # st2.s_name = 'rose'
    #
    # db.session.add(st)
    # db.session.add(st1)
    # db.session.add(st2)

    # db.session.commit()
    student_updata = []
    for i in range(10):
        student = Student()
        # 生成10个影分身之术
        student.s_name = '影分身之术%d' % random.randrange(100)
        student_updata.append(student)
    db.session.add_all(student_updata)
    db.session.commit()
    return 'hello'


# 查看
@main.route('/get_value/')
def get_values():
    querys = Student.query.all()
    for query in querys:
        print(query.s_name)
    return '工程师查看'


# 修改
@main.route('/modify_student')
def modify_student():
    # 找到第一个数据赋值给student
    student = Student.query.first()
    student.s_name = '我是小明'
    db.session.add(student)
    db.session.commit()
    return 'modify success'


# 删除
@main.route('/deletes_student')
def deletes_student():
    student = Student.query.first()
    db.session.delete(student)
    db.session.commit()
    return 'delete success'


# id查询
@main.route('/query_id')
def query_id():
    # 不能这样写 Student.id,因为不能遍历本身
    students = Student.query.all()
    for student in students:
        print(student.id)
    return 'id'

