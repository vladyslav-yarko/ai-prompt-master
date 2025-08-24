from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base, BaseFields


class User(Base, BaseFields):
    __tablename__ = "users"
    
    # Telegram uses big integers for their ids
    telegramId: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    chatId: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    
    stats: Mapped["UserStats"] = relationship("UserStats", back_populates="user", uselist=False)
    achievements: Mapped[list["Achievement"]] = relationship("Achievement", back_populates="users", secondary="user_achievements")
