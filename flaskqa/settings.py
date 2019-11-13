import os 

# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_DATABASE_URI = "postgres://gcklzkkygxoeeq:8b31f0330761c818ad90bac7a519784a84ecb20895a67836708e3b95426c9d86@ec2-54-75-249-16.eu-west-1.compute.amazonaws.com:5432/d9ptt6kvfesls0"
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False