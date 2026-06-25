from pydantic import BaseModel
from datetime import date


class MascotaBase(BaseModel):
    especie_mascota: str
    nombre: str
    raza: str
    fecha_nacimiento: date


class MascotaCreate(MascotaBase):  # Lo que recibe el POST
    id_propietario: int


class MascotaResponse(MascotaBase):  # Lo que devuelve la API
    id_mascotas: int
    id_propietario: int

    model_config = {'from_attributes': True}