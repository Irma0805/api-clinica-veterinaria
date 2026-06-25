from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.schemas.mascota import MascotaCreate, MascotaResponse
from app.services import mascota as service

from fastapi import HTTPException

router = APIRouter(prefix='/mascotas', tags=['Mascotas'])


@router.get('/', response_model=list[MascotaResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get('/{id}', response_model=MascotaResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    return service.get_by_id(db, id)


@router.post('/', response_model=MascotaResponse, status_code=status.HTTP_201_CREATED)
def crear(data: MascotaCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put('/{id}', response_model=MascotaResponse)
def actualizar(id: int, data: MascotaCreate, db: Session = Depends(get_db)):
    mascota = service.update(db, id, data)
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return mascota


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    exito = service.delete(db, id)
    if not exito:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return None