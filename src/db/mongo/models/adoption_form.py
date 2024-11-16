from src.db.mongo.models import MongoBase

class AdoptionForm(MongoBase):
    adopting_person_id: int
    foster_home_id: int
    animal_id: int
