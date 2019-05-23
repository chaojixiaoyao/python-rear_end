from flask import (
    Blueprint,
    render_template,
)
from models.model import Person
from models.model import db

main = Blueprint('show_data', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/create_data')
def create_data():
    db.create_all()
    return render_template('show_index.html')


@main.route('/add_person')
def add():
    p = Person()
    p.p_name = '逍遥'
    db.session.add(p)
    db.session.commit()
    return 'Person add '


# 查询数据库
@main.route('/get_person')
def get_person():
    persons = Person.query.all()
    # for person in persons:
    #     print(person.p_name)
    return render_template('person.html', value=persons)
