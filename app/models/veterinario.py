from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database.db_connection import Base


class Veterinario(Base):
    __tablename__ = 'veterinarios'

    id_veterinario: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(50))
    apellidos: Mapped[str] = mapped_column(String(100))
    especialidad: Mapped[str] = mapped_column(String(100))