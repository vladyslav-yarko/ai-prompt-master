from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from src.databases import db_session
from src.services import GameService
from src.repositories import GameRepository, UserRepository, UserStatsRepository, LevelRepository, UserAchievementRepository, AchievementRepository
from src.bot.text import e_authorize_text


class GameMiddleware(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ):
        async for session in db_session():
            data['session'] = session
            service = GameService(
                session=session,
                game_repo=GameRepository,
                user_repo=UserRepository,
                user_stats_repo=UserStatsRepository,
                level_repo=LevelRepository,
                user_achievement_repo=UserAchievementRepository,
                achievement_repo=AchievementRepository
            )
            data['service'] = service
            telegram_id = event.from_user.id
            user = await service.get_user_one(telegram_id)
            if user:
                data["user"] = user
                result = await handler(event, data)
                return result
            await event.answer(e_authorize_text.render(), parse_mode="Markdown")
