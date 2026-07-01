from sqlalchemy.orm import Session
from app.models.veterinario import Veterinario
from app.schemas.veterinario import VeterinarioCreate


def get_all(db: Session):
    return db.query(Veterinario).all()


def get_by_id(db: Session, id: int):
    return db.query(Veterinario).filter(Veterinario.id_veterinario == id).first()


def create(db: Session, data: VeterinarioCreate):
    nuevo = Veterinario(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def update(db: Session, id: int, data: VeterinarioCreate):
    veterinario = get_by_id(db, id)
    if veterinario:
        for key, value in data.model_dump().items():
            setattr(veterinario, key, value)
        db.commit()
        db.refresh(veterinario)
    return veterinario


def delete(db: Session, id: int):
    veterinario = get_by_id(db, id)
    if veterinario:
        db.delete(veterinario)
        db.commit()
    return veterinario