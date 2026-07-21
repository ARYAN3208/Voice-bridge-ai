from pydantic import BaseModel


class VoiceUploadRequest(BaseModel):
    filename: str


class VoiceUploadResponse(BaseModel):
    voice_note_id: int
    message: str


class VoiceRecordResponse(BaseModel):
    voice_note_id: int
    duration: float


class SpeechToTextResponse(BaseModel):
    transcript: str
    confidence: float


class TextToSpeechRequest(BaseModel):
    text: str
    language: str
    voice: str


class TextToSpeechResponse(BaseModel):
    audio_path: str


class ConversationRequest(BaseModel):
    source_language: str
    target_language: str


class ConversationResponse(BaseModel):
    transcript: str
    translated_text: str
    audio_path: str


class VoiceResponse(BaseModel):
    id: int
    transcript: str
    duration: float
    audio_path: str


class VoiceMetadataResponse(BaseModel):
    duration: float
    sample_rate: int
    channels: int
    audio_format: str


class VoiceDeleteResponse(BaseModel):
    message: str