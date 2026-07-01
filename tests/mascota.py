import random
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Test 1: GET lista devuelve 200 y una lista
def test_obtener_mascotas():
    response = client.get('/mascotas/')  # Revisa si tu ruta es /mascotas/ o /mascota/
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test 2: POST crea una mascota y devuelve 201
def test_crear_mascota():
    nombre_aleatorio = f"Firu-{random.randint(1000, 9999)}"

    response = client.post('/mascotas/', json={
        'nombre': nombre_aleatorio,
        'especie_mascota': 'Perro',
        'raza': 'Pastor Alemán',
        'fecha_nacimiento': '2023-01-15',
        'id_propietario': 1  # <-- ¡Cambiado a 'id_propietario'!
    })

    assert response.status_code == 201, f"Error de validación en mascota: {response.json()}"
    assert response.json()['nombre'] == nombre_aleatorio