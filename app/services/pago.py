from sqlalchemy.orm import Session
from app.models.pago import Pago
from app.schemas.pago import PagoCreate


def get_all(db: Session):
    return db.query(Pago).all()


def get_by_id(db: Session, id: int):
    return db.query(Pago).filter(Pago.id_pago == id).first()


def create(db: Session, data: PagoCreate):
    nuevo = Pago(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def update(db: Session, id: int, data: PagoCreate):
    pago = get_by_id(db, id)
    if pago:
        for key, value in data.model_dump().items():
            setattr(pago, key, value)
        db.commit()
        db.refresh(pago)
    return pago


def delete(db: Session, id: int):
    pago = get_by_id(db, id)
    if pago:
        db.delete(pago)
        db.commit()
    return pago