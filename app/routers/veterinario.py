from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.db_connection import get_db
from app.schemas.veterinario import VeterinarioCreate, VeterinarioResponse
from app.services import veterinario as service

router = APIRouter(prefix='/veterinarios', tags=['Veterinarios'])


@router.get('/', response_model=list[VeterinarioResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get('/{id}', response_model=VeterinarioResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    veterinario = service.get_by_id(db, id)
    if veterinario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Veterinario con id {id} no encontrado"
        )
    return veterinario


@router.post('/', response_model=VeterinarioResponse, status_code=status.HTTP_201_CREATED)
def crear(data: VeterinarioCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put('/{id}', response_model=VeterinarioResponse)
def actualizar(id: int, data: VeterinarioCreate, db: Session = Depends(get_db)):
    veterinario = service.update(db, id, data)
    if veterinario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Veterinario con id {id} no encontrado"
        )
    return veterinario


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    veterinario = service.get_by_id(db, id)
    if veterinario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Veterinario con id {id} no encontrado"
        )

    try:
        service.delete(db, id)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se puede eliminar el veterinario porque tiene citas asociadas."
        )