import pymongo

from config import DBNAME

MONGO_HOST = "mongodb"
MONGO_PORT = "27017"
MONGO_DBNAME = DBNAME

def generate_mongo_url() -> str:
    """
    Generate Mongo DB URL
    """
    return f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"

MONGO_URL = generate_mongo_url()
MONGO_CLIENT = pymongo.MongoClient(MONGO_URL)
MONGO_DB = MONGO_CLIENT[MONGO_DBNAME]
