from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
)
from models.model import User
from models.model import db
main = Blueprint('Blue_main', __name__)


def main_init(app):
    app.register_blueprint(blueprint=main)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/create')
def create():
    db.create_all()
    return 'database create success'


@main.route('/login', methods=['GET', 'POST'])
def login():
    form_data = request.form
    user = User()
    user.name = form_data.get('username', '')
    user.password = form_data.get('password', '')
    db.session.add(user)
    db.session.commit()
    return render_template('login.html')
