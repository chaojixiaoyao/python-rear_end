from flask import (
    render_template,
    Blueprint,
    request,
    redirect,
    url_for,
    flash,
)

main = Blueprint('BP', __name__)


@main.route('/hello_BP')
def index():
    return render_template('hello_Bootstrap.html')


@main.route('/ready_login', methods=['GET', 'POST'])
def login_ready():
    if request.method == 'GET':
        return render_template('user_login.html')
    elif request.method == 'POST':
        flash('用户名或密码错误')
        # 跳转到hello_Bootstrap.html
        return redirect(url_for('BP.login'))


@main.route('/user_login', methods=['POST'])
def login():
    return render_template('hello_Bootstrap.html')
