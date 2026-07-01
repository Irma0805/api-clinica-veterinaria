from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_listar_citas():
    response = client.get('/citas/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_crear_cita():
    response = client.post('/citas/', json={
        'id_mascota': 1,
        'id_veterinario': 2,
        'diagnostico': 'Revisión general',
        'fecha': '2026-07-01',
        'estado': 'programada',
        'valor_consulta': 50.00
    })
    assert response.status_code == 201
    assert response.json()['diagnostico'] == 'Revisión general'


def test_cita_no_encontrada():
    response = client.get('/citas/9999')
    assert response.status_code == 404


def test_crear_cita_sin_datos():
    response = client.post('/citas/', json={})
    assert response.status_code == 422