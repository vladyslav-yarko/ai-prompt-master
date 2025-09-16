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


@router.message(StateFilter(None), Command('authorize'))
async def authorize_hand(message: Message, state: FSMContext, service: UserService):
    await UserMessageResponse(
        message=message,
        state=state
    ).authorize_hand(service)


@router.message(StateFilter(None), Command('delete'))
async def delete_command_hand(message: Message, state: FSMContext, service: UserService):
    await UserMessageResponse(
        message=message,
        state=state
    ).delete_command_hand(service)
    
    
@router.message(StateFilter(None), Command("profile"))
async def profile_hand(message: Message, state: FSMContext, service: UserService):
    await UserMessageResponse(
        message=message,
        state=state
    ).profile_hand(service)
    
    
@router.callback_query(StateFilter(UserState.delete), CallDataEq("delete"))
async def delete_hand(callback: CallbackQuery, state: FSMContext, service: UserService):
    await UserCallbackResponse(
        callback=callback,
        state=state
    ).delete_hand(service)
