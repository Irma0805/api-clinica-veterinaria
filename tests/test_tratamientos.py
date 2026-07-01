from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_listar_tratamientos():
    response = client.get('/tratamientos/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_crear_tratamiento():
    response = client.post('/tratamientos/', json={
        'nombre_tratamiento': 'Vacuna antirrábica',
        'tipo_tratamiento': 'Vacuna',
        'descripcion': 'Vacuna obligatoria anual',
        'precio_kg': 15.50
    })
    assert response.status_code == 201
    assert response.json()['nombre_tratamiento'] == 'Vacuna antirrábica'


def test_tratamiento_no_encontrado():
    response = client.get('/tratamientos/9999')
    assert response.status_code == 404


def test_crear_tratamiento_sin_datos():
    response = client.post('/tratamientos/', json={})
    assert response.status_code == 422