from aiogram.filters import Filter
from aiogram.types import CallbackQuery, TelegramObject
from aiogram.fsm.context import FSMContext


class CallDataIn(Filter):
    def __init__(self, *args: str):
        self.data = args

    async def __call__(self, callback: CallbackQuery):
        result = callback.data in self.data
        return result
