from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository


class ProgressDataService(Service):
    def __init__(
        self,
        session: AsyncSession,
        level_repo: Repository,
        achievement_repo: Repository
    ):
        super().__init__(session)
        self.repo = None
        self.level_repo = level_repo
        self.achievement_repo = achievement_repo
        
    async def get_levels(self) -> dict:
        self.repo = self.level_repo
        data = await super().get()
        self.repo = None
        return data
