from pydantic import BaseModel
from datetime import date


class CitasTratamientosBase(BaseModel):
    id_cita: int
    id_tratamiento: int
    fecha_inicio: date
    fecha_fin: date
    dosis: str
    seguimiento: str


class CitasTratamientosCreate(CitasTratamientosBase):
    pass


class CitasTratamientosResponse(CitasTratamientosBase):

    model_config = {'from_attributes': True}