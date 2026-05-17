from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from server.database import SessionLocal, engine
from server import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://kinokist.github.io",   # 프론트엔드 도메인
    "http://localhost:8000"         # 로컬 테스트용
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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