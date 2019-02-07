import os


class DefaultConfig(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db".format(
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD"),
        db=os.environ.get("DB"),
        host=os.environ.get("HOST")
    )
