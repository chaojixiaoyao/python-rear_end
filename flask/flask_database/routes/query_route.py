from flask import (
    Blueprint,
    render_template,
    request,
)
from App.models import db
from App.models import Teacher
import random

main = Blueprint('query_route', __name__)


def init_blue2(app):
    app.register_blueprint(blueprint=main)


# 查询
@main.route('/show_data')
def show_data():
    # # 获取 Teacher的数据
    # student = Teacher.query.all()
    # 得到大于50Teacher的id
    # teacher = Teacher.query.filter(Teacher.id.__gt__(50))/(Teacher.id > (50)
    # 得到小于50Teacher的id
    # teacher = Teacher.query.filter(Teacher.id.__lt__(50))
    # 得到大于等于50Teacher的id
    # teacher = Teacher.query.filter(Teacher.id.__lt__(50))
    # 得到Teacher中指定的字符
    # teacher = Teacher.query.filter(Teacher.name.contains('遥'))
    # 得到Teacher中指定的字符
    teacher = Teacher.query.filter(Teacher.name.startswith('遥'))
    return render_template('index.html', values=teacher)


# 筛选
@main.route('/screen')
def screen_value():
    # 通过id过滤
    # teacher = Teacher.query.filter_by(id=1)
    # 根据id进行排序
    # teacher = Teacher.query.order_by('id')
    # 组合使用时order_by必须写在前面，offset和limit不分顺序，都是先执行offset，后limit
    teacher = Teacher.query.order_by('id').offset(3).limit(4)
    return teacher


@main.route('/get_teacher')
def get_teacher():
    # get没找到会返回None
    teacher = Teacher.query.get(1)
    print(teacher.name)
    return 'teacher'


# 手写数据分页
@main.route('/get_pagination')
def get_page():
    """
    实现结果分页：
        数据
        你想要第几页的数据
        每一页有多少数据
    :return:
    """
    # 接收从前端来的数据, 默认是一页, 获取前三条数据
    page = request.args.get('page', 1, type=int)
    print(request.args, 'args在这')
    print(page, 'page在这')
    per_page = request.args.get('per_page', 3, type=int)
    # (page - 1)是跳过第一页
    teacher = Teacher.query.limit(per_page).offset((page - 1) * page * per_page)
    return render_template('pagination.html', teachers=teacher)


# 插入数据
@main.route('/insert_data')
def insert_data():
    teacher_list = []
    for i in range(10):
        teachers = Teacher()
        teachers.name = 'teacher%d' % random.randrange(20)
        teacher_list.append(teachers)
    db.session.add_all(teacher_list)
    db.session.commit()
    return 'success upgrate data'


# 分页
@main.route('/get_pagination_value')
def get_pagination_value():
    te


@main.route('/New_teacher')
def New_student():
    student = Teacher()
    rd = random.randrange(100)
    student.name = '冥想是个好东西%d' % rd
    student.age = rd
    db.session.add(student)
    db.session.commit()
    return 'upgrate data'

