from src.db.mongo.models import MongoBase


class ReturnForm(MongoBase):
    animal_id: int
    person_id: int
    return_reason: str
