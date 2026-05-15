from sqlalchemy.orm import Session
from models import TransportRecord

def create_record(db: Session, data):
    record = TransportRecord(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_records(db: Session):
    return db.query(TransportRecord).all()