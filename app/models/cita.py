from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Float, ForeignKey
from app.database.db_connection import Base


class Cita(Base):
    __tablename__ = 'citas'

    id_cita: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_mascota: Mapped[int] = mapped_column(ForeignKey('mascotas.id_mascotas'))
    id_veterinario: Mapped[int] = mapped_column(ForeignKey('veterinarios.id_veterinario'))
    diagnostico: Mapped[str] = mapped_column(String(255))
    fecha: Mapped[Date] = mapped_column(Date)
    estado: Mapped[str] = mapped_column(String(50))
    valor_consulta: Mapped[float] = mapped_column(Float)