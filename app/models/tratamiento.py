from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from app.database.db_connection import Base


class Tratamiento(Base):
    __tablename__ = 'tratamientos'

    id_tratamiento: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre_tratamiento: Mapped[str] = mapped_column(String(100))
    tipo_tratamiento: Mapped[str] = mapped_column(String(100))
    descripcion: Mapped[str] = mapped_column(String(255))
    precio_kg: Mapped[float] = mapped_column(Float)