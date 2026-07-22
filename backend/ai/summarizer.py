import json

from ai.model_loader import get_gemini_client
from ai.prompt_templates import SUMMARY_PROMPT


class Summarizer:

    def __init__(self):
        self.client = get_gemini_client()

    async def summarize(
        self,
        text: str,
    ) -> str:

        prompt = SUMMARY_PROMPT.format(
            text=text,
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()

    async def summarize_json(
        self,
        text: str,
    ):

        prompt = f"""
You are an AI meeting assistant.

Summarize the conversation.

Return ONLY valid JSON.

JSON Format:

{{
    "title":"",
    "summary":"",
    "key_points":[]
}}

Conversation:

{text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return json.loads(response.text)


summarizer = Summarizer()