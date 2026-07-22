from .audio_exporter import AudioExporter
from .csv_exporter import CSVExporter
from .json_exporter import JSONExporter
from .pdf_exporter import PDFExporter
from .text_exporter import TextExporter
from .translation_exporter import TranslationExporter


class ExportManager:
    def __init__(self):
        self.text = TextExporter()
        self.translation = TranslationExporter()
        self.audio = AudioExporter()
        self.pdf = PDFExporter()
        self.json = JSONExporter()
        self.csv = CSVExporter()


export_manager = ExportManager()