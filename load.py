from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def load_data(data):
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    db = client["prefectDB"]
    collection = db["dados"]
    result = collection.insert_one(data)
    return str(result.inserted_id)
