from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base


class UserAchievement(Base):
    __tablename__ = "user_achievements"

    userId: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    achievementId: Mapped[int] = mapped_column(ForeignKey("achievements.id"), primary_key=True)
