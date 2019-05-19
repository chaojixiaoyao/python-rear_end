from flask import(
    Flask,
    render_template,
    request,
)
from models import User

app = Flask(__name__)


@app.route('/')
def user_index():
    user = User(1, '我是李逍遥')
    # 红色的user是jinjia模板里定义的接收参数
    return render_template('index.html', user=user)


# 路由函数定义了地址栏
@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    print(user_id)
    if int(user_id) == 1:
        user = User(1, '我是李逍遥')
    return render_template('user_id.html', user=user)


# 循环学习
@app.route('/names')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, '我是逍遥'+str(i))
        users.append(user)
    return render_template('users.html', users=users)


@app.route('/one')
def return_one():
    return render_template('base_one.html')


@app.route('/two')
def return_two():
    return render_template('base_two.html')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=2000,
    )
    app.run(**config)

