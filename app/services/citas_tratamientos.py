from sqlalchemy.orm import Session
from app.models.citas_tratamientos import CitasTratamientos
from app.schemas.citas_tratamientos import CitasTratamientosCreate


def get_all(db: Session):
    return db.query(CitasTratamientos).all()


def get_by_ids(db: Session, id_cita: int, id_tratamiento: int):
    return db.query(CitasTratamientos).filter(
        CitasTratamientos.id_cita == id_cita,
        CitasTratamientos.id_tratamiento == id_tratamiento
    ).first()


def create(db: Session, data: CitasTratamientosCreate):
    nueva = CitasTratamientos(**data.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def update(db: Session, id_cita: int, id_tratamiento: int, data: CitasTratamientosCreate):
    registro = get_by_ids(db, id_cita, id_tratamiento)
    if registro:
        for key, value in data.model_dump().items():
            setattr(registro, key, value)
        db.commit()
        db.refresh(registro)
    return registro


def delete(db: Session, id_cita: int, id_tratamiento: int):
    registro = get_by_ids(db, id_cita, id_tratamiento)
    if registro:
        db.delete(registro)
        db.commit()
    return registro