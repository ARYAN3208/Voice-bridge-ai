from pathlib import Path

from deepgram import SpeakOptions

from ai.model_loader import get_deepgram_client


class TTSEngine:

    def __init__(self):
        self.client = get_deepgram_client()

    async def generate_speech(
        self,
        text: str,
        output_path: str,
        voice: str = "aura-2-thalia-en",
    ):

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        options = SpeakOptions(
            model=voice,
        )

        response = self.client.speak.rest.v("1").save(
            output_path,
            {
                "text": text,
            },
            options,
        )

        return {
            "success": True,
            "path": output_path,
            "voice": voice,
            "response": response,
        }


tts_engine = TTSEngine()