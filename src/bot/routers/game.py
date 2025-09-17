
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
    
    
@router.callback_query(StateFilter(GameState.active), CallDataStarts("description_game_"))
async def game_info_hand(callback: CallbackQuery, state: FSMContext, service: GameService):
    await GameCallbackResponse(
        callback=callback,
        state=state
    ).game_info_hand(service)
    
    
# Learn mode
    
@router.callback_query(StateIn(GameState.active, ActiveGameState.learn_waiting), CallDataEq("start_game_learnMode"))
async def learn_game_hand(callback: CallbackQuery, state: FSMContext, service: GameService):
    await GameCallbackResponse(
        callback=callback,
        state=state
    ).learn_game_hand(service)
    
    
@router.callback_query(StateFilter(ActiveGameState.learn_mode), CallDataStartsIn("game_learn_1", "game_learn_2"))
async def active_learn_game_hand(callback: CallbackQuery, state: FSMContext, service: GameService):
    await GameCallbackResponse(
        callback=callback,
        state=state
    ).active_learn_game_hand(service)
    
    
# Creative mode    
    
@router.callback_query(StateIn(GameState.active, ActiveGameState.creative_waiting), CallDataEq("start_game_creativeMode"))
async def creative_game_hand(callback: CallbackQuery, state: FSMContext, service: GameService):
    await GameCallbackResponse(
        callback=callback,
        state=state
    ).creative_game_hand(service)
    
    
@router.message(StateFilter(ActiveGameState.creative_mode))
async def active_creative_game_hand(message: Message, state: FSMContext, service: GameService):
    await GameMessageResponse(
        message=message,
        state=state
    ).active_creative_game_hand(service)
