from google import genai

from config import settings


class Translator:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> dict:

        if not text.strip():
            raise ValueError("Text cannot be empty.")

        prompt = f"""
You are a professional translator.

Translate the following text.

Rules:
- Preserve the original meaning.
- Do not add or remove information.
- Keep names unchanged.
- Return only the translated text.

Source Language:
{source_language}

Target Language:
{target_language}

Text:
{text}
"""

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
        )

        translated_text = response.text.strip()

        return {
            "source_language": source_language,
            "target_language": target_language,
            "original_text": text,
            "translated_text": translated_text,
        }


translator = Translator()