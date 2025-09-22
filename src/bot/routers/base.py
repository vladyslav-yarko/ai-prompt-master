from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.bot.middlewares import BaseRouterMiddleware
from src.bot.responses import BaseMessageResponse, BaseCallbackResponse
from src.bot.filters import CallDataEq
from src.services import ProgressDataService


router = Router()
router.message.middleware(BaseRouterMiddleware())
# Callback query does not need the service, so middleware was not applied


@router.message(StateFilter(None), Command('start'))
async def start_hand(message: Message, state: FSMContext):
    await BaseMessageResponse(
        message=message,
        state=state
    ).start_hand()


@router.message(StateFilter(None), Command('help'))
async def help_hand(message: Message, state: FSMContext):
    await BaseMessageResponse(
        message=message,
        state=state
    ).help_hand()
    
    
@router.message(StateFilter(None), Command("levels"))
async def levels_hand(message: Message, state: FSMContext, service: ProgressDataService):
    await BaseMessageResponse(
        message=message,
        state=state
    ).levels_hand(service)
    
    
@router.message(StateFilter(None), Command("achievements"))
async def achievement_hand(message: Message, state: FSMContext, service: ProgressDataService):
    await BaseMessageResponse(
        message=message,
        state=state
    ).achievement_hand(service)
    
    
@router.message(StateFilter(None), Command("rules"))
async def rules_hand(message: Message, state: FSMContext):
    await BaseMessageResponse(
        message=message,
        state=state
    ).rules_hand()
    
    
@router.message(StateFilter("*"), Command("quit"))
async def message_quit_hand(message: Message, state: FSMContext):
    await BaseMessageResponse(
        message=message,
        state=state
    ).message_quit_hand()
    
    
@router.callback_query(StateFilter("*"), CallDataEq("quit"))
async def callback_quit_hand(callback: CallbackQuery, state: FSMContext):
    await BaseCallbackResponse(
        callback=callback,
        state=state
    ).callback_quit_hand()
