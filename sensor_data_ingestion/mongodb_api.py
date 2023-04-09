from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
db = client[settings.MONGODB_DB_NAME]

def insert_document(collection_name, document):
    collection = db[collection_name]
    return collection.insert_one(document)