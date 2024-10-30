from pydantic import BaseModel


class Animal(BaseModel):
    name: str
    species: str
    common_name: str
    rescued: bool
