from pydantic import BaseModel


class FosterHome(BaseModel):
    city: str
    street_name: str
    street_number: str
    apartment_number: int | None
    details: str | None
