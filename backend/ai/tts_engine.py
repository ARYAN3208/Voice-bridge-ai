from pathlib import Path
from uuid import uuid4

from gtts import gTTS

from backend.utils.constants import EXPORT_AUDIO_DIR


class TTSEngine:
    def __init__(self):
        Path(EXPORT_AUDIO_DIR).mkdir(parents=True, exist_ok=True)

    def generate_speech(
        self,
        text: str,
        language: str,
    ) -> dict:

        if not text.strip():
            raise ValueError("Text cannot be empty.")

        filename = f"{uuid4().hex}.mp3"
        output_path = Path(EXPORT_AUDIO_DIR) / filename

        speech = gTTS(
            text=text,
            lang=language,
            slow=False,
        )

        speech.save(str(output_path))

        return {
            "language": language,
            "audio_path": str(output_path),
            "filename": filename,
        }


tts_engine = TTSEngine()