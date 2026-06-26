from pydantic import BaseModel


class TratamientoBase(BaseModel):
    nombre_tratamiento: str
    tipo_tratamiento: str
    descripcion: str
    precio_kg: float


class TratamientoCreate(TratamientoBase):
    pass


class TratamientoResponse(TratamientoBase):
    id_tratamiento: int

    model_config = {'from_attributes': True}