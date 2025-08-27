from typing import Optional

from src.utils.repository import SQLAlchemyRepository
from src.models import Achievement


class AchievementRepository(SQLAlchemyRepository):
    model = Achievement

    async def get_by_condition_key(self, condition_key: str) -> Optional[list[Achievement]]:
        data = await self.get(conditionKey=condition_key)
        return data[0]
