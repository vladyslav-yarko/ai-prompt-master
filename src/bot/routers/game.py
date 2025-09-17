
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.bot.responses import GameMessageResponse, GameCallbackResponse
from src.bot.middlewares import GameMiddleware
from src.bot.filters import CallDataStarts, StateIn, CallDataEq, CallDataStartsIn
from src.bot.fsm import GameState, ActiveGameState
from src.services import GameService
from src.models import User


router = Router()
router.message.middleware(GameMiddleware())
router.callback_query.middleware(GameMiddleware())
