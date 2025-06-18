import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://admin:admin123@db3:5432/auth'
    SQLALCHEMY_TRACK_MODIFICATIONS = False