from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



def init_db(app):
    db.init_app(app)



class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16))




