from http import HTTPStatus

from fastapi.testclient import TestClient

from deadpoolandwolverine_backend.app import app


def teste_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organização)
    response = client.get('/')  # Act (Ação)
    assert response.status_code == HTTPStatus.OK  # Assert (Acerto)
    assert response.json() == {'Hello': 'World'}  # Assert (Acerto)
