from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database.db_connection import get_db
from app.schemas.mascota import MascotaCreate, MascotaResponse
from app.services import mascota as service

router = APIRouter(prefix='/mascotas', tags=['Mascotas'])

@router.get('/', response_model=list[MascotaResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get('/{id}', response_model=MascotaResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    mascota = service.get_by_id(db, id)
    if not mascota:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La mascota con ID {id} no existe."
        )
    return mascota

@router.post('/', response_model=MascotaResponse, status_code=status.HTTP_201_CREATED)
def crear(data: MascotaCreate, db: Session = Depends(get_db)):
    try:
        return service.create(db, data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo registrar la mascota. Verifica que el id_propietario exista en la base de datos."
        )

@router.put('/{id}', response_model=MascotaResponse)
def actualizar(id: int, data: MascotaCreate, db: Session = Depends(get_db)):
    try:
        mascota = service.update(db, id, data)
        if not mascota:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se puede actualizar: La mascota con ID {id} no existe."
            )
        return mascota
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error al actualizar: Asegúrate de que el id_propietario asignado sea válido."
        )

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    exito = service.delete(db, id)
    if not exito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se puede eliminar: La mascota con ID {id} no existe."
        )
    return None