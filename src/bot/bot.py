from aiogram import Bot as AiogramBot, Dispatcher

from src.utils.application import Application
from src.config import settings
from src.bot.lifespan import on_startup, on_shutdown
from src.bot.commands import commands
from src.bot.routers import *


class Bot(Application):
    pass

