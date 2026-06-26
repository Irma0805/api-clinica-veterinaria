from fastapi import FastAPI
from app.database.db_connection import Base, engine


from app.routers import mascota as mascota_router
from app.routers import propietario as propietario_router
from app.routers import veterinario as veterinario_router
from app.routers import cita as cita_router

from app.models.propietario import Propietario
from app.models.mascota import Mascota
from app.models.veterinario import Veterinario
from app.models.cita import Cita

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


@app.get("/", tags=["Home"])
def home():
    return {"message": "API Clínica Veterinaria"}