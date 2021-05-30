from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Кофе")
        ],
        [
            KeyboardButton(text="Молоко"),
            KeyboardButton(text="Сахар"),
        ],
    ],
    resize_keyboard=True
)
