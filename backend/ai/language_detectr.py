from langdetect import DetectorFactory, LangDetectException, detect, detect_langs

DetectorFactory.seed = 42


class LanguageDetector:
    def detect_language(self, text: str) -> dict:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        try:
            language = detect(text)
            probabilities = detect_langs(text)

            confidence = 0.0

            if probabilities:
                confidence = probabilities[0].prob

            return {
                "language": language,
                "confidence": round(confidence, 4),
            }

        except LangDetectException:
            return {
                "language": "unknown",
                "confidence": 0.0,
            }

    def is_supported(self, language: str, supported_languages: list[str]) -> bool:
        return language.lower() in supported_languages


language_detector = LanguageDetector()