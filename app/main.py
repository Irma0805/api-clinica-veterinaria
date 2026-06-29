from fastapi import FastAPI
from app.database.db_connection import Base, engine


from app.routers import mascota as mascota_router
from app.routers import propietario as propietario_router
from app.routers import veterinario as veterinario_router
from app.routers import cita as cita_router
from app.routers import tratamiento as tratamiento_router
from app.routers import citas_tratamientos as citas_tratamientos_router
from app.routers import pago as pago_router
from app.routers import detalle_pago as detalle_pago_router

from app.models.propietario import Propietario # noqa
from app.models.mascota import Mascota # noqa
from app.models.veterinario import Veterinario # noqa
from app.models.cita import Cita # noqa
from app.models.tratamiento import Tratamiento # noqa
from app.models.citas_tratamientos import CitasTratamientos  # noqa
from app.models.pago import Pago  # noqa
from app.models.detalle_pago import DetallePago  # noqa

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Clínica Veterinaria",
    version="1.0.0",
    description="API REST para gestión de clínica veterinaria"
)

# Registramos ambos módulos en FastAPI
app.include_router(mascota_router.router)
app.include_router(propietario_router.router)
app.include_router(veterinario_router.router)
app.include_router(cita_router.router)
app.include_router(tratamiento_router.router)
app.include_router(citas_tratamientos_router.router)
app.include_router(pago_router.router)
app.include_router(detalle_pago_router.router)


@app.get("/", tags=["Home"])
def home():
    return {"message": "API Clínica Veterinaria"}