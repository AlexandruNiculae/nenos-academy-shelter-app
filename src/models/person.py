from src.models.mongo_base import MongoBase


class Person(MongoBase):  # make it a mongo db object to have the id attribute
    name: str
    surname: str
    email_address: str
    phone_number: str
