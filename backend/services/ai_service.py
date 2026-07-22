from ai.action_items import action_item_extractor
from ai.diarization import diarization_engine
from ai.keyword_extractor import keyword_extractor
from ai.sentiment import sentiment_analyzer
from ai.summarizer import summarizer
from ai.translator import translator
from ai.tts_engine import tts_engine
from ai.whisper_engine import whisper_engine


class AIService:

    async def transcribe_audio(
        self,
        audio_path: str,
        language: str | None = None,
    ):
        return await whisper_engine.transcribe(
            audio_path=audio_path,
            language=language,
        )

    async def translate_text(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ):
        return await translator.translate(
            text=text,
            source_language=source_language,
            target_language=target_language,
        )

    async def summarize_text(
        self,
        text: str,
    ):
        return await summarizer.summarize_json(text)

    async def analyze_sentiment(
        self,
        text: str,
    ):
        return await sentiment_analyzer.analyze_json(text)

    async def extract_keywords(
        self,
        text: str,
    ):
        return await keyword_extractor.extract_json(text)

    async def extract_action_items(
        self,
        text: str,
    ):
        return await action_item_extractor.extract_json(text)

    async def diarize_audio(
        self,
        audio_path: str,
        language: str | None = None,
    ):
        return await diarization_engine.diarize(
            audio_path=audio_path,
            language=language,
        )

    async def generate_speech(
        self,
        text: str,
        output_path: str,
        voice: str = "aura-2-thalia-en",
    ):
        return await tts_engine.generate_speech(
            text=text,
            output_path=output_path,
            voice=voice,
        )

    async def process_pipeline(
        self,
        audio_path: str,
        source_language: str,
        target_language: str,
        output_audio_path: str,
    ):

        transcription = await self.transcribe_audio(
            audio_path=audio_path,
            language=source_language,
        )

        transcript = transcription["transcript"]

        translation = await self.translate_text(
            text=transcript,
            source_language=source_language,
            target_language=target_language,
        )

        summary = await self.summarize_text(
            transcript,
        )

        sentiment = await self.analyze_sentiment(
            transcript,
        )

        keywords = await self.extract_keywords(
            transcript,
        )

        action_items = await self.extract_action_items(
            transcript,
        )

        diarization = await self.diarize_audio(
            audio_path=audio_path,
            language=source_language,
        )

        speech = await self.generate_speech(
            text=translation,
            output_path=output_audio_path,
        )

        return {
            "transcription": transcription,
            "translation": translation,
            "summary": summary,
            "sentiment": sentiment,
            "keywords": keywords,
            "action_items": action_items,
            "diarization": diarization,
            "speech": speech,
        }


ai_service = AIService()