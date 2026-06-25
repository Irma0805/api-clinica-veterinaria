from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database.db_connection import Base


class Propietario(Base):
    __tablename__ = 'propietarios'

    id_propietario: Mapped[int] = mapped_column(primary_key=True, index=True)
    DNI: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    nombre: Mapped[str] = mapped_column(String(50))
    apellidos: Mapped[str] = mapped_column(String(100))
    telefono: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(100))