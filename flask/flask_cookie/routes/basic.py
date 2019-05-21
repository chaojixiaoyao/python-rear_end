from flask import (
    render_template,
    Blueprint,
    request,
    Response,
    redirect,
    url_for,
    session,
)

main = Blueprint('first_blue', __name__)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username', '')

        response = Response(response='登陆成功%s' % username)
        # 加入cookie
        # 键值对
        response.set_cookie('user', username)
        # 设置session
        session['user'] = response
        return response


@main.route('/registered')
def registered():
    return render_template('index.html')


@main.route('/logout')
def logout():
    # 清除cookies
    response = redirect(url_for('home'))
    # response.delete_cookie(''user)
    response.delete_cookie('session')
    return response
