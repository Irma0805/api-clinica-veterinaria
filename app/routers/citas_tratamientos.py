from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.schemas.citas_tratamientos import CitasTratamientosCreate, CitasTratamientosResponse
from app.services import citas_tratamientos as service

router = APIRouter(prefix='/citas-tratamientos', tags=['Citas Tratamientos'])


@router.get('/', response_model=list[CitasTratamientosResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get('/{id_cita}/{id_tratamiento}', response_model=CitasTratamientosResponse)
def obtener(id_cita: int, id_tratamiento: int, db: Session = Depends(get_db)):
    registro = service.get_by_ids(db, id_cita, id_tratamiento)
    if registro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Registro con id_cita {id_cita} e id_tratamiento {id_tratamiento} no encontrado"
        )
    return registro


@router.post('/', response_model=CitasTratamientosResponse, status_code=status.HTTP_201_CREATED)
def crear(data: CitasTratamientosCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put('/{id_cita}/{id_tratamiento}', response_model=CitasTratamientosResponse)
def actualizar(id_cita: int, id_tratamiento: int, data: CitasTratamientosCreate, db: Session = Depends(get_db)):
    registro = service.update(db, id_cita, id_tratamiento, data)
    if registro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Registro con id_cita {id_cita} e id_tratamiento {id_tratamiento} no encontrado"
        )
    return registro


@router.delete('/{id_cita}/{id_tratamiento}', status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id_cita: int, id_tratamiento: int, db: Session = Depends(get_db)):
    registro = service.delete(db, id_cita, id_tratamiento)
    if registro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Registro con id_cita {id_cita} e id_tratamiento {id_tratamiento} no encontrado"
        )