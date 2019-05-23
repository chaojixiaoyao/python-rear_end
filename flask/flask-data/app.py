from flask import (
    Flask,
    Blueprint,
    render_template,
)
from routes.show import main
from models.model import init_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

app.register_blueprint(blueprint=main)

init_db(app)

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port='2000',
    )
    app.run(**config)

