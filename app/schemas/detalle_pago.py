from pydantic import BaseModel


class DetallePagoBase(BaseModel):
    id_pago: int
    seguro: str
    forma_pago: str


class DetallePagoCreate(DetallePagoBase):
    pass


class DetallePagoResponse(DetallePagoBase):
    id_detalle_pago: int

    model_config = {'from_attributes': True}