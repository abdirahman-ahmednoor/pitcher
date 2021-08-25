import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS =True
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # simplemde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # photos uplaod configuration
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blade:maziwa@localhost/pitch'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blade:maziwa@localhost/pitch_test'

config_options = {
    'production':ProdConfig,
    'development':DevConfig,
    'test':TestConfig
}


                                   