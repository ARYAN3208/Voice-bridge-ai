from fastapi import status


def test_get_history(client):
    response = client.get("/api/history")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_get_history_by_id(client):
    response = client.get("/api/history/1")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_404_NOT_FOUND,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_delete_history(client):
    response = client.delete("/api/history/1")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_404_NOT_FOUND,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_clear_history(client):
    response = client.delete("/api/history")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_download_history(client):
    response = client.get("/api/history/export")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_404_NOT_FOUND,
    )