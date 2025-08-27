from aiogram.filters import Filter
from aiogram.types import CallbackQuery, TelegramObject
from aiogram.fsm.context import FSMContext


class CallDataIn(Filter):
    def __init__(self, *args: str):
        self.data = args

    async def __call__(self, callback: CallbackQuery):
        result = callback.data in self.data
        return result


class CallDataEq(Filter):
    def __init__(self, data: str):
        self.data = data

    async def __call__(self, callback: CallbackQuery):
        result = self.data == callback.data
        return result
    
    
class CallDataStarts(Filter):
    def __init__(self, data: str):
        self.data = data

    async def __call__(self, callback: CallbackQuery):
        result = callback.data.startswith(self.data)
        return result
    
    
class CallDataStartsIn(Filter):
    def __init__(self, *args: str):
        self.data = args

    async def __call__(self, callback: CallbackQuery):
        result = False
        for d in self.data:
            if callback.data.startswith(d):
                result = True
        return result


class StateIn(Filter):
    def __init__(self, *args: FSMContext):
        self.states = args

    async def __call__(self, obj: TelegramObject, state: FSMContext):
        current_state = await state.get_state()
        result = current_state in self.states
        return result
