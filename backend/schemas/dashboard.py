from datetime import datetime

from pydantic import BaseModel


class DashboardResponse(BaseModel):
    user_id: int
    total_translations: int
    total_voice_notes: int
    total_languages: int
    last_active: datetime


class DashboardStatsResponse(BaseModel):
    total_translations: int
    total_voice_notes: int
    total_documents: int
    total_audio_duration: float
    average_translation_time: float


class RecentActivityResponse(BaseModel):
    activities: list[str]


class OverviewResponse(BaseModel):
    active_users: int
    translations_today: int
    voice_notes_today: int


class AIStatusResponse(BaseModel):
    speech_to_text: str
    translation: str
    text_to_speech: str
    llm: str


class QuickActionResponse(BaseModel):
    actions: list[str]


class NotificationResponse(BaseModel):
    notifications: list[str]


class SystemHealthResponse(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    uptime: str