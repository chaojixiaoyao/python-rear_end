
from models import create_app

app = create_app()


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=2001,
    )
    app.run(**config)


