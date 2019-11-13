import os 
import psycopg2

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
conn = psycopg2.connect('DATABASE_URL', sslmode='require')