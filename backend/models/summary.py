from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Summary(Base):
    __tablename__ = "summaries"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    history_id: Mapped[int] = mapped_column(
        ForeignKey("history.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    summary: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    keywords: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    action_items: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    sentiment: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    history = relationship(
        "History",
        back_populates="summary"
    )