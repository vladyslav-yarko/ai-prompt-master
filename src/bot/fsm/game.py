from aiogram.fsm.state import StatesGroup, State


class GameState(StatesGroup):
    active = State()
    
    learn_mode = State()
    creative_mode = State()
    code_mode = State()
    anti_prompt_mode = State()
    puzzles_mode = State()
    
    
class ActiveGameState(StatesGroup):    
    learn_mode = State()
    learn_waiting = State()
    
    creative_mode = State()
    creative_waiting = State()
    
    code_mode = State()
    code_waiting = State()
    
    anti_prompt_mode = State()
    anti_prompt_waiting = State()
    
    puzzles_mode = State()
    puzzles_waiting = State()
