from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base, BaseFields


class Level(Base, BaseFields):
    __tablename__ = "levels"
    
    # At first i wanted to use enum but afterward changed
    # title: Mapped[LevelEnum] = mapped_column(SQLEnum(LevelEnum, name='level_title'), default=LevelEnum.beginner)
    title: Mapped[str] = mapped_column(String(50), default="beginner")
    requiredScore: Mapped[int] = mapped_column(nullable=False)
    emoji: Mapped[str] = mapped_column(String(50), nullable=False)
    
    # Users with defined level
    users: Mapped[list["UserStats"]] = relationship("UserStats", back_populates="level", uselist=True)
