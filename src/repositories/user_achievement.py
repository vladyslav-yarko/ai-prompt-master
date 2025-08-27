from typing import Optional

from src.utils.repository import SQLAlchemyRepository
from src.models import UserAchievement


class UserAchievementRepository(SQLAlchemyRepository):
    model = UserAchievement

    async def get_by_user_id(self, user_id: int) -> Optional[list[UserAchievement]]:
        data = await self.get(userId=user_id)
        return data[0]
