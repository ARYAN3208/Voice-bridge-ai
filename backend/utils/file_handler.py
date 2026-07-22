import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from backend.utils.constants import (
    AUDIO_UPLOAD_DIR,
    TEMP_UPLOAD_DIR,
    EXPORT_AUDIO_DIR,
    EXPORT_TEXT_DIR,
    EXPORT_TRANSLATION_DIR,
)


for directory in [
    AUDIO_UPLOAD_DIR,
    TEMP_UPLOAD_DIR,
    EXPORT_AUDIO_DIR,
    EXPORT_TEXT_DIR,
    EXPORT_TRANSLATION_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)


class FileHandler:

    @staticmethod
    async def save_audio(file: UploadFile) -> Path:
        extension = Path(file.filename).suffix.lower()
        filename = f"{uuid4().hex}{extension}"
        destination = AUDIO_UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        await file.close()

        return destination

    @staticmethod
    async def save_temp(file: UploadFile) -> Path:
        extension = Path(file.filename).suffix.lower()
        filename = f"{uuid4().hex}{extension}"
        destination = TEMP_UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        await file.close()

        return destination

    @staticmethod
    def save_text(filename: str, content: str) -> Path:
        path = EXPORT_TEXT_DIR / filename

        with path.open("w", encoding="utf-8") as f:
            f.write(content)

        return path

    @staticmethod
    def save_translation(filename: str, content: str) -> Path:
        path = EXPORT_TRANSLATION_DIR / filename

        with path.open("w", encoding="utf-8") as f:
            f.write(content)

        return path

    @staticmethod
    def delete_file(file_path: str | Path) -> bool:
        path = Path(file_path)

        if path.exists():
            path.unlink()
            return True

        return False

    @staticmethod
    def file_exists(file_path: str | Path) -> bool:
        return Path(file_path).exists()

    @staticmethod
    def get_file_size(file_path: str | Path) -> int:
        return Path(file_path).stat().st_size

    @staticmethod
    def get_extension(file_path: str | Path) -> str:
        return Path(file_path).suffix.lower()

    @staticmethod
    def create_directory(directory: str | Path) -> Path:
        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        return path