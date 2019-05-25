from flask import (
    Flask,
    Blueprint,
    render_template,
)
from routes.show import main
from models.model import init_db
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhos:3306/database_name'
"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
    'sqlite:///sqlite3.db'
    'mysql+pymysql://root:12345678@localhos:2000/database_name'
    'mysql(数据库名)+pymysql(数据库驱动)://root(用户名):12345678(密码)@localhos(主机):2000(端口)/database_name(数据库名)'
"""

app.register_blueprint(blueprint=main)

init_db(app)

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port='2000',
    )
    app.run(**config)

