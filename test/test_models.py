from pytest import raises

from src.models.animal import Animal
from src.models.foster_home import FosterHome


def test_create_animal_with_valid_data() -> None:
    _ = Animal(
        name="Rocky",
        species="Felis Catus",
        common_name="cat",
        rescued=True
    )

def test_create_animal_with_invalid_data() -> None:
    with raises(ValueError):
        _ = Animal(
            name=1231,
            species="Felis Catus",
            common_name="cat",
            rescued=True
        )

def test_create_foster_home_with_valid_data() -> None:
    _ = FosterHome(
        city="Bucuresti",
        street_name="Revolutiei",
        street_number="12",
        apartment_number=None,
        details="Usa de pe stanga"
    )

def test_create_foster_home_with_invalid_data() -> None:
    with raises(ValueError):
        _ = FosterHome(
            city="Bucuresti",
            street_name="Revolutiei",
            street_number=12,
            apartment_number=9,
            details="Usa de pe dreapta"
        )
