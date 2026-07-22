import json

from ai.model_loader import get_gemini_client
from ai.prompt_templates import KEYWORD_PROMPT


class KeywordExtractor:

    def __init__(self):
        self.client = get_gemini_client()

    async def extract(
        self,
        text: str,
    ):

        prompt = KEYWORD_PROMPT.format(
            text=text,
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()

    async def extract_json(
        self,
        text: str,
    ):

        prompt = f"""
You are an AI keyword extraction engine.

Extract important information.

Return ONLY valid JSON.

JSON Format:

{{
    "keywords": [],
    "topics": [],
    "technologies": [],
    "entities": []
}}

Text:

{text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return json.loads(response.text)


keyword_extractor = KeywordExtractor()