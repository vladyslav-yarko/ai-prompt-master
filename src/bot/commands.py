from aiogram.types import BotCommand


commands = [
    BotCommand(command="start", description="Почати роботу з ботом"),
    BotCommand(command="help", description="Пояснення команд і можливостей"),
    BotCommand(command="rules", description="Правила гри та як усе працює"),
    BotCommand(command="authorize", description="Створити акаунт"),
    BotCommand(command="delete", description="Видалити акаунт назавжди"),
    BotCommand(command="profile", description="Показати статистику"),
    BotCommand(command="levels", description="Подивитись усі доступні рівні"),
    BotCommand(command="achievements", description="Переглянути всі доступні досягнення"),
    BotCommand(command="quit", description="Повернутись в головне меню"),
    BotCommand(command="games", description="Почати гру")
]
