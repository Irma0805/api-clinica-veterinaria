import random
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

# Test 1: GET lista devuelve 200 y una lista
def test_listar_propietarios():
    response = client.get('/propietarios/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test 2: POST crea y devuelve 201
def test_crear_propietario():
    email_aleatorio = f"jose.test{random.randint(1000, 9999)}@ejemplo.com"

    response = client.post('/propietarios/', json={
        'nombre': 'Jose',
        'apellidos': 'García',
        'telefono': '612345678',
        'email': email_aleatorio,
        'DNI': '12345678Z'  # <-- ¡Añadimos el campo obligatorio que faltaba!
    })

    assert response.status_code == 201
    assert response.json()['nombre'] == 'Jose'
    assert response.json()['telefono'] == '612345678'

# Test 3: GET por id inexistente devuelve 404
def test_propietario_no_encontrado():
    response = client.get('/propietarios/9999')
    assert response.status_code == 404

# Test 4: POST con teléfono inválido devuelve 422 (Validación de Pydantic)
def test_crear_propietario_telefono_invalido():
    response = client.post('/propietarios/', json={
        'nombre': 'Marta',
        'apellidos': 'López',
        'telefono': '1234',  # Teléfono inválido (menos de 9 dígitos)
        'email': 'marta@email.com'
    })
    assert response.status_code == 422

# Test 5: POST sin datos obligatorios devuelve 422
def test_crear_propietario_sin_datos():
    response = client.post('/propietarios/', json={})
    assert response.status_code == 422