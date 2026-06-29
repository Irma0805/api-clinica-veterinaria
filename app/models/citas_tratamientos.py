from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, ForeignKey
from app.database.db_connection import Base


class CitasTratamientos(Base):
    __tablename__ = 'citas_tratamientos'

    id_cita: Mapped[int] = mapped_column(ForeignKey('citas.id_cita'), primary_key=True)
    id_tratamiento: Mapped[int] = mapped_column(ForeignKey('tratamientos.id_tratamiento'), primary_key=True)
    fecha_inicio: Mapped[Date] = mapped_column(Date)
    fecha_fin: Mapped[Date] = mapped_column(Date)
    dosis: Mapped[str] = mapped_column(String(100))
    seguimiento: Mapped[str] = mapped_column(String(255))