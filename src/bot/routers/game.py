
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


# Base game commands

@router.message(StateIn(None, GameState.active), Command("games"))
async def command_games_hand(message: Message, state: FSMContext, user: User, service: GameService):
    await GameMessageResponse(
        message=message,
        state=state
    ).command_games_hand(user, service)
    
    
@router.callback_query(StateFilter(ActiveGameState), CallDataEq("games"))
async def callback_games_hand(callback: CallbackQuery, state: FSMContext, user: User, service: GameService):
    await GameCallbackResponse(
        callback=callback,
        state=state
    ).callback_games_hand(user, service)
