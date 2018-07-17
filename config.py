class Config:
    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:123456@127.0.0.1/flask_app'


settings = {
    'dev': DevelopmentConfig,

    'default': DevelopmentConfig
}
