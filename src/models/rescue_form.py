from pydantic import BaseModel

from src.models.animal import Animal


class RescueForm(BaseModel):
    rescued_animal: Animal
    rescued_state: str
