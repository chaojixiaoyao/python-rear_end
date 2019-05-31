from flask import (
    Flask,
    Blueprint,
)
from models.db import envs
from models.model import init_db
from routes.route_index import main_init


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.secret_key = 'r15fd58v1d45v4ss54v'
    # 初始化服务器配置
    app.config.from_object(envs.get('develop'))

    # 在route中定义函数，这里导入参数调用实现懒加载
    main_init(app)

    # 初始化第三方插件，库
    init_db(app)

    return app
