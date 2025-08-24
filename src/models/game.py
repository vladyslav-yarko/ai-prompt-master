from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base, BaseFields


class Game(Base, BaseFields):
    __tablename__ = "games"
    
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    shortDescription: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    mode: Mapped[str] = mapped_column(String(100), nullable=False)
    
    achievements: Mapped[list["Achievement"]] = relationship("Achievement", back_populates="game", uselist=True)
