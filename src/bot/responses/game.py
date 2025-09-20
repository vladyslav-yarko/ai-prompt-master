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


class GameCallbackResponse(CallbackResponse):
    async def callback_games_hand(self, user: User, service: GameService) -> None:
        if not user:
            self.text = e_games_hand_text.render()
            await self.answer()
            return 
        games = await service.get()
        await self.state.set_state(GameState.active)
        self.text = s_games_hand_text.render()
        await self.answer()
        for game in games:
            self.text = s_games_hand_text_game.render(**game.to_dict())
            self.keyboard = games_hand_keyboard(game.title, game.mode)
            await self.answer()
            
    async def game_info_hand(self, service: GameService) -> None:
        title = self.callback.data.split("_")[-1]
        game = await service.get_one(title)
        self.text = s_game_info_hand_text.render(**game.to_dict())
        self.keyboard = game_info_hand_keyboard(game.mode)
        self.click_text = title
        await self.answer()
        
    async def learn_game_hand(self, service: GameService) -> None:
        task, task1, task2 = await service.start_learn_mode()
        self.text = task
        self.keyboard = learn_game_hand_keyboard()
        await self.state.update_data(game_learn_1=task1, game_learn_2=task2, learnModeTask=task)
        await self.state.set_state(ActiveGameState.learn_mode)
        await self.answer()

    async def active_learn_game_hand(self, service: GameService) -> None:
        self.click_text = "Вибір зроблено 🧠"
        state_data = await self.state.get_data()
        prompt = state_data.get(self.callback.data)
        response, mode = await service.check_learn_mode(
            self.callback.from_user.id,
            prompt
        )
        self.text = response
        self.keyboard = continue_keyboard(mode)
        await self.state.set_state(ActiveGameState.learn_waiting)
        learn_mode_data = state_data.get("learnModeData")
        learn_mode_data.append(AIPrompt(state_data.get("learnModeTask")).message)
        learn_mode_data.append(UserPrompt(prompt).message)
        await self.state.update_data(learnModeData=learn_mode_data)
        await self.answer()
        
    async def creative_game_hand(self, service: GameService) -> None:
        task = await service.start_creative_mode()
        self.text = task
        await self.state.set_state(ActiveGameState.creative_mode)
        await self.answer()
        
    async def code_game_hand(self, service: GameService) -> None:
        task = await service.start_code_mode()
        self.text = task
        await self.state.set_state(ActiveGameState.code_mode)
        await self.answer()
