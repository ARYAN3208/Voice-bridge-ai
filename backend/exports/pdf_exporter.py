from pathlib import Path
from uuid import uuid4

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

from backend.utils.constants import EXPORT_DIR


class PDFExporter:
    def __init__(self):
        self.export_directory = Path(EXPORT_DIR) / "pdf"
        self.export_directory.mkdir(parents=True, exist_ok=True)

    def export(
        self,
        title: str,
        content: str,
        filename: str | None = None,
    ) -> str:

        if filename is None:
            filename = f"{uuid4().hex}.pdf"

        if not filename.endswith(".pdf"):
            filename += ".pdf"

        output_path = self.export_directory / filename

        document = SimpleDocTemplate(str(output_path))

        styles = getSampleStyleSheet()

        elements = [
            Paragraph(f"<b>{title}</b>", styles["Heading1"]),
            Paragraph(content.replace("\n", "<br/>"), styles["BodyText"]),
        ]

        document.build(elements)

        return str(output_path)