from pathlib import Path
from uuid import uuid4

from backend.utils.constants import EXPORT_TEXT_DIR


class TextExporter:
    def __init__(self):
        Path(EXPORT_TEXT_DIR).mkdir(parents=True, exist_ok=True)

    def export(
        self,
        text: str,
        filename: str | None = None,
    ) -> str:

        if filename is None:
            filename = f"{uuid4().hex}.txt"

        if not filename.endswith(".txt"):
            filename += ".txt"

        output_path = Path(EXPORT_TEXT_DIR) / filename

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)

        return str(output_path)