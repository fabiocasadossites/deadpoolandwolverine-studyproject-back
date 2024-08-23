import pytest
from fastapi.testclient import TestClient

from deadpoolandwolverine_backend.app import app


@pytest.fixture
def client():
    return TestClient(app)  # Setup (Configuração)
