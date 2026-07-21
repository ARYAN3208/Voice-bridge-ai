from datetime import datetime

from pydantic import BaseModel


class HistoryResponse(BaseModel):
    id: int
    activity_type: str
    created_at: datetime


class HistoryDetailResponse(BaseModel):
    id: int
    user_id: int
    translation_id: int
    activity_type: str
    created_at: datetime


class HistorySearchRequest(BaseModel):
    query: str


class HistorySearchResponse(BaseModel):
    results: list[HistoryDetailResponse]


class HistorySummaryResponse(BaseModel):
    history_id: int
    summary: str


class HistoryKeywordsResponse(BaseModel):
    history_id: int
    keywords: list[str]


class HistoryTranslationResponse(BaseModel):
    history_id: int
    translated_text: str


class HistoryAudioResponse(BaseModel):
    history_id: int
    audio_url: str


class DeleteHistoryResponse(BaseModel):
    message: str


class DeleteAllHistoryResponse(BaseModel):
    message: str