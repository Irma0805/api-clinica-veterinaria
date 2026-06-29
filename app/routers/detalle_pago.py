from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.schemas.detalle_pago import DetallePagoCreate, DetallePagoResponse
from app.services import detalle_pago as service

router = APIRouter(prefix='/detalle-pago', tags=['Detalle Pago'])


@router.get('/', response_model=list[DetallePagoResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get('/{id}', response_model=DetallePagoResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    detalle = service.get_by_id(db, id)
    if detalle is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Detalle de pago con id {id} no encontrado"
        )
    return detalle


@router.post('/', response_model=DetallePagoResponse, status_code=status.HTTP_201_CREATED)
def crear(data: DetallePagoCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put('/{id}', response_model=DetallePagoResponse)
def actualizar(id: int, data: DetallePagoCreate, db: Session = Depends(get_db)):
    detalle = service.update(db, id, data)
    if detalle is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Detalle de pago con id {id} no encontrado"
        )
    return detalle


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    detalle = service.delete(db, id)
    if detalle is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Detalle de pago con id {id} no encontrado"
        )