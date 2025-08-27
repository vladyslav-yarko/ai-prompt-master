from src.bot.utils.keyboard import InlineKeyboard
from src.bot.utils.button import CallbackButton


def delete_command_hand_keyboard() -> InlineKeyboard:
    keyboard = InlineKeyboard(
        [
            [
                CallbackButton(text="Так", callback="delete").button
            ],
            [
                CallbackButton(text="Ні", callback="quit").button
            ]
        ]
    ).keyboard()
    return keyboard
