import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://admin:admin123@db2:5432/usuarios'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
