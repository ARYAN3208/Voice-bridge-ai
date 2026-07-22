import csv
from pathlib import Path
from uuid import uuid4

from backend.utils.constants import EXPORT_DIR


class CSVExporter:
    def __init__(self):
        self.export_directory = Path(EXPORT_DIR) / "csv"
        self.export_directory.mkdir(parents=True, exist_ok=True)

    def export(
        self,
        data: list[dict],
        filename: str | None = None,
    ) -> str:

        if not data:
            raise ValueError("No data available for export.")

        if filename is None:
            filename = f"{uuid4().hex}.csv"

        if not filename.endswith(".csv"):
            filename += ".csv"

        output_path = self.export_directory / filename

        with open(
            output_path,
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=data[0].keys(),
            )

            writer.writeheader()
            writer.writerows(data)

        return str(output_path)