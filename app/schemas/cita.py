from pydantic import BaseModel
from datetime import date


class CitaBase(BaseModel):
    id_mascota: int
    id_veterinario: int
    diagnostico: str
    fecha: date
    estado: str
    valor_consulta: float


class CitaCreate(CitaBase):
    pass


class CitaResponse(CitaBase):
    id_cita: int

    model_config = {'from_attributes': True}