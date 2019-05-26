
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


# 开发者环境
class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'flask_database_develop',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


# 测试环境
class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'flask_database_testing',
        }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


# 演示环境
class StagingConfig(Config):
    TESTING = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '2000',
        'NAME': 'flask_database_staging',
        }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


# 线上环境
class ProductConfig(Config):
    TESTING = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '2000',
        'NAME': 'flask_database_product',
        }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
}

