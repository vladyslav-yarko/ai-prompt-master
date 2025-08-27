from typing import Optional

from src.utils.repository import SQLAlchemyRepository
from src.models import Game


class GameRepository(SQLAlchemyRepository):
    model = Game
    
    async def get_one_by_title(self, title: str) -> Optional[Game]:
        data = await self.get_one(title=title)
        return data
