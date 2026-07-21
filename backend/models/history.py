from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class History(Base):
    __tablename__ = "history"

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
        nullable=False,
        unique=True
    )

    activity_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="histories"
    )

    translation = relationship(
        "Translation",
        back_populates="history"
    )

    summary = relationship(
        "Summary",
        back_populates="history",
        uselist=False,
        cascade="all, delete-orphan"
    )