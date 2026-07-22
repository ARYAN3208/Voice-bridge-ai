from pathlib import Path
from shutil import copy2
from uuid import uuid4

from backend.utils.constants import EXPORT_AUDIO_DIR


class AudioExporter:
    def __init__(self):
        Path(EXPORT_AUDIO_DIR).mkdir(parents=True, exist_ok=True)

    def export(
        self,
        source_path: str,
        filename: str | None = None,
    ) -> str:

        source = Path(source_path)

        if not source.exists():
            raise FileNotFoundError(f"{source_path} not found.")

        extension = source.suffix

        if filename is None:
            filename = f"{uuid4().hex}{extension}"
        elif not filename.endswith(extension):
            filename += extension

        destination = Path(EXPORT_AUDIO_DIR) / filename

        copy2(source, destination)

        return str(destination)