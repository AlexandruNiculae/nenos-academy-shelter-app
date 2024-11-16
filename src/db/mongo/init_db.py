from src.db.mongo.connection import MONGO_DB
from src.db.mongo.models import * # pylint: disable=wildcard-import

_mongo_db_models = [
    AdoptionForm,
    RescueForm,
    ReturnForm,
]

def _create_collections_from_models(*models: list[MongoBase]) -> None:
    """
    Creates the mongo db collections for the objects given
    """
    existing_collections = MONGO_DB.list_collection_names()

    for model in models:
        # Use model name as the collection name, converting to snake_case if needed
        collection_name = model.__name__.lower()

        # Create collection if it doesn't exist already
        if collection_name not in existing_collections:
            MONGO_DB.create_collection(collection_name)
            print(f"Created collection: {collection_name}")
        else:
            print(f"Collection '{collection_name}' already exists")

def init_mongo_db() -> None:
    """
    Init Mongo DB
    """
    _create_collections_from_models(*_mongo_db_models)
