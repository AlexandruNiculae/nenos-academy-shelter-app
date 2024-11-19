from pydantic import BaseModel

class AddAnimalDto(BaseModel):
    name: str
    species: str
    common_name: str
    rescued: bool = False
