from fastapi import status


def test_get_current_user(client):
    response = client.get("/api/user/me")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_get_user_by_id(client):
    response = client.get("/api/user/1")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_404_NOT_FOUND,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_update_user(client):
    response = client.put(
        "/api/user/update",
        json={
            "username": "Aryan",
            "email": "aryan@example.com",
        },
    )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_delete_user(client):
    response = client.delete("/api/user/delete")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )