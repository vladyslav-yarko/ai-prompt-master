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


class MessageResponse(Response):
    def __init__(
        self, 
        message: Message, 
        text: str = '', 
        keyboard: Optional[Keyboard] = None, 
        state: Optional[FSMContext] = None,
        parse_mode: Optional[str] = "Markdown"):
        self.message = message
        self.keyboard = keyboard
        self.text = text
        self.state = state
        self.parse_mode = parse_mode

    async def answer(self):
        await self.message.answer(
            text=self.text,
            reply_markup=self.keyboard,
            parse_mode=self.parse_mode
        )


class CallbackResponse(Response):
    def __init__(
        self, 
        callback: CallbackQuery, 
        text: str = "", 
        keyboard: Optional[Keyboard] = None, 
        click_text: str = "", 
        state: Optional[FSMContext] = None,
        parse_mode: Optional[str] = "Markdown"):
        self.callback = callback
        self.keyboard = keyboard
        self.text = text
        self.click_text = click_text
        self.state = state
        self.parse_mode = parse_mode

    async def answer(self):
        await self.callback.answer(self.click_text)
        await self.callback.message.answer(
            text=self.text,
            reply_markup=self.keyboard,
            parse_mode=self.parse_mode
        )
