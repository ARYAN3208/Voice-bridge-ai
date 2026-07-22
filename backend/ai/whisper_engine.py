from pathlib import Path

from faster_whisper import WhisperModel

from config import settings
from backend.ai.model_loader import load_whisper_model


class WhisperEngine:
    def __init__(self):
        self.model = load_whisper_model()

    def transcribe(
        self,
        audio_path: str,
        language: str | None = None,
    ) -> dict:

        path = Path(audio_path)

        if not path.exists():
            raise FileNotFoundError(f"{audio_path} not found.")

        segments, info = self.model.transcribe(
            str(path),
            language=language,
            beam_size=settings.WHISPER_BEAM_SIZE,
        )

        transcript = ""

        for segment in segments:
            transcript += segment.text.strip() + " "

        return {
            "text": transcript.strip(),
            "language": info.language,
            "language_probability": info.language_probability,
            "duration": info.duration,
        }


whisper_engine = WhisperEngine()