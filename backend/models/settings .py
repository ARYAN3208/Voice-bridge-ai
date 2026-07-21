from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Settings(Base):
    __tablename__ = "settings"

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

    theme: Mapped[str] = mapped_column(
        String(20),
        default="light"
    )

    language: Mapped[str] = mapped_column(
        String(50),
        default="English"
    )

    notifications_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    email_notifications: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    voice_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    auto_detect_language: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    save_history: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="settings"
    )