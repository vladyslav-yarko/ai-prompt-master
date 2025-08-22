from abc import ABC, abstractmethod
from typing import Optional

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from src.bot.utils.keyboard import Keyboard


class Response(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def answer(self):
        raise NotImplementedError()
