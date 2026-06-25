from fastapi import FastAPI
from app.database.db_connection import Base, engine


from app.routers import mascota as mascota_router
from app.routers import propietario as propietario_router  # 👈 NUEVO

from app.models.propietario import Propietario
from app.models.mascota import Mascota

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Clínica Veterinaria",
    version="1.0.0",
    description="API REST para gestión de clínica veterinaria"
)

# Registramos ambos módulos en FastAPI
app.include_router(mascota_router.router)
app.include_router(propietario_router.router)  # 👈 NUEVO


@app.get("/", tags=["Home"])
def home():
    return {"message": "API Clínica Veterinaria"}