from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_DIR = BASE_DIR / "backend" / "uploads"
EXPORT_DIR = BASE_DIR / "backend" / "exports"

AUDIO_UPLOAD_DIR = UPLOAD_DIR / "audio"
TEMP_UPLOAD_DIR = UPLOAD_DIR / "temp"

EXPORT_AUDIO_DIR = EXPORT_DIR / "audio"
EXPORT_TEXT_DIR = EXPORT_DIR / "transcripts"
EXPORT_TRANSLATION_DIR = EXPORT_DIR / "translations"

SUPPORTED_AUDIO_FORMATS = {
    ".wav",
    ".mp3",
    ".m4a",
    ".aac",
    ".ogg",
    ".flac"
}

MAX_AUDIO_SIZE = 25 * 1024 * 1024

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "gu": "Gujarati",
    "bn": "Bengali",
    "pa": "Punjabi",
    "ur": "Urdu"
}

DEFAULT_SOURCE_LANGUAGE = "auto"
DEFAULT_TARGET_LANGUAGE = "en"

DEFAULT_TTS_VOICE = "default"

JWT_ALGORITHM = "HS256"

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

ALLOWED_EXPORT_FORMATS = {
    "txt",
    "pdf",
    "docx"
}