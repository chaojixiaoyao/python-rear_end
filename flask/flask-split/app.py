from flask import (
    Flask,
    Blueprint,
    render_template,
)
from App import create_app

app = create_app()

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=2000,
    )
    app.run(**config)



