from pydantic import BaseModel

from src.models.foster_home import FosterHome
from src.models.animal import Animal
from src.models.person import Person


class AdoptionForm(BaseModel):
    adopting_person: Person
    foster_home: FosterHome
    adopted_animal: Animal
