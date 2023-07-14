from pymongo import MongoClient

def connect_to_database():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.ymail
    return db
