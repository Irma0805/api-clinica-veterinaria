from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, ForeignKey
from app.database.db_connection import Base


class Mascota(Base):
    __tablename__ = 'mascotas'

    id_mascotas: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_propietario: Mapped[int] = mapped_column(ForeignKey('propietarios.id_propietario'))
    especie_mascota: Mapped[str] = mapped_column(String(50))
    nombre: Mapped[str] = mapped_column(String(50))
    raza: Mapped[str] = mapped_column(String(50))
    fecha_nacimiento: Mapped[Date] = mapped_column(Date)