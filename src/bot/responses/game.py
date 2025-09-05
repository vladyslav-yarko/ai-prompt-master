from src.bot.utils.response import MessageResponse, CallbackResponse
from src.bot.text.game import *
from src.bot.fsm.game import GameState, ActiveGameState
from src.bot.keyboards.inline.game import (
    games_hand_keyboard, 
    game_info_hand_keyboard, 
    learn_game_hand_keyboard,
    continue_keyboard
)
from src.services import GameService
from src.models import User
from src.utils.prompt import AIPrompt, UserPrompt


class GameMessageResponse(MessageResponse):
    pass
