from flask import (
    Flask,
    render_template,
    Blueprint,
    request,
)
from routes.basic import main

app = Flask(__name__)


# 注册蓝图
app.register_blueprint(blueprint=main)


@app.route('/')
def home():
    # 拿到cookies
    user = request.cookies.get('user', '')
    return render_template('home.html', username=user)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=2000,
    )
    app.run(**config)

