import os

class Config(object):
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.getcwd()+"/login/users.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWITTER_OAUTH_CLIENT_KEY = "Yn6TucxEQvMhs90HAthcsfF5j"
    TWITTER_OAUTH_CLIENT_SECRET = "R8QbaPF1Qsd0Oqe10eSYNO59l8f8fXOWSjjaOOX0cjm3iwL9n7"
    EMAIL_SENDER = ""
    EMAIL_PASSWORD = ""
