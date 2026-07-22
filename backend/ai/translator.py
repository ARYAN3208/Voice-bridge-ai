import json

from ai.model_loader import get_gemini_client
from ai.prompt_templates import (
    TRANSLATION_PROMPT,
    GRAMMAR_PROMPT,
)

class Translator:

    def __init__(self):
        self.client = get_gemini_client()

    async def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ):

        prompt = TRANSLATION_PROMPT.format(
            source_language=source_language,
            target_language=target_language,
            text=text,
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()

    async def grammar_correct(
        self,
        text: str,
    ):

        prompt = GRAMMAR_PROMPT.format(
            text=text,
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()

    async def translate_json(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ):

        prompt = f"""
Return ONLY valid JSON.

Translate the following text.

Source Language:
{source_language}

Target Language:
{target_language}

Text:
{text}

JSON Format:

{{
    "translation": "...",
    "source_language": "{source_language}",
    "target_language": "{target_language}"
}}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return json.loads(response.text)


translator = Translator()