from pathlib import Path
from uuid import uuid4

from backend.utils.constants import EXPORT_TRANSLATION_DIR


class TranslationExporter:
    def __init__(self):
        Path(EXPORT_TRANSLATION_DIR).mkdir(parents=True, exist_ok=True)

    def export(
        self,
        text: str,
        source_language: str,
        target_language: str,
        filename: str | None = None,
    ) -> str:

        if filename is None:
            filename = (
                f"{source_language}_{target_language}_{uuid4().hex}.txt"
            )

        output_path = Path(EXPORT_TRANSLATION_DIR) / filename

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)

        return str(output_path)