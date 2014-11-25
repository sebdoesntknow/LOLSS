import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # Get secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Mailserver conf
    LOLSS_MAIL_SUBJECT_PREFIX = os.environ.get('LOLSS_MAIL_PREFIX')
    LOLSS_MAIL_SENDER = os.environ.get('LOLSS_MAIL_SENDER')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAILSERVER_PORT')
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    LOLSS_ADMIN = os.environ.get('LOLSS_ADMIN')

    # Database features
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

config = {
            'development': DevelopmentConfig,
            'testing': TestingConfig,
            'production': ProductionConfig,
            ## Default value when no explicit env ##
            'default': DevelopmentConfig
        }

