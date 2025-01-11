import uvicorn
from fastapi import FastAPI

from config import API_HOST, API_PORT
from api.routers.status import router as status_router
from api.routers.animals import router as animals_router

from db.sql.init_db import init_sql_db
from db.mongo.init_db import init_mongo_db


# Create FastAPI app
app = FastAPI(
    title="Nenos Academy Shelter API",
    description="An API used in the for the Nenos Academy Shelter App",
    version="1.0.0",
)

# Include routers
app.include_router(status_router, prefix="/api", tags=["API"])
app.include_router(animals_router, prefix="/animals", tags=["Animals"])

# Run the app via uvicorn
if __name__ == "__main__":
    print("Initialiazing SQL database")
    init_sql_db()

    print("Initialiazing Mongo database")
    init_mongo_db()

    uvicorn.run("api.main:app", host=API_HOST, port=API_PORT, reload=True)
