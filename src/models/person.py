from pydantic import BaseModel


class Person(BaseModel):
    name: str
    surname: str
    email_address: str
    phone_number: str