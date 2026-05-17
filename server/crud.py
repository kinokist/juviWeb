from sqlalchemy.orm import Session
from server.models import TransportRecord

def create_record(db: Session, data):
    record = TransportRecord(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_records(db: Session):
    return db.query(TransportRecord).all()

def delete_record(db: Session, id: int):
    record = db.query(TransportRecord).filter(TransportRecord.id == id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()

    return {"success": True}