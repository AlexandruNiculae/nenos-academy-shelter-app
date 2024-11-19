from fastapi import APIRouter, Response

from src.common.data_transfer_objects.animals import AddAnimalDto
from src.db.sql.queries.animals import add_animal_into_the_db

router = APIRouter()

# GET -> fetch data
# PUT -> add data
# POST -> functions
# DELETE -> delete add

@router.put("")
def add_animal(dto: AddAnimalDto) -> Response:
    """
    Adds an animal to the database
    """

    add_animal_into_the_db(
        name=dto.name,
        species=dto.species,
        common_name=dto.common_name,
        rescued=dto.rescued,
    )
