from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from app.database.db_connection import Base


class Pago(Base):
    __tablename__ = 'pagos'

    id_pago: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_propietario: Mapped[int] = mapped_column(ForeignKey('propietarios.id_propietario'))
    id_tratamiento: Mapped[int] = mapped_column(ForeignKey('tratamientos.id_tratamiento'))
    estado: Mapped[str] = mapped_column(String(50))
