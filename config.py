import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'samplesqlserver-123.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'azuredb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'udacity@2020'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'blobstorageaccoun12'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '/OMzQLNMFa5FoXi8N9syp6was+4lA3yesv1p8vI194VtaT7rHT8x7ujT/4PbLIoSv43ljyqAQEynQBVqpRKgcA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
