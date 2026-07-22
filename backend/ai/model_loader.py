from functools import lru_cache

from deepgram import DeepgramClient
from google import genai

from config import settings


class AIModelLoader:
    def __init__(self):
        self._deepgram = None
        self._gemini = None

    @property
    def deepgram(self):
        if self._deepgram is None:
            self._deepgram = DeepgramClient(settings.DEEPGRAM_API_KEY)
        return self._deepgram

    @property
    def gemini(self):
        if self._gemini is None:
            self._gemini = genai.Client(
                api_key=settings.GEMINI_API_KEY
            )
        return self._gemini


@lru_cache
def get_model_loader():
    return AIModelLoader()


@lru_cache
def get_deepgram_client():
    return get_model_loader().deepgram


@lru_cache
def get_gemini_client():
    return get_model_loader().gemini