from typing import Optional

from src.utils.repository import SQLAlchemyRepository
from src.models import UserStats


class UserStatsRepository(SQLAlchemyRepository):
    model = UserStats

    async def get_one_by_user_id(self, user_id: int) -> Optional[UserStats]:
        data = await self.get_one(userId=user_id)
        return data
    
    async def update_one_by_user_id(self, user_id: int, **kwargs) -> Optional[UserStats]:
        data = await self.update_one(kwargs, userId=user_id)
        return data
