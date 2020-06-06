import os

class Config(object):
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.getcwd()+"/login/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWITTER_OAUTH_CLIENT_KEY = ""
    TWITTER_OAUTH_CLIENT_SECRET = ""
