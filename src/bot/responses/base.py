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
