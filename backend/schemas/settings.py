from pydantic import BaseModel


class SettingsResponse(BaseModel):
    theme: str
    language: str
    notifications_enabled: bool
    email_notifications: bool
    voice_enabled: bool
    auto_detect_language: bool
    save_history: bool


class UpdateSettingsRequest(BaseModel):
    theme: str
    language: str
    notifications_enabled: bool
    email_notifications: bool
    voice_enabled: bool
    auto_detect_language: bool
    save_history: bool


class UpdateSettingsResponse(BaseModel):
    message: str


class ThemeRequest(BaseModel):
    theme: str


class LanguageRequest(BaseModel):
    language: str


class NotificationRequest(BaseModel):
    notifications_enabled: bool
    email_notifications: bool


class PrivacyRequest(BaseModel):
    save_history: bool


class VoiceSettingsRequest(BaseModel):
    voice_enabled: bool


class TranslationSettingsRequest(BaseModel):
    auto_detect_language: bool


class ResetSettingsResponse(BaseModel):
    message: str