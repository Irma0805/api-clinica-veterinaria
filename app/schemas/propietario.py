from pydantic import BaseModel, Field, EmailStr, field_validator
import re


# 1. ESQUEMA BASE: Campos comunes con validaciones de longitud
class PropietarioBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50, description="Nombre del propietario")
    apellidos: str = Field(..., min_length=2, max_length=100, description="Apellidos del propietario")

    # EmailStr valida automáticamente que tenga estructura de correo real (ejemplo@dominio.com)
    email: EmailStr

    telefono: str = Field(..., description="Teléfono de contacto de 9 dígitos")
    DNI: str = Field(..., description="DNI con 8 números y una letra")


# 2. ESQUEMA DE CREACIÓN: Aquí añadimos las reglas estrictas de formato
class PropietarioCreate(PropietarioBase):

    # Validador para el teléfono (9 dígitos numéricos en España)
    @field_validator('telefono')
    def validar_telefono_espanol(cls, v):
        # Limpiamos espacios o guiones si el usuario los puso por error
        telefono_limpio = v.replace(" ", "").replace("-", "")

        # Verifica que tenga 9 números y empiece por un número lógico de teléfono (6, 7, 8 o 9)
        if not re.match(r'^[6789]\d{8}$', telefono_limpio):
            raise ValueError('El teléfono debe tener exactamente 9 dígitos numéricos.')
        return telefono_limpio

    # Validador para el DNI (8 números y 1 letra)
    @field_validator('DNI')
    def validar_dni_formato(cls, v):
        dni_limpio = v.upper().strip()  # Lo pasa a mayúsculas y limpia espacios

        if not re.match(r'^\d{8}[A-Z]$', dni_limpio):
            raise ValueError('El DNI debe tener 8 números seguidos de una letra (ej: 12345678Z).')
        return dni_limpio


# 3. ESQUEMA DE RESPUESTA: Lo que la API muestra hacia afuera
class PropietarioResponse(PropietarioBase):
    id_propietario: int  # Usa 'id' o 'id_propietario' según como lo tengas en tu modelo de Base de Datos

    class Config:
        from_attributes = True  # Requerido en Pydantic v2 para leer objetos de SQLAlchemy