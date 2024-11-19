from src.db.sql.connection import SQLSesssion
from src.db.sql.models import Animal




def add_animal_into_the_db(name: str, species: str, common_name: str, rescued: bool) -> None:
    """
    Add an animal into the database
    """
    with SQLSesssion() as session:
        animal = Animal(
            name=name,
            species=species,
            common_name=common_name,
            rescued=rescued
        )
        session.add(animal)
        session.commit()
