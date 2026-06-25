from sqlalchemy.orm import Session
from app.models.propietario import Propietario
from app.schemas.propietario import PropietarioCreate


def get_all(db: Session):
    return db.query(Propietario).all()


def get_by_id(db: Session, id: int):
    return db.query(Propietario).filter(Propietario.id_propietario == id).first()


def create(db: Session, data: PropietarioCreate):
    nuevo = Propietario(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update(db: Session, id: int, data: PropietarioCreate):
    propietario = get_by_id(db, id)
    if propietario:
        for key, value in data.model_dump().items():
            setattr(propietario, key, value)
        db.commit()
        db.refresh(propietario)
    return propietario


def delete(db: Session, id: int):
    propietario = get_by_id(db, id)
    if propietario:
        db.delete(propietario)
        db.commit()
        return True
    return False