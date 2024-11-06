import sqlalchemy
from sqlalchemy.orm import sessionmaker
from src.models.sql_base import SQL_Base
from src.models.animal import Animal # import all of your objects that inherit from SQLBase

url = 'mysql+pymysql://root:123456@localhost/nenos_academy'
engine = sqlalchemy.create_engine(url)

SQL_Base.metadata.create_all(engine)

# example of interacting with the db
# Session = sessionmaker(bind=engine)
# session = Session()

# for i in range(10):
#     new_animal = Animal(
#         name=str(i),
#         species=str(i),
#         common_name=str(i),
#         rescued=True,
#     )
#     session.add(new_animal)

# session.commit()  # required to persist the changes in db