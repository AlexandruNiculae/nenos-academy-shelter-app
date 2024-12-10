from sqlalchemy import Column, Integer, String

from db.sql.models import SQL_Base


class FosterHome(SQL_Base):
    __tablename__ = 'foster_home'  # db table name

    id = Column(Integer, primary_key=True)  # id column (mandatory)
    city = Column(String(10), nullable=False) # db column
    street_name = Column(String(10), nullable=False) # db column
    street_number = Column(String(10), nullable=False) # db column
    apartment_number = Column(Integer, nullable=True) # db column
    details = Column(String(128), nullable=True) # db column
