from aiogram import Bot as AiogramBot, Dispatcher

from src.utils.application import Application
from src.config import settings
from src.bot.lifespan import on_startup, on_shutdown
from src.bot.commands import commands
from src.bot.routers import *


class Bot(Application):
    def __init__(self):
        super().__init__()
        self.token = settings.BOT_TOKEN
        self.dp = Dispatcher()
        self.dp.startup.register(on_startup)
        self.dp.shutdown.register(on_shutdown)
        self.commands = commands
        self.routers = [
            base_router,
            user_router,
            game_router
        ]
        self.dp.include_routers(*self.routers)
