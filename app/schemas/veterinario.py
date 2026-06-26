from pydantic import BaseModel


class VeterinarioBase(BaseModel):
    nombre: str
    apellidos: str
    especialidad: str


class VeterinarioCreate(VeterinarioBase):
    pass


class VeterinarioResponse(VeterinarioBase):
    id_veterinario: int

    model_config = {'from_attributes': True}