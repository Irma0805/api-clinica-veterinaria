from sqlalchemy.orm import Session
from app.models.mascota import Mascota
from app.schemas.mascota import MascotaCreate


def get_all(db: Session):
    return db.query(Mascota).all()


def get_by_id(db: Session, id: int):
    return db.query(Mascota).filter(Mascota.id_mascotas == id).first()


def create(db: Session, data: MascotaCreate):
    nueva = Mascota(**data.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def update(db: Session, id: int, data: MascotaCreate):
    mascota = get_by_id(db, id)
    if mascota:
        for key, value in data.model_dump().items():
            setattr(mascota, key, value)
        db.commit()
        db.refresh(mascota)
    return mascota


def delete(db: Session, id: int):
    mascota = get_by_id(db, id)
    if mascota:
        db.delete(mascota)
        db.commit()
        return True
    return False