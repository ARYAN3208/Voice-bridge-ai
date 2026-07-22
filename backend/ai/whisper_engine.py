from pathlib import Path
from deepgram import (
    FileSource,
    PrerecordedOptions,
)

from ai.model_loader import get_deepgram_client


class WhisperEngine:

    def __init__(self):
        self.client = get_deepgram_client()

    async def transcribe(
        self,
        audio_path: str,
        language: str | None = None,
        diarize: bool = True,
        punctuate: bool = True,
        smart_format: bool = True,
    ):

        audio_file = Path(audio_path)

        with open(audio_file, "rb") as file:
            payload: FileSource = {
                "buffer": file.read(),
            }

        options = PrerecordedOptions(
            model="nova-3",
            language=language,
            smart_format=smart_format,
            punctuate=punctuate,
            diarize=diarize,
            detect_language=language is None,
        )

        response = self.client.listen.rest.v("1").transcribe_file(
            payload,
            options,
        )

        result = response.results.channels[0].alternatives[0]

        return {
            "transcript": result.transcript,
            "confidence": result.confidence,
            "language": response.results.channels[0].detected_language,
            "words": result.words,
        }


whisper_engine = WhisperEngine()