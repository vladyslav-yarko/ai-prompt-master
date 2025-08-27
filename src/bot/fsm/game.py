from aiogram.fsm.state import StatesGroup, State


class GameState(StatesGroup):
    active = State()
    
    learn_mode = State()
    creative_mode = State()
    code_mode = State()
    anti_prompt_mode = State()
    puzzles_mode = State()

