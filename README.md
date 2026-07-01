# 🐾 API REST Clínica Veterinaria

API REST para la gestión de una clínica veterinaria, desarrollada con FastAPI y PostgreSQL.

## 👥 Equipo

- **Irma Ortiz** — [@Irma0805](https://github.com/Irma0805)
- **Carmen Lareo** — [@carmenlareo](https://github.com/carmenlareo)

Proyecto desarrollado en el Bootcamp de Programación de **Factoría F5**.

---

## 🛠️ Tecnologías

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.13 | Lenguaje principal |
| FastAPI | Latest | Framework de la API REST |
| SQLAlchemy | 2.0 | ORM para la base de datos |
| PostgreSQL | 18 | Base de datos relacional |
| Pydantic | V2 | Validación de datos |
| psycopg | 3 | Driver de conexión a PostgreSQL |
| pytest | Latest | Tests automáticos |
| uvicorn | Latest | Servidor ASGI |

---

## 🏗️ Arquitectura

El proyecto sigue una arquitectura de **4 capas** con separación de responsabilidades:

```
app/
├── config/
│   └── settings.py          # Variables de entorno (.env)
├── database/
│   └── db_connection.py     # Conexión a PostgreSQL
├── models/                  # Capa 1: Tablas SQLAlchemy
│   ├── propietario.py
│   ├── mascota.py
│   ├── veterinario.py
│   ├── cita.py
│   ├── tratamiento.py
│   ├── citas_tratamientos.py
│   ├── pago.py
│   └── detalle_pago.py
├── schemas/                 # Capa 2: Validación Pydantic
│   ├── propietario.py
│   ├── mascota.py
│   ├── veterinario.py
│   ├── cita.py
│   ├── tratamiento.py
│   ├── citas_tratamientos.py
│   ├── pago.py
│   └── detalle_pago.py
├── services/                # Capa 3: Lógica de negocio
│   ├── propietario.py
│   ├── mascota.py
│   ├── veterinario.py
│   ├── cita.py
│   ├── tratamiento.py
│   ├── citas_tratamientos.py
│   ├── pago.py
│   └── detalle_pago.py
├── routers/                 # Capa 4: Endpoints HTTP
│   ├── propietario.py
│   ├── mascota.py
│   ├── veterinario.py
│   ├── cita.py
│   ├── tratamiento.py
│   ├── citas_tratamientos.py
│   ├── pago.py
│   └── detalle_pago.py
└── main.py                  # Punto de entrada de la aplicación
```

---

## 📊 Modelo de datos

```
Propietarios (1) ──→ (N) Mascotas
Mascotas     (1) ──→ (N) Citas
Veterinarios (1) ──→ (N) Citas
Citas        (N) ──→ (M) Tratamientos  ← tabla puente citas_tratamientos
Propietarios (1) ──→ (N) Pagos
Tratamientos (1) ──→ (N) Pagos
Pagos        (1) ──→ (1) Detalle_del_pago
```

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Irma0805/api-clinica-veterinaria.git
cd api-clinica-veterinaria
```

### 2. Crear y activar el entorno virtual

```bash
# Windows/PowerShell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto basándote en `.env.example`:

```env
app_name=API Clínica Veterinaria
app_version=1.0.0
app_description=API REST para gestión de clínica veterinaria
db_host=localhost
db_port=5432
db_name=clinica_veterinaria
db_user=postgres
db_password=tu_password
```

### 5. Crear la base de datos

Crea una base de datos vacía llamada `clinica_veterinaria` en PostgreSQL. Las tablas se crean automáticamente al arrancar el servidor.

### 6. Arrancar el servidor

```bash
uvicorn app.main:app --reload
```

---

## 📡 Endpoints disponibles

| Entidad | GET lista | GET por id | POST | PUT | DELETE |
|---|---|---|---|---|---|
| Propietarios | `GET /propietarios/` | `GET /propietarios/{id}` | `POST /propietarios/` | `PUT /propietarios/{id}` | `DELETE /propietarios/{id}` |
| Mascotas | `GET /mascotas/` | `GET /mascotas/{id}` | `POST /mascotas/` | `PUT /mascotas/{id}` | `DELETE /mascotas/{id}` |
| Veterinarios | `GET /veterinarios/` | `GET /veterinarios/{id}` | `POST /veterinarios/` | `PUT /veterinarios/{id}` | `DELETE /veterinarios/{id}` |
| Citas | `GET /citas/` | `GET /citas/{id}` | `POST /citas/` | `PUT /citas/{id}` | `DELETE /citas/{id}` |
| Tratamientos | `GET /tratamientos/` | `GET /tratamientos/{id}` | `POST /tratamientos/` | `PUT /tratamientos/{id}` | `DELETE /tratamientos/{id}` |
| Citas Tratamientos | `GET /citas-tratamientos/` | `GET /citas-tratamientos/{id_cita}/{id_tratamiento}` | `POST /citas-tratamientos/` | `PUT /citas-tratamientos/{id_cita}/{id_tratamiento}` | `DELETE /citas-tratamientos/{id_cita}/{id_tratamiento}` |
| Pagos | `GET /pagos/` | `GET /pagos/{id}` | `POST /pagos/` | `PUT /pagos/{id}` | `DELETE /pagos/{id}` |
| Detalle Pago | `GET /detalle-pago/` | `GET /detalle-pago/{id}` | `POST /detalle-pago/` | `PUT /detalle-pago/{id}` | `DELETE /detalle-pago/{id}` |

---

## ✅ Códigos de respuesta HTTP

| Código | Significado | Cuándo ocurre |
|---|---|---|
| 200 | OK | GET correcto |
| 201 | Created | POST correcto |
| 204 | No Content | DELETE correcto |
| 404 | Not Found | Recurso no encontrado |
| 409 | Conflict | Intento de eliminar un registro con dependencias |
| 422 | Unprocessable Entity | Datos de entrada inválidos (Pydantic) |

---

## 🧪 Tests

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Ejecutar tests de una entidad concreta
pytest tests/test_veterinarios.py -v
```

---

## 📐 Principios aplicados

- **KISS** — cada archivo tiene una única responsabilidad
- **DRY** — el patrón de 4 capas se repite igual para cada entidad
- **YAGNI** — solo se implementa lo necesario para cada entidad

---

## 🔀 GitFlow

El proyecto usa GitFlow con ramas protegidas:

- `main` — rama de producción (solo recibe merges desde develop)
- `develop` — rama de desarrollo (integración de features)
- `feature/*` — ramas de funcionalidades (una por entidad)

Todas las PRs requieren **1 aprobación** antes del merge.

---

## 📚 Documentación automática

Con el servidor arrancado, accede a la documentación interactiva en:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
