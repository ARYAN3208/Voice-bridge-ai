from collections import defaultdict

from ai.whisper_engine import whisper_engine


class DiarizationEngine:

    async def diarize(
        self,
        audio_path: str,
        language: str = None,
    ):

        result = await whisper_engine.transcribe(
            audio_path=audio_path,
            language=language,
        )

        words = result.get("words", [])

        speakers = defaultdict(list)

        for word in words:
            speaker = word.get("speaker", "Unknown")
            text = word.get("punctuated_word") or word.get("word", "")
            speakers[speaker].append(text)

        conversation = []

        for speaker in sorted(speakers.keys()):
            conversation.append(
                {
                    "speaker": f"Speaker {speaker}",
                    "text": " ".join(speakers[speaker]).strip(),
                }
            )

        return {
            "language": result.get("language"),
            "confidence": result.get("confidence"),
            "speakers": len(speakers),
            "conversation": conversation,
        }

    async def speaker_transcript(
        self,
        audio_path: str,
        language: str = None,
    ):

        result = await self.diarize(
            audio_path=audio_path,
            language=language,
        )

        lines = []

        for item in result["conversation"]:
            lines.append(
                f'{item["speaker"]}: {item["text"]}'
            )

        return "\n".join(lines)


diarization_engine = DiarizationEngine()