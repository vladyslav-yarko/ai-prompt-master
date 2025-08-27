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
    
    @transaction
    async def check_mode(self, telegram_id: int, prompt: str, mode: str) -> str:
        response = await self.check_prompt(prompt)
        score = find_score(response)
        user_data = await self.get_user_one_with_data(telegram_id)
        user = user_data.get("user")
        # User statistics
        user_statistics = user_data.get("statistics")
        total_score = user_statistics.totalScore + score
        total_games_played = user_statistics.totalGamesPlayed + 1
        mode_score = getattr(user_statistics, mode) + score
        # User level
        user_level = user_data.get("level")
        level_id = user_level.id
        next_level = await self.level_repo(self.session).get_next(level_id)
        if next_level and next_level.requiredScore <= total_score:
            level_id = next_level.id
        mode_score_d = {mode: mode_score}
        await self.user_stats_repo(self.session).update_one_by_user_id(
            user.id, 
            totalScore=total_score,
            totalGamesPlayed=total_games_played,
            levelId=level_id,
            **mode_score_d
        )
        # User achievements
        mode_achievements = await self.achievement_repo(self.session).get_by_condition_key(mode)
        user_achievements_ids = [ach.id for ach in user_data["achievements"]]
        new_achievements = []
        for achievement in mode_achievements:
            if achievement.conditionValue <= mode_score:
                if achievement.id not in user_achievements_ids:
                    new_achievements.append({
                        "userId": user.id,
                        "achievementId": achievement.id
                    })
        if new_achievements:
            await self.user_achievement_repo(self.session).create_many(new_achievements)
        return response
        
    
    # learn mode
    async def start_learn_mode(self) -> tuple[str, str, str]:
        task = await self.ask_llm([
            SystemPrompt(task_learn_prompt.render()).message,
            UserPrompt(start_learn_prompt.render()).message
        ])
        task1, task2 = task.split("-----")
        return task, task1, task2
    
    async def check_learn_mode(self, telegram_id: int, prompt: str) -> tuple[str, str]:
        mode = "learnMode"
        response = await self.check_mode(
            telegram_id=telegram_id,
            prompt=prompt,
            mode=mode
        )
        return response, mode
    
    # creative mode
    async def start_creative_mode(self) -> str:
        task = await self.ask_llm([
            SystemPrompt(task_creative_prompt.render()).message,
            UserPrompt(start_creative_prompt.render()).message
        ])
        return task
    
    async def check_creative_mode(self, telegram_id: int, prompt: str) -> str:
        mode = "creativeMode"
        response = await self.check_mode(
            telegram_id=telegram_id,
            prompt=prompt,
            mode=mode
        )
        return response, mode
    
    # code mode    
    async def start_code_mode(self) -> str:
        task = await self.ask_llm([
            SystemPrompt(task_code_prompt.render()).message,
            UserPrompt(start_code_prompt.render()).message
        ])
        return task
    
    async def check_code_mode(self, telegram_id: int, prompt: str) -> str:
        mode = "codeMode"
        response = await self.check_mode(
            telegram_id=telegram_id,
            prompt=prompt,
            mode=mode
        )
        return response, mode
    
    # anti-prompt mode    
    async def start_anti_prompt_mode(self) -> str:
        task = await self.ask_llm([
            SystemPrompt(task_anti_prompt_prompt.render()).message,
            UserPrompt(start_anti_prompt_prompt.render()).message
        ])
        return task
    
    async def check_anti_prompt_mode(self, telegram_id: int, prompt: str) -> str:
        mode = "antiPromptMode"
        response = await self.check_mode(
            telegram_id=telegram_id,
            prompt=prompt,
            mode=mode
        )
        return response, mode
