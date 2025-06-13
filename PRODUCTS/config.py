import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://admin:admin123@db:5432/productos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False