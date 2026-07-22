from ai.whisper_engine import whisper_engine
from ai.translator import translator
from ai.tts_engine import tts_engine
from ai.summarizer import summarizer
from ai.sentiment import sentiment_analyzer
from ai.keyword_extractor import keyword_extractor
from ai.action_items import action_item_extractor


class RealtimePipeline:

    async def process(
        self,
        audio_path: str,
        source_language: str,
        target_language: str,
        output_audio: str,
    ):

        transcription = await whisper_engine.transcribe(
            audio_path=audio_path,
            language=source_language,
        )

        transcript = transcription["transcript"]

        translation = await translator.translate(
            text=transcript,
            source_language=source_language,
            target_language=target_language,
        )

        summary = await summarizer.summarize(
            transcript,
        )

        sentiment = await sentiment_analyzer.analyze_json(
            transcript,
        )

        keywords = await keyword_extractor.extract_json(
            transcript,
        )

        action_items = await action_item_extractor.extract_json(
            transcript,
        )

        await tts_engine.generate_speech(
            text=translation,
            output_path=output_audio,
        )

        return {
            "transcript": transcript,
            "translation": translation,
            "summary": summary,
            "sentiment": sentiment,
            "keywords": keywords,
            "action_items": action_items,
            "audio": output_audio,
        }


realtime_pipeline = RealtimePipeline()