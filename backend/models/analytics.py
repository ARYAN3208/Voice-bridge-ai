from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Analytics(Base):
    __tablename__ = "analytics"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )

    total_translations: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    total_voice_notes: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    total_audio_duration: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    total_documents_translated: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    total_characters_translated: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    languages_used: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    average_translation_time: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    last_active: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="analytics"
    )