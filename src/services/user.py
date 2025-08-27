from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction
from src.models import Base
from src.enums.level import LevelEnum


class UserService(Service):
    def __init__(
        self,
        session: AsyncSession,
        user_repo: Repository,
        user_stats_repo: Repository,
        user_achievement_repo: Repository,
        level_repo: Repository,
        achievement_repo: Repository
    ):
        super().__init__(session)
        self.repo = user_repo
        self.user_repo = user_repo
        self.user_stats_repo = user_stats_repo
        self.user_achievement_repo = user_achievement_repo
        self.level_repo = level_repo
        self.achievement_repo = achievement_repo
        
    @transaction
    async def create_one(self, data: dict) -> Optional[Base]:
        user = await self.get_user_one(telegram_id=data.get("telegramId"))
        if user:
            return None
        user = await super().create_one(data)
        level = await self.level_repo(self.session).get_one_by_title(LevelEnum.beginner.value)
        await self.user_stats_repo(self.session).create_one(userId=user.id, levelId=level.id)
        return user
