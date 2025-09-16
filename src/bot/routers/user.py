from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.bot.responses import UserMessageResponse, UserCallbackResponse
from src.bot.middlewares.user import UserMiddleware
from src.bot.filters import CallDataEq
from src.bot.fsm.user import UserState
from src.services import UserService


router = Router()
router.message.middleware(UserMiddleware())
router.callback_query.middleware(UserMiddleware())
