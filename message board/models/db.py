def get_db_url(dbinfo):
    # dbinfo.get不到值得话，就返回 or后的
    ENGINE = dbinfo.get('ENGINE') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'root'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    MANE = dbinfo.get('NAME') or 'test'
    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, MANE)


class Config:
    DEBUG = False

    TESTING = False

    SECRET_KEY = '1234567881231545fjsoghficgsdf58sff'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'message_board',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


envs = {
    'develop': DevelopConfig,
}
