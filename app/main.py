from fastapi import FastAPI
from app.config.settings import settings
from app.database.db_connection import engine, Base
from contextlib import asynccontextmanager
from sqlalchemy import text

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    lifespan=lifespan
)

@app.get('/', tags=['Home'])
def home():
    return {'message': 'API Clínica Veterinaria'}

@app.get('/health-db', tags=['Health'])
def db_check():
    with engine.connect() as connection:
        connection.execute(text('SELECT 1'))
    return {'message': 'Conexión a BD OK'}