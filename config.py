from decouple import config as cf

SECRET_KEY = cf('SECRET_KEY')
DATABASE_URL = cf('DATABASE_URL')
API_KEY = cf('DATABASE_URL')
REST_ENDPOINT = cf('REST_ENDPOINT')