from sqlalchemy.orm import Session
from app.models.cita import Cita
from app.schemas.cita import CitaCreate


def get_all(db: Session):
    return db.query(Cita).all()


def get_by_id(db: Session, id: int):
    return db.query(Cita).filter(Cita.id_cita == id).first()


def create(db: Session, data: CitaCreate):
    nueva = Cita(**data.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def update(db: Session, id: int, data: CitaCreate):
    cita = get_by_id(db, id)
    if cita:
        for key, value in data.model_dump().items():
            setattr(cita, key, value)
        db.commit()
        db.refresh(cita)
    return cita


def delete(db: Session, id: int):
    cita = get_by_id(db, id)
    if cita:
        db.delete(cita)
        db.commit()
    return cita