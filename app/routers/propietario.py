from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database.db_connection import get_db
from app.schemas.propietario import PropietarioCreate, PropietarioResponse
from app.services import propietario as service

router = APIRouter(prefix='/propietarios', tags=['Propietarios'])

@router.get('/', response_model=list[PropietarioResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get('/{id}', response_model=PropietarioResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    propietario = service.get_by_id(db, id)
    if not propietario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El propietario con ID {id} no existe."
        )
    return propietario

@router.post('/', response_model=PropietarioResponse, status_code=status.HTTP_201_CREATED)
def crear(data: PropietarioCreate, db: Session = Depends(get_db)):
    try:
        return service.create(db, data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo registrar: El DNI o el Email ya están registrados."
        )

@router.put('/{id}', response_model=PropietarioResponse)
def actualizar(id: int, data: PropietarioCreate, db: Session = Depends(get_db)):
    propietario = service.update(db, id, data)
    if not propietario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se puede actualizar: El propietario con ID {id} no existe."
        )
    return propietario

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    try:
        exito = service.delete(db, id)
        if not exito:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se puede eliminar: El propietario con ID {id} no existe."
            )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se puede eliminar el propietario porque tiene mascotas asociadas."
        )