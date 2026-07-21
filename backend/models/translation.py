from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Translation(Base):
    __tablename__ = "translations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    source_language: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    target_language: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    input_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    translated_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    translation_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    confidence_score: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    processing_time: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="translations"
    )

    history = relationship(
        "History",
        back_populates="translation",
        uselist=False,
        cascade="all, delete-orphan"
    )