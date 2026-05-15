from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/records")
def create(data: schemas.TransportCreate, db: Session = Depends(get_db)):
    return crud.create_record(db, data)

@app.get("/records")
def read(db: Session = Depends(get_db)):
    return crud.get_records(db)