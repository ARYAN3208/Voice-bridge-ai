import re
from pathlib import Path
from email_validator import validate_email, EmailNotValidError

from backend.utils.constants import (
    SUPPORTED_AUDIO_FORMATS,
    MAX_AUDIO_SIZE,
)


def validate_email_address(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*()_\-+=<>?/{}[\]|\\:;,.~`]", password):
        return False, "Password must contain at least one special character."

    return True, "Valid password."


def validate_username(username: str) -> tuple[bool, str]:
    if len(username) < 3:
        return False, "Username must be at least 3 characters long."

    if len(username) > 30:
        return False, "Username cannot exceed 30 characters."

    if not re.fullmatch(r"[A-Za-z0-9_.]+", username):
        return (
            False,
            "Username can contain only letters, numbers, underscores, and periods.",
        )

    return True, "Valid username."


def validate_audio_file(filename: str, file_size: int) -> tuple[bool, str]:
    extension = Path(filename).suffix.lower()

    if extension not in SUPPORTED_AUDIO_FORMATS:
        return False, "Unsupported audio format."

    if file_size > MAX_AUDIO_SIZE:
        return False, "File size exceeds the allowed limit."

    return True, "Valid audio file."


def validate_language(language_code: str, supported_languages: dict) -> bool:
    return language_code in supported_languages or language_code == "auto"


def validate_text(text: str, max_length: int = 5000) -> tuple[bool, str]:
    if not text.strip():
        return False, "Text cannot be empty."

    if len(text) > max_length:
        return False, f"Text cannot exceed {max_length} characters."

    return True, "Valid text."