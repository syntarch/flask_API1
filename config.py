import os


current_path = os.path.dirname(os.path.realpath(__file__))
db_path = "sqlite:///" + current_path + "\\project.db"


class Config:
    DEBUG = False
    SECRET_KEY = 'no_one_know'
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False