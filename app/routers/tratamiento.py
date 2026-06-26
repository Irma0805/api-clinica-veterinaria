from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.schemas.tratamiento import TratamientoCreate, TratamientoResponse
from app.services import tratamiento as service

router = APIRouter(prefix='/tratamientos', tags=['Tratamientos'])


@router.get('/', response_model=list[TratamientoResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get('/{id}', response_model=TratamientoResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    tratamiento = service.get_by_id(db, id)
    if tratamiento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tratamiento con id {id} no encontrado"
        )
    return tratamiento


@router.post('/', response_model=TratamientoResponse, status_code=status.HTTP_201_CREATED)
def crear(data: TratamientoCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put('/{id}', response_model=TratamientoResponse)
def actualizar(id: int, data: TratamientoCreate, db: Session = Depends(get_db)):
    tratamiento = service.update(db, id, data)
    if tratamiento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tratamiento con id {id} no encontrado"
        )
    return tratamiento


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    tratamiento = service.delete(db, id)
    if tratamiento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tratamiento con id {id} no encontrado"
        )