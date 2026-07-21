from pydantic import BaseModel, EmailStr


class ProfileResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    profile_picture: str | None
    is_active: bool
    is_verified: bool


class UpdateProfileRequest(BaseModel):
    full_name: str
    email: EmailStr


class UpdateProfileResponse(BaseModel):
    message: str


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str


class ChangePasswordResponse(BaseModel):
    message: str


class AvatarUploadResponse(BaseModel):
    profile_picture: str
    message: str


class AvatarDeleteResponse(BaseModel):
    message: str


class ProfileActivityResponse(BaseModel):
    activities: list[str]


class ProfileStatisticsResponse(BaseModel):
    total_translations: int
    total_voice_notes: int
    total_documents: int
    languages_used: int


class ProfilePreferencesResponse(BaseModel):
    theme: str
    language: str
    notifications_enabled: bool
    voice_enabled: bool
