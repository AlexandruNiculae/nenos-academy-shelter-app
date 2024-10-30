from pydantic import BaseModel

from src.models.animal import Animal
from src.models.person import Person

class ReturnForm(BaseModel):
    returned_animal: Animal
    returning_person: Person
    return_reason: str
