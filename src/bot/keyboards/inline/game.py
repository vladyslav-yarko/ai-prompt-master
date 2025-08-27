from src.bot.utils.keyboard import InlineKeyboard
from src.bot.utils.button import CallbackButton


def games_hand_keyboard(game_title: str, mode: str) -> InlineKeyboard:
    keyboard = InlineKeyboard(
        [
            [
                CallbackButton(text="Грати 🎮", callback=f"start_game_{mode}").button
            ],
            [
                CallbackButton(text="Опис 📝", callback=f"description_game_{game_title}").button,
                CallbackButton(text="Меню 🏠", callback="quit").button
            ]
        ]
    ).keyboard()
    return keyboard


def game_info_hand_keyboard(mode: str) -> InlineKeyboard:
    keyboard = InlineKeyboard(
        [
            [
                CallbackButton(text="Грати 🎮", callback=f"start_game_{mode}").button
            ],
            [
                CallbackButton(text="Меню 🏠", callback="quit").button
            ]
        ]
    ).keyboard()
    return keyboard


def learn_game_hand_keyboard() -> InlineKeyboard:
    keyboard = InlineKeyboard(
        [
            [
                CallbackButton(text="1 ➡️", callback=f"game_learn_1").button,
                CallbackButton(text="2 ➡️", callback=f"game_learn_2").button
            ]
        ]
    ).keyboard()
    return keyboard
