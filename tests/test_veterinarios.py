from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_listar_veterinarios():
    response = client.get('/veterinarios/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_crear_veterinario():
    response = client.post('/veterinarios/', json={
        'nombre': 'Paula',
        'apellidos': 'Ríos',
        'especialidad': 'Cirugía'
    })
    assert response.status_code == 201
    assert response.json()['nombre'] == 'Paula'


def test_veterinario_no_encontrado():
    response = client.get('/veterinarios/9999')
    assert response.status_code == 404


def test_crear_veterinario_sin_datos():
    response = client.post('/veterinarios/', json={})
    assert response.status_code == 422