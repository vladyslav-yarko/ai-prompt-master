from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction
from src.utils.prompt import UserPrompt, SystemPrompt
from src.utils.regex import find_score
from src.models import Base
from src.prompts.game import *


class GameService(Service):
    def __init__(
        self,
        session: AsyncSession,
        game_repo: Repository,
        user_repo: Repository,
        user_stats_repo: Repository,
        level_repo: Repository,
        user_achievement_repo: Repository,
        achievement_repo: Repository
    ):
        super().__init__(session)
        self.repo = game_repo
        self.game_repo = game_repo
        self.user_repo = user_repo
        self.user_stats_repo = user_stats_repo
        self.level_repo = level_repo
        self.user_achievement_repo = user_achievement_repo
        self.achievement_repo = achievement_repo
        
    async def get(self) -> list[Base]:
        data = await super().get()
        return data.get("data")

    async def get_one(self, title: str) -> Optional[Base]:
        data = await self.game_repo(self.session).get_one_by_title(title)
        return data
    
    async def check_prompt(self, prompt: str, **kwargs) -> str:
        data = await self.ask_llm([
            SystemPrompt(check_prompt.render()).message,
            UserPrompt(prompt).message
        ])
        return data
