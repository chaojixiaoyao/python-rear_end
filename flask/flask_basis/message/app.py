from flask import (
    Flask,
    render_template,
    flash,
    request,
    abort,
)

app = Flask(__name__)
app.secret_key = 'rand *&kf;'


@app.route('/')
def hello_world():
    flash('hello peter')
    return render_template('message_index.html')


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username', '')
    userpassword = form.get('password', '')
    if not username:
        flash('请输入用户名')
        return render_template('message_index.html')
    if not userpassword:
        flash('请输入密码')
        return render_template('message_index.html')
    if username == 'lixiaoyao' and userpassword == '123456':
        flash('登陆成功')
        return render_template('message_index.html')
    else:
        flash('密码错误')
        return render_template('message_index.html')


# 错误页面
@app.errorhandler(404)
def error(e):
    return render_template('404.html')


@app.route('/users/<user_id>')
def users(user_id):
    print(user_id)
    if int(user_id) == 1:
        return render_template('user.html')
    else:
        abort(404)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=2000,
    )
    app.run(**config)
