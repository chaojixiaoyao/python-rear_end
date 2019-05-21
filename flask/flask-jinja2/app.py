from flask import (
    Flask,
    render_template,
    Blueprint,
    request,
    session,
    Session,
)
from routes.basic import main
from routes.jinja2_route import main as main2

app = Flask(__name__)

app.secret_key = 'rand123_456_s_d__ee'


# 注册蓝图
app.register_blueprint(blueprint=main)
app.register_blueprint(blueprint=main2)


@app.route('/')
def home():
    # 拿到cookies
    # user = request.cookies.get('user', '')
    user = session.get('user')
    return render_template('home.html', username=user)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=2000,
    )
    app.run(**config)

