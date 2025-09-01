from src.bot.utils.response import MessageResponse, CallbackResponse
from src.bot.utils.markdown import escape_md
from src.bot.text.user import *
from src.bot.keyboards.inline.user import delete_command_hand_keyboard
from src.bot.fsm.user import UserState
from src.services import UserService


class UserMessageResponse(MessageResponse):
    async def authorize_hand(self, service: UserService) -> None:
        data = {
            "telegramId": self.message.from_user.id,
            "chatId": self.message.chat.id
        }
        user = await service.create_one(data)
        if not user:
            self.text = e_authorize_hand_text.render()
        else:
            self.text = s_authorize_hand_text.render()
        await self.answer()
