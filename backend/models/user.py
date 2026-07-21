from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    full_name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password: Mapped[str] = mapped_column(String(255), nullable=False)

    profile_picture: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    translations = relationship(
        "Translation",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    voice_notes = relationship(
        "VoiceNote",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    histories = relationship(
        "History",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    analytics = relationship(
        "Analytics",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    settings = relationship(
        "Settings",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )