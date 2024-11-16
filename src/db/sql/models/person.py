from sqlalchemy import Column, Integer, String

from src.db.sql.models import SQL_Base


class Person(SQL_Base):
    __tablename__ = 'person'  # db table name

    id = Column(Integer, primary_key=True)  # id column (mandatory)
    name = Column(String(10), nullable=False) # db column
    surname = Column(String(10), nullable=False) # db column
    email_address = Column(String(10), nullable=False) # db column
    phone_number = Column(String(10), nullable=False) # db column
