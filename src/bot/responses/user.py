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

    async def delete_command_hand(self, service: UserService) -> None:
        user = await service.get_user_one(self.message.from_user.id)
        if not user:
            self.text = e_delete_command_hand_text.render()
        else:
            self.text = s_delete_command_hand_text.render()
            self.keyboard = delete_command_hand_keyboard()
            await self.state.set_state(UserState.delete)
        await self.answer()
        
    async def profile_hand(self, service: UserService) -> None:
        user = await service.get_user_one_with_data(self.message.from_user.id)
        if not user:
            self.text = e_profile_hand_text.render()
        else:
            self.text = s_profile_hand_text.render(
                username=escape_md(self.message.from_user.username),
                # There is a shorthand
                # achievements=user["achievements"],
                # statistics=user["statistics"],
                # level=user["level"]
                **user
            )
        await self.answer()
        
        
class UserCallbackResponse(CallbackResponse):
    pass
