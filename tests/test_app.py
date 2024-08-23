from http import HTTPStatus


def teste_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (Ação)
    assert response.status_code == HTTPStatus.OK  # Assert (Acerto)
    assert response.json() == {'message': 'Hello World'}  # Assert (Acerto)
