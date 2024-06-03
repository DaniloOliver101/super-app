# db_config.py
import os
from pymongo import MongoClient

DATABASE_NAME = 'bank'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'root'

def get_db(collection_name):
    client = MongoClient(
        host='mongodb://localhost:27017/',
        username=DATABASE_USER,
        password=DATABASE_PASSWORD
    )
    db = client[DATABASE_NAME]
    return db[collection_name]