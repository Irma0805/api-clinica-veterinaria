from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.db_connection import get_db
from app.schemas.pago import PagoCreate, PagoResponse
from app.services import pago as service

router = APIRouter(prefix='/pagos', tags=['Pagos'])


@router.get('/', response_model=list[PagoResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get('/{id}', response_model=PagoResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    pago = service.get_by_id(db, id)
    if pago is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pago con id {id} no encontrado"
        )
    return pago


@router.post('/', response_model=PagoResponse, status_code=status.HTTP_201_CREATED)
def crear(data: PagoCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put('/{id}', response_model=PagoResponse)
def actualizar(id: int, data: PagoCreate, db: Session = Depends(get_db)):
    pago = service.update(db, id, data)
    if pago is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pago con id {id} no encontrado"
        )
    return pago


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    pago = service.get_by_id(db, id)
    if pago is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pago con id {id} no encontrado"
        )
    try:
        service.delete(db, id)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se puede eliminar el pago porque tiene un detalle de pago asociado."
        )