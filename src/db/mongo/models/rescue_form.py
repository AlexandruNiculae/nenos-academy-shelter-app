from src.db.mongo.models import MongoBase


class RescueForm(MongoBase):
    animal_id: int
    rescued_state: str
