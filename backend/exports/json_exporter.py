import json
from pathlib import Path
from uuid import uuid4

from backend.utils.constants import EXPORT_DIR


class JSONExporter:
    def __init__(self):
        self.export_directory = Path(EXPORT_DIR) / "json"
        self.export_directory.mkdir(parents=True, exist_ok=True)

    def export(
        self,
        data: dict | list,
        filename: str | None = None,
    ) -> str:

        if filename is None:
            filename = f"{uuid4().hex}.json"

        if not filename.endswith(".json"):
            filename += ".json"

        output_path = self.export_directory / filename

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

        return str(output_path)