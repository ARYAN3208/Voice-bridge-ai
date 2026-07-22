import json

from ai.model_loader import get_gemini_client
from ai.prompt_templates import ACTION_ITEMS_PROMPT


class ActionItemExtractor:

    def __init__(self):
        self.client = get_gemini_client()

    async def extract(
        self,
        text: str,
    ):

        prompt = ACTION_ITEMS_PROMPT.format(
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
You are an AI meeting assistant.

Extract all action items from the conversation.

Return ONLY valid JSON.

JSON Format:

{{
    "tasks":[
        {{
            "task":"",
            "owner":"",
            "priority":"",
            "deadline":"",
            "status":"Pending"
        }}
    ]
}}

Conversation:

{text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return json.loads(response.text)


action_item_extractor = ActionItemExtractor()