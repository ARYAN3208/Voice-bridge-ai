from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class VoiceNote(Base):
    __tablename__ = "voice_notes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    translation_id: Mapped[int] = mapped_column(
        ForeignKey("translations.id", ondelete="CASCADE"),
        nullable=False
    )

    original_audio_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    translated_audio_path: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    transcript: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    duration: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    file_size: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    audio_format: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="voice_notes"
    )

    translation = relationship(
        "Translation"
    )