from flask import (
    Flask,
    render_template,
    Blueprint,
    request,
    session,
)
from flask_bootstrap import Bootstrap
from routes.basic import main
from routes.jinja2_route import main as main2
from routes.Bootstrap_route import main as main3


app = Flask(__name__)

app.secret_key = 'rand123_456_s_d__ee'

# 用于构建整洁且具有吸引力的网页
bootstrap = Bootstrap(app=app)

# 注册蓝图
app.register_blueprint(blueprint=main)
app.register_blueprint(blueprint=main2)
app.register_blueprint(blueprint=main3)


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
        port=2012,
    )
    app.run(**config)

