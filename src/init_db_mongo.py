from pymongo import MongoClient

from src.models.person import Person


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["nenos-academy"]

def create_collections_from_models(*models):
    for model in models:
        # Use model name as the collection name, converting to snake_case if needed
        collection_name = model.__name__.lower()
        
        # Create collection if it doesn't exist already
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Created collection: {collection_name}")
        else:
            print(f"Collection '{collection_name}' already exists")

# Call the function with each model
mongodb_models = [
    Person
]

create_collections_from_models(*mongodb_models)  # create mongo db collections
