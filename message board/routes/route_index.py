from flask import (
    Blueprint,
    render_template,
    request,
    session,
    Response,
    redirect,
    url_for,
)
from models.model import db
from models.model import Data
main = Blueprint('Blue_main', __name__)


def main_init(app):
    app.register_blueprint(blueprint=main)


@main.route('/')
def index():
    # 拿到cookie
    user = session.get('user', '')
    print([user])
    return render_template('index.html', username=user)


@main.route('/create')
def create():
    db.create_all()
    return 'database create success'


@main.route('/login', methods=['GET', 'POST'])
def login():
    user = Data()
    if request.method == 'POST':
        # 验证用户输入的是否合规
        if user.validate_login():
            # 判断是否重名
            if user.validate_name_password():
                # 存入数据库
                user.name = user.username
                user.password = user.password
                db.session.add(user)
                db.session.commit()
                cookie()
                result = '登陆成功'
                return render_template('login.html', result=result)
            else:
                result = '已有用户名或密码，请重新输入'
                return render_template('login.html', result=result)
        else:
            result = '用户名或密码错误'
            return render_template('login.html', result=result)
    else:
        result = '是否显示'
        return render_template('login.html', result=result)


@main.route('/cookie')
def cookie():
    # 设置cookie
    username = request.form.get('username', '')
    print(username)
    print(type(username))
    #  # 设置session
    session['user'] = username
    # 设置cookie
    response = Response(response='{}'.format(username))
    response.set_cookie('user', username)
    return response


@main.route('/logout')
def logout():
    # 清除cookies
    response = redirect(url_for('.index'))
    # response.delete_cookie(''user)
    response.delete_cookie('session')
    return response
