from flask import (
    Blueprint,
    render_template,

)

main = Blueprint('jinja2_blue', __name__)


@main.route('/templates')
def index():
    return render_template('show_index.html')


@main.route('/inherit')
def inherit():
    return render_template('index_inherit.html')


@main.route('/ceshi')
def ceshi():
    return render_template('index_content.html')


@main.route('/parameter')
def parameter():
    para = ['peter', 'jack', 'rose']
    message = '<h4>我是李逍遥</h4>'
    return render_template('index_inherit.html', value=para, msg=message)
