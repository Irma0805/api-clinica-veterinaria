from pydantic import BaseModel, Field, field_validator
from datetime import date


class MascotaBase(BaseModel):
    especie_mascota: str = Field(..., min_length=2, max_length=50, description="Ej: Perro, Gato")
    nombre: str = Field(..., min_length=1, max_length=50, description="Nombre de la mascota")
    raza: str = Field(..., min_length=2, max_length=50, description="Raza de la mascota")
    fecha_nacimiento: date


class MascotaCreate(MascotaBase):
    id_propietario: int

    # Validador para evitar fechas de nacimiento en el futuro
    @field_validator('fecha_nacimiento')
    def validar_fecha_nacimiento(cls, v):
        if v > date.today():
            raise ValueError('La fecha de nacimiento no puede ser una fecha futura.')
        return v

class MascotaResponse(MascotaBase):
    id_mascotas: int
    id_propietario: int

    class Config:
        from_attributes = True  # El estándar correcto para Pydantic v2 en tu entorno