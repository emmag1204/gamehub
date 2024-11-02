import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/games.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/images')