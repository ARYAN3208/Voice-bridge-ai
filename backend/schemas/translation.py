from pydantic import BaseModel


class TextTranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str


class VoiceTranslationRequest(BaseModel):
    source_language: str
    target_language: str


class DocumentTranslationRequest(BaseModel):
    source_language: str
    target_language: str


class TranslationResponse(BaseModel):
    translated_text: str
    source_language: str
    target_language: str
    confidence_score: float


class SupportedLanguagesResponse(BaseModel):
    languages: list[str]


class LanguageDetectionResponse(BaseModel):
    language: str
    confidence: float


class SummaryRequest(BaseModel):
    text: str


class SummaryResponse(BaseModel):
    summary: str


class KeywordResponse(BaseModel):
    keywords: list[str]


class ActionItemResponse(BaseModel):
    action_items: list[str]


class TitleResponse(BaseModel):
    title: str


class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float


class RAGSearchRequest(BaseModel):
    query: str


class RAGSearchResponse(BaseModel):
    results: list[str]