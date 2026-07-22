from fastapi import status


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "healthy"


def test_docs_available(client):
    response = client.get("/docs")

    assert response.status_code == status.HTTP_200_OK


def test_openapi_available(client):
    response = client.get("/openapi.json")

    assert response.status_code == status.HTTP_200_OK


def test_redoc_available(client):
    response = client.get("/redoc")

    assert response.status_code == status.HTTP_200_OK