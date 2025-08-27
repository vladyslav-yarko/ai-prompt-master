from typing import Optional

from src.utils.repository import SQLAlchemyRepository
from src.models import Level


class LevelRepository(SQLAlchemyRepository):
    model = Level
    
    async def get_one_by_title(self, title: str) -> Optional[Level]:
        data = await self.get_one(title=title)
        return data
