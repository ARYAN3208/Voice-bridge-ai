import json

from ai.model_loader import get_gemini_client
from ai.prompt_templates import SENTIMENT_PROMPT


class SentimentAnalyzer:

    def __init__(self):
        self.client = get_gemini_client()

    async def analyze(
        self,
        text: str,
    ) -> str:

        prompt = SENTIMENT_PROMPT.format(
            text=text,
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()

    async def analyze_json(
        self,
        text: str,
    ):

        prompt = f"""
Analyze the sentiment.

Return ONLY valid JSON.

JSON Format:

{{
    "sentiment":"",
    "confidence":0.0,
    "emotion":"",
    "reason":""
}}

Text:

{text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return json.loads(response.text)


sentiment_analyzer = SentimentAnalyzer()