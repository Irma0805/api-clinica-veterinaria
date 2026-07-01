from pydantic import BaseModel


class PagoBase(BaseModel):
    id_propietario: int
    id_tratamiento: int
    estado: str


class PagoCreate(PagoBase):
    pass


class PagoResponse(PagoBase):
    id_pago: int

    model_config = {'from_attributes': True}