import pytest
from fastapi.testclient import TestClient

from backend.main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def sample_user():
    return {
        "username": "aryan",
        "email": "aryan@example.com",
        "password": "Password@123",
    }


@pytest.fixture
def login_data():
    return {
        "email": "aryan@example.com",
        "password": "Password@123",
    }


@pytest.fixture
def sample_translation():
    return {
        "text": "Hello, how are you?",
        "source_language": "en",
        "target_language": "hi",
    }


@pytest.fixture
def sample_audio():
    return {
        "filename": "sample.wav"
    }