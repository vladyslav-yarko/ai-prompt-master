from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base, BaseFields


class UserStats(Base, BaseFields):
    __tablename__ = "user_stats"
    
    userId: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    
    levelId: Mapped[int] = mapped_column(ForeignKey("levels.id"), nullable=False)
    totalScore: Mapped[int] = mapped_column(default=0)
    totalGamesPlayed: Mapped[int] = mapped_column(default=0)
    learnMode: Mapped[int] = mapped_column(default=0)
    creativeMode: Mapped[int] = mapped_column(default=0)
    codeMode: Mapped[int] = mapped_column(default=0)
    antiPromptMode: Mapped[int] = mapped_column(default=0)
    puzzleMode: Mapped[int] = mapped_column(default=0)
    
    level: Mapped["Level"] = relationship("Level", back_populates="users", uselist=False)
    user: Mapped["User"] = relationship("User", back_populates="stats", uselist=False)
