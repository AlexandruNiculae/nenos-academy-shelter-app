from db.sql.init_db import init_sql_db
from db.mongo.init_db import init_mongo_db


if __name__ == "__main__":
    print("Initialiazing SQL database")
    init_sql_db()

    print("Initialiazing Mongo database")
    init_mongo_db()
