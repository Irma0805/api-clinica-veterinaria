from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.db_connection import get_db
from app.schemas.cita import CitaCreate, CitaResponse
from app.services import cita as service

router = APIRouter(prefix='/citas', tags=['Citas'])


@router.get('/', response_model=list[CitaResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get('/{id}', response_model=CitaResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    cita = service.get_by_id(db, id)
    if cita is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cita con id {id} no encontrada"
        )
    return cita


@router.post('/', response_model=CitaResponse, status_code=status.HTTP_201_CREATED)
def crear(data: CitaCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put('/{id}', response_model=CitaResponse)
def actualizar(id: int, data: CitaCreate, db: Session = Depends(get_db)):
    cita = service.update(db, id, data)
    if cita is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cita con id {id} no encontrada"
        )
    return cita


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    cita = service.get_by_id(db, id)
    if cita is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cita con id {id} no encontrada"
        )
    try:
        service.delete(db, id)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se puede eliminar la cita porque tiene tratamientos asociados."
        )