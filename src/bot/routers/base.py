from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.bot.middlewares import BaseMiddleware
from src.bot.responses import BaseMessageResponse, BaseCallbackResponse
from src.bot.filters import CallDataEq
from src.services import ProgressDataService


router = Router()
router.message.middleware(BaseMiddleware())
# Callback query does not need the service, so middleware was not applied


@router.message(StateFilter(None), Command('start'))
async def start_hand(message: Message, state: FSMContext):
    await BaseMessageResponse(
        message=message,
        state=state
    ).start_hand()
