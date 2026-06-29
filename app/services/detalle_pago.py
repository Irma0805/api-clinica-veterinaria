from sqlalchemy.orm import Session
from app.models.detalle_pago import DetallePago
from app.schemas.detalle_pago import DetallePagoCreate


def get_all(db: Session):
    return db.query(DetallePago).all()


def get_by_id(db: Session, id: int):
    return db.query(DetallePago).filter(DetallePago.id_detalle_pago == id).first()


def create(db: Session, data: DetallePagoCreate):
    nuevo = DetallePago(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def update(db: Session, id: int, data: DetallePagoCreate):
    detalle = get_by_id(db, id)
    if detalle:
        for key, value in data.model_dump().items():
            setattr(detalle, key, value)
        db.commit()
        db.refresh(detalle)
    return detalle


def delete(db: Session, id: int):
    detalle = get_by_id(db, id)
    if detalle:
        db.delete(detalle)
        db.commit()
    return detalle