TRANSLATION_PROMPT = """
You are an expert multilingual translator.

Translate the given text.

Rules:

- Preserve meaning.
- Preserve names.
- Preserve numbers.
- Preserve punctuation.
- Do not explain.
- Return ONLY the translated text.

Source Language:
{source_language}

Target Language:
{target_language}

Text:
{text}
"""


GRAMMAR_PROMPT = """
You are an English grammar expert.

Correct grammar without changing the meaning.

Rules:

- Preserve tone.
- Preserve formatting.
- Preserve names.
- Do not explain.
- Return ONLY corrected text.

Text:

{text}
"""


SUMMARY_PROMPT = """
You are an AI meeting assistant.

Summarize the following conversation.

Rules:

- Keep it concise.
- Use bullet points.
- Include important decisions.
- Include important discussions.
- Ignore greetings.

Conversation:

{text}
"""


ACTION_ITEMS_PROMPT = """
You are an AI meeting assistant.

Extract action items.

Return ONLY JSON.

JSON Format:

[
    {
        "task":"",
        "owner":"",
        "deadline":""
    }
]

Conversation:

{text}
"""


SENTIMENT_PROMPT = """
Analyze the sentiment.

Return ONLY JSON.

JSON Format:

{
    "sentiment":"",
    "confidence":""
}

Text:

{text}
"""


KEYWORD_PROMPT = """
Extract important keywords.

Rules:

- Ignore stop words.
- Return ONLY JSON.

JSON Format:

{
    "keywords":[]
}

Text:

{text}
"""


LANGUAGE_DETECTION_PROMPT = """
Identify the language.

Return ONLY JSON.

JSON Format:

{
    "language":"",
    "code":""
}

Text:

{text}
"""


JSON_TRANSLATION_PROMPT = """
Translate the text.

Return ONLY JSON.

JSON Format:

{
    "translation":"",
    "source_language":"",
    "target_language":""
}

Source Language:
{source_language}

Target Language:
{target_language}

Text:

{text}
"""