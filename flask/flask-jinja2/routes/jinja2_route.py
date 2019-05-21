from flask import (
    Blueprint,
    render_template,

)

main = Blueprint('jinja2_blue', __name__)


@main.route('/template')
def index():
    return render_template('index.html')


@main.route('/inherit')
def inherit():
    return render_template('index_inherit.html')
