from flask import (
    Flask,
    Blueprint,
)
from App.models import init_db
from routes.route import init_blue
from routes.query_route import init_blue2
from App.settinge import envs
from App.models import db


def create_app():
    app = Flask(__name__)
    # 初始化服务器配置
    app.config.from_object(envs.get('develop'))
    # 在route中定义函数，这里转入参数调用实现懒加载
    init_blue(app)
    init_blue2(app)
    # 初始化第三方插件，库
    init_db(app)


    return app
