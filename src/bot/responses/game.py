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
    async def command_games_hand(self, user: User, service: GameService) -> None:
        if not user:
            self.text = e_games_hand_text.render()
            await self.answer()
            return 
        games = await service.get()
        await self.state.set_state(GameState.active)
        state_data = await self.state.get_data()
        learn_mode = state_data.get("learnModeData")
        if learn_mode is None:
            await self.state.update_data(
                learnModeData=[],
                creativeModeData=[],
                codeModeData=[],
                antiPromptModeData=[],
                puzzleModeData=[]
            )
        self.text = s_games_hand_text.render()
        await self.answer()
        for game in games:
            self.text = s_games_hand_text_game.render(**game.to_dict())
            self.keyboard = games_hand_keyboard(game.title, game.mode)
            await self.answer()        
        
    async def active_creative_game_hand(self, service: GameService) -> None:
        prompt = self.message.text
        response, mode = await service.check_creative_mode(
            self.message.from_user.id,
            prompt
        )
        self.text = response
        self.keyboard = continue_keyboard(mode)
        await self.state.set_state(ActiveGameState.creative_waiting)
        await self.answer()        
        
    async def active_code_game_hand(self, service: GameService) -> None:
        prompt = self.message.text
        response, mode = await service.check_code_mode(
            self.message.from_user.id,
            prompt
        )
        self.text = response
        self.keyboard = continue_keyboard(mode)
        await self.state.set_state(ActiveGameState.code_waiting)
        await self.answer()  
        
    async def active_anti_prompt_game_hand(self, service: GameService) -> None:
        prompt = self.message.text
        response, mode = await service.check_anti_prompt_mode(
            self.message.from_user.id,
            prompt
        )
        self.text = response
        self.keyboard = continue_keyboard(mode)
        await self.state.set_state(ActiveGameState.anti_prompt_waiting)
        await self.answer()  
        
    async def active_puzzles_game_hand(self, service: GameService) -> None:
        prompt = self.message.text
        response, mode = await service.check_puzzles_mode(
            self.message.from_user.id,
            prompt
        )
        self.text = response
        self.keyboard = continue_keyboard(mode)
        await self.state.set_state(ActiveGameState.puzzles_waiting)
        await self.answer()  
