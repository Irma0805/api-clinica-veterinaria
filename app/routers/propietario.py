from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.schemas.propietario import PropietarioCreate, PropietarioResponse
from app.services import propietario as service

from fastapi import HTTPException

router = APIRouter(prefix='/propietarios', tags=['Propietarios'])


@router.get('/', response_model=list[PropietarioResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get('/{id}', response_model=PropietarioResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    return service.get_by_id(db, id)


@router.post('/', response_model=PropietarioResponse, status_code=status.HTTP_201_CREATED)
def crear(data: PropietarioCreate, db: Session = Depends(get_db)):
    return service.create(db, data)

@router.put('/{id}', response_model=PropietarioResponse)
def actualizar(id: int, data: PropietarioCreate, db: Session = Depends(get_db)):
    propietario = service.update(db, id, data)
    if not propietario:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return propietario

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int, db: Session = Depends(get_db)):
    exito = service.delete(db, id)
    if not exito:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return None