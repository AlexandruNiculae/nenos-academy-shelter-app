from sqlalchemy import Column, Integer, String, Boolean

from db.sql.models import SQL_Base


class Animal(SQL_Base):  # inherit from sql base to make it an sql object and connect it to a table
    __tablename__ = 'animals'  # db table name

    id = Column(Integer, primary_key=True)  # id column (mandatory)
    name = Column(String(10), nullable=False) # db column
    species = Column(String(10), nullable=False) # db column
    common_name = Column(String(10), nullable=False) # db column
    rescued = Column(Boolean, nullable=False)
