from fastapi import status


def test_translate_text(client, sample_translation):
    response = client.post(
        "/api/translation/translate",
        json=sample_translation,
    )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_detect_language(client):
    response = client.post(
        "/api/translation/detect-language",
        json={
            "text": "Hello World"
        },
    )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_400_BAD_REQUEST,
    )


def test_supported_languages(client):
    response = client.get(
        "/api/translation/languages"
    )

    assert response.status_code == status.HTTP_200_OK


def test_empty_translation(client):
    response = client.post(
        "/api/translation/translate",
        json={
            "text": "",
            "source_language": "en",
            "target_language": "hi",
        },
    )

    assert response.status_code in (
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


def test_invalid_language(client):
    response = client.post(
        "/api/translation/translate",
        json={
            "text": "Hello",
            "source_language": "abc",
            "target_language": "xyz",
        },
    )

    assert response.status_code in (
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    )