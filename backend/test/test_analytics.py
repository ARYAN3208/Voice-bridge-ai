from fastapi import status


def test_dashboard_analytics(client):
    response = client.get("/api/analytics/dashboard")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_translation_statistics(client):
    response = client.get("/api/analytics/translations")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_language_statistics(client):
    response = client.get("/api/analytics/languages")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_usage_statistics(client):
    response = client.get("/api/analytics/usage")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_export_analytics(client):
    response = client.get("/api/analytics/export")

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_404_NOT_FOUND,
    )