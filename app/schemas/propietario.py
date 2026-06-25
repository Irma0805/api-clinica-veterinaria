from pydantic import BaseModel, EmailStr


class PropietarioBase(BaseModel):
    DNI: str
    nombre: str
    apellidos: str
    telefono: str
    email: str


class PropietarioCreate(PropietarioBase):
    pass  # De momento lo que se envía para crear es lo mismo que la base


class PropietarioResponse(PropietarioBase):
    id_propietario: int

    model_config = {'from_attributes': True}