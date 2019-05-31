from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import request

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    Bootstrap(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16))
    password = db.Column(db.String(16))


class Data(User):

    def __init__(self):
        self.data = request.form
        self.username = self.data.get('username')
        self.password = self.data.get('password')

    def validate_login(self):
        return len(self.username) > 3 and len(self.password) > 6

    def validate_name_password(self):
        return self.username != User.name and self.password != User.password
