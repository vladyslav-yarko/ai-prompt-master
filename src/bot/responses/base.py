from src.bot.utils.response import MessageResponse, CallbackResponse
from src.bot.text.base import *
from src.services import ProgressDataService


class BaseMessageResponse(MessageResponse):
    async def start_hand(self) -> None:
        self.text = s_start_hand_text.render()
        await self.answer()

    async def help_hand(self) -> None:
        self.text = s_help_hand_text.render()
        await self.answer()
        
    async def levels_hand(self, service: ProgressDataService) -> None:
        data = await service.get_levels()
        self.text = s_levels_hand_text.render(levels=data.get("data"))
        await self.answer()
        
    async def achievement_hand(self, service: ProgressDataService) -> None:
        data = await service.get_achievements()
        self.text = s_achievements_hand_text.render(achievements=data.get("data"))
        await self.answer()
        
    async def rules_hand(self) -> None:
        self.text = s_rules_hand_text.render()
        await self.answer()
        
    async def message_quit_hand(self) -> None:
        current_state = await self.state.get_state()
        if current_state is None:
            self.text = e_quit_hand_text.render()
        else:
            self.text = s_quit_hand_text.render()
            await self.state.clear()
        await self.answer()
        
        
class BaseCallbackResponse(CallbackResponse):
    async def callback_quit_hand(self) -> None:
        current_state = await self.state.get_state()
        if current_state is None:
            self.text = e_quit_hand_text.render()
            self.click_text = "Ти в головному меню 🏠"
        else:
            self.text = s_quit_hand_text.render()
            self.click_text = "Ти повернувся в головне меню 🏠"
        await self.state.clear()
        await self.answer()
