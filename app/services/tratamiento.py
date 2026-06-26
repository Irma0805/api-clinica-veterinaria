from sqlalchemy.orm import Session
from app.models.tratamiento import Tratamiento
from app.schemas.tratamiento import TratamientoCreate


def get_all(db: Session):
    return db.query(Tratamiento).all()


def get_by_id(db: Session, id: int):
    return db.query(Tratamiento).filter(Tratamiento.id_tratamiento == id).first()


def create(db: Session, data: TratamientoCreate):
    nuevo = Tratamiento(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def update(db: Session, id: int, data: TratamientoCreate):
    tratamiento = get_by_id(db, id)
    if tratamiento:
        for key, value in data.model_dump().items():
            setattr(tratamiento, key, value)
        db.commit()
        db.refresh(tratamiento)
    return tratamiento


def delete(db: Session, id: int):
    tratamiento = get_by_id(db, id)
    if tratamiento:
        db.delete(tratamiento)
        db.commit()
    return tratamiento