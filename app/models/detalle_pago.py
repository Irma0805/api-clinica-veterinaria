from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from app.database.db_connection import Base


class DetallePago(Base):
    __tablename__ = 'detalle_del_pago'

    id_detalle_pago: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_pago: Mapped[int] = mapped_column(ForeignKey('pagos.id_pago'))
    seguro: Mapped[str] = mapped_column(String(100))
    forma_pago: Mapped[str] = mapped_column(String(100))