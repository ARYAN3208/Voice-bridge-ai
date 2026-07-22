from fastapi import status


def test_get_profile(client):
    response = client.get("/api/profile")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_update_profile(client):
    response = client.put(
        "/api/profile",
        json={
            "full_name": "Aryan Lande",
            "bio": "VoiceBridge AI Developer",
        },
    )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_change_password(client):
    response = client.put(
        "/api/profile/change-password",
        json={
            "current_password": "Password@123",
            "new_password": "NewPassword@123",
        },
    )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_upload_profile_picture(client):
    response = client.post(
        "/api/profile/upload-picture",
        files={
            "file": (
                "profile.png",
                b"dummy-image",
                "image/png",
            )
        },
    )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    )