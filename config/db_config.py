# db_config.py
import os
import mysql.connector
from dotenv import load_dotenv
from pymongo import MongoClient
from urllib.parse import quote


# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Database:
    def __init__(self):
        self.db_config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME')
        }

    def get_connection(self):
        return mysql.connector.connect(**self.db_config)


class DBConfig:
    def __init__(self):
        try:
            user = quote(os.getenv('MONGO_DB_USER'))
            password = quote(os.getenv('MONGO_DB_PASSWORD'))
            host = os.getenv('MONGO_HOST')
            port = os.getenv('MONGO_PORT')
            database = os.getenv('MONGO_DB')
            self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/')
            self.db = self.client[database]
        except Exception as e:
            raise Exception(f"Error connecting to MongoDB: {e}")

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        self.client.close()