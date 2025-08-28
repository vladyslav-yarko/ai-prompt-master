from aiogram import Dispatcher

from src.utils.logger import logger


async def on_startup(dispatcher: Dispatcher):
    logger.info("Bot is staring...")


async def on_shutdown(dispatcher: Dispatcher):
    logger.info("Bot is shutting down...")
