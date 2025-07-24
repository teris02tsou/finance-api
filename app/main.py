from fastapi import FastAPI
from app.database.db import database, engine, metadata
from app.models.transaction import transactions

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "Personal Finance API is running!"}
