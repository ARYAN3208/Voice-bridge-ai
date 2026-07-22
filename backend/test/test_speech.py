from pathlib import Path

from fastapi import status


def test_speech_to_text(client):
    sample_file = Path("backend/test/sample.wav")

    if not sample_file.exists():
        return

    with open(sample_file, "rb") as audio:
        response = client.post(
            "/api/speech/transcribe",
            files={
                "file": (
                    sample_file.name,
                    audio,
                    "audio/wav",
                )
            },
        )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_translate_audio(client):
    sample_file = Path("backend/test/sample.wav")

    if not sample_file.exists():
        return

    with open(sample_file, "rb") as audio:
        response = client.post(
            "/api/speech/translate",
            files={
                "file": (
                    sample_file.name,
                    audio,
                    "audio/wav",
                )
            },
            data={
                "target_language": "hi",
            },
        )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
    )


def test_invalid_audio(client):
    response = client.post(
        "/api/speech/transcribe",
        files={
            "file": (
                "sample.txt",
                b"Invalid Audio",
                "text/plain",
            )
        },
    )

    assert response.status_code in (
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


def test_missing_audio(client):
    response = client.post(
        "/api/speech/transcribe"
    )

    assert response.status_code in (
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    )